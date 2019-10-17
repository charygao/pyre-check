# pyre-ignore-all-errors

import unittest
from typing import Dict, List

from .. import safe_json


class BasicTestCase(unittest.TestCase):
    def test_loads(self):
        # Lists.
        self.assertEqual(safe_json.loads("[]", List[int]), [])
        self.assertEqual(safe_json.loads("[1]", List[int]), [1])
        self.assertEqual(safe_json.loads("[1, 2]", List[int]), [1, 2])

        self.assertEqual(
            safe_json.loads('[{"1": 1}]', List[Dict[str, int]]), [{"1": 1}]
        )

        with self.assertRaises(safe_json.InvalidJson):
            safe_json.loads("[1, 'string']", List[int])

        # Dictionaries.
        self.assertEqual(safe_json.loads("{}", Dict[int, str]), {})
        self.assertEqual(safe_json.loads('{"1": 1}', Dict[str, int]), {"1": 1})

        with self.assertRaises(safe_json.InvalidJson):
            safe_json.loads('{"1": "string"}', Dict[str, int])
        with self.assertRaises(safe_json.InvalidJson):
            safe_json.loads('{"1": 1, "2": "2"}', Dict[str, int])

        self.assertEqual(
            safe_json.loads('{"1": {"2": 3}}', Dict[str, Dict[str, int]]),
            {"1": {"2": 3}},
        )


if __name__ == "__main__":
    unittest.main()