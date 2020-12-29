import sys
from pathlib import Path
workspace_directory = Path(Path(__file__).parent.parent.parent)
sys.path.insert(0, str(workspace_directory))

from scripts.lexical_analysis.chunker import (
    pattern_1,
    pattern_2,
    pattern_3,
    pattern_4,
    pattern_5,
    pattern_6,
    pattern_7,
    pattern_10,
    pattern_11,
    pattern_12,
    pattern_13,
    pattern_14,
    RegexpParser,
    hasPattern_x,

    correct_1,
    correct_2,
    correct_3,
    correct_4,
    correct_5,
)

from scripts.crl.pos_tagger import (
    pos_tagger
)

from nltk import (
    word_tokenize
)

import unittest


class Test_Lexical_Analysis_Pattern_Detection(unittest.TestCase):
    def test_pattern_1(self):
        inputs_ = [
            "There is a school bus.",
            "Move that apple juice.",
            "Move that apple pie.",
        ]
        for i, input_ in enumerate(inputs_):
            tokenized_sentence = word_tokenize(input_)
            tagged_sentence = pos_tagger.tag(tokenized_sentence)
            chunker = RegexpParser(pattern_1)
            result = chunker.parse(tagged_sentence)

            pattern_id = "pattern_1"

            error_msg = "Sentence {}-th -- '{}' -- does not contain {} \n {}".format(
                i, tagged_sentence, pattern_id, pattern_1)
            self.assertEqual(hasPattern_x(
                result, pattern_id), True, error_msg)

    def test_pattern_2(self):
        inputs_ = [
            "Move the hand eventually slowly.",
        ]
        for i, input_ in enumerate(inputs_):
            tokenized_sentence = word_tokenize(input_)
            tagged_sentence = pos_tagger.tag(tokenized_sentence)
            chunker = RegexpParser(pattern_2)
            result = chunker.parse(tagged_sentence)

            pattern_id = "pattern_2"

            error_msg = "Sentence {}-th -- '{}' -- does not contain {} \n {}".format(
                i, tagged_sentence, pattern_id, pattern_2)
            self.assertEqual(hasPattern_x(
                result, pattern_id), True, error_msg)

    def test_pattern_3(self):
        inputs_ = [
            "Move the small red apple.",
        ]
        for i, input_ in enumerate(inputs_):
            tokenized_sentence = word_tokenize(input_)
            tagged_sentence = pos_tagger.tag(tokenized_sentence)
            chunker = RegexpParser(pattern_3)
            result = chunker.parse(tagged_sentence)

            pattern_id = "pattern_3"

            error_msg = "Sentence {}-th -- '{}' -- does not contain {} \n {}".format(
                i, tagged_sentence, pattern_id, pattern_3)
            self.assertEqual(hasPattern_x(
                result, pattern_id), True, error_msg)

    def test_pattern_4(self):
        inputs_ = [
            "Your robot needs to move this table.",
        ]
        for i, input_ in enumerate(inputs_):
            tokenized_sentence = word_tokenize(input_)
            tagged_sentence = pos_tagger.tag(tokenized_sentence)
            chunker = RegexpParser(pattern_4)
            result = chunker.parse(tagged_sentence)

            pattern_id = "pattern_4"

            error_msg = "Sentence {}-th -- '{}' -- does not contain {} \n {}".format(
                i, tagged_sentence, pattern_id, pattern_4)
            self.assertEqual(hasPattern_x(
                result, pattern_id), True, error_msg)

    def test_pattern_5(self):
        inputs_ = [
            "You needs to move this table.",
        ]
        for i, input_ in enumerate(inputs_):
            tokenized_sentence = word_tokenize(input_)
            tagged_sentence = pos_tagger.tag(tokenized_sentence)
            chunker = RegexpParser(pattern_5)
            result = chunker.parse(tagged_sentence)

            pattern_id = "pattern_5"

            error_msg = "Sentence {}-th -- '{}' -- does not contain {} \n {}".format(
                i, tagged_sentence, pattern_id, pattern_5)
            self.assertEqual(hasPattern_x(
                result, pattern_id), True, error_msg)

    def test_pattern_6(self):
        inputs_ = [
            "You needs to move this table.",
            "You have to save this table.",
            "Sawyer want to pick this table.",
        ]
        for i, input_ in enumerate(inputs_):
            tokenized_sentence = word_tokenize(input_)
            tagged_sentence = pos_tagger.tag(tokenized_sentence)
            chunker = RegexpParser(pattern_6)
            result = chunker.parse(tagged_sentence)

            pattern_id = "pattern_6"

            error_msg = "Sentence {}-th -- '{}' -- does not contain {} \n {}".format(
                i, tagged_sentence, pattern_id, pattern_6)
            self.assertEqual(hasPattern_x(
                result, pattern_id), True, error_msg)

    def test_pattern_7(self):
        inputs_ = [
            "You needs to move this table.",
            "You have to save this table.",
            "Sawyer want to pick this table.",
        ]
        for i, input_ in enumerate(inputs_):
            tokenized_sentence = word_tokenize(input_)
            tagged_sentence = pos_tagger.tag(tokenized_sentence)
            chunker = RegexpParser(pattern_6)
            result = chunker.parse(tagged_sentence)

            pattern_id = "pattern_6"

            error_msg = "Sentence {}-th -- '{}' -- does not contain {} \n {}".format(
                i, tagged_sentence, pattern_id, pattern_6)
            self.assertEqual(hasPattern_x(
                result, pattern_id), True, error_msg)

    def test_pattern_10(self):
        inputs_ = [
            "We needs to move this table.",
        ]
        for i, input_ in enumerate(inputs_):
            tokenized_sentence = word_tokenize(input_)
            tagged_sentence = pos_tagger.tag(tokenized_sentence)
            chunker = RegexpParser(pattern_10)
            result = chunker.parse(tagged_sentence)

            pattern_id = "pattern_10"

            error_msg = "Sentence {}-th -- '{}' -- does not contain {} \n {}".format(
                i, tagged_sentence, pattern_id, pattern_10)
            self.assertEqual(hasPattern_x(
                result, pattern_id), True, error_msg)

    def test_pattern_10(self):
        inputs_ = [
            "We needs to move this table.",
        ]
        for i, input_ in enumerate(inputs_):
            tokenized_sentence = word_tokenize(input_)
            tagged_sentence = pos_tagger.tag(tokenized_sentence)
            chunker = RegexpParser(pattern_10)
            result = chunker.parse(tagged_sentence)

            pattern_id = "pattern_10"

            error_msg = "Sentence {}-th -- '{}' -- does not contain {} \n {}".format(
                i, tagged_sentence, pattern_id, pattern_10)
            self.assertEqual(hasPattern_x(
                result, pattern_id), True, error_msg)

    def test_pattern_11(self):
        inputs_ = [
            "Our robot needs to move this table.",
        ]
        for i, input_ in enumerate(inputs_):
            tokenized_sentence = word_tokenize(input_)
            tagged_sentence = pos_tagger.tag(tokenized_sentence)
            chunker = RegexpParser(pattern_11)
            result = chunker.parse(tagged_sentence)

            pattern_id = "pattern_11"

            error_msg = "Sentence {}-th -- '{}' -- does not contain {} \n {}".format(
                i, tagged_sentence, pattern_id, pattern_11)
            self.assertEqual(hasPattern_x(
                result, pattern_id), True, error_msg)

    def test_pattern_12(self):
        inputs_ = [
            "I needs to move this table.",
        ]
        for i, input_ in enumerate(inputs_):
            tokenized_sentence = word_tokenize(input_)
            tagged_sentence = pos_tagger.tag(tokenized_sentence)
            chunker = RegexpParser(pattern_12)
            result = chunker.parse(tagged_sentence)

            pattern_id = "pattern_12"

            error_msg = "Sentence {}-th -- '{}' -- does not contain {} \n {}".format(
                i, tagged_sentence, pattern_id, pattern_12)
            self.assertEqual(hasPattern_x(
                result, pattern_id), True, error_msg)

    def test_pattern_13(self):
        inputs_ = [
            "My robot needs to move this table.",
        ]
        for i, input_ in enumerate(inputs_):
            tokenized_sentence = word_tokenize(input_)
            tagged_sentence = pos_tagger.tag(tokenized_sentence)
            chunker = RegexpParser(pattern_13)
            result = chunker.parse(tagged_sentence)

            pattern_id = "pattern_13"

            error_msg = "Sentence {}-th -- '{}' -- does not contain {} \n {}".format(
                i, tagged_sentence, pattern_id, pattern_13)
            self.assertEqual(hasPattern_x(
                result, pattern_id), True, error_msg)

    def test_pattern_14(self):
        inputs_ = [
            "My robot needs to increase from 30 to 40 cm.",
        ]
        for i, input_ in enumerate(inputs_):
            tokenized_sentence = word_tokenize(input_)
            tagged_sentence = pos_tagger.tag(tokenized_sentence)
            chunker = RegexpParser(pattern_14)
            result = chunker.parse(tagged_sentence)

            pattern_id = "pattern_14"

            error_msg = "Sentence {}-th -- '{}' -- does not contain {} \n {}".format(
                i, tagged_sentence, pattern_id, pattern_14)
            self.assertEqual(hasPattern_x(
                result, pattern_id), True, error_msg)


class Test_Lexical_Analysis_Pattern_Correction(unittest.TestCase):
    def test_correct_pattern_1(self):
        inputs_ = [
            (
                "There is a school bus.",
                "There is a bus ."
            ),
            (
                "Move that apple juice.",
                "Move that juice ."
            ),
            (
                "Move that apple pie.",
                "Move that pie ."
            ),
        ]
        for i, (input_, expect_) in enumerate(inputs_):
            tokenized_sentence = word_tokenize(input_)
            tagged_sentence = pos_tagger.tag(tokenized_sentence)
            chunker = RegexpParser(pattern_1)
            result = chunker.parse(tagged_sentence)

            correction = correct_1(result)
            correction = " ".join(correction)

            error_msg = "Sentence {}-th -- '{}' -- expect result: '{}' / while correction return: '{}'".format(
                i, input_, expect_, correction)
            self.assertEqual(expect_, correction, error_msg)

    def test_correction_pattern_2(self):
        inputs_ = [
            (
                "Move the hand eventually slowly.",
                "Move the hand eventually and slowly ."
            ),
            (
                "Move the hand eventually slowly gradually.",
                "Move the hand eventually and slowly and gradually ."
            )
        ]
        for i, (input_, expect_) in enumerate(inputs_):
            tokenized_sentence = word_tokenize(input_)
            tagged_sentence = pos_tagger.tag(tokenized_sentence)
            chunker = RegexpParser(pattern_2)
            result = chunker.parse(tagged_sentence)

            correction = correct_2(result)
            correction = " ".join(correction)

            error_msg = "Sentence {}-th -- '{}' -- expect result: '{}' / while correction return: '{}'".format(
                i, input_, expect_, correction)
            self.assertEqual(expect_, correction, error_msg)

    def test_correction_pattern_3(self):
        inputs_ = [
            (
                "Move the small red apple.",
                "Move the small and red apple .",
            )
        ]
        for i, (input_, expect_) in enumerate(inputs_):
            tokenized_sentence = word_tokenize(input_)
            tagged_sentence = pos_tagger.tag(tokenized_sentence)
            chunker = RegexpParser(pattern_3)
            result = chunker.parse(tagged_sentence)

            correction = correct_3(result)
            correction = " ".join(correction)

            error_msg = "Sentence {}-th -- '{}' -- expect result: '{}' / while correction return: '{}'".format(
                i, input_, expect_, correction)
            self.assertEqual(expect_, correction, error_msg)

    def test_correction_pattern_4(self):
        inputs_ = [
            (
                "Your robot needs to move this table.",
                "the user 's robot needs to move this table .",
            )
        ]
        for i, (input_, expect_) in enumerate(inputs_):
            tokenized_sentence = word_tokenize(input_)
            tagged_sentence = pos_tagger.tag(tokenized_sentence)
            chunker = RegexpParser(pattern_4)
            result = chunker.parse(tagged_sentence)

            correction = correct_4(result)
            correction = " ".join(correction)

            error_msg = "Sentence {}-th -- '{}' -- expect result: '{}' / while correction return: '{}'".format(
                i, input_, expect_, correction)
            self.assertEqual(expect_, correction, error_msg)

    def test_correction_pattern_5(self):
        inputs_ = [
            (
                "You needs to move this table.",
                "the user needs to move this table ."
            )

        ]
        for i, (input_,expect_) in enumerate(inputs_):
            tokenized_sentence = word_tokenize(input_)
            tagged_sentence = pos_tagger.tag(tokenized_sentence)
            chunker = RegexpParser(pattern_5)
            result = chunker.parse(tagged_sentence)

            correction = correct_5(result)
            correction = " ".join(correction)

            error_msg = "Sentence {}-th -- '{}' -- expect result: '{}' / while correction return: '{}'".format(
                i, input_, expect_, correction)
            self.assertEqual(expect_, correction, error_msg)


if __name__ == "__main__":
    unittest.main()
