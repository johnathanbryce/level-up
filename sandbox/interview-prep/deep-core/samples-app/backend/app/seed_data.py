"""Seed data for the samples API (dummy in-memory records).

Fields match the assignment spec: id, name, rock_type, grade (g/t), depth_m (m).
"""

SAMPLES = [
    {
        "id": 1,
        "name": "DH-001 surface",
        "rock_type": "granite",
        "grade": 2.4,
        "depth_m": 12.5,
    },
    {
        "id": 2,
        "name": "DH-001 mid",
        "rock_type": "basalt",
        "grade": 5.1,
        "depth_m": 48.0,
    },
    {
        "id": 3,
        "name": "DH-002 surface",
        "rock_type": "shale",
        "grade": 0.0,
        "depth_m": 7.2,
    },
    {
        "id": 4,
        "name": "DH-002 deep",
        "rock_type": "limestone",
        "grade": 3.8,
        "depth_m": 103.4,
    },
    {
        "id": 5,
        "name": "DH-003 surface",
        "rock_type": "sandstone",
        "grade": 1.2,
        "depth_m": 21.9,
    },
    {
        "id": 6,
        "name": "DH-001 mid",
        "rock_type": "basalt",
        "grade": 2.1,
        "depth_m": 52.0,
    },
]
