-- Runs automatically the first time the Postgres container initializes its data
-- directory (when mounted into /docker-entrypoint-initdb.d/ via docker-compose).
-- Creates the table + seeds dummy rows so you have data to query immediately.

CREATE TABLE IF NOT EXISTS drillholes (
    id          SERIAL PRIMARY KEY,
    hole_id     TEXT NOT NULL,
    status      TEXT NOT NULL CHECK (status IN ('planned', 'logging', 'complete')),
    rock_type   TEXT NOT NULL,
    grade       NUMERIC(6, 2) NOT NULL CHECK (grade >= 0),
    depth_m     NUMERIC(7, 2) NOT NULL CHECK (depth_m > 0),
    logged_at   TIMESTAMPTZ NOT NULL DEFAULT now()
);

INSERT INTO drillholes (hole_id, status, rock_type, grade, depth_m, logged_at) VALUES
    ('DH-001', 'complete', 'granite',    2.45, 120.50, '2026-05-01 09:15:00+00'),
    ('DH-002', 'complete', 'basalt',     0.80, 88.20,  '2026-05-03 14:30:00+00'),
    ('DH-003', 'logging',  'quartzite',  5.10, 210.00, '2026-05-10 11:00:00+00'),
    ('DH-004', 'logging',  'schist',     1.25, 64.75,  '2026-05-12 08:45:00+00'),
    ('DH-005', 'planned',  'granite',    0.00, 150.00, '2026-05-20 16:20:00+00'),
    ('DH-006', 'complete', 'limestone',  3.30, 99.90,  '2026-05-22 10:05:00+00'),
    ('DH-007', 'planned',  'basalt',     0.00, 300.00, '2026-05-25 13:00:00+00'),
    ('DH-008', 'logging',  'granite',    4.75, 175.40, '2026-05-28 07:30:00+00'),
    ('DH-009', 'complete', 'schist',     1.90, 42.10,  '2026-06-01 12:00:00+00'),
    ('DH-010', 'planned',  'quartzite',  0.00, 260.00, '2026-06-05 15:45:00+00');
