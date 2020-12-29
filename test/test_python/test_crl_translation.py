import sys
from pathlib import Path
workspace_directory = Path(Path(__file__).parent.parent.parent)
sys.path.insert(0, str(workspace_directory))


from scripts.crl.translation import (
    translation
)
from scripts.crl.crl_grammar import (
    dynamic_crl_grammar
)
from scripts.crl.syntactic_parser import (
    BottomUpChartParser
)


import unittest

from nltk import (
    word_tokenize
)

from nltk.tree import (
    Tree
)


class Test_Translation(unittest.TestCase):
    def test_translation(self):
        inputs_ = [
            (
                "There is an apple.",
                "There is an apple ."
            ),
            (
                "Please move the apple.",
                "the robot move the apple ."
            ),
            (
                "move the apple.",
                "the robot move the apple ."
            ),

            (
                "slowly move the apple.",
                "the robot slowly move the apple ."
            ),
        ]

        for i, (input_, expect_) in enumerate(inputs_):
            tokenized = word_tokenize(input_)
            grammar = dynamic_crl_grammar(tokenized)
            parser = BottomUpChartParser(grammar)
            result = parser.parse(tokenized)
            trans_ = translation(result)
            trans_ = " ".join(trans_)
            error_msg = "Sentence {}-th: '{}' / Expect: <{}> . Actual: <{}>".format(
                i, input_, expect_, trans_)
            self.assertEqual(expect_, trans_, error_msg)


if __name__ == "__main__":
    unittest.main()
