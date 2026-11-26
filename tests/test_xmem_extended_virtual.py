"""Tests for TitleVirtualAllocEx and XMem extended virtual shims (RT-XMEM-EXTENDED-VIRTUAL)."""
import os
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class XMemExtendedVirtualTest(unittest.TestCase):
    def test_xmem_extended_shims_present(self):
        xmem_path = os.path.join(ROOT, "runtime", "shims", "xmem.cpp")
        self.assertTrue(os.path.exists(xmem_path), "xmem.cpp must exist")
        with open(xmem_path, "r", encoding="utf-8") as f:
            content = f.read()

        for symbol in [
            "TitleVirtualAllocEx",
            "TitleVirtualProtectEx",
            "TitleVirtualQuery",
            "TitleVirtualQueryEx",
            "XMemVirtualFree",
            "XMemVirtualProtect",
            '"VirtualAllocEx"',
            '"VirtualProtectEx"',
            '"VirtualQuery"',
            '"VirtualQueryEx"',
            '"XMemVirtualFree"',
            '"XMemVirtualProtect"',
        ]:
            self.assertIn(symbol, content, f"Expected {symbol} in xmem.cpp")


if __name__ == "__main__":
    unittest.main()
