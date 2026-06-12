"use client";

import { useEffect, useState } from "react";

// Your FastAPI server. Change the port here if you run uvicorn somewhere else.
const API = "http://localhost:8000";

type Status = "planned" | "logging" | "complete";

type Drillhole = {
  id: number;
  hole_id: string;
  status: Status;
  rock_type: string;
  grade: number;
  depth_m: number;
  logged_at: string;
};

const STATUSES: Status[] = ["planned", "logging", "complete"];

const emptyForm = {
  hole_id: "",
  status: "planned" as Status,
  rock_type: "",
  grade: "",
  depth_m: "",
};

export default function Home() {
  const [rows, setRows] = useState<Drillhole[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [statusFilter, setStatusFilter] = useState<"" | Status>("");
  const [form, setForm] = useState(emptyForm);
  const [submitting, setSubmitting] = useState(false);

  async function load() {
    setLoading(true);
    setError(null);
    try {
      const qs = statusFilter ? `?status=${statusFilter}` : "";
      const res = await fetch(`${API}/drillholes${qs}`);
      if (!res.ok) throw new Error(`GET /drillholes -> ${res.status}`);
      setRows(await res.json());
    } catch (e) {
      setError(e instanceof Error ? e.message : "Failed to load");
    } finally {
      setLoading(false);
    }
  }

  // Reload whenever the status filter changes.
  useEffect(() => {
    load();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [statusFilter]);

  async function onCreate(e: React.FormEvent) {
    e.preventDefault();
    setSubmitting(true);
    setError(null);
    try {
      const res = await fetch(`${API}/drillholes`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          hole_id: form.hole_id,
          status: form.status,
          rock_type: form.rock_type,
          grade: parseFloat(form.grade),
          depth_m: parseFloat(form.depth_m),
        }),
      });
      if (!res.ok) throw new Error(`POST /drillholes -> ${res.status}`);
      setForm(emptyForm);
      await load();
    } catch (e) {
      setError(e instanceof Error ? e.message : "Failed to create");
    } finally {
      setSubmitting(false);
    }
  }

  async function onDelete(id: number) {
    setError(null);
    try {
      const res = await fetch(`${API}/drillholes/${id}`, { method: "DELETE" });
      if (!res.ok) throw new Error(`DELETE /drillholes/${id} -> ${res.status}`);
      await load();
    } catch (e) {
      setError(e instanceof Error ? e.message : "Failed to delete");
    }
  }

  return (
    <main>
      <h1>Drillhole Records</h1>

      {error && <div className="error">{error}</div>}

      {/* Create form */}
      <form className="create-form" onSubmit={onCreate}>
        <div>
          <label>Hole ID</label>
          <input
            value={form.hole_id}
            onChange={(e) => setForm({ ...form, hole_id: e.target.value })}
            required
          />
        </div>
        <div>
          <label>Status</label>
          <select
            value={form.status}
            onChange={(e) => setForm({ ...form, status: e.target.value as Status })}
          >
            {STATUSES.map((s) => (
              <option key={s} value={s}>
                {s}
              </option>
            ))}
          </select>
        </div>
        <div>
          <label>Rock type</label>
          <input
            value={form.rock_type}
            onChange={(e) => setForm({ ...form, rock_type: e.target.value })}
            required
          />
        </div>
        <div>
          <label>Grade</label>
          <input
            type="number"
            step="0.01"
            value={form.grade}
            onChange={(e) => setForm({ ...form, grade: e.target.value })}
            required
          />
        </div>
        <div>
          <label>Depth (m)</label>
          <input
            type="number"
            step="0.01"
            value={form.depth_m}
            onChange={(e) => setForm({ ...form, depth_m: e.target.value })}
            required
          />
        </div>
        <button type="submit" disabled={submitting}>
          {submitting ? "Adding…" : "Add"}
        </button>
      </form>

      {/* Filter */}
      <div className="toolbar">
        <div>
          <label>Filter by status</label>
          <select
            value={statusFilter}
            onChange={(e) => setStatusFilter(e.target.value as "" | Status)}
          >
            <option value="">all</option>
            {STATUSES.map((s) => (
              <option key={s} value={s}>
                {s}
              </option>
            ))}
          </select>
        </div>
        <span className="muted">{rows.length} record(s)</span>
      </div>

      {/* Table */}
      {loading ? (
        <p className="muted">Loading…</p>
      ) : rows.length === 0 ? (
        <p className="muted">No drillholes found.</p>
      ) : (
        <table>
          <thead>
            <tr>
              <th>ID</th>
              <th>Hole</th>
              <th>Status</th>
              <th>Rock</th>
              <th>Grade</th>
              <th>Depth (m)</th>
              <th>Logged</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            {rows.map((r) => (
              <tr key={r.id}>
                <td>{r.id}</td>
                <td>{r.hole_id}</td>
                <td>
                  <span className={`status-pill status-${r.status}`}>{r.status}</span>
                </td>
                <td>{r.rock_type}</td>
                <td>{r.grade}</td>
                <td>{r.depth_m}</td>
                <td className="muted">{new Date(r.logged_at).toLocaleDateString()}</td>
                <td>
                  <button className="danger" onClick={() => onDelete(r.id)}>
                    Delete
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </main>
  );
}
