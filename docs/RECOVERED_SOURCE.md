# Recovered historical source and modern reconstruction

## 2015 archive

[`archive/2015/network_topology.py`](../archive/2015/network_topology.py) is an unchanged copy of the recovered Mininet topology. It defines five switches and nine hosts attached to each of switches s2–s5 (36 hosts total), with eight inter-switch links. Its header states ten hosts per switch, but the executable code differs.

Two additional Python 2-era controller scripts were provided for review: `HoneypotInSDN.py` and `AutomatedScriptOnAttack.py`. **Their original copies are not in this public repository.** They have obsolete REST integrations and embedded demonstration settings. The submitted scripts show named flow updates, but do not demonstrate precise source-IP matches for the proposed DROP rules.

## 2026 reconstruction

[`src/HoneypotInSDN.py`](../src/HoneypotInSDN.py) and [`src/AutomatedScriptOnAttack.py`](../src/AutomatedScriptOnAttack.py) reuse the **filenames** of two historical scripts, but are **new, read-only Python 3 replacements**, supported by `src/sdn_security.py`. They parse logs and emit review proposals. They **do not** contact OpenDaylight, provision topology, or install network flows.

See [modernization notes](PYTHON3_MODERNIZATION.md) and [security release notes](SECURITY_RELEASE_NOTES.md). This is documentation of a student-team project, not an attribution of all code to any one participant. No modern controller integration has been validated.
