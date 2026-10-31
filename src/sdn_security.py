"""Read-only SDN honeypot demonstration utilities (Python 3.13+)."""
from dataclasses import asdict, dataclass
from ipaddress import IPv4Address, ip_address
from pathlib import Path
import json
import re

CANDIDATES = re.compile(r"(?<![\w.])(?:\d{1,3}\.){3}\d{1,3}(?![\w.])")

@dataclass(frozen=True)
class FlowProposal:
    source_ip: str
    switch_id: str
    action: str = "REVIEW_FOR_BLOCK"

def extract_failed_login_ips(log_text: str) -> list[str]:
    seen = set()
    ips = []
    for line in log_text.splitlines():
        if "failed" not in line.casefold():
            continue
        for match in CANDIDATES.finditer(line):
            try:
                ip = ip_address(match.group())
            except ValueError:
                continue
            if isinstance(ip, IPv4Address) and str(ip) not in seen:
                seen.add(str(ip))
                ips.append(str(ip))
    return ips

def read_honeypot_log(path: str | Path) -> list[str]:
    return extract_failed_login_ips(Path(path).read_text(encoding="utf-8", errors="replace"))

def build_review_proposals(ips: list[str], switch_id: str) -> list[FlowProposal]:
    if not switch_id:
        raise ValueError("switch_id is required")
    return [FlowProposal(str(ip_address(ip)), switch_id) for ip in ips]

def serialize_proposals(proposals: list[FlowProposal]) -> str:
    return json.dumps([asdict(p) for p in proposals], indent=2)
