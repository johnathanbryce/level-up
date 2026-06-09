# Database / Backend (Area 4)

## Likely Deep Core architecture (peer-level inference)

_Next.js (Node) app layer via route handlers/server actions + standalone Python geostat/agent services + Supabase Postgres. Why split: geostats ecosystem (PyKrige/GeostatsPy/GemPy + NumPy/SciPy) is Python._

## Supabase = Postgres+ (RLS)

- Supabase is managed Postgres plus auth, storage, realtime, edge functions

## Schema + indexing basics

- Postgres default, index what you filter/join on.

## Long-job persistence (3D model build)

- A model build = a job row in Postgres: id, status (queued/running/complete/failed), params, dataset_version, result_ref, timestamps. The client polls this row for status
- Large artifacts do not go in the DB - store them in **object storage** (S3 / Supabase Storage) and keep only a URL reference in the job row
- Caseway angle: same pattern as handling uploaded documents - metadata in the DB, the heavy file in object strorage, referenced by key
