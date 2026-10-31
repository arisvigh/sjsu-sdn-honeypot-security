# Security release notes

## Public repository status

- Original, unchanged 2015 Mininet topology: [`archive/2015/network_topology.py`](../archive/2015/network_topology.py).
- Original controller / attack-response scripts: **not published** in this repository. Historical copies include demonstration credentials, HTTP-based controller requests and fixed lab settings.
- Modern Python 3 replacements: [`src/HoneypotInSDN.py`](../src/HoneypotInSDN.py), [`src/AutomatedScriptOnAttack.py`](../src/AutomatedScriptOnAttack.py) and [`src/sdn_security.py`](../src/sdn_security.py).

## 2026 security design

The modern scripts parse a configurable local honeypot log, validate and deduplicate IPs, and emit JSON proposals for human review. No controller URL or credentials are needed because these modules have **no network-writing functionality**. Log processing does not truncate or modify its input. `.gitignore` excludes environment files and logs. `.env.example` remains an illustrative legacy configuration reference; the read-only scripts only use `KIPPO_LOG_PATH` and `SDN_SWITCH_ID`.

The modern code should not be described as a patched, drop-in equivalent to the historic flow programmer. An actual network enforcement component would require separate, tested implementation with authenticated TLS, restrictive permissions and explicit operator approvals.

See [modernization details](PYTHON3_MODERNIZATION.md).
