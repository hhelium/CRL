import sys
from pathlib import Path
workspace_directory = Path(Path(__file__).parent.parent.parent)
sys.path.insert(0, str(workspace_directory))

from scripts.crl.pos_tagger import (
    SpacySequentialTagger,
)

import unittest


class Test_Spacy_Tagger(unittest.TestCase):
    def test_pos_tagging(self):
        inputs_ = [
            (
                ["Apple", "is", "looking", "at", "buying", "UK",
                 "startup", "for", "$", "1", "billion"],
                ["NNP", "VBZ", "VBG", "IN", "VBG",
                    "NNP", "NN", "IN", "$", "CD", "CD"]
            )

        ]
        tagger = SpacySequentialTagger()
        for i, (input_, expect_) in enumerate(inputs_):
            word_tag_pairs = tagger.tag(input_)
            tags = [t for w, t in word_tag_pairs]
            error_msg = "Spacy's result: {} / Expect: {}".format(tags, expect_)
            self.assertEqual(tags, expect_, error_msg)


if __name__ == "__main__":
    unittest.main()
