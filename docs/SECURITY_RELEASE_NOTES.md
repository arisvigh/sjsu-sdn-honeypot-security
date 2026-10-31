# Secure archival release notes

The two legacy controller scripts have been reviewed and sanitized offline, but have **not been committed to this repository** because automated publication was blocked. Their release package is available separately from the project discussion.

Changes in sanitized copies:
- Removed embedded administrator credentials; use `ODL_USERNAME` and `ODL_PASSWORD` environment variables.
- Replaced fixed controller address with `ODL_CONTROLLER_HOST`.
- Replaced fixed Kippo log paths with `KIPPO_LOG_PATH`.
- Removed an interactive debugger statement and disabled destructive log truncation.
- Required explicit `ENABLE_LEGACY_FLOW_WRITES=I_UNDERSTAND` in an isolated test environment before controller writes.
- Added `.env.example` and `.gitignore` rules for local secrets and logs.

**Important:** These are Python 2-era historical demonstrations, not audited, modernized, or verified operational security software. Some legacy HTTP/controller assumptions remain. Avoid running them on production networks. A safe modern implementation needs substantial redesign, validation and authorization controls.

The sanitized files must still be reviewed locally before public upload. The source file `src/network_topology.py` is already published.
