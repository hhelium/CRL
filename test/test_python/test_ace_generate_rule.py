import sys
from pathlib import Path
workspace_directory = Path(Path(__file__).parent.parent.parent)
sys.path.insert(0, str(workspace_directory))


from scripts.ace.generate_rule import (
    generate_rules,
    write_rules
)
from scripts.crl.crl_grammar import (
    dynamic_crl_grammar
)
from scripts.lemmatize.lemmatizer import (
    spacy_lemmatizer
)


from nltk import (
    word_tokenize
)

import unittest


class Test_ACE_Lexical_Rule_Generation(unittest.TestCase):
    def test_rule_generating(self):
        inputs_ = [
            (
                "There is an apple.",
                set([
                    "noun_sg(apple, apple, neutr)."
                ])
            ),
            (
                "A robot moves slowly.",
                set([
                    "noun_sg(robot, robot, neutr).",
                    "iv_finsg(moves, move).",
                    "tv_finsg(moves, move).",
                    "adv(slowly, slowly)."
                ])
            ),
        ]
        for i, (input_, expect_) in enumerate(inputs_):
            tokenized = word_tokenize(input_)
            grammar = dynamic_crl_grammar(tokenized)
            productions = grammar.productions()
            rules = generate_rules(productions, spacy_lemmatizer)
            rules = set(rules)

            error_msg = "Sentence {}-th -- '{}'. Expect: <{}> / Actual: <{}>".format(
                i, input_, expect_, rules)
            self.assertEqual(expect_, rules, error_msg)

    # @unittest.skip("Not run unless specified")
    def test_tmp(self):
        inputs_ = [
            (
                "A robot picks the apple slowly.",
                set([
                    "noun_sg(robot, robot, neutr).",
                    "iv_finsg(moves, move).",
                    "tv_finsg(moves, move).",
                    "adv(slowly, slowly)."
                ])
            ),
        ]
        for i, (input_, expect_) in enumerate(inputs_):
            tokenized = word_tokenize(input_)
            grammar = dynamic_crl_grammar(tokenized)
            productions = grammar.productions()
            write_rules(productions, spacy_lemmatizer)


if __name__ == "__main__":
    unittest.main()
