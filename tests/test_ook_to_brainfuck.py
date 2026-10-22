from pathlib import Path
import unittest

from tools.ook_to_brainfuck import translate


ROOT = Path(__file__).resolve().parents[1]


class OokTranslationTests(unittest.TestCase):
    def test_all_instruction_pairs(self):
        source = (
            "Ook. Ook? Ook? Ook. Ook. Ook. Ook! Ook! "
            "Ook. Ook! Ook! Ook. Ook! Ook? Ook? Ook! Ook? Ook?"
        )
        self.assertEqual(translate(source), "><+-,.[]")

    def test_example_matches_brainfuck_source(self):
        ook = (ROOT / "examples/ook/hello.ook").read_text()
        brainfuck = (ROOT / "examples/brainfuck/hello.bf").read_text()
        expected = "".join(c for c in brainfuck if c in "><+-,.[]")
        self.assertEqual(translate(ook), expected)

    def test_nested_loops(self):
        self.assertEqual(
            translate("Ook! Ook? Ook! Ook? Ook? Ook! Ook? Ook!"), "[[]]"
        )

    def test_whitespace_and_empty_source(self):
        self.assertEqual(translate(" \n\t"), "")
        self.assertEqual(translate("Ook.\n\tOok."), "+")

    def test_invalid_sources(self):
        for source in (
            "Ook.", "Ook Ook.", "Ook. Ook. garbage", "ook. ook.",
            "Ook! Ook?", "Ook? Ook!", "Ook? Ook! Ook! Ook?",
        ):
            with self.subTest(source=source), self.assertRaises(ValueError):
                translate(source)


if __name__ == "__main__":
    unittest.main()
