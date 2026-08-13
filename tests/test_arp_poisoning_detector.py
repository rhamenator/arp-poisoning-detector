import io
import unittest
from contextlib import redirect_stdout

from arp_poisoning_detector import check_for_arp_poisoning, parse_arp_table


class ArpDetectorTests(unittest.TestCase):
    def test_parser_accepts_hyphenated_and_colon_separated_addresses(self):
        entries = parse_arp_table(
            "192.0.2.1 aa-bb-cc-dd-ee-ff dynamic\n"
            "192.0.2.2 aa:bb:cc:dd:ee:00 dynamic\n"
        )
        self.assertEqual(2, len(entries))

    def test_parser_ignores_unrelated_lines(self):
        self.assertEqual([], parse_arp_table("Interface: example\nnot an arp row\n"))

    def test_conflicting_mac_addresses_are_reported(self):
        output = io.StringIO()
        with redirect_stdout(output):
            detected = check_for_arp_poisoning(
                [
                    ("192.0.2.10", "aa-bb-cc-dd-ee-ff", "dynamic"),
                    ("192.0.2.10", "11-22-33-44-55-66", "dynamic"),
                ]
            )
        self.assertTrue(detected)
        self.assertIn("Potential ARP poisoning", output.getvalue())

    def test_repeated_identical_mapping_is_not_reported(self):
        output = io.StringIO()
        with redirect_stdout(output):
            detected = check_for_arp_poisoning(
                [
                    ("192.0.2.10", "aa-bb-cc-dd-ee-ff", "dynamic"),
                    ("192.0.2.10", "aa-bb-cc-dd-ee-ff", "dynamic"),
                ]
            )
        self.assertFalse(detected)
        self.assertIn("not detected", output.getvalue())

    def test_invalid_mac_is_ignored(self):
        self.assertFalse(check_for_arp_poisoning([("192.0.2.1", "invalid", "dynamic")]))


if __name__ == "__main__":
    unittest.main()
