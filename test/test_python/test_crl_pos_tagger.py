import sys
from pathlib import Path
workspace_directory = Path(Path(__file__).parent.parent.parent)
sys.path.insert(0, str(workspace_directory))

from scripts.crl.pos_tagger import (
    SpacySequentialTagger,
    DynamicSequentialTagger,
    StaticSequentialTagger,
    CascadeTagger,
    word_tokenize
)

import unittest


class Test_Component_Taggers(unittest.TestCase):
    def test_spacy_pos_tagging(self):
        inputs_ = [
            (
                ["Apple", "is", "looking", "at", "buying", "UK",
                 "startup", "for", "$", "1", "billion"],
                ["NNP", "VBZ", "VBG", "IN", "VBG",
                    "NNP", "NN", "IN", "$", "CD", "CD"]
            ),
            (
                ["'s"], ["POS"]
            ),

        ]
        tagger = SpacySequentialTagger()
        for i, (input_, expect_) in enumerate(inputs_):
            word_tag_pairs = tagger.tag(input_)
            tags = [t for w, t in word_tag_pairs]
            error_msg = "Spacy's result: {} / Expect: {} -- at {}-th sentence: {}".format(
                tags, expect_, i, input_)
            self.assertEqual(tags, expect_, error_msg)

    def test_dynamic_pos_tagging(self):
        inputs_ = [
            (
                ["pick"], ["VB"]
            ),
            (
                ["picks"], ["VBZ"]
            ),
            (
                ["moves"], ["VBZ"]
            ),

        ]
        tagger = DynamicSequentialTagger()
        for i, (input_, expect_) in enumerate(inputs_):
            word_tag_pairs = tagger.tag(input_)
            tags = [t for w, t in word_tag_pairs]
            error_msg = "Dynamic's result: {} / Expect: {} -- at sentence {}-th --'{}'".format(
                tags, expect_, i, input_)
            self.assertEqual(tags, expect_, error_msg)

    def test_static_pos_tagging(self):
        inputs_ = [
            (
                ["Which"], ["WHICH"]
            ),
            (
                ["Who"], ["WHO"]
            ),
            (
                ["Where"], ["WHERE"]
            ),
            (
                ["How"], ["HOW"]
            ),
            (
                ["She"], ["SHE"]
            ),
            (
                ["he"], ["HE"]
            ),
            (
                ["Her"], ["HER"]
            ),
            (
                ["his"], ["HIS"]
            ),
            (
                ["That"], ["THAT"]
            ),

            (
                ["And"], ["AND"]
            ),
            (
                ["Or"], ["OR"]
            ),
            (
                ["As"], ["AS"],
            ),
            (
                ["Than"], ["THAN"],
            ),
            (
                ["Much"], ["MUCH"],
            ),
            (
                ["More"], ["MORE"],
            ),
            (
                ["Most"], ["MOST"],
            ),
            (
                ["By"], ["BY"],
            ),
            (
                ["There"], ["THERE"],
            ),

            (
                ["If"], ["IF"],
            ),

            (
                ["Then"], ["THEN"],
            ),

            (
                ["Not"], ["NOT"],
            ),

            (
                ["?"], ["QUESTION"]
            ),
            (
                ["!"], ["EXCLAM"]
            ),
            (
                ["."], ["PERIOD"]
            ),
            (
                [","], ["COMMA"]
            ),
            (
                [":"], ["COLON"]
            ),
            (
                ["To"], ["TO"]
            ),
            (
                ["Among"], ["IN"]
            ),
            (
                ["Over"], ["IN"]
            ),
            (
                ["Back"], ["IN"]
            ),
            (
                ["One"], ["IN"]
            ),
            (
                ["Down"], ["IN"]
            ),
            (
                ["Way"], ["IN"]
            ),
            (
                ["Through"], ["IN"]
            ),
            (
                ["Against"], ["IN"]
            ),
            (
                ["In"], ["IN"]
            ),
            (
                ["Beyond"], ["IN"]
            ),
            (
                ["Open"], ["IN"]
            ),
            (
                ["Between"], ["IN"]
            ),
            (
                ["Out"], ["IN"]
            ),
            (
                ["Even"], ["IN"]
            ),
            (
                ["Aback"], ["IN"]
            ),
            (
                ["From"], ["FROM"]
            ),
            (
                ["For"], ["IN"]
            ),
            (
                ["Away"], ["IN"]
            ),
            (
                ["Aside"], ["IN"]
            ),
            (
                ["Behind"], ["IN"]
            ),
            (
                ["Above"], ["IN"]
            ),
            (
                ["Under"], ["IN"]
            ),
            (
                ["Forward"], ["IN"]
            ),
            (
                ["Before"], ["IN"]
            ),
            (
                ["Forth"], ["IN"]
            ),
            (
                ["Into"], ["IN"]
            ),
            (
                ["Towards"], ["IN"]
            ),
            (
                ["Around"], ["IN"]
            ),
            (
                ["After"], ["IN"]
            ),
            (
                ["Upon"], ["IN"]
            ),
            (
                ["Along"], ["IN"]
            ),
            (
                ["With"], ["IN"]
            ),

            (
                ["Apart"], ["IN"]
            ),
            (
                ["On"], ["IN"]
            ),
            (
                ["About"], ["IN"]
            ),
            (
                ["Off"], ["IN"]
            ),
            (
                ["Ahead"], ["IN"]
            ),
            (
                ["Past"], ["IN"]
            ),
            (
                ["Up"], ["IN"]
            ),
            (
                ["Together"], ["IN"]
            ),
            (
                ["Across"], ["IN"]
            ),
            (
                ["Below"], ["IN"]
            ),
            (
                ["Without"], ["IN"]
            ),
            (
                ["Toward"], ["IN"]
            ),
            (
                ["Onto"], ["IN"]
            ),
            (
                ["Round"], ["IN"]
            ),
            (
                ["At"], ["IN"]
            ),

            (
                ["of"], ["POS_of"]
            ),
            (
                ["Am"], ["AUX"]
            ),
            (
                ["Is"], ["AUX"]
            ),
            (
                ["Are"], ["AUX"]
            ),
            (
                ["Be"], ["AUX"]
            ),
            (
                ["Do"], ["AUX_DO"]
            ),
            (
                ["Does"], ["AUX_DO"]
            ),

            (
                ["Please"], ["PLEASE"]
            ),

            (
                ["No"], ["NO"]
            ),

            # * Measurement tags:
            (
                ["Kg"], ["MN"]
            ),
            (
                ["g"], ["MN"]
            ),
            (
                ["Celsius"], ["MN"]
            ),
            (
                ["Fahrenheit"], ["MN"]
            ),
            (
                ["ton"], ["MN"]
            ),
            (
                ["cup"], ["MN"]
            ),
            (
                ["degree"], ["MN"]
            ),
            (
                ["minute"], ["MN"]
            ),
            (
                ["hour"], ["MN"]
            ),
            (
                ["qt"], ["MN"]
            ),
            (
                ["lbs"], ["MN"]
            ),
            (
                ["pound"], ["MN"]
            ),

            # * Variables
            (
                ["X9"], ["VAR"]
            ),
            (
                ["X"], ["VAR"]
            ),
            (
                ["Y"], ["VAR"]
            ),
            (
                ["Z"], ["VAR"]
            ),
            (
                ["Z99"], ["VAR"]
            ),

            # * POS used for lexical analysis
            (
                ["Your"], ["YOUR"]
            ),
            (
                ["you"], ["YOU"]
            ),

            (
                ["We"], ["WE"]
            ),
            (
                ["Our"], ["OUR"]
            ),
            (
                ["I"], ["I"]
            ),
            (
                ["My"], ["MY"]
            ),
        ]
        tagger = StaticSequentialTagger()
        for i, (input_, expect_) in enumerate(inputs_):
            word_tag_pairs = tagger.tag(input_)
            tags = [t for w, t in word_tag_pairs]
            error_msg = "Static's result: {} / Expect: {} -- at sentence {}-th --'{}'".format(
                tags, expect_, i, input_)
            self.assertEqual(tags, expect_, error_msg)

    def test_cascade_pos_tagging(self):
        inputs_ = [
            (
                ['A', 'robot', 'runs', '.'],
                ['DET', 'NN', 'VBZ', 'PERIOD']
            ),
            (
                ['A', 'robot', 'runs', 'slowly', '.'],
                ['DET', 'NN', 'VBZ', 'RB', 'PERIOD']
            ),
            (
                ['A', 'robot', 'throws', 'an', 'apple', '.'],
                ['DET', 'NN', 'VBZ', 'DET', 'NN', 'PERIOD']
            ),
            (
                ['A', 'robot', 'throws', 'an', 'apple', 'slowly', '.'],
                ['DET', 'NN', 'VBZ', 'DET', 'NN', 'RB', 'PERIOD']
            ),
            (
                ['A', 'robot', 'throws', 'an', 'red', 'apple', 'slowly', '.'],
                ['DET', 'NN', 'VBZ', 'DET', 'JJ', 'NN', 'RB', 'PERIOD']
            ),
            (
                ['A', 'robot', 'throws', 'an', 'small',
                 'and', 'red', 'apple', 'slowly', '.'],
                ['DET', 'NN', 'VBZ', 'DET', 'JJ',
                 'AND', 'JJ', 'NN', 'RB', 'PERIOD']
            ),
            (
                ['A', 'robot', 'throws', 'an', 'small', 'and', 'red',
                 'apple', 'slowly', 'under', 'the', 'table', '.'],
                ['DET', 'NN', 'VBZ', 'DET', 'JJ', 'AND', 'JJ',
                 'NN', 'RB', 'IN', 'DET', 'NN', 'PERIOD']
            ),
            (
                ['A', 'robot', 'under', 'the', 'table', 'throws', 'an',
                 'small', 'and', 'red', 'apple', 'slowly', '.'],
                ['DET', 'NN', 'IN', 'DET', 'NN', 'VBZ', 'DET',
                 'JJ', 'AND', 'JJ', 'NN', 'RB', 'PERIOD']
            ),
            (
                ['A', 'robot', 'moves', 'slowly', '.'],
                ['DET', 'NN', 'VBZ', 'RB', 'PERIOD']
            ),
            (
                ['The', 'robot', 'can', 'capture', 'the',
                 'red', 'apple', 'on', 'the', 'table', '.'],
                ['DET', 'NN', 'MD', 'VB', 'DET',
                 'JJ', 'NN', 'IN', 'DET', 'NN', 'PERIOD'],
            ),
            (
                ['John', 'runs', '.'],
                ['NNP', 'VBZ', 'PERIOD']
            ),
            (
                ['John', 'runs', 'slowly', '.'],
                ['NNP', 'VBZ', 'RB', 'PERIOD']
            ),
            (
                ['John', 'throws', 'an', 'apple', '.'],
                ['NNP', 'VBZ', 'DET', 'NN', 'PERIOD']
            ),
            (
                ['John', 'throws', 'an', 'apple', 'slowly', '.'],
                ['NNP', 'VBZ', 'DET', 'NN', 'RB', 'PERIOD']
            ),
            (
                ['John', 'throws', 'an', 'red', 'apple', 'slowly', '.'],
                ['NNP', 'VBZ', 'DET', 'JJ', 'NN', 'RB', 'PERIOD']
            ),
            (
                ['John', 'throws', 'an', 'red', 'apple',
                 'slowly', 'under', 'the', 'table', '.'],
                ['NNP', 'VBZ', 'DET', 'JJ', 'NN',
                 'RB', 'IN', 'DET', 'NN', 'PERIOD']
            ),
            (
                ['John', 'moves', 'slowly', '.'],
                ['NNP', 'VBZ', 'RB', 'PERIOD']
            ),
            (
                ['The', 'robot', 'which', 'is', 'an', 'agent', 'throws', 'an',
                    'red', 'apple', 'slowly', 'under', 'the', 'table', '.'],
                ['DET', 'NN', 'WHICH', 'AUX', 'DET', 'NN', 'VBZ', 'DET',
                    'JJ', 'NN', 'RB', 'IN', 'DET', 'NN', 'PERIOD']
            ),
            (
                ['There', 'is', 'a', 'small', 'and', 'red', 'orange', '.'],
                ["THERE", "AUX", "DET", "JJ", "AND", "JJ", "NN", "PERIOD"]
            ),
            (
                ['She', 'runs', '.'],
                ['SHE', 'VBZ', 'PERIOD']
            ),
            (
                ['She', 'runs', 'slowly', '.'],
                ['SHE', 'VBZ', 'RB', 'PERIOD'],
            ),
            (
                ['She', 'throws', 'an', 'apple', '.'],
                ['SHE', 'VBZ', 'DET', 'NN', 'PERIOD'],
            ),
            (
                ['She', 'throws', 'an', 'apple', 'slowly', '.'],
                ['SHE', 'VBZ', 'DET', 'NN', 'RB', 'PERIOD']
            ),
            (
                ['She', 'throws', 'an', 'red', 'apple', 'slowly', '.'],
                ['SHE', 'VBZ', 'DET', 'JJ', 'NN', 'RB', 'PERIOD']
            ),
            (
                ['She', 'throws', 'an', 'red', 'apple',
                 'slowly', 'under', 'the', 'table', '.'],
                ['SHE', 'VBZ', 'DET', 'JJ', 'NN',
                 'RB', 'IN', 'DET', 'NN', 'PERIOD'],
            ),
            (
                ['She', 'moves', 'slowly', '.'],
                ['SHE', 'VBZ', 'RB', 'PERIOD'],
            ),
            (
                ['A', 'small', 'robot', 'runs', '.'],
                ['DET', 'JJ', 'NN', 'VBZ', 'PERIOD'],
            ),
            (
                ['A', 'small', 'robot', 'runs', 'slowly', '.'],
                ['DET', 'JJ', 'NN', 'VBZ', 'RB', 'PERIOD'],
            ),
            (
                ['A', 'small', 'robot', 'throws', 'an', 'apple', '.'],
                ['DET', 'JJ', 'NN', 'VBZ', 'DET', 'NN', 'PERIOD'],
            ),
            (
                ['A', 'small', 'robot', 'throws', 'an', 'apple', 'slowly', '.'],
                ['DET', 'JJ', 'NN', 'VBZ', 'DET', 'NN', 'RB', 'PERIOD'],
            ),
            (
                ['A', 'small', 'and', 'green', 'robot',
                    'throws', 'an', 'apple', '.'],
                ['DET', 'JJ', 'AND', 'JJ', 'NN',
                    'VBZ', 'DET', 'NN', 'PERIOD'],
            ),
            (
                ['A', 'small', 'and', 'green', 'robot',
                 'throws', 'an', 'apple', 'slowly', '.'],
                ['DET', 'JJ', 'AND', 'JJ', 'NN',
                 'VBZ', 'DET', 'NN', 'RB', 'PERIOD'],
            ),
            (
                ['John', "'s", 'robot', 'runs', '.'],
                ['NNP', "POS", 'NN', 'VBZ', 'PERIOD'],
            ),
            # - (
            # -     ['John', "'s", 'robot', 'runs', 'slowly', '.'],
            # - ),
            # - (
            # -     ['John', "'s", 'robot', 'throws', 'an', 'apple', '.'],
            # - ),
            # - (
            # -     ['John', "'s", 'robot', 'throws', 'an', 'apple', 'slowly', '.'],
            # - ),
            # - (
            # -     ['John', "'s", 'robot', 'throws', 'an',
            # -         'red', 'apple', 'slowly', '.'],
            # - ),
            # - (
            # -     ['John', "'s", 'robot', 'throws', 'an', 'red',
            # -      'apple', 'slowly', 'under', 'the', 'table', '.'],
            # - ),
            # - (
            # -     ['John', "'s", 'robot', 'moves', 'slowly', '.'],
            # - ),
            # - (
            # -     ['John', "'s", 'small', 'robot', 'runs', '.'],
            # - ),
            # - (
            # -     ['John', "'s", 'small', 'robot', 'runs', 'slowly', '.'],
            # - ),
            # - (
            # -     ['John', "'s", 'small', 'robot', 'throws', 'an', 'apple', '.'],
            # - ),
            # - (
            # -     ['John', "'s", 'small', 'robot', 'throws',
            # -         'an', 'apple', 'slowly', '.'],
            # - ),
            # - (
            # -     ['John', "'s", 'small', 'robot', 'throws',
            # -      'an', 'red', 'apple', 'slowly', '.'],
            # - ),
            # - (
            # -     ['John', "'s", 'small', 'robot', 'throws', 'an', 'red',
            # -      'apple', 'slowly', 'under', 'the', 'table', '.'],
            # - ),
            # - (
            # -     ['John', "'s", 'small', 'robot', 'moves', 'slowly', '.'],
            # - ),
            # - (
            # -     ['The', 'company', "'s", 'robot', 'runs', '.'],
            # - ),
            # - (
            # -     ['The', 'company', "'s", 'robot', 'runs', 'slowly', '.'],
            # - ),
            # - (
            # -     ['The', 'company', "'s", 'robot', 'throws', 'an', 'apple', '.'],
            # - ),
            # - (
            # -     ['The', 'company', "'s", 'robot', 'throws',
            # -         'an', 'apple', 'slowly', '.'],
            # - ),
            # - (
            # -     ['The', 'company', "'s", 'robot', 'throws',
            # -      'an', 'red', 'apple', 'slowly', '.'],
            # - ),
            # - (
            # -     ['The', 'company', "'s", 'robot', 'throws', 'an', 'red',
            # -      'apple', 'slowly', 'under', 'the', 'table', '.'],
            # - ),
            # - (
            # -     ['The', 'company', "'s", 'robot', 'moves', 'slowly', '.'],
            # - ),
            # - (
            # -     ['The', 'robot', 'of', 'the', 'company', 'runs', '.'],
            # - ),
            # - (
            # -     ['The', 'robot', 'of', 'the', 'company', 'runs', 'slowly', '.'],
            # - ),
            # - (
            # -     ['The', 'robot', 'of', 'the', 'company',
            # -         'throws', 'an', 'apple', '.'],
            # - ),
            # - (
            # -     ['The', 'robot', 'of', 'the', 'company',
            # -      'throws', 'an', 'apple', 'slowly', '.'],
            # - ),
            # - (
            # -     ['The', 'robot', 'of', 'the', 'company', 'throws',
            # -      'an', 'red', 'apple', 'slowly', '.'],
            # - ),
            # - (
            # -     ['The', 'robot', 'of', 'the', 'company', 'throws', 'an',
            # -      'red', 'apple', 'slowly', 'under', 'the', 'table', '.'],
            # - ),
            # - (
            # -     ['The', 'robot', 'of', 'the', 'company', 'moves', 'slowly', '.'],
            # - ),
            # - (
            # -     ['The', 'robot', 'of', 'company', 'runs', '.'],
            # - ),
            # - (
            # -     ['The', 'robot', 'of', 'company', 'runs', 'slowly', '.'],
            # - ),
            # - (
            # -     ['The', 'robot', 'of', 'company', 'throws', 'an', 'apple', '.'],
            # - ),
            # - (
            # -     ['The', 'robot', 'of', 'company', 'throws',
            # -         'an', 'apple', 'slowly', '.'],
            # - ),
            # - (
            # -     ['The', 'robot', 'of', 'company', 'throws',
            # -      'an', 'red', 'apple', 'slowly', '.'],
            # - ),
            # - (
            # -     ['The', 'robot', 'of', 'company', 'throws', 'an', 'red',
            # -      'apple', 'slowly', 'under', 'the', 'table', '.'],
            # - ),
            # - (
            # -     ['The', 'robot', 'of', 'company', 'moves', 'slowly', '.'],
            # - ),
            # - (
            # -     ['The', 'robot', 'which', 'is', 'an', 'agent', 'runs', '.'],
            # - ),
            # - (
            # -     ['The', 'robot', 'which', 'is', 'an',
            # -         'agent', 'runs', 'slowly', '.'],
            # - ),
            # - (
            # -     ['The', 'robot', 'which', 'is', 'an',
            # -      'agent', 'throws', 'an', 'apple', '.'],
            # - ),
            # - (
            # -     ['The', 'robot', 'which', 'is', 'an', 'agent',
            # -      'throws', 'an', 'apple', 'slowly', '.'],
            # - ),
            # - (
            # -     ['The', 'robot', 'which', 'is', 'an', 'agent',
            # -      'throws', 'an', 'red', 'apple', 'slowly', '.'],
            # - ),
            # - (
            # -     ['The', 'robot', 'which', 'is', 'an', 'agent', 'throws', 'an',
            # -      'red', 'apple', 'slowly', 'under', 'the', 'table', '.'],
            # - ),
            # - (
            # -     ['The', 'robot', 'which', 'is', 'an',
            # -         'agent', 'moves', 'slowly', '.'],
            # - ),
            # - (
            # -     ['John', 'who', 'is', 'an', 'agent', 'runs', '.'],
            # - ),
            # - (
            # -     ['John', 'who', 'is', 'an', 'agent', 'runs', 'slowly', '.'],
            # - ),
            # - (
            # -     ['John', 'who', 'is', 'an', 'agent', 'throws', 'an', 'apple', '.'],
            # - ),
            # - (
            # -     ['John', 'who', 'is', 'an', 'agent',
            # -      'throws', 'an', 'apple', 'slowly', '.'],
            # - ),
            # - (
            # -     ['John', 'who', 'is', 'an', 'agent', 'throws',
            # -      'an', 'red', 'apple', 'slowly', '.'],
            # - ),
            # - (
            # -     ['John', 'who', 'is', 'an', 'agent', 'throws', 'an', 'red',
            # -      'apple', 'slowly', 'under', 'the', 'table', '.'],
            # - ),
            # - (
            # -     ['John', 'who', 'is', 'an', 'agent', 'moves', 'slowly', '.'],
            # - ),
            # - (
            # -     ['The', 'robot', 'runs', '.'],
            # - ),
            # - (
            # -     ['The', 'robot', 'runs', 'slowly', '.'],
            # - ),
            # - (
            # -     ['The', 'robot', 'throws', '3', 'kg', 'of', 'apple', '.'],
            # - ),
            # - (
            # -     ['The', 'robot', 'throws', '3', 'kg', 'of', 'apple', 'slowly', '.'],
            # - ),
            # - (
            # -     ['The', 'robot', 'throws', '3', 'kg',
            # -      'of', 'red', 'apple', 'slowly', '.'],
            # - ),
            # - (
            # -     ['The', 'robot', 'throws', '3', 'kg', 'of', 'red',
            # -      'apple', 'slowly', 'under', 'the', 'table', '.'],
            # - ),
            # - (
            # -     ['The', 'robot', 'moves', 'slowly', '.'],
            # - ),
            # - (
            # -     ['The', 'robot', 'is', 'a', 'agent', '.'],
            # - ),
            # - (
            # -     ['The', 'robot', 'is', '3', 'pound', '.'],
            # - ),
            # - (
            # -     ['The', 'robot', 'is', '3', 'pound', 'of', 'metal', '.'],
            # - ),
            # - (
            # -     ['The', 'robot', 'is', 'small', '.'],
            # - ),
            # - (
            # -     ['The', 'robot', 'is', 'small', 'and', 'red', '.'],
            # - ),
            # - (
            # -     ['The', 'robot', 'is', 'as', 'small', 'as', 'the', 'box', '.'],
            # - ),
            # - (
            # -     ['The', 'robot', 'is', 'smaller', 'than', 'the', 'red', 'box', '.'],
            # - ),
            # - (
            # -     ['The', 'robot', 'is', 'more', 'small',
            # -      'than', 'the', 'red', 'box', '.'],
            # - ),
            # - (
            # -     ['The', 'robot', 'is', 'much', 'smaller',
            # -      'than', 'the', 'red', 'box', '.'],
            # - ),
            # - (
            # -     ['The', 'robot', 'is', 'much', 'more',
            # -      'small', 'than', 'the', 'red', 'box', '.'],
            # - ),
            # - (
            # -     ['The', 'robot', 'can', 'run', '.'],
            # - ),
            # - (
            # -     ['The', 'robot', 'should', 'run', 'slowly', '.'],
            # - ),
            # - (
            # -     ['The', 'robot', 'may', 'throw', 'an', 'apple', '.'],
            # - ),
            # - (
            # -     ['The', 'robot', 'might', 'throw', 'an', 'apple', 'slowly', '.'],
            # - ),
            # - (
            # -     ['The', 'robot', 'can', 'throw', 'an',
            # -         'red', 'apple', 'slowly', '.'],
            # - ),
            # - (
            # -     ['The', 'robot', 'can', 'throw', 'an', 'red',
            # -      'apple', 'slowly', 'under', 'the', 'table', '.'],
            # - ),
            # - (
            # -     ['The', 'robot', 'can', 'move', 'slowly', '.'],
            # - ),
            # - (
            # -     ['The', 'robot', 'can', 'be', 'small', '.'],
            # - ),
            # - (
            # -     ['The', 'robot', 'can', 'be', 'small', 'and', 'red', '.'],
            # - ),
            # - (
            # -     ['The', 'robot', 'can', 'be', 'as',
            # -         'small', 'as', 'the', 'box', '.'],
            # - ),
            # - (
            # -     ['The', 'robot', 'can', 'be', 'smaller',
            # -      'than', 'the', 'red', 'box', '.'],
            # - ),
            # - (
            # -     ['The', 'robot', 'can', 'be', 'more', 'small',
            # -      'than', 'the', 'red', 'box', '.'],
            # - ),
            # - (
            # -     ['The', 'robot', 'can', 'be', 'much', 'smaller',
            # -      'than', 'the', 'red', 'box', '.'],
            # - ),
            # - (
            # -     ['The', 'robot', 'can', 'be', 'much', 'more',
            # -      'small', 'than', 'the', 'red', 'box', '.'],
            # - ),
            # - (
            # -     ['The', 'robot', 'can', 'be', 'small', 'under', 'the', 'table', '.'],
            # - ),
            # - (
            # -     ['The', 'robot', 'can', 'be', 'small', 'and',
            # -      'red', 'under', 'the', 'table', '.'],
            # - ),
            # - (
            # -     ['The', 'robot', 'can', 'be', 'as', 'small', 'as',
            # -      'the', 'box', 'under', 'the', 'table', '.'],
            # - ),
            # - (
            # -     ['The', 'robot', 'can', 'be', 'smaller', 'than',
            # -      'the', 'red', 'box', 'under', 'the', 'table', '.'],
            # - ),
            # - (
            # -     ['The', 'robot', 'can', 'be', 'more', 'small', 'than',
            # -      'the', 'red', 'box', 'under', 'the', 'table', '.'],
            # - ),
            # - (
            # -     ['The', 'robot', 'can', 'be', 'much', 'smaller', 'than',
            # -      'the', 'red', 'box', 'under', 'the', 'table', '.'],
            # - ),
            # - (
            # -     ['The', 'robot', 'can', 'be', 'much', 'more', 'small', 'than',
            # -      'the', 'red', 'box', 'under', 'the', 'table', '.'],
            # - ),
            # - (
            # -     ['There', 'is', 'an', 'apple', '.'],
            # - ),
            # - (
            # -     ['There', 'is', '3', 'kg', 'of', 'apples', '.'],
            # - ),
            # - (
            # -     ['There', 'is', 'no', 'apple', '.'],
            # - ),
            # - (
            # -     ['There', 'is', 'no', 'apples', 'on', 'the', 'table', '.'],
            # - ),
            # - (
            # -     ['There', 'is', 'no', 'apples', 'under', 'the', 'chair', '.'],
            # - ),
            # - (
            # -     ['Does', 'the', 'robot', 'move', '?'],
            # - ),
            # - (
            # -     ['Does', 'the', 'robot', 'move', 'slowly', '?'],
            # - ),
            # - (
            # -     ['Does', 'the', 'robot', 'slowly', 'move', '?'],
            # - ),
            # - (
            # -     ['Does', 'the', 'robot', 'run', '?'],
            # - ),
            # - (
            # -     ['Does', 'the', 'robot', 'run', 'slowly', '?'],
            # - ),
            # - (
            # -     ['Does', 'the', 'robot', 'throw', '3', 'kg', 'of', 'apple', '?'],
            # - ),
            # - (
            # -     ['Does', 'the', 'robot', 'throw', '3',
            # -      'kg', 'of', 'apple', 'slowly', '?'],
            # - ),
            # - (
            # -     ['Does', 'the', 'robot', 'throw', '3', 'kg',
            # -      'of', 'red', 'apple', 'slowly', '?'],
            # - ),
            # - (
            # -     ['Does', 'the', 'robot', 'throw', '3', 'kg', 'of', 'red',
            # -      'apple', 'slowly', 'under', 'the', 'table', '?'],
            # - ),
            # - (
            # -     ['Does', 'the', 'robot', 'move', 'slowly', '?'],
            # - ),
            # - (
            # -     ['Is', 'the', 'red', 'apple', 'small', '?'],
            # - ),
            # - (
            # -     ['Is', 'the', 'apple', 'smaller', 'than', 'the', 'red', 'box', '?'],
            # - ),
            # - (
            # -     ['Is', 'the', 'apple', 'more', 'small',
            # -      'than', 'the', 'red', 'box', '?'],
            # - ),
            # - (
            # -     ['Is', 'the', 'apple', 'much', 'more',
            # -      'small', 'than', 'the', 'red', 'box', '?'],
            # - ),
            # - (
            # -     ['Is', 'the', 'apple', 'as', 'small',
            # -         'as', 'the', 'red', 'block', '?'],
            # - ),
            # - (
            # -     ['Is', 'the', 'apple', 'small', 'and', 'red', '?'],
            # - ),
            # - (
            # -     ['Is', 'the', 'apple', 'an', 'agent', '?'],
            # - ),
            # - (
            # -     ['Is', 'John', 'an', 'agent', '?'],
            # - ),
            # - (
            # -     ['Is', 'John', 'an', 'robot', '?'],
            # - ),
            # - (
            # -     ['Who', 'does', 'move', '?'],
            # - ),
            # - (
            # -     ['Who', 'does', 'move', 'slowly', '?'],
            # - ),
            # - (
            # -     ['Who', 'does', 'slowly', 'move', '?'],
            # - ),
            # - (
            # -     ['Who', 'does', 'run', '?'],
            # - ),
            # - (
            # -     ['Who', 'does', 'run', 'slowly', '?'],
            # - ),
            # - (
            # -     ['Who', 'does', 'throw', '3', 'kg', 'of', 'apple', '?'],
            # - ),
            # - (
            # -     ['Who', 'does', 'throw', '3', 'kg', 'of', 'apple', 'slowly', '?'],
            # - ),
            # - (
            # -     ['Who', 'does', 'throw', '3', 'kg',
            # -         'of', 'red', 'apple', 'slowly', '?'],
            # - ),
            # - (
            # -     ['Who', 'does', 'throw', '3', 'kg', 'of', 'red',
            # -      'apple', 'slowly', 'under', 'the', 'table', '?'],
            # - ),
            # - (
            # -     ['Who', 'is', 'small', '?'],
            # - ),
            # - (
            # -     ['Who', 'is', 'smart', '?'],
            # - ),
            # - (
            # -     ['Who', 'is', 'small', 'and', 'red', '?'],
            # - ),
            # - (
            # -     ['Who', 'is', 'as', 'small', 'as', 'the', 'red', 'block', '?'],
            # - ),
            # - (
            # -     ['Who', 'is', 'smaller', 'than', 'the', 'red', 'block', '?'],
            # - ),
            # - (
            # -     ['Who', 'is', 'much', 'smaller', 'than', 'the', 'red', 'block', '?'],
            # - ),
            # - (
            # -     ['Who', 'is', 'the', 'robot', '?'],
            # - ),
            # - (
            # -     ['Who', 'is', 'the', 'agent', '?'],
            # - ),
            # - (
            # -     ['Who', 'is', 'the', 'smallest', 'agent', '?'],
            # - ),
            # - (
            # -     ['Who', 'is', 'John', '?'],
            # - ),
            # - (
            # -     ['Which', 'robot', 'does', 'move', '?'],
            # - ),
            # - (
            # -     ['Which', 'robot', 'does', 'move', 'slowly', '?'],
            # - ),
            # - (
            # -     ['Which', 'robot', 'does', 'slowly', 'move', '?'],
            # - ),
            # - (
            # -     ['Which', 'robot', 'does', 'run', '?'],
            # - ),
            # - (
            # -     ['Which', 'robot', 'does', 'run', 'slowly', '?'],
            # - ),
            # - (
            # -     ['Which', 'robot', 'does', 'throw', '3', 'kg', 'of', 'apple', '?'],
            # - ),
            # - (
            # -     ['Which', 'robot', 'does', 'throw', '3',
            # -      'kg', 'of', 'apple', 'slowly', '?'],
            # - ),
            # - (
            # -     ['Which', 'robot', 'does', 'throw', '3', 'kg',
            # -      'of', 'red', 'apple', 'slowly', '?'],
            # - ),
            # - (
            # -     ['Which', 'robot', 'does', 'throw', '3', 'kg', 'of', 'red',
            # -      'apple', 'slowly', 'under', 'the', 'table', '?'],
            # - ),
            # - (
            # -     ['Which', 'robot', 'is', 'small', '?'],
            # - ),
            # - (
            # -     ['Which', 'robot', 'is', 'small', 'and', 'red', '?'],
            # - ),
            # - (
            # -     ['which', 'robot', 'is', 'smaller',
            # -         'than', 'the', 'red', 'block', '?'],
            # - ),
            # - (
            # -     ['which', 'robot', 'is', 'as', 'small',
            # -      'as', 'the', 'red', 'block', '?'],
            # - ),
            # - (
            # -     ['which', 'robot', 'is', 'an', 'agent', '?'],
            # - ),
            # - (
            # -     ['which', 'robot', 'is', 'John', '?'],
            # - ),
            # - (
            # -     ['which', 'robot', 'is', 'John', "'s", 'parent', '?'],
            # - ),
            # - (
            # -     ['Where', 'does', 'the', 'robot', 'move', '?'],
            # - ),
            # - (
            # -     ['Where', 'does', 'the', 'robot', 'slowly', 'run', '?'],
            # - ),
            # - (
            # -     ['Where', 'does', 'the', 'robot',
            # -         'under', 'the', 'table', 'run', '?'],
            # - ),
            # - (
            # -     ['Where', 'does', 'the', 'robot', 'throw',
            # -      '3', 'kg', 'of', 'apple', '?'],
            # - ),
            # - (
            # -     ['Where', 'does', 'the', 'robot', 'slowly',
            # -      'throw', '3', 'kg', 'of', 'apple', '?'],
            # - ),
            # - (
            # -     ['Where', 'does', 'the', 'robot', 'slowly',
            # -      'throw', '3', 'kg', 'of', 'red', 'apple', '?'],
            # - ),
            # - (
            # -     ['Where', 'does', 'the', 'robot', 'slowly', 'under', 'the',
            # -      'table', 'throw', '3', 'kg', 'of', 'red', 'apple', '?'],
            # - ),
            # - (
            # -     ['Where', 'is', 'an', 'apple', '?'],
            # - ),
            # - (
            # -     ['Where', 'is', 'the', 'robot', '?'],
            # - ),
            # - (
            # -     ['How', 'does', 'robot', 'move', '?'],
            # - ),
            # - (
            # -     ['How', 'does', 'robot', 'slowly', 'move', '?'],
            # - ),
            # - (
            # -     ['How', 'does', 'robot', 'run', '?'],
            # - ),
            # - (
            # -     ['How', 'does', 'robot', 'throw', '3', 'kg', 'of', 'apple', '?'],
            # - ),
            # - (
            # -     ['How', 'does', 'robot', 'slowly', 'throw',
            # -      '3', 'kg', 'of', 'apple', '?'],
            # - ),
            # - (
            # -     ['How', 'does', 'robot', 'slowly', 'throw',
            # -      '3', 'kg', 'of', 'red', 'apple', '?'],
            # - ),
            # - (
            # -     ['How', 'does', 'robot', 'slowly', 'under', 'the', 'table',
            # -      'throw', '3', 'kg', 'of', 'red', 'apple', '?'],
            # - )

            # * Practical tests:
            (
                ['The', 'robot', 'asks', 'the', 'users',
                    'to', 'enter', 'the', 'input', '.'],
                ['DET', 'NN', 'VBZ', 'DET', 'NNS',
                    'TO', 'VB', 'DET', 'NN', 'PERIOD'],
            )
        ]
        tagger = CascadeTagger()
        for i, (input_, expect_) in enumerate(inputs_):
            word_tag_pairs = tagger.tag(input_)
            tags = [t for w, t in word_tag_pairs]
            error_msg = "Cascade's result: {} /\n Expect: {} -- at sentence {}-th --'{}'".format(
                tags, expect_, i, input_)
            self.assertEqual(tags, expect_, error_msg)


if __name__ == "__main__":
    unittest.main()
