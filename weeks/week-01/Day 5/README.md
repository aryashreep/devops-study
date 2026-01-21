# Lab Snapshot Utility (Placeholder)

This repo includes:

- a lightweight Python virtual environment bootstrapper
- a placeholder utility for managing lab snapshots (create/list/restore)

## Files

- `env_bootstrap.py` → creates `.venv` and installs requirements
- `tools/lab_snapshot.py` → placeholder snapshot tool
- `requirements.txt` → optional dependency list

## Quick Start

### 1) Bootstrap venv

```bash
python env_bootstrap.py
```

### 2) Activate venv

- Linux/macOS:

```bash
source .venv/bin/activate
```

- Windows:

```bash
.venv\Scripts\activate
```

### 3) Run tool

- Help:

```bash
python tools/lab_snapshot.py --help
```

- Create snapshot (placeholder metadata):

```bash
python tools/lab_snapshot.py create --label "baseline"
```

- List snapshots:

```bash
python tools/lab_snapshot.py list

```

- Restore snapshot:

```bash
python tools/lab_snapshot.py restore --id <snapshot_id>

```

- Snapshot Storage: Snapshots are stored under:

```bash
.lab_snapshots/

```
