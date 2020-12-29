import sys
from pathlib import Path
workspace_directory = Path(Path(__file__).parent.parent.parent)
sys.path.insert(0, str(workspace_directory))

from scripts.crl.translation import (
    parse_production,
    current_production
)

from nltk.grammar import (
    Production, parse_cfg,
    Nonterminal
)

from nltk.tree import (
    Tree
)
import unittest


class Test_CFG_Production(unittest.TestCase):
    def test_production_from_grammar(self):
        grammar_str = """
        S -> NP VP
        PP -> P NP
        NP -> Det N | NP PP
        VP -> V NP | VP PP
        Det -> 'a' | 'the'
        N -> 'dog' | 'cat'
        V -> 'chased' | 'sat'
        P -> 'on' | 'in'
        """

        grammar = parse_cfg(grammar_str)
        productions = grammar.productions()

        expect_production = Production(
            lhs=Nonterminal("S"), rhs=[Nonterminal("NP"), Nonterminal("VP")])
        error_msg = "Expect to find '{}', but can not see in \n{}".format(
            expect_production, grammar_str)
        self.assertIn(expect_production, productions, error_msg)

        expect_production = Production(
            lhs=Nonterminal("N"), rhs=['dog'])
        error_msg = "Expect to find '{}', but can not see in \n{}".format(
            expect_production, grammar_str)
        self.assertIn(expect_production, productions, error_msg)

        expect_not_in = Production(
            lhs="S",
            rhs=["NP", "VP"]
        )
        self.assertNotIn(expect_not_in, productions, error_msg)

        expect_not_in = Production(
            lhs=Nonterminal("N"),
            rhs=["'dog'"]
        )
        self.assertNotIn(expect_not_in, productions, error_msg)

    def test_parse_production(self):
        inputs_ = [
            (
                "PP -> P NP",
                Production(Nonterminal("PP"), [
                           Nonterminal("P"), Nonterminal("NP")])
            ),
            (
                "S -> NP VP",
                Production(Nonterminal("S"), [
                           Nonterminal("NP"), Nonterminal("VP")])
            ),
            (
                "THERE -> 'There'",
                Production(Nonterminal("THERE"), [
                           'There'])
            )
        ]
        for i, (input_, expect_) in enumerate(inputs_):
            production = parse_production(input_)

            error_msg = "Sentence {}-th -- '{}' -- Expect result: {} / Actual result: {}".format(
                i, input_, expect_, production)
            self.assertEqual(expect_, production, error_msg)

    def test_current_production(self):
        inputs_ = [
            (
                """
                (S
                    (sentence
                        (type_1_sentence_coord_1
                        (type_1_sentence_coord_2
                            (type_2_sentence
                            (THERE There)
                            (AUX is)
                            (Noun_Phrase
                                (det (DET an))
                                (Noun_w_support
                                (Adj_phrase
                                    (Adj_core (JJ small))
                                    (AND and)
                                    (Adj_phrase (Adj_core (JJ red))))
                                (Noun_Count (NN apple)))))))
                        (PERIOD .)))
                """,
                Production(Nonterminal("S"), [Nonterminal("sentence")])
            )
        ]

        for i, (input_, expect_) in enumerate(inputs_):
            tree = Tree.parse(input_)
            production = current_production(tree)
            
            self.assertEqual(expect_,production)


if __name__ == "__main__":
    unittest.main()
