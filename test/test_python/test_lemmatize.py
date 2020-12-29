import sys
from pathlib import Path
workspace_directory = Path(Path(__file__).parent.parent.parent)
sys.path.insert(0, str(workspace_directory))


from scripts.lemmatize.lemmatizer import (
    conjugate_singularize,
    conjugate_pluralize,
    SpacyLemmatizer
)

import unittest


class Test_Conjugate_Verb(unittest.TestCase):
    def test_singularize_verb(self):
        inputs_ = [
            (
                "move",
                "moves"
            ),
            (
                "pick",
                "picks"
            )
        ]

        for i, (input_, expect_) in enumerate(inputs_):
            singularized_verb = conjugate_singularize(input_)
            error_msg = "Sentence {}-th: '{}'. Expect: <{}> / Actual: <{}>".format(
                i, input_, expect_, singularized_verb)
            self.assertEqual(expect_, singularized_verb, error_msg)

    def test_pluralize_verb(self):
        inputs_ = [
            (
                "moves",
                "move"
            ),
            (
                "picks",
                "pick"
            )
        ]

        for i, (input_, expect_) in enumerate(inputs_):
            singularized_verb = conjugate_pluralize(input_)
            error_msg = "Sentence {}-th: '{}'. Expect: <{}> / Actual: <{}>".format(
                i, input_, expect_, singularized_verb)
            self.assertEqual(expect_, singularized_verb, error_msg)


class Test_Conjugate_Adj(unittest.TestCase):
    def test_adj_comparative_lemmatizer(self):
        inputs_ = [
            (
                "higher",
                "high"
            ),
            (
                "bigger",
                "big"
            )
        ]
        lemmatizer = SpacyLemmatizer()
        for i, (input_, expect_) in enumerate(inputs_):
            lemma = lemmatizer.lemmatize(input_)
            error_msg = "Sentence {}-th -- '{}'. Expect: <{}> / Actual: <{}>".format(
                i, input_, expect_, lemma)
            self.assertEqual(expect_, lemma, error_msg)


if __name__ == "__main__":
    unittest.main()
