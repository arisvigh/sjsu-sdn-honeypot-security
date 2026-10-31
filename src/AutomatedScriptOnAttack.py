#!/usr/bin/env python3
"""Preview proposed actions from historical honeypot logs. No network writes."""
import argparse
import os
from pathlib import Path
from sdn_security import build_review_proposals, read_honeypot_log, serialize_proposals

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--log", type=Path, default=Path(os.getenv("KIPPO_LOG_PATH", "./kippo.log")))
    parser.add_argument("--switch-id", default=os.getenv("SDN_SWITCH_ID", "s2"))
    args = parser.parse_args()
    try:
        ips = read_honeypot_log(args.log)
    except OSError as exc:
        parser.error(f"Unable to read honeypot log: {exc}")
    print(serialize_proposals(build_review_proposals(ips, args.switch_id)))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
