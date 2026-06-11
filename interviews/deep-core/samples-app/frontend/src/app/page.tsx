"use client";
import { useState, useEffect } from "react";
import useDebounceInput from "@/hooks/useDebounceInput";

// Data contract — mirrors the backend `Sample` Pydantic model.
type Sample = {
  id: number;
  name: string;
  rock_type: string;
  grade: number;
  depth_m: number;
};

const API_URL = "http://localhost:8000";

export default function Home() {
  // data fetch state
  const [samplesData, setSamplesData] = useState<Sample[]>([]);
  const [isLoading, setIsLoading] = useState<boolean>(false);
  const [errorMessage, setErrorMessage] = useState<string>("");
  // input state
  const [input, setInput] = useState<string>("");

  const { debouncedInput } = useDebounceInput(input, 300);

  useEffect(() => {
    const controller = new AbortController();
    const { signal } = controller;
    const fetchSamplesData = async () => {
      setIsLoading(true);
      setErrorMessage("");
      try {
        const url = debouncedInput
          ? `${API_URL}/samples?rock_type=${encodeURIComponent(debouncedInput)}`
          : `${API_URL}/samples`;

        const res = await fetch(url, { signal });
        if (!res.ok) throw new Error(`HTTP ${res.status}`);
        const data = await res.json();
        setSamplesData(data);
        setIsLoading(false);
      } catch (error: any) {
        setIsLoading(false);

        if (error.name === "AbortError") {
          console.log("Fetch safely aborted");
        } else {
          setErrorMessage("Unable to fetch samples data. Please try again");
          console.error("Fetch error:", error);
        }
      }
    };

    fetchSamplesData();

    return () => {
      controller.abort();
    };
  }, [debouncedInput]);

  return (
    <main style={{ maxWidth: 640, margin: "2rem auto", padding: "0 1rem" }}>
      <h1>Samples Explorer</h1>

      <input
        type="text"
        placeholder="Filter by rock type (e.g. granite)"
        style={{ width: "100%", padding: "0.5rem", margin: "1rem 0" }}
        value={input}
        onChange={(e) => setInput(e.target.value)}
      />

      {isLoading && <p>Fetching samples...</p>}
      {!isLoading && errorMessage && <p>{errorMessage}</p>}
      {!isLoading && !errorMessage && samplesData.length === 0 && (
        <p>No samples found.</p>
      )}
      {!isLoading && !errorMessage && samplesData.length > 0 && (
        <ul style={{ listStyle: "none", padding: 0 }}>
          {samplesData.map((sample) => (
            <li
              key={sample.id}
              style={{
                border: "1px solid #ddd",
                borderRadius: 6,
                padding: "0.75rem",
                marginBottom: "0.5rem",
              }}
            >
              {sample.name} - {sample.grade} - {sample.rock_type}
            </li>
          ))}
        </ul>
      )}
    </main>
  );
}
