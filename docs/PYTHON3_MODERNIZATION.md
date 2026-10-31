# Python 3 modernization (2026)

The original 2015 scripts were Python 2 programs using obsolete OpenDaylight Helium APIs and embedded lab details. These **replacement modules** preserve the honeypot-log analysis concept, but are **read-only**: no controller requests and no flow-table changes.

- Supported design target: Python 3.15; locally syntax-checked and unit-tested under Python 3.13.
- No external Python dependencies.
- Log reading is non-destructive, with validation and deduplication of observed IPv4 addresses.
- Output is a JSON review proposal, **not** a deployed firewall or flow rule.
- The original source should be preserved separately as a historical artifact if appropriately reviewed.

Example:

```bash
python src/AutomatedScriptOnAttack.py --log ./sanitized-kippo.log --switch-id s2
python -m unittest discover -s tests -v
```

**Not a drop-in migration.** Actual OpenDaylight integration must be redesigned for an up-to-date controller with authenticated TLS, restricted permissions, narrowly scoped policy, rollback, and lab integration testing.
