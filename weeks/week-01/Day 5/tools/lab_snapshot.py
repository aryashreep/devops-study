#!/usr/bin/env python3
"""
Lab Snapshot Utility (placeholder)
----------------------------------
This is a placeholder script for managing lab snapshots.

Future capability ideas:
- create snapshot (archive files, export configs)
- list snapshots
- restore snapshot
- compare snapshots
"""

import argparse
import json
from datetime import datetime
from pathlib import Path


SNAPSHOT_DIR = Path(".lab_snapshots")


def ensure_dir():
    SNAPSHOT_DIR.mkdir(exist_ok=True)


def create_snapshot(label: str):
    ensure_dir()
    ts = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
    snapshot_id = f"{ts}_{label}".replace(" ", "_")
    meta = {
        "id": snapshot_id,
        "label": label,
        "created_utc": ts,
        "note": "placeholder snapshot metadata",
    }
    out = SNAPSHOT_DIR / f"{snapshot_id}.json"
    out.write_text(json.dumps(meta, indent=2), encoding="utf-8")
    print(f"[OK] Snapshot created (placeholder): {out}")


def list_snapshots():
    ensure_dir()
    files = sorted(SNAPSHOT_DIR.glob("*.json"))
    if not files:
        print("[INFO] No snapshots found.")
        return
    for f in files:
        print("-", f.name)


def restore_snapshot(snapshot_id: str):
    ensure_dir()
    f = SNAPSHOT_DIR / f"{snapshot_id}.json"
    if not f.exists():
        raise SystemExit(f"[ERROR] Snapshot not found: {snapshot_id}")
    print(f"[OK] Restored snapshot (placeholder): {f}")


def main():
    parser = argparse.ArgumentParser(description="Lab snapshot manager (placeholder)")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_create = sub.add_parser("create", help="Create a snapshot (placeholder metadata)")
    p_create.add_argument("--label", required=True, help="Snapshot label/name")

    sub.add_parser("list", help="List snapshots")

    p_restore = sub.add_parser("restore", help="Restore a snapshot (placeholder)")
    p_restore.add_argument("--id", required=True, help="Snapshot id")

    args = parser.parse_args()

    if args.cmd == "create":
        create_snapshot(args.label)
    elif args.cmd == "list":
        list_snapshots()
    elif args.cmd == "restore":
        restore_snapshot(args.id)


if __name__ == "__main__":
    main()
