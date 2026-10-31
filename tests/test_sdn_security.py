import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from sdn_security import extract_failed_login_ips, build_review_proposals, serialize_proposals

class HoneypotTests(unittest.TestCase):
    def test_deduplication(self):
        lines = "login failed 192.0.2.15\nFAILED 192.0.2.15\nlogin ok 198.51.100.2\nfailed 203.0.113.5"
        self.assertEqual(extract_failed_login_ips(lines), ["192.0.2.15", "203.0.113.5"])
    def test_invalid_address(self):
        self.assertEqual(extract_failed_login_ips("failed 999.2.3.4"), [])
    def test_review_only(self):
        item = build_review_proposals(["192.0.2.15"], "s2")[0]
        self.assertEqual(item.action, "REVIEW_FOR_BLOCK")
        self.assertIn("192.0.2.15", serialize_proposals([item]))

if __name__ == "__main__":
    unittest.main()
