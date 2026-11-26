"""Tests for UCRT environment shims and TerminateProcess routing (RT-UCRT-ENV-TERMINATE-PROCESS)."""
import os
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class UcrtProcessShimsTest(unittest.TestCase):
    def test_ucrt_process_shims_present(self):
        process_path = os.path.join(ROOT, "runtime", "shims", "process.cpp")
        self.assertTrue(os.path.exists(process_path), "process.cpp must exist")
        with open(process_path, "r", encoding="utf-8") as f:
            content = f.read()

        for symbol in [
            "game_terminate_process",
            "game_initialize_narrow_environment",
            "game_initialize_wide_environment",
            "game_get_initial_narrow_environment",
            "game_get_initial_wide_environment",
            "game_register_thread_local_exe_atexit_callback",
            "game_set_app_type",
            '"TerminateProcess"',
            '"_initialize_narrow_environment"',
            '"api-ms-win-core-processthreads-l1-1-3.dll"',
            '"api-ms-win-core-processenvironment-l1-2-0.dll"',
        ]:
            self.assertIn(symbol, content, f"Expected {symbol} in process.cpp")


if __name__ == "__main__":
    unittest.main()
