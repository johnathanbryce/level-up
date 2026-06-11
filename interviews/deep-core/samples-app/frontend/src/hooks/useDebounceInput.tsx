import { useState, useEffect } from "react";

const useDebounceInput = (input: string, delay: number = 300) => {
  const [debouncedInput, setDebouncedInput] = useState<string>("");

  useEffect(() => {
    const timer = setTimeout(() => {
      setDebouncedInput(input);
    }, delay);
    return () => clearTimeout(timer);
  }, [input, delay]);

  return { debouncedInput };
};

export default useDebounceInput;
