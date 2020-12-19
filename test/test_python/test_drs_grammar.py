import sys
from pathlib import Path
workspace_directory = Path(Path(__file__).parent.parent.parent)
sys.path.insert(0, str(workspace_directory))


import unittest
from scripts.drs import (
    grammar_test_str
)
from lark import Lark


class Test_Lexical(unittest.TestCase):

    def test_property_degree_property(self):
        inputs_ = [
            "pos_as",
            "pos",
            "comp_than",
            "comp",
            "sup",
        ]
        parser = Lark(grammar_test_str, start="test_property_degree_property")

        for i, input_ in enumerate(inputs_):
            try:
                result = parser.parse(input_)
            except:
                error_msg = "Sentence {}-th is in valid: {}".format(i, input_)
                self.fail(error_msg)

    def test_adv_degree_property(self):
        inputs_ = [
            "pos",
            "comp",
            "sup",
        ]
        parser = Lark(grammar_test_str, start="test_adv_degree_property")

        for i, input_ in enumerate(inputs_):
            try:
                result = parser.parse(input_)
            except:
                error_msg = "Sentence {}-th is in valid: {}".format(i, input_)
                self.fail(error_msg)

    def test_count_property(self):
        inputs_ = [
            "na",
            "1",
            "20",
            "40",
            "120",
            "70"
        ]
        parser = Lark(grammar_test_str, start="test_count_property")

        for i, input_ in enumerate(inputs_):
            try:
                result = parser.parse(input_)
            except:
                error_msg = "Sentence {}-th is in valid: {}".format(i, input_)
                self.fail(error_msg)

    def test_operator_property(self):
        inputs_ = [
            "eq",
            "geq",
            "greater",
            "leq",
            "less",
            "exactly",
            "na",
        ]
        parser = Lark(grammar_test_str, start="test_operator_property")

        for i, input_ in enumerate(inputs_):
            try:
                result = parser.parse(input_)
            except:
                error_msg = "Sentence {}-th is in valid: {}".format(i, input_)
                self.fail(error_msg)

    def test_unit_property(self):
        inputs_ = [
            "na",
            "pick",
            "move",
            "throw",
            "grasp",
        ]
        parser = Lark(grammar_test_str, start="test_unit_property")

        for i, input_ in enumerate(inputs_):
            try:
                result = parser.parse(input_)
            except:
                error_msg = "Sentence {}-th is in valid: {}".format(i, input_)
                self.fail(error_msg)

    def test_quantity_property(self):
        inputs_ = [
            "dom",
            "mass",
            "countable",
        ]
        parser = Lark(grammar_test_str, start="test_quantity_property")

        for i, input_ in enumerate(inputs_):
            try:
                result = parser.parse(input_)
            except:
                error_msg = "Sentence {}-th is in valid: {}".format(i, input_)
                self.fail(error_msg)

    def test_valid_lexicon(self):
        inputs_ = [
            "pick",
            "move",
            "slowly",
            "fast",
            "red",
        ]
        parser = Lark(grammar_test_str, start="test_valid_lexicon")

        for i, input_ in enumerate(inputs_):
            try:
                result = parser.parse(input_)
            except:
                error_msg = "Sentence {}-th is in valid: {}".format(i, input_)
                self.fail(error_msg)

    def test_object(self):
        inputs_ = [
            "object",

        ]
        parser = Lark(grammar_test_str, start="test_object")

        for i, input_ in enumerate(inputs_):
            try:
                result = parser.parse(input_)
            except:
                error_msg = "Sentence {}-th is in valid: {}".format(i, input_)
                self.fail(error_msg)

    def test_property(self):
        inputs_ = [
            "property",

        ]
        parser = Lark(grammar_test_str, start="test_property")

        for i, input_ in enumerate(inputs_):
            try:
                result = parser.parse(input_)
            except:
                error_msg = "Sentence {}-th is in valid: {}".format(i, input_)
                self.fail(error_msg)

    def test_relation(self):
        inputs_ = [
            "relation",

        ]
        parser = Lark(grammar_test_str, start="test_relation")

        for i, input_ in enumerate(inputs_):
            try:
                result = parser.parse(input_)
            except:
                error_msg = "Sentence {}-th is in valid: {}".format(i, input_)
                self.fail(error_msg)

    def test_predicate(self):
        inputs_ = [
            "predicate",

        ]
        parser = Lark(grammar_test_str, start="test_predicate")

        for i, input_ in enumerate(inputs_):
            try:
                result = parser.parse(input_)
            except:
                error_msg = "Sentence {}-th is in valid: {}".format(i, input_)
                self.fail(error_msg)

    def test_modifier_adv(self):
        inputs_ = [
            "modifier_adv",

        ]
        parser = Lark(grammar_test_str, start="test_modifier_adv")

        for i, input_ in enumerate(inputs_):
            try:
                result = parser.parse(input_)
            except:
                error_msg = "Sentence {}-th is in valid: {}".format(i, input_)
                self.fail(error_msg)

    def test_modifier_pp(self):
        inputs_ = [
            "modifier_pp",

        ]
        parser = Lark(grammar_test_str, start="test_modifier_pp")

        for i, input_ in enumerate(inputs_):
            try:
                result = parser.parse(input_)
            except:
                error_msg = "Sentence {}-th is in valid: {}".format(i, input_)
                self.fail(error_msg)

    def test_query(self):
        inputs_ = [
            "query",

        ]
        parser = Lark(grammar_test_str, start="test_query")

        for i, input_ in enumerate(inputs_):
            try:
                result = parser.parse(input_)
            except:
                error_msg = "Sentence {}-th is in valid: {}".format(i, input_)
                self.fail(error_msg)

    def test_query_wh_word(self):
        inputs_ = [
            "who",
            "what",
            "which",
            "how",
            "where",
            "when",

        ]
        parser = Lark(grammar_test_str, start="test_query_wh_word")

        for i, input_ in enumerate(inputs_):
            try:
                result = parser.parse(input_)
            except:
                error_msg = "Sentence {}-th is in valid: {}".format(i, input_)
                self.fail(error_msg)

    def test_neg(self):
        inputs_ = [
            "-",

        ]
        parser = Lark(grammar_test_str, start="test_neg")

        for i, input_ in enumerate(inputs_):
            try:
                result = parser.parse(input_)
            except:
                error_msg = "Sentence {}-th is in valid: {}".format(i, input_)
                self.fail(error_msg)

    def test_named_entity(self):
        inputs_ = [
            "named('John')",
            "named('Bob')",
            "named('Jack')"

        ]
        parser = Lark(grammar_test_str, start="test_named_entity")

        for i, input_ in enumerate(inputs_):
            try:
                result = parser.parse(input_)
            except:
                error_msg = "Sentence {}-th is in valid: {}".format(i, input_)
                self.fail(error_msg)

    def test_disjunct(self):
        inputs_ = [
            "v",
        ]
        parser = Lark(grammar_test_str, start="test_disjunct")

        for i, input_ in enumerate(inputs_):
            try:
                result = parser.parse(input_)
            except:
                error_msg = "Sentence {}-th is in valid: {}".format(i, input_)
                self.fail(error_msg)

    def test_implication(self):
        inputs_ = [
            "=>",

        ]
        parser = Lark(grammar_test_str, start="test_implication")

        for i, input_ in enumerate(inputs_):
            try:
                result = parser.parse(input_)
            except:
                error_msg = "Sentence {}-th is in valid: {}".format(i, input_)
                self.fail(error_msg)

    def test_command(self):
        inputs_ = [
            "command",

        ]
        parser = Lark(grammar_test_str, start="test_command")

        for i, input_ in enumerate(inputs_):
            try:
                result = parser.parse(input_)
            except:
                error_msg = "Sentence {}-th is in valid: {}".format(i, input_)
                self.fail(error_msg)

    def test_possibility(self):
        inputs_ = [
            "may",
            "can",
            "should",
            "must",
        ]
        parser = Lark(grammar_test_str, start="test_possibility")

        for i, input_ in enumerate(inputs_):
            try:
                result = parser.parse(input_)
            except:
                error_msg = "Sentence {}-th is in valid: {}".format(i, input_)
                self.fail(error_msg)

    def test_question(self):
        inputs_ = [
            "question",

        ]
        parser = Lark(grammar_test_str, start="test_question")

        for i, input_ in enumerate(inputs_):
            try:
                result = parser.parse(input_)
            except:
                error_msg = "Sentence {}-th is in valid: {}".format(i, input_)
                self.fail(error_msg)

    def test_open_circle_bracket(self):
        inputs_ = [
            "(",

        ]
        parser = Lark(grammar_test_str, start="test_open_circle_bracket")

        for i, input_ in enumerate(inputs_):
            try:
                result = parser.parse(input_)
            except:
                error_msg = "Sentence {}-th is in valid: {}".format(i, input_)
                self.fail(error_msg)

    def test_close_circle_bracket(self):
        inputs_ = [
            ")",
        ]
        parser = Lark(grammar_test_str, start="test_close_circle_bracket")

        for i, input_ in enumerate(inputs_):
            try:
                result = parser.parse(input_)
            except:
                error_msg = "Sentence {}-th is in valid: {}".format(i, input_)
                self.fail(error_msg)

    def test_open_square_bracket(self):
        inputs_ = [
            "["
        ]
        parser = Lark(grammar_test_str, start="test_open_square_bracket")

        for i, input_ in enumerate(inputs_):
            try:
                result = parser.parse(input_)
            except:
                error_msg = "Sentence {}-th is in valid: {}".format(i, input_)
                self.fail(error_msg)

    def test_close_square_bracket(self):
        inputs_ = [
            "]",

        ]
        parser = Lark(grammar_test_str, start="test_close_square_bracket")

        for i, input_ in enumerate(inputs_):
            try:
                result = parser.parse(input_)
            except:
                error_msg = "Sentence {}-th is in valid: {}".format(i, input_)
                self.fail(error_msg)

    def test_drs(self):
        inputs_ = [
            "drs",

        ]
        parser = Lark(grammar_test_str, start="test_drs")

        for i, input_ in enumerate(inputs_):
            try:
                result = parser.parse(input_)
            except:
                error_msg = "Sentence {}-th is in valid: {}".format(i, input_)
                self.fail(error_msg)

    def test_sid_tid(self):
        inputs_ = [
            "-1/2",
            "-10/4",
            "-1/20"
        ]
        parser = Lark(grammar_test_str, start="test_sid_tid")

        for i, input_ in enumerate(inputs_):
            try:
                result = parser.parse(input_)
            except:
                error_msg = "Sentence {}-th is in valid: {}".format(i, input_)
                self.fail(error_msg)

    def test_named(self):
        inputs_ = [
            "named",

        ]
        parser = Lark(grammar_test_str, start="test_named")

        for i, input_ in enumerate(inputs_):
            try:
                result = parser.parse(input_)
            except:
                error_msg = "Sentence {}-th is in valid: {}".format(i, input_)
                self.fail(error_msg)

    def test_single_quote(self):
        inputs_ = [
            "'",

        ]
        parser = Lark(grammar_test_str, start="test_single_quote")

        for i, input_ in enumerate(inputs_):
            try:
                result = parser.parse(input_)
            except:
                error_msg = "Sentence {}-th is in valid: {}".format(i, input_)
                self.fail(error_msg)

    def test_variable(self):
        inputs_ = [
            "X",
            "A",
            "B",
            "B10",
            "C2",

        ]
        parser = Lark(grammar_test_str, start="test_variable")

        for i, input_ in enumerate(inputs_):
            try:
                result = parser.parse(input_)
            except:
                error_msg = "Sentence {}-th is in valid: {}".format(i, input_)
                self.fail(error_msg)

    def test_sep(self):
        inputs_ = [
            ",",
        ]
        parser = Lark(grammar_test_str, start="test_sep")

        for i, input_ in enumerate(inputs_):
            try:
                result = parser.parse(input_)
            except:
                error_msg = "Sentence {}-th is in valid: {}".format(i, input_)
                self.fail(error_msg)


class Test_Rule(unittest.TestCase):
    def test_object_condition(self):
        inputs_ = [
            "object(A, robot, countable, na, eq, 1)",
            "object(A, robot, countable, na, eq, 1)",
            "object(A, apple, countable, na, eq, 1)",
            "object(A, apple, countable, na, eq, 1)",
            "object(A, robot, countable, na, eq, 1)",
            "object(B, apple, countable, na, eq, 1)",
            "object(A, robot, countable, na, eq, 1)",
            "object(B, apple, countable, na, eq, 1)",
            "object(A, robot, countable, na, eq, 1)",
            "object(B, apple, countable, na, eq, 1)",
            "object(A, robot, countable, na, eq, 1)",
            "object(B, apple, countable, na, eq, 1)",
            "object(A, robot, countable, na, eq, 1)",
            "object(B, apple, countable, na, eq, 1)",
            "object(B, robot, countable, na, eq, 1)",
            "object(C, company, countable, na, eq, 1)",
            "object(B, robot, countable, na, eq, 1)",
            "object(C, company, countable, na, eq, 1)",
            "object(E, agent, countable, na, eq, 1)",
            "object(D, robot, countable, na, eq, 1)",
            "object(A, apple, countable, na, eq, 1)",
            "object(C, table, countable, na, eq, 1)",
            "object(C, agent, countable, na, eq, 1)",
            "object(B, robot, countable, na, eq, 1)",
            "object(A, agent, countable, na, eq, 1)",
            "object(C, apple, countable, na, eq, 1)",
            "object(A, agent, countable, na, eq, 1)",
            "object(C, apple, countable, na, eq, 1)",
            "object(E, table, countable, na, eq, 1)",
            "object(C, robot, countable, na, eq, 1)",
            "object(A, apple, countable, kg, eq, 3)",
            "object(C, robot, countable, na, eq, 1)",
            "object(A, apple, countable, kg, eq, 3)",
            "object(C, robot, countable, na, eq, 1)",
            "object(A, metal, countable, pound, eq, 3)",
            "object(A, robot, countable, na, eq, 1)",
            "object(B, apple, countable, na, eq, 1)",
            "object(A, robot, countable, na, eq, 1)",
            "object(B, apple, countable, na, eq, 1)",
            "object(D, table, countable, na, eq, 1)",
            "object(A, apple, countable, na, eq, 1)",
            "object(D, apple, countable, na, eq, 1)",
            "object(C, box, countable, na, eq, 1)",
            "object(D, apple, countable, na, eq, 1)",
            "object(C, box, countable, na, eq, 1)",
            "object(C, apple, countable, na, eq, 1)",
            "object(A, agent, countable, na, eq, 1)",
            "object(A, agent, countable, na, eq, 1)",
            "object(D, block, countable, na, eq, 1)",
            "object(D, block, countable, na, eq, 1)",
            "object(C, agent, countable, na, eq, 1)",
            "object(A, robot, countable, na, eq, 1)",
            "object(D, block, countable, na, eq, 1)",
            "object(A, robot, countable, na, eq, 1)",
            "object(D, block, countable, na, eq, 1)",
            "object(A, robot, countable, na, eq, 1)",
        ]
        parser = Lark(grammar_test_str, start="test_object_condition")
        for i, input_ in enumerate(inputs_):
            try:
                result = parser.parse(input_)
            except:
                error_msg = "Sentence {}-th is in valid: {}".format(i, input_)
                self.fail(error_msg)

    def test_predicate_condition(self):
        inputs_ = [
            "predicate(B, run, A)",
            "predicate(B, run, A)",
            "predicate(B, throw, named('John'), A)",
            "predicate(B, throw, named('John'), A)",
            "predicate(C, throw, A, B)",
            "predicate(C, throw, A, B)",
            "predicate(C, throw, A, B)",
            "predicate(C, throw, A, B)",
            "predicate(C, throw, A, B)",
            "predicate(A, run, B)",
            "predicate(A, run, B)",
            "predicate(F, be, D, E)",
            "predicate(B, throw, D, A)",
            "predicate(D, be, B, C)",
            "predicate(A, move, B)",
            "predicate(B, be, named('John'), A)",
            "predicate(D, throw, named('John'), C)",
            "predicate(B, be, named('John'), A)",
            "predicate(D, throw, named('John'), C)",
            "predicate(B, throw, C, A)",
            "predicate(B, throw, C, A)",
            "predicate(B, be, C, A)",
            "predicate(C, throw, A, B)",
            "predicate(C, throw, A, B)",
            "predicate(B, be, D, A)",
            "predicate(B, be, D, A)",
            "predicate(B, be, C, A)",
            "predicate(B, be, named('John'), A)",
            "predicate(B, move, A)",
            "predicate(B, move, A)",
            "predicate(C, be, A, B)",
            "predicate(C, be, A, B)",
            "predicate(B, be, A, C)",
            "predicate(B, be, A, named('John'))",
            "predicate(C, be, A, B)",
            "predicate(C, be, A, B)",
            "predicate(B, be, A, named('John'))",
        ]
        parser = Lark(grammar_test_str, start="test_predicate_condition")
        for i, input_ in enumerate(inputs_):
            try:
                result = parser.parse(input_)
            except:
                error_msg = "Sentence {}-th is in valid: {}".format(i, input_)
                self.fail(error_msg)

    def test_property_condition(self):
        inputs_ = [
            "property(A,small,pos)",
            "property(A,small,pos)",
            "property(B,red,pos)",
            "property(A,small,pos)",
            "property(A,green,pos)",
            "property(A,red,pos)",
            "property(C,red,pos)",
            "property(C,red,pos)",
            "property(A,red,pos)",
            "property(B,red,pos)",
            "property(B,red,pos)",
            "property(C,red,pos)",
            "property(A,small,comp_than,C)",
            "property(C,red,pos)",
            "property(A,small,comp_than,C)",
            "property(D,red,pos)",
            "property(B,small,pos_as,D)",
            "property(D,red,pos)",
            "property(B,small,comp_than,D)",
            "property(C,small,sup)",
            "property(D,red,pos)",
            "property(B,small,comp_than,D)",
            "property(D,red,pos)",
            "property(B,small,pos_as,D)",
        ]
        parser = Lark(grammar_test_str, start="test_property_condition")
        for i, input_ in enumerate(inputs_):
            try:
                result = parser.parse(input_)
            except:
                error_msg = "Sentence {}-th is in valid: {}".format(i, input_)
                self.fail(error_msg)

    def test_relation_condition(self):
        inputs_ = [
            "relation(A,of,named('John'))",
            "relation(A,of,named('John'))",
            "relation(B,of,C)",
            "relation(B,of,C)",
        ]
        parser = Lark(grammar_test_str, start="test_relation_condition")
        for i, input_ in enumerate(inputs_):
            try:
                result = parser.parse(input_)
            except:
                error_msg = "Sentence {}-th is in valid: {}".format(i, input_)
                self.fail(error_msg)

    def test_modifier_adv_condition(self):
        inputs_ = [
            "modifier_adv(B,slowly,pos)",
            "modifier_adv(B,slowly,pos)",
            "modifier_adv(C,slowly,pos)",
            "modifier_adv(C,slowly,pos)",
            "modifier_adv(C,slowly,pos)",
            "modifier_adv(A,slowly,pos)",
            "modifier_adv(B,slowly,pos)",
            "modifier_adv(A,slowly,pos)",
            "modifier_adv(D,slowly,pos)",
            "modifier_adv(D,slowly,pos)",
            "modifier_adv(B,slowly,pos)",
            "modifier_adv(B,slowly,pos)",
            "modifier_adv(C,slowly,pos)",
            "modifier_adv(C,slowly,pos)",
            "modifier_adv(B,slowly,pos)",
            "modifier_adv(B,slowly,pos)",
        ]
        parser = Lark(grammar_test_str, start="test_modifier_adv_condition")
        for i, input_ in enumerate(inputs_):
            try:
                result = parser.parse(input_)
            except:
                error_msg = "Sentence {}-th is in valid: {}".format(i, input_)
                self.fail(error_msg)

    def test_modifier_pp_condition(self):
        inputs_ = [
            "modifier_pp(B,under,C)",
            "modifier_pp(D,under,E)",
            "modifier_pp(C,under,D)",
        ]
        parser = Lark(grammar_test_str, start="test_modifier_pp_condition")
        for i, input_ in enumerate(inputs_):
            try:
                result = parser.parse(input_)
            except:
                error_msg = "Sentence {}-th is in valid: {}".format(i, input_)
                self.fail(error_msg)

    def test_query_condition(self):
        inputs_ = [
            "query(A,who)",
            "query(A,who)",
            "query(A,who)",
            "query(A,who)",
            "query(A,who)",
            "query(A,who)",
            "query(A,which)",
            "query(A,which)",
            "query(A,which)",
        ]
        parser = Lark(grammar_test_str, start="test_query_condition")
        for i, input_ in enumerate(inputs_):
            try:
                result = parser.parse(input_)
            except:
                error_msg = "Sentence {}-th is in valid: {}".format(i, input_)
                self.fail(error_msg)


class Test_Rule_Main(unittest.TestCase):
    def test_atomic_condition(self):
        inputs_ = [
            "object(A,robot,countable,na,eq,1)-1/2",
            "predicate(B,run,A)-1/3",
            "object(A,robot,countable,na,eq,1)-1/2",
            "predicate(B,run,A)-1/3",
            "modifier_adv(B,slowly,pos)-1/4",
            "object(A,apple,countable,na,eq,1)-1/4",
            "predicate(B,throw,named('John'),A)-1/2",
            "object(A,apple,countable,na,eq,1)-1/4",
            "predicate(B,throw,named('John'),A)-1/2",
            "modifier_adv(B,slowly,pos)-1/5",
            "object(A,robot,countable,na,eq,1)-1/3",
            "property(A,small,pos)-1/2",
            "object(B,apple,countable,na,eq,1)-1/6",
            "predicate(C,throw,A,B)-1/4",
            "modifier_adv(C,slowly,pos)-1/7",
            "object(A,robot,countable,na,eq,1)-1/3",
            "property(A,small,pos)-1/2",
            "object(B,apple,countable,na,eq,1)-1/7",
            "property(B,red,pos)-1/6",
            "predicate(C,throw,A,B)-1/4",
            "modifier_adv(C,slowly,pos)-1/8",
            "object(A,robot,countable,na,eq,1)-1/5",
            "property(A,small,pos)-1/2",
            "property(A,green,pos)-1/4",
            "object(B,apple,countable,na,eq,1)-1/8",
            "predicate(C,throw,A,B)-1/6",
            "relation(A,of,named('John'))-1/2",
            "object(A,robot,countable,na,eq,1)-1/4",
            "object(B,apple,countable,na,eq,1)-1/7",
            "predicate(C,throw,A,B)-1/5",
            "relation(A,of,named('John'))-1/2",
            "object(A,robot,countable,na,eq,1)-1/4",
            "object(B,apple,countable,na,eq,1)-1/7",
            "predicate(C,throw,A,B)-1/5",
            "modifier_adv(C,slowly,pos)-1/8",
            "relation(B,of,C)-1/3",
            "object(B,robot,countable,na,eq,1)-1/2",
            "predicate(A,run,B)-1/6",
            "object(C,company,countable,na,eq,1)-1/5",
            "relation(B,of,C)-1/3",
            "object(B,robot,countable,na,eq,1)-1/2",
            "predicate(A,run,B)-1/6",
            "modifier_adv(A,slowly,pos)-1/7",
            "object(C,company,countable,na,eq,1)-1/5",
            "predicate(F,be,D,E)-1/4",
            "object(E,agent,countable,na,eq,1)-1/6",
            "object(D,robot,countable,na,eq,1)-1/2",
            "object(A,apple,countable,na,eq,1)-1/10",
            "property(A,red,pos)-1/9",
            "object(C,table,countable,na,eq,1)-1/14",
            "predicate(B,throw,D,A)-1/7",
            "modifier_pp(B,under,C)-1/12",
            "modifier_adv(B,slowly,pos)-1/11",
            "predicate(D,be,B,C)-1/4",
            "object(C,agent,countable,na,eq,1)-1/6",
            "object(B,robot,countable,na,eq,1)-1/2",
            "predicate(A,move,B)-1/7",
            "modifier_adv(A,slowly,pos)-1/8",
            "object(A,agent,countable,na,eq,1)-1/5",
            "predicate(B,be,named('John'),A)-1/3",
            "object(C,apple,countable,na,eq,1)-1/9",
            "property(C,red,pos)-1/8",
            "predicate(D,throw,named('John'),C)-1/6",
            "modifier_adv(D,slowly,pos)-1/10",
            "object(A,agent,countable,na,eq,1)-1/5",
            "predicate(B,be,named('John'),A)-1/3",
            "object(C,apple,countable,na,eq,1)-1/9",
            "property(C,red,pos)-1/8",
            "object(E,table,countable,na,eq,1)-1/13",
            "predicate(D,throw,named('John'),C)-1/6",
            "modifier_pp(D,under,E)-1/11",
            "modifier_adv(D,slowly,pos)-1/10",
            "object(C,robot,countable,na,eq,1)-1/2",
            "object(A,apple,countable,kg,eq,3)-1/7",
            "predicate(B,throw,C,A)-1/3",
            "modifier_adv(B,slowly,pos)-1/8",
            "object(C,robot,countable,na,eq,1)-1/2",
            "object(A,apple,countable,kg,eq,3)-1/8",
            "property(A,red,pos)-1/7",
            "predicate(B,throw,C,A)-1/3",
            "modifier_adv(B,slowly,pos)-1/9",
            "object(C,robot,countable,na,eq,1)-1/2",
            "object(A,metal,countable,pound,eq,3)-1/7",
            "predicate(B,be,C,A)-1/3",
            "object(A,robot,countable,na,eq,1)-1/2",
            "object(A,robot,countable,na,eq,1)-1/2",

        ]
        parser = Lark(grammar_test_str, start="test_atomic_condition")
        for i, input_ in enumerate(inputs_):
            try:
                result = parser.parse(input_)
            except:
                error_msg = "Sentence {}-th is in valid: {}".format(i, input_)
                self.fail(error_msg)

    def test_complex_condition(self):
        inputs_ = [
            "-(drs([A],[object(A,apple,countable,na,eq,1)-1/4]))",
            "question(drs([A,B,C,D],[object(D,apple,countable,na,eq,1)-1/3,property(C,red,pos)-1/7,object(C,box,countable,na,eq,1)-1/8,property(A,small,comp_than,C)-1/4,predicate(B,be,D,A)-1/1]))",
            "question(drs([A,B,C,D],[object(D,apple,countable,na,eq,1)-1/3,property(C,red,pos)-1/8,object(C,box,countable,na,eq,1)-1/9,property(A,small,comp_than,C)-1/5,predicate(B,be,D,A)-1/1]))",
            "question(drs([A,B,C],[object(C,apple,countable,na,eq,1)-1/3,object(A,agent,countable,na,eq,1)-1/5,predicate(B,be,C,A)-1/1]))",
            "question(drs([A,B],[object(A,agent,countable,na,eq,1)-1/4,predicate(B,be,named('John'),A)-1/1]))",
            "question(drs([A,B],[query(A,who)-1/1,predicate(B,move,A)-1/3,modifier_adv(B,slowly,pos)-1/4]))",
            "question(drs([A,B],[query(A,who)-1/1,modifier_adv(B,slowly,pos)-1/3,predicate(B,move,A)-1/4]))",
            "question(drs([A,B,C,D],[query(A,who)-1/1,property(D,red,pos)-1/7,object(D,block,countable,na,eq,1)-1/8,property(B,small,pos_as,D)-1/4,predicate(C,be,A,B)-1/2]))",
            "question(drs([A,B,C,D],[query(A,who)-1/1,property(D,red,pos)-1/6,object(D,block,countable,na,eq,1)-1/7,property(B,small,comp_than,D)-1/3,predicate(C,be,A,B)-1/2]))",
            "question(drs([A,B,C],[query(A,who)-1/1,property(C,small,sup)-1/4,object(C,agent,countable,na,eq,1)-1/5,predicate(B,be,A,C)-1/2]))",
            "question(drs([A,B],[query(A,who)-1/1,predicate(B,be,A,named('John'))-1/2]))",
            "question(drs([A,B,C,D],[query(A,which)-1/1,object(A,robot,countable,na,eq,1)-1/2,property(D,red,pos)-1/7,object(D,block,countable,na,eq,1)-1/8,property(B,small,comp_than,D)-1/4,predicate(C,be,A,B)-1/3]))",
            "question(drs([A,B,C,D],[query(A,which)-1/1,object(A,robot,countable,na,eq,1)-1/2,property(D,red,pos)-1/8,object(D,block,countable,na,eq,1)-1/9,property(B,small,pos_as,D)-1/5,predicate(C,be,A,B)-1/3]))",
            "question(drs([A,B],[query(A,which)-1/1,object(A,robot,countable,na,eq,1)-1/2,predicate(B,be,A,named('John'))-1/3]))",
            "command(drs([A,B,C],[object(C,apple,countable,na,eq,1)-1/5,object(B,table,countable,na,eq,1)-1/8,predicate(A,move,named('Sawyer'),C)-1/3,modifier_adv(A,slowly,pos)-1/9,modifier_pp(A,on,B)-1/6]))",
            "command(drs([A,B,C],[property(C,red,pos)-1/5,object(C,apple,countable,na,eq,1)-1/6,object(B,table,countable,na,eq,1)-1/9,predicate(A,move,named('Sawyer'),C)-1/3,modifier_pp(A,on,B)-1/7]))",
            "command(drs([A,B,C],[property(C,red,pos)-1/5,object(C,apple,countable,na,eq,1)-1/6,object(B,table,countable,na,eq,1)-1/9,predicate(A,move,named('Sawyer'),C)-1/3,modifier_adv(A,slowly,pos)-1/10,modifier_pp(A,on,B)-1/7]))",
            "command(drs([A,B,C],[property(C,red,pos)-1/5,object(C,apple,countable,na,eq,1)-1/6,object(B,table,countable,na,eq,1)-1/9,predicate(A,pick,named('Sawyer'),C)-1/3,modifier_adv(A,slowly,pos)-1/10,modifier_pp(A,on,B)-1/7]))",
            "command(drs([A,B,C],[property(C,red,pos)-1/5,object(C,apple,countable,na,eq,1)-1/6,object(B,table,countable,na,eq,1)-1/9,predicate(A,grasp,named('Sawyer'),C)-1/3,modifier_adv(A,slowly,pos)-1/10,modifier_pp(A,on,B)-1/7]))",
            "=>(drs([A,B,C],[relation(B,of,C)-1/4,object(B,robot,countable,na,eq,1)-1/3,predicate(A,run,B)-1/7,object(C,company,countable,na,eq,1)-1/6]),drs([D],[predicate(D,run,B)-1/14,modifier_adv(D,slowly,pos)-1/15]))",
            "=>(drs([A,B,C,D],[relation(C,of,D)-1/4,object(C,robot,countable,na,eq,1)-1/3,object(A,apple,countable,na,eq,1)-1/9,predicate(B,throw,C,A)-1/7,object(D,company,countable,na,eq,1)-1/6]),drs([E,F],[object(E,apple,countable,na,eq,1)-1/18,predicate(F,throw,C,E)-1/16,modifier_adv(F,slowly,pos)-1/19]))",
            "=>(drs([A,B,C,D],[relation(C,of,D)-1/4,object(C,robot,countable,na,eq,1)-1/3,object(A,apple,countable,na,eq,1)-1/10,property(A,red,pos)-1/9,predicate(B,throw,C,A)-1/7,modifier_adv(B,slowly,pos)-1/11,object(D,company,countable,na,eq,1)-1/6]),drs([E,F,G],[object(E,apple,countable,na,eq,1)-1/21,property(E,red,pos)-1/20,predicate(F,throw,C,E)-1/18,modifier_pp(F,under,G)-1/23,modifier_adv(F,slowly,pos)-1/22,object(G,table,countable,na,eq,1)-1/25]))",
            "=>(drs([A,B,C],[relation(B,of,C)-1/4,object(B,robot,countable,na,eq,1)-1/3,predicate(A,run,B)-1/7,object(C,company,countable,na,eq,1)-1/6]),drs([D],[predicate(D,run,B)-1/14,modifier_adv(D,slowly,pos)-1/15]))",
            "=>(drs([A,B,C,D],[relation(C,of,D)-1/4,object(C,robot,countable,na,eq,1)-1/3,object(A,apple,countable,na,eq,1)-1/9,predicate(B,throw,C,A)-1/7,object(D,company,countable,na,eq,1)-1/6]),drs([E,F],[object(E,apple,countable,na,eq,1)-1/18,predicate(F,throw,C,E)-1/16,modifier_adv(F,slowly,pos)-1/19]))",
            "=>(drs([A,B,C,D],[relation(C,of,D)-1/4,object(C,robot,countable,na,eq,1)-1/3,object(A,apple,countable,na,eq,1)-1/10,property(A,red,pos)-1/9,predicate(B,throw,C,A)-1/7,modifier_adv(B,slowly,pos)-1/11,object(D,company,countable,na,eq,1)-1/6]),drs([E,F,G],[object(E,apple,countable,na,eq,1)-1/21,property(E,red,pos)-1/20,predicate(F,throw,C,E)-1/18,modifier_pp(F,under,G)-1/23,modifier_adv(F,slowly,pos)-1/22,object(G,table,countable,na,eq,1)-1/25]))",
            "=>(drs([A,B,C],[object(A,agent,countable,na,eq,1)-1/6,predicate(B,be,named('John'),A)-1/4,predicate(C,run,named('John'))-1/7]),drs([D,E,F],[object(D,agent,countable,na,eq,1)-1/13,predicate(E,be,named('John'),D)-1/11,predicate(F,run,named('John'))-1/14,modifier_adv(F,slowly,pos)-1/15]))",
            "=>(drs([A,B,C,D],[object(A,agent,countable,na,eq,1)-1/6,predicate(B,be,named('John'),A)-1/4,object(C,apple,countable,na,eq,1)-1/9,predicate(D,throw,named('John'),C)-1/7]),drs([E,F,G,H],[object(E,agent,countable,na,eq,1)-1/15,predicate(F,be,named('John'),E)-1/13,object(G,apple,countable,na,eq,1)-1/18,predicate(H,throw,named('John'),G)-1/16,modifier_adv(H,slowly,pos)-1/19]))",
            "=>(drs([A,B,C,D],[object(A,agent,countable,na,eq,1)-1/6,predicate(B,be,named('John'),A)-1/4,object(C,apple,countable,na,eq,1)-1/10,property(C,red,pos)-1/9,predicate(D,throw,named('John'),C)-1/7,modifier_adv(D,slowly,pos)-1/11]),drs([E,F,G,H,I],[object(E,agent,countable,na,eq,1)-1/17,predicate(F,be,named('John'),E)-1/15,object(G,apple,countable,na,eq,1)-1/21,property(G,red,pos)-1/20,object(I,table,countable,na,eq,1)-1/25,predicate(H,throw,named('John'),G)-1/18,modifier_pp(H,under,I)-1/23,modifier_adv(H,slowly,pos)-1/22]))",
            "v(drs([A,B],[object(A,robot,countable,na,eq,1)-1/3,property(A,small,pos)-1/2,predicate(B,run,A)-1/4]),drs([C,D],[object(C,robot,countable,na,eq,1)-1/8,property(C,small,pos)-1/7,predicate(D,run,C)-1/9,modifier_adv(D,slowly,pos)-1/10]))",
            "v(drs([A,B,C],[object(A,robot,countable,na,eq,1)-1/3,property(A,small,pos)-1/2,object(B,apple,countable,na,eq,1)-1/6,predicate(C,throw,A,B)-1/4]),drs([D,E,F],[object(D,robot,countable,na,eq,1)-1/10,property(D,small,pos)-1/9,object(E,apple,countable,na,eq,1)-1/13,predicate(F,throw,D,E)-1/11,modifier_adv(F,slowly,pos)-1/14]))",
            "v(drs([A,B,C],[object(A,robot,countable,na,eq,1)-1/3,property(A,small,pos)-1/2,object(B,apple,countable,na,eq,1)-1/7,property(B,red,pos)-1/6,predicate(C,throw,A,B)-1/4,modifier_adv(C,slowly,pos)-1/8]),drs([D,E,F,G],[object(D,robot,countable,na,eq,1)-1/12,property(D,small,pos)-1/11,object(E,apple,countable,na,eq,1)-1/16,property(E,red,pos)-1/15,object(G,table,countable,na,eq,1)-1/20,predicate(F,throw,D,E)-1/13,modifier_pp(F,under,G)-1/18,modifier_adv(F,slowly,pos)-1/17]))",
            "v(drs([A,B],[object(A,robot,countable,na,eq,1)-1/3,property(A,small,pos)-1/2,predicate(B,run,A)-1/4]),drs([C],[object(C,apple,countable,na,eq,1)-1/9]))",
            "v(drs([A,B,C],[object(A,robot,countable,na,eq,1)-1/3,property(A,small,pos)-1/2,object(B,apple,countable,na,eq,1)-1/6,predicate(C,throw,A,B)-1/4]),drs([D],[object(D,apple,countable,na,eq,1)-1/11]))",
            "v(drs([A,B,C],[object(A,robot,countable,na,eq,1)-1/3,property(A,small,pos)-1/2,object(B,apple,countable,na,eq,1)-1/7,property(B,red,pos)-1/6,predicate(C,throw,A,B)-1/4,modifier_adv(C,slowly,pos)-1/8]),drs([D],[object(D,apple,countable,na,eq,3)-1/13]))",
        ]
        parser = Lark(grammar_test_str, start="test_complex_condition")
        for i, input_ in enumerate(inputs_):
            try:
                result = parser.parse(input_)
            except:
                error_msg = "Sentence {}-th is in valid: {}".format(i, input_)
                self.fail(error_msg)

    def test_condition(self):
        inputs_ = [
            "object(A,robot,countable,na,eq,1)-1/2",
            "predicate(B,run,A)-1/3",
            "object(A,robot,countable,na,eq,1)-1/2",
            "predicate(B,run,A)-1/3",
            "modifier_adv(B,slowly,pos)-1/4",
            "object(A,apple,countable,na,eq,1)-1/4",
            "predicate(B,throw,named('John'),A)-1/2",
            "object(A,apple,countable,na,eq,1)-1/4",
            "predicate(B,throw,named('John'),A)-1/2",
            "modifier_adv(B,slowly,pos)-1/5",
            "object(A,robot,countable,na,eq,1)-1/3",
            "property(A,small,pos)-1/2",
            "object(B,apple,countable,na,eq,1)-1/6",
            "predicate(C,throw,A,B)-1/4",
            "modifier_adv(C,slowly,pos)-1/7",
            "object(A,robot,countable,na,eq,1)-1/3",
            "property(A,small,pos)-1/2",
            "object(B,apple,countable,na,eq,1)-1/7",
            "property(B,red,pos)-1/6",
            "predicate(C,throw,A,B)-1/4",
            "modifier_adv(C,slowly,pos)-1/8",
            "object(A,robot,countable,na,eq,1)-1/5",
            "property(A,small,pos)-1/2",
            "property(A,green,pos)-1/4",
            "object(B,apple,countable,na,eq,1)-1/8",
            "predicate(C,throw,A,B)-1/6",
            "relation(A,of,named('John'))-1/2",
            "object(A,robot,countable,na,eq,1)-1/4",
            "object(B,apple,countable,na,eq,1)-1/7",
            "predicate(C,throw,A,B)-1/5",
            "relation(A,of,named('John'))-1/2",
            "object(A,robot,countable,na,eq,1)-1/4",
            "object(B,apple,countable,na,eq,1)-1/7",
            "predicate(C,throw,A,B)-1/5",
            "modifier_adv(C,slowly,pos)-1/8",
            "relation(B,of,C)-1/3",
            "object(B,robot,countable,na,eq,1)-1/2",
            "predicate(A,run,B)-1/6",
            "object(C,company,countable,na,eq,1)-1/5",
            "relation(B,of,C)-1/3",
            "object(B,robot,countable,na,eq,1)-1/2",
            "predicate(A,run,B)-1/6",
            "modifier_adv(A,slowly,pos)-1/7",
            "object(C,company,countable,na,eq,1)-1/5",
            "predicate(F,be,D,E)-1/4",
            "object(E,agent,countable,na,eq,1)-1/6",
            "object(D,robot,countable,na,eq,1)-1/2",
            "object(A,apple,countable,na,eq,1)-1/10",
            "property(A,red,pos)-1/9",
            "object(C,table,countable,na,eq,1)-1/14",
            "predicate(B,throw,D,A)-1/7",
            "modifier_pp(B,under,C)-1/12",
            "modifier_adv(B,slowly,pos)-1/11",
            "predicate(D,be,B,C)-1/4",
            "object(C,agent,countable,na,eq,1)-1/6",
            "object(B,robot,countable,na,eq,1)-1/2",
            "predicate(A,move,B)-1/7",
            "modifier_adv(A,slowly,pos)-1/8",
            "object(A,agent,countable,na,eq,1)-1/5",
            "predicate(B,be,named('John'),A)-1/3",
            "object(C,apple,countable,na,eq,1)-1/9",
            "property(C,red,pos)-1/8",
            "predicate(D,throw,named('John'),C)-1/6",
            "modifier_adv(D,slowly,pos)-1/10",
            "object(A,agent,countable,na,eq,1)-1/5",
            "predicate(B,be,named('John'),A)-1/3",
            "object(C,apple,countable,na,eq,1)-1/9",
            "property(C,red,pos)-1/8",
            "object(E,table,countable,na,eq,1)-1/13",
            "predicate(D,throw,named('John'),C)-1/6",
            "modifier_pp(D,under,E)-1/11",
            "modifier_adv(D,slowly,pos)-1/10",
            "object(C,robot,countable,na,eq,1)-1/2",
            "object(A,apple,countable,kg,eq,3)-1/7",
            "predicate(B,throw,C,A)-1/3",
            "modifier_adv(B,slowly,pos)-1/8",
            "object(C,robot,countable,na,eq,1)-1/2",
            "object(A,apple,countable,kg,eq,3)-1/8",
            "property(A,red,pos)-1/7",
            "predicate(B,throw,C,A)-1/3",
            "modifier_adv(B,slowly,pos)-1/9",
            "object(C,robot,countable,na,eq,1)-1/2",
            "object(A,metal,countable,pound,eq,3)-1/7",
            "predicate(B,be,C,A)-1/3",
            "object(A,robot,countable,na,eq,1)-1/2",
            "object(A,robot,countable,na,eq,1)-1/2",
            "-(drs([A],[object(A,apple,countable,na,eq,1)-1/4]))",
            "question(drs([A,B,C,D],[object(D,apple,countable,na,eq,1)-1/3,property(C,red,pos)-1/7,object(C,box,countable,na,eq,1)-1/8,property(A,small,comp_than,C)-1/4,predicate(B,be,D,A)-1/1]))",
            "question(drs([A,B,C,D],[object(D,apple,countable,na,eq,1)-1/3,property(C,red,pos)-1/8,object(C,box,countable,na,eq,1)-1/9,property(A,small,comp_than,C)-1/5,predicate(B,be,D,A)-1/1]))",
            "question(drs([A,B,C],[object(C,apple,countable,na,eq,1)-1/3,object(A,agent,countable,na,eq,1)-1/5,predicate(B,be,C,A)-1/1]))",
            "question(drs([A,B],[object(A,agent,countable,na,eq,1)-1/4,predicate(B,be,named('John'),A)-1/1]))",
            "question(drs([A,B],[query(A,who)-1/1,predicate(B,move,A)-1/3,modifier_adv(B,slowly,pos)-1/4]))",
            "question(drs([A,B],[query(A,who)-1/1,modifier_adv(B,slowly,pos)-1/3,predicate(B,move,A)-1/4]))",
            "question(drs([A,B,C,D],[query(A,who)-1/1,property(D,red,pos)-1/7,object(D,block,countable,na,eq,1)-1/8,property(B,small,pos_as,D)-1/4,predicate(C,be,A,B)-1/2]))",
            "question(drs([A,B,C,D],[query(A,who)-1/1,property(D,red,pos)-1/6,object(D,block,countable,na,eq,1)-1/7,property(B,small,comp_than,D)-1/3,predicate(C,be,A,B)-1/2]))",
            "question(drs([A,B,C],[query(A,who)-1/1,property(C,small,sup)-1/4,object(C,agent,countable,na,eq,1)-1/5,predicate(B,be,A,C)-1/2]))",
            "question(drs([A,B],[query(A,who)-1/1,predicate(B,be,A,named('John'))-1/2]))",
            "question(drs([A,B,C,D],[query(A,which)-1/1,object(A,robot,countable,na,eq,1)-1/2,property(D,red,pos)-1/7,object(D,block,countable,na,eq,1)-1/8,property(B,small,comp_than,D)-1/4,predicate(C,be,A,B)-1/3]))",
            "question(drs([A,B,C,D],[query(A,which)-1/1,object(A,robot,countable,na,eq,1)-1/2,property(D,red,pos)-1/8,object(D,block,countable,na,eq,1)-1/9,property(B,small,pos_as,D)-1/5,predicate(C,be,A,B)-1/3]))",
            "question(drs([A,B],[query(A,which)-1/1,object(A,robot,countable,na,eq,1)-1/2,predicate(B,be,A,named('John'))-1/3]))",
            "command(drs([A,B,C],[object(C,apple,countable,na,eq,1)-1/5,object(B,table,countable,na,eq,1)-1/8,predicate(A,move,named('Sawyer'),C)-1/3,modifier_adv(A,slowly,pos)-1/9,modifier_pp(A,on,B)-1/6]))",
            "command(drs([A,B,C],[property(C,red,pos)-1/5,object(C,apple,countable,na,eq,1)-1/6,object(B,table,countable,na,eq,1)-1/9,predicate(A,move,named('Sawyer'),C)-1/3,modifier_pp(A,on,B)-1/7]))",
            "command(drs([A,B,C],[property(C,red,pos)-1/5,object(C,apple,countable,na,eq,1)-1/6,object(B,table,countable,na,eq,1)-1/9,predicate(A,move,named('Sawyer'),C)-1/3,modifier_adv(A,slowly,pos)-1/10,modifier_pp(A,on,B)-1/7]))",
            "command(drs([A,B,C],[property(C,red,pos)-1/5,object(C,apple,countable,na,eq,1)-1/6,object(B,table,countable,na,eq,1)-1/9,predicate(A,pick,named('Sawyer'),C)-1/3,modifier_adv(A,slowly,pos)-1/10,modifier_pp(A,on,B)-1/7]))",
            "command(drs([A,B,C],[property(C,red,pos)-1/5,object(C,apple,countable,na,eq,1)-1/6,object(B,table,countable,na,eq,1)-1/9,predicate(A,grasp,named('Sawyer'),C)-1/3,modifier_adv(A,slowly,pos)-1/10,modifier_pp(A,on,B)-1/7]))",
            "=>(drs([A,B,C],[relation(B,of,C)-1/4,object(B,robot,countable,na,eq,1)-1/3,predicate(A,run,B)-1/7,object(C,company,countable,na,eq,1)-1/6]),drs([D],[predicate(D,run,B)-1/14,modifier_adv(D,slowly,pos)-1/15]))",
            "=>(drs([A,B,C,D],[relation(C,of,D)-1/4,object(C,robot,countable,na,eq,1)-1/3,object(A,apple,countable,na,eq,1)-1/9,predicate(B,throw,C,A)-1/7,object(D,company,countable,na,eq,1)-1/6]),drs([E,F],[object(E,apple,countable,na,eq,1)-1/18,predicate(F,throw,C,E)-1/16,modifier_adv(F,slowly,pos)-1/19]))",
            "=>(drs([A,B,C,D],[relation(C,of,D)-1/4,object(C,robot,countable,na,eq,1)-1/3,object(A,apple,countable,na,eq,1)-1/10,property(A,red,pos)-1/9,predicate(B,throw,C,A)-1/7,modifier_adv(B,slowly,pos)-1/11,object(D,company,countable,na,eq,1)-1/6]),drs([E,F,G],[object(E,apple,countable,na,eq,1)-1/21,property(E,red,pos)-1/20,predicate(F,throw,C,E)-1/18,modifier_pp(F,under,G)-1/23,modifier_adv(F,slowly,pos)-1/22,object(G,table,countable,na,eq,1)-1/25]))",
            "=>(drs([A,B,C],[relation(B,of,C)-1/4,object(B,robot,countable,na,eq,1)-1/3,predicate(A,run,B)-1/7,object(C,company,countable,na,eq,1)-1/6]),drs([D],[predicate(D,run,B)-1/14,modifier_adv(D,slowly,pos)-1/15]))",
            "=>(drs([A,B,C,D],[relation(C,of,D)-1/4,object(C,robot,countable,na,eq,1)-1/3,object(A,apple,countable,na,eq,1)-1/9,predicate(B,throw,C,A)-1/7,object(D,company,countable,na,eq,1)-1/6]),drs([E,F],[object(E,apple,countable,na,eq,1)-1/18,predicate(F,throw,C,E)-1/16,modifier_adv(F,slowly,pos)-1/19]))",
            "=>(drs([A,B,C,D],[relation(C,of,D)-1/4,object(C,robot,countable,na,eq,1)-1/3,object(A,apple,countable,na,eq,1)-1/10,property(A,red,pos)-1/9,predicate(B,throw,C,A)-1/7,modifier_adv(B,slowly,pos)-1/11,object(D,company,countable,na,eq,1)-1/6]),drs([E,F,G],[object(E,apple,countable,na,eq,1)-1/21,property(E,red,pos)-1/20,predicate(F,throw,C,E)-1/18,modifier_pp(F,under,G)-1/23,modifier_adv(F,slowly,pos)-1/22,object(G,table,countable,na,eq,1)-1/25]))",
            "=>(drs([A,B,C],[object(A,agent,countable,na,eq,1)-1/6,predicate(B,be,named('John'),A)-1/4,predicate(C,run,named('John'))-1/7]),drs([D,E,F],[object(D,agent,countable,na,eq,1)-1/13,predicate(E,be,named('John'),D)-1/11,predicate(F,run,named('John'))-1/14,modifier_adv(F,slowly,pos)-1/15]))",
            "=>(drs([A,B,C,D],[object(A,agent,countable,na,eq,1)-1/6,predicate(B,be,named('John'),A)-1/4,object(C,apple,countable,na,eq,1)-1/9,predicate(D,throw,named('John'),C)-1/7]),drs([E,F,G,H],[object(E,agent,countable,na,eq,1)-1/15,predicate(F,be,named('John'),E)-1/13,object(G,apple,countable,na,eq,1)-1/18,predicate(H,throw,named('John'),G)-1/16,modifier_adv(H,slowly,pos)-1/19]))",
            "=>(drs([A,B,C,D],[object(A,agent,countable,na,eq,1)-1/6,predicate(B,be,named('John'),A)-1/4,object(C,apple,countable,na,eq,1)-1/10,property(C,red,pos)-1/9,predicate(D,throw,named('John'),C)-1/7,modifier_adv(D,slowly,pos)-1/11]),drs([E,F,G,H,I],[object(E,agent,countable,na,eq,1)-1/17,predicate(F,be,named('John'),E)-1/15,object(G,apple,countable,na,eq,1)-1/21,property(G,red,pos)-1/20,object(I,table,countable,na,eq,1)-1/25,predicate(H,throw,named('John'),G)-1/18,modifier_pp(H,under,I)-1/23,modifier_adv(H,slowly,pos)-1/22]))",
            "v(drs([A,B],[object(A,robot,countable,na,eq,1)-1/3,property(A,small,pos)-1/2,predicate(B,run,A)-1/4]),drs([C,D],[object(C,robot,countable,na,eq,1)-1/8,property(C,small,pos)-1/7,predicate(D,run,C)-1/9,modifier_adv(D,slowly,pos)-1/10]))",
            "v(drs([A,B,C],[object(A,robot,countable,na,eq,1)-1/3,property(A,small,pos)-1/2,object(B,apple,countable,na,eq,1)-1/6,predicate(C,throw,A,B)-1/4]),drs([D,E,F],[object(D,robot,countable,na,eq,1)-1/10,property(D,small,pos)-1/9,object(E,apple,countable,na,eq,1)-1/13,predicate(F,throw,D,E)-1/11,modifier_adv(F,slowly,pos)-1/14]))",
            "v(drs([A,B,C],[object(A,robot,countable,na,eq,1)-1/3,property(A,small,pos)-1/2,object(B,apple,countable,na,eq,1)-1/7,property(B,red,pos)-1/6,predicate(C,throw,A,B)-1/4,modifier_adv(C,slowly,pos)-1/8]),drs([D,E,F,G],[object(D,robot,countable,na,eq,1)-1/12,property(D,small,pos)-1/11,object(E,apple,countable,na,eq,1)-1/16,property(E,red,pos)-1/15,object(G,table,countable,na,eq,1)-1/20,predicate(F,throw,D,E)-1/13,modifier_pp(F,under,G)-1/18,modifier_adv(F,slowly,pos)-1/17]))",
            "v(drs([A,B],[object(A,robot,countable,na,eq,1)-1/3,property(A,small,pos)-1/2,predicate(B,run,A)-1/4]),drs([C],[object(C,apple,countable,na,eq,1)-1/9]))",
            "v(drs([A,B,C],[object(A,robot,countable,na,eq,1)-1/3,property(A,small,pos)-1/2,object(B,apple,countable,na,eq,1)-1/6,predicate(C,throw,A,B)-1/4]),drs([D],[object(D,apple,countable,na,eq,1)-1/11]))",
            "v(drs([A,B,C],[object(A,robot,countable,na,eq,1)-1/3,property(A,small,pos)-1/2,object(B,apple,countable,na,eq,1)-1/7,property(B,red,pos)-1/6,predicate(C,throw,A,B)-1/4,modifier_adv(C,slowly,pos)-1/8]),drs([D],[object(D,apple,countable,na,eq,3)-1/13]))",
        ]
        parser = Lark(grammar_test_str, start="test_condition")
        for i, input_ in enumerate(inputs_):
            try:
                result = parser.parse(input_)
            except:
                error_msg = "Sentence {}-th is in valid: {}".format(i, input_)
                self.fail(error_msg)

    def test_conditions(self):
        inputs_ = [
            "[object(A,robot,countable,na,eq,1)-1/2,predicate(B,run,A)-1/3]",
            "[object(A,robot,countable,na,eq,1)-1/2,predicate(B,run,A)-1/3,modifier_adv(B,slowly,pos)-1/4]",
            "[object(A,apple,countable,na,eq,1)-1/4,predicate(B,throw,named('John'),A)-1/2]",
            "[object(A,apple,countable,na,eq,1)-1/4,predicate(B,throw,named('John'),A)-1/2,modifier_adv(B,slowly,pos)-1/5]",
            "[object(A,robot,countable,na,eq,1)-1/3,property(A,small,pos)-1/2,object(B,apple,countable,na,eq,1)-1/6,predicate(C,throw,A,B)-1/4,modifier_adv(C,slowly,pos)-1/7]",
            "[object(A,robot,countable,na,eq,1)-1/3,property(A,small,pos)-1/2,object(B,apple,countable,na,eq,1)-1/7,property(B,red,pos)-1/6,predicate(C,throw,A,B)-1/4,modifier_adv(C,slowly,pos)-1/8]",
            "[object(A,robot,countable,na,eq,1)-1/5,property(A,small,pos)-1/2,property(A,green,pos)-1/4,object(B,apple,countable,na,eq,1)-1/8,predicate(C,throw,A,B)-1/6]",
            "[relation(A,of,named('John'))-1/2,object(A,robot,countable,na,eq,1)-1/4,object(B,apple,countable,na,eq,1)-1/7,predicate(C,throw,A,B)-1/5]",
            "[relation(A,of,named('John'))-1/2,object(A,robot,countable,na,eq,1)-1/4,object(B,apple,countable,na,eq,1)-1/7,predicate(C,throw,A,B)-1/5,modifier_adv(C,slowly,pos)-1/8]",
            "[relation(B,of,C)-1/3,object(B,robot,countable,na,eq,1)-1/2,predicate(A,run,B)-1/6,object(C,company,countable,na,eq,1)-1/5]",
            "[relation(B,of,C)-1/3,object(B,robot,countable,na,eq,1)-1/2,predicate(A,run,B)-1/6,modifier_adv(A,slowly,pos)-1/7,object(C,company,countable,na,eq,1)-1/5]",
            "[predicate(F,be,D,E)-1/4,object(E,agent,countable,na,eq,1)-1/6,object(D,robot,countable,na,eq,1)-1/2,object(A,apple,countable,na,eq,1)-1/10,property(A,red,pos)-1/9,object(C,table,countable,na,eq,1)-1/14,predicate(B,throw,D,A)-1/7,modifier_pp(B,under,C)-1/12,modifier_adv(B,slowly,pos)-1/11]",
            "[predicate(D,be,B,C)-1/4,object(C,agent,countable,na,eq,1)-1/6,object(B,robot,countable,na,eq,1)-1/2,predicate(A,move,B)-1/7,modifier_adv(A,slowly,pos)-1/8]",
            "[object(A,agent,countable,na,eq,1)-1/5,predicate(B,be,named('John'),A)-1/3,object(C,apple,countable,na,eq,1)-1/9,property(C,red,pos)-1/8,predicate(D,throw,named('John'),C)-1/6,modifier_adv(D,slowly,pos)-1/10]",
            "[object(A,agent,countable,na,eq,1)-1/5,predicate(B,be,named('John'),A)-1/3,object(C,apple,countable,na,eq,1)-1/9,property(C,red,pos)-1/8,object(E,table,countable,na,eq,1)-1/13,predicate(D,throw,named('John'),C)-1/6,modifier_pp(D,under,E)-1/11,modifier_adv(D,slowly,pos)-1/10]",
            "[object(C,robot,countable,na,eq,1)-1/2,object(A,apple,countable,kg,eq,3)-1/7,predicate(B,throw,C,A)-1/3,modifier_adv(B,slowly,pos)-1/8]",
            "[object(C,robot,countable,na,eq,1)-1/2,object(A,apple,countable,kg,eq,3)-1/8,property(A,red,pos)-1/7,predicate(B,throw,C,A)-1/3,modifier_adv(B,slowly,pos)-1/9]",
            "[object(C,robot,countable,na,eq,1)-1/2,object(A,metal,countable,pound,eq,3)-1/7,predicate(B,be,C,A)-1/3]",
            "[object(A,robot,countable,na,eq,1)-1/2,can(drs([B,C],[object(B,apple,countable,na,eq,1)-1/7,property(B,red,pos)-1/6,predicate(C,throw,A,B)-1/4,modifier_adv(C,slowly,pos)-1/8]))]",
            "[object(A,robot,countable,na,eq,1)-1/2,can(drs([B,C,D],[object(B,apple,countable,na,eq,1)-1/7,property(B,red,pos)-1/6,object(D,table,countable,na,eq,1)-1/11,predicate(C,throw,A,B)-1/4,modifier_pp(C,under,D)-1/9,modifier_adv(C,slowly,pos)-1/8]))]",
            "[-(drs([A],[object(A,apple,countable,na,eq,1)-1/4]))]",
            "[question(drs([A,B,C,D],[object(D,apple,countable,na,eq,1)-1/3,property(C,red,pos)-1/7,object(C,box,countable,na,eq,1)-1/8,property(A,small,comp_than,C)-1/4,predicate(B,be,D,A)-1/1]))]",
            "[question(drs([A,B,C,D],[object(D,apple,countable,na,eq,1)-1/3,property(C,red,pos)-1/8,object(C,box,countable,na,eq,1)-1/9,property(A,small,comp_than,C)-1/5,predicate(B,be,D,A)-1/1]))]",
            "[question(drs([A,B,C],[object(C,apple,countable,na,eq,1)-1/3,object(A,agent,countable,na,eq,1)-1/5,predicate(B,be,C,A)-1/1]))]",
            "[question(drs([A,B],[object(A,agent,countable,na,eq,1)-1/4,predicate(B,be,named('John'),A)-1/1]))]",
            "[question(drs([A,B],[query(A,who)-1/1,predicate(B,move,A)-1/3,modifier_adv(B,slowly,pos)-1/4]))]",
            "[question(drs([A,B],[query(A,who)-1/1,modifier_adv(B,slowly,pos)-1/3,predicate(B,move,A)-1/4]))]",
            "[question(drs([A,B,C,D],[query(A,who)-1/1,property(D,red,pos)-1/7,object(D,block,countable,na,eq,1)-1/8,property(B,small,pos_as,D)-1/4,predicate(C,be,A,B)-1/2]))]",
            "[question(drs([A,B,C,D],[query(A,who)-1/1,property(D,red,pos)-1/6,object(D,block,countable,na,eq,1)-1/7,property(B,small,comp_than,D)-1/3,predicate(C,be,A,B)-1/2]))]",
            "[question(drs([A,B,C],[query(A,who)-1/1,property(C,small,sup)-1/4,object(C,agent,countable,na,eq,1)-1/5,predicate(B,be,A,C)-1/2]))]",
            "[question(drs([A,B],[query(A,who)-1/1,predicate(B,be,A,named('John'))-1/2]))]",
            "[question(drs([A,B,C,D],[query(A,which)-1/1,object(A,robot,countable,na,eq,1)-1/2,property(D,red,pos)-1/7,object(D,block,countable,na,eq,1)-1/8,property(B,small,comp_than,D)-1/4,predicate(C,be,A,B)-1/3]))]",
            "[question(drs([A,B,C,D],[query(A,which)-1/1,object(A,robot,countable,na,eq,1)-1/2,property(D,red,pos)-1/8,object(D,block,countable,na,eq,1)-1/9,property(B,small,pos_as,D)-1/5,predicate(C,be,A,B)-1/3]))]",
            "[question(drs([A,B],[query(A,which)-1/1,object(A,robot,countable,na,eq,1)-1/2,predicate(B,be,A,named('John'))-1/3]))]",
            "[command(drs([A,B,C],[object(C,apple,countable,na,eq,1)-1/5,object(B,table,countable,na,eq,1)-1/8,predicate(A,move,named('Sawyer'),C)-1/3,modifier_adv(A,slowly,pos)-1/9,modifier_pp(A,on,B)-1/6]))]",
            "[command(drs([A,B,C],[property(C,red,pos)-1/5,object(C,apple,countable,na,eq,1)-1/6,object(B,table,countable,na,eq,1)-1/9,predicate(A,move,named('Sawyer'),C)-1/3,modifier_pp(A,on,B)-1/7]))]",
            "[command(drs([A,B,C],[property(C,red,pos)-1/5,object(C,apple,countable,na,eq,1)-1/6,object(B,table,countable,na,eq,1)-1/9,predicate(A,move,named('Sawyer'),C)-1/3,modifier_adv(A,slowly,pos)-1/10,modifier_pp(A,on,B)-1/7]))]",
            "[command(drs([A,B,C],[property(C,red,pos)-1/5,object(C,apple,countable,na,eq,1)-1/6,object(B,table,countable,na,eq,1)-1/9,predicate(A,pick,named('Sawyer'),C)-1/3,modifier_adv(A,slowly,pos)-1/10,modifier_pp(A,on,B)-1/7]))]",
            "[command(drs([A,B,C],[property(C,red,pos)-1/5,object(C,apple,countable,na,eq,1)-1/6,object(B,table,countable,na,eq,1)-1/9,predicate(A,grasp,named('Sawyer'),C)-1/3,modifier_adv(A,slowly,pos)-1/10,modifier_pp(A,on,B)-1/7]))]",
            "[=>(drs([A,B,C],[relation(B,of,C)-1/4,object(B,robot,countable,na,eq,1)-1/3,predicate(A,run,B)-1/7,object(C,company,countable,na,eq,1)-1/6]),drs([D],[predicate(D,run,B)-1/14,modifier_adv(D,slowly,pos)-1/15]))]",
            "[=>(drs([A,B,C,D],[relation(C,of,D)-1/4,object(C,robot,countable,na,eq,1)-1/3,object(A,apple,countable,na,eq,1)-1/9,predicate(B,throw,C,A)-1/7,object(D,company,countable,na,eq,1)-1/6]),drs([E,F],[object(E,apple,countable,na,eq,1)-1/18,predicate(F,throw,C,E)-1/16,modifier_adv(F,slowly,pos)-1/19]))]",
            "[=>(drs([A,B,C,D],[relation(C,of,D)-1/4,object(C,robot,countable,na,eq,1)-1/3,object(A,apple,countable,na,eq,1)-1/10,property(A,red,pos)-1/9,predicate(B,throw,C,A)-1/7,modifier_adv(B,slowly,pos)-1/11,object(D,company,countable,na,eq,1)-1/6]),drs([E,F,G],[object(E,apple,countable,na,eq,1)-1/21,property(E,red,pos)-1/20,predicate(F,throw,C,E)-1/18,modifier_pp(F,under,G)-1/23,modifier_adv(F,slowly,pos)-1/22,object(G,table,countable,na,eq,1)-1/25]))]",
            "[=>(drs([A,B,C],[relation(B,of,C)-1/4,object(B,robot,countable,na,eq,1)-1/3,predicate(A,run,B)-1/7,object(C,company,countable,na,eq,1)-1/6]),drs([D],[predicate(D,run,B)-1/14,modifier_adv(D,slowly,pos)-1/15]))]",
            "[=>(drs([A,B,C,D],[relation(C,of,D)-1/4,object(C,robot,countable,na,eq,1)-1/3,object(A,apple,countable,na,eq,1)-1/9,predicate(B,throw,C,A)-1/7,object(D,company,countable,na,eq,1)-1/6]),drs([E,F],[object(E,apple,countable,na,eq,1)-1/18,predicate(F,throw,C,E)-1/16,modifier_adv(F,slowly,pos)-1/19]))]",
            "[=>(drs([A,B,C,D],[relation(C,of,D)-1/4,object(C,robot,countable,na,eq,1)-1/3,object(A,apple,countable,na,eq,1)-1/10,property(A,red,pos)-1/9,predicate(B,throw,C,A)-1/7,modifier_adv(B,slowly,pos)-1/11,object(D,company,countable,na,eq,1)-1/6]),drs([E,F,G],[object(E,apple,countable,na,eq,1)-1/21,property(E,red,pos)-1/20,predicate(F,throw,C,E)-1/18,modifier_pp(F,under,G)-1/23,modifier_adv(F,slowly,pos)-1/22,object(G,table,countable,na,eq,1)-1/25]))]",
            "[=>(drs([A,B,C],[object(A,agent,countable,na,eq,1)-1/6,predicate(B,be,named('John'),A)-1/4,predicate(C,run,named('John'))-1/7]),drs([D,E,F],[object(D,agent,countable,na,eq,1)-1/13,predicate(E,be,named('John'),D)-1/11,predicate(F,run,named('John'))-1/14,modifier_adv(F,slowly,pos)-1/15]))]",
            "[=>(drs([A,B,C,D],[object(A,agent,countable,na,eq,1)-1/6,predicate(B,be,named('John'),A)-1/4,object(C,apple,countable,na,eq,1)-1/9,predicate(D,throw,named('John'),C)-1/7]),drs([E,F,G,H],[object(E,agent,countable,na,eq,1)-1/15,predicate(F,be,named('John'),E)-1/13,object(G,apple,countable,na,eq,1)-1/18,predicate(H,throw,named('John'),G)-1/16,modifier_adv(H,slowly,pos)-1/19]))]",
            "[=>(drs([A,B,C,D],[object(A,agent,countable,na,eq,1)-1/6,predicate(B,be,named('John'),A)-1/4,object(C,apple,countable,na,eq,1)-1/10,property(C,red,pos)-1/9,predicate(D,throw,named('John'),C)-1/7,modifier_adv(D,slowly,pos)-1/11]),drs([E,F,G,H,I],[object(E,agent,countable,na,eq,1)-1/17,predicate(F,be,named('John'),E)-1/15,object(G,apple,countable,na,eq,1)-1/21,property(G,red,pos)-1/20,object(I,table,countable,na,eq,1)-1/25,predicate(H,throw,named('John'),G)-1/18,modifier_pp(H,under,I)-1/23,modifier_adv(H,slowly,pos)-1/22]))]",
            "[v(drs([A,B],[object(A,robot,countable,na,eq,1)-1/3,property(A,small,pos)-1/2,predicate(B,run,A)-1/4]),drs([C,D],[object(C,robot,countable,na,eq,1)-1/8,property(C,small,pos)-1/7,predicate(D,run,C)-1/9,modifier_adv(D,slowly,pos)-1/10]))]",
            "[v(drs([A,B,C],[object(A,robot,countable,na,eq,1)-1/3,property(A,small,pos)-1/2,object(B,apple,countable,na,eq,1)-1/6,predicate(C,throw,A,B)-1/4]),drs([D,E,F],[object(D,robot,countable,na,eq,1)-1/10,property(D,small,pos)-1/9,object(E,apple,countable,na,eq,1)-1/13,predicate(F,throw,D,E)-1/11,modifier_adv(F,slowly,pos)-1/14]))]",
            "[v(drs([A,B,C],[object(A,robot,countable,na,eq,1)-1/3,property(A,small,pos)-1/2,object(B,apple,countable,na,eq,1)-1/7,property(B,red,pos)-1/6,predicate(C,throw,A,B)-1/4,modifier_adv(C,slowly,pos)-1/8]),drs([D,E,F,G],[object(D,robot,countable,na,eq,1)-1/12,property(D,small,pos)-1/11,object(E,apple,countable,na,eq,1)-1/16,property(E,red,pos)-1/15,object(G,table,countable,na,eq,1)-1/20,predicate(F,throw,D,E)-1/13,modifier_pp(F,under,G)-1/18,modifier_adv(F,slowly,pos)-1/17]))]",
            "[v(drs([A,B],[object(A,robot,countable,na,eq,1)-1/3,property(A,small,pos)-1/2,predicate(B,run,A)-1/4]),drs([C],[object(C,apple,countable,na,eq,1)-1/9]))]",
            "[v(drs([A,B,C],[object(A,robot,countable,na,eq,1)-1/3,property(A,small,pos)-1/2,object(B,apple,countable,na,eq,1)-1/6,predicate(C,throw,A,B)-1/4]),drs([D],[object(D,apple,countable,na,eq,1)-1/11]))]",
            "[v(drs([A,B,C],[object(A,robot,countable,na,eq,1)-1/3,property(A,small,pos)-1/2,object(B,apple,countable,na,eq,1)-1/7,property(B,red,pos)-1/6,predicate(C,throw,A,B)-1/4,modifier_adv(C,slowly,pos)-1/8]),drs([D],[object(D,apple,countable,na,eq,3)-1/13]))]",
        ]
        parser = Lark(grammar_test_str, start="test_conditions")
        for i, input_ in enumerate(inputs_):
            try:
                result = parser.parse(input_)
            except:
                error_msg = "Sentence {}-th is in valid: {}".format(i, input_)
                self.fail(error_msg)

    def test_domain(self):
        inputs_ = [
            "[A, B]",
            "[A, B]",
            "[A, B]",
            "[A, B]",
            "[A, B, C]",
            "[A, B, C]",
            "[A, B, C]",
            "[A, B, C]",
            "[A, B, C]",
            "[A, B, C]",
            "[A, B, C]",
            "[A, B, C, D, E, F]",
            "[A, B, C, D]",
            "[A, B, C, D]",
            "[A, B, C, D, E]",
            "[A, B, C]",
            "[A, B, C]",
            "[A, B, C]",
            "[A]",
            "[A]",
            "[]"
        ]
        parser = Lark(grammar_test_str, start="test_domain")
        for i, input_ in enumerate(inputs_):
            try:
                result = parser.parse(input_)
            except:
                error_msg = "Sentence {}-th is in valid: {}".format(i, input_)
                self.fail(error_msg)

    def test_drs_statement(self):
        inputs_ = [
            "drs([A,B],[object(A,robot,countable,na,eq,1)-1/2,predicate(B,run,A)-1/3])",
            "drs([A,B],[object(A,robot,countable,na,eq,1)-1/2,predicate(B,run,A)-1/3,modifier_adv(B,slowly,pos)-1/4])",
            "drs([A,B],[object(A,apple,countable,na,eq,1)-1/4,predicate(B,throw,named('John'),A)-1/2])",
            "drs([A,B],[object(A,apple,countable,na,eq,1)-1/4,predicate(B,throw,named('John'),A)-1/2,modifier_adv(B,slowly,pos)-1/5])",
            "drs([A,B,C],[object(A,robot,countable,na,eq,1)-1/3,property(A,small,pos)-1/2,object(B,apple,countable,na,eq,1)-1/6,predicate(C,throw,A,B)-1/4,modifier_adv(C,slowly,pos)-1/7])",
            "drs([A,B,C],[object(A,robot,countable,na,eq,1)-1/3,property(A,small,pos)-1/2,object(B,apple,countable,na,eq,1)-1/7,property(B,red,pos)-1/6,predicate(C,throw,A,B)-1/4,modifier_adv(C,slowly,pos)-1/8])",
            "drs([A,B,C],[object(A,robot,countable,na,eq,1)-1/5,property(A,small,pos)-1/2,property(A,green,pos)-1/4,object(B,apple,countable,na,eq,1)-1/8,predicate(C,throw,A,B)-1/6])",
            "drs([A,B,C],[relation(A,of,named('John'))-1/2,object(A,robot,countable,na,eq,1)-1/4,object(B,apple,countable,na,eq,1)-1/7,predicate(C,throw,A,B)-1/5])",
            "drs([A,B,C],[relation(A,of,named('John'))-1/2,object(A,robot,countable,na,eq,1)-1/4,object(B,apple,countable,na,eq,1)-1/7,predicate(C,throw,A,B)-1/5,modifier_adv(C,slowly,pos)-1/8])",
            "drs([A,B,C],[relation(B,of,C)-1/3,object(B,robot,countable,na,eq,1)-1/2,predicate(A,run,B)-1/6,object(C,company,countable,na,eq,1)-1/5])",
            "drs([A,B,C],[relation(B,of,C)-1/3,object(B,robot,countable,na,eq,1)-1/2,predicate(A,run,B)-1/6,modifier_adv(A,slowly,pos)-1/7,object(C,company,countable,na,eq,1)-1/5])",
            "drs([A,B,C,D,E,F],[predicate(F,be,D,E)-1/4,object(E,agent,countable,na,eq,1)-1/6,object(D,robot,countable,na,eq,1)-1/2,object(A,apple,countable,na,eq,1)-1/10,property(A,red,pos)-1/9,object(C,table,countable,na,eq,1)-1/14,predicate(B,throw,D,A)-1/7,modifier_pp(B,under,C)-1/12,modifier_adv(B,slowly,pos)-1/11])",
            "drs([A,B,C,D],[predicate(D,be,B,C)-1/4,object(C,agent,countable,na,eq,1)-1/6,object(B,robot,countable,na,eq,1)-1/2,predicate(A,move,B)-1/7,modifier_adv(A,slowly,pos)-1/8])",
            "drs([A,B,C,D],[object(A,agent,countable,na,eq,1)-1/5,predicate(B,be,named('John'),A)-1/3,object(C,apple,countable,na,eq,1)-1/9,property(C,red,pos)-1/8,predicate(D,throw,named('John'),C)-1/6,modifier_adv(D,slowly,pos)-1/10])",
            "drs([A,B,C,D,E],[object(A,agent,countable,na,eq,1)-1/5,predicate(B,be,named('John'),A)-1/3,object(C,apple,countable,na,eq,1)-1/9,property(C,red,pos)-1/8,object(E,table,countable,na,eq,1)-1/13,predicate(D,throw,named('John'),C)-1/6,modifier_pp(D,under,E)-1/11,modifier_adv(D,slowly,pos)-1/10])",
            "drs([A,B,C],[object(C,robot,countable,na,eq,1)-1/2,object(A,apple,countable,kg,eq,3)-1/7,predicate(B,throw,C,A)-1/3,modifier_adv(B,slowly,pos)-1/8])",
            "drs([A,B,C],[object(C,robot,countable,na,eq,1)-1/2,object(A,apple,countable,kg,eq,3)-1/8,property(A,red,pos)-1/7,predicate(B,throw,C,A)-1/3,modifier_adv(B,slowly,pos)-1/9])",
            "drs([A,B,C],[object(C,robot,countable,na,eq,1)-1/2,object(A,metal,countable,pound,eq,3)-1/7,predicate(B,be,C,A)-1/3])",
            "drs([A],[object(A,robot,countable,na,eq,1)-1/2,can(drs([B,C],[object(B,apple,countable,na,eq,1)-1/7,property(B,red,pos)-1/6,predicate(C,throw,A,B)-1/4,modifier_adv(C,slowly,pos)-1/8]))])",
            "drs([A],[object(A,robot,countable,na,eq,1)-1/2,can(drs([B,C,D],[object(B,apple,countable,na,eq,1)-1/7,property(B,red,pos)-1/6,object(D,table,countable,na,eq,1)-1/11,predicate(C,throw,A,B)-1/4,modifier_pp(C,under,D)-1/9,modifier_adv(C,slowly,pos)-1/8]))])",
            "drs([],[-(drs([A],[object(A,apple,countable,na,eq,1)-1/4]))])",
            "drs([],[question(drs([A,B,C,D],[object(D,apple,countable,na,eq,1)-1/3,property(C,red,pos)-1/7,object(C,box,countable,na,eq,1)-1/8,property(A,small,comp_than,C)-1/4,predicate(B,be,D,A)-1/1]))])",
            "drs([],[question(drs([A,B,C,D],[object(D,apple,countable,na,eq,1)-1/3,property(C,red,pos)-1/8,object(C,box,countable,na,eq,1)-1/9,property(A,small,comp_than,C)-1/5,predicate(B,be,D,A)-1/1]))])",
            "drs([],[question(drs([A,B,C],[object(C,apple,countable,na,eq,1)-1/3,object(A,agent,countable,na,eq,1)-1/5,predicate(B,be,C,A)-1/1]))])",
            "drs([],[question(drs([A,B],[object(A,agent,countable,na,eq,1)-1/4,predicate(B,be,named('John'),A)-1/1]))])",
            "drs([],[question(drs([A,B],[query(A,who)-1/1,predicate(B,move,A)-1/3,modifier_adv(B,slowly,pos)-1/4]))])",
            "drs([],[question(drs([A,B],[query(A,who)-1/1,modifier_adv(B,slowly,pos)-1/3,predicate(B,move,A)-1/4]))])",
            "drs([],[question(drs([A,B,C,D],[query(A,who)-1/1,property(D,red,pos)-1/7,object(D,block,countable,na,eq,1)-1/8,property(B,small,pos_as,D)-1/4,predicate(C,be,A,B)-1/2]))])",
            "drs([],[question(drs([A,B,C,D],[query(A,who)-1/1,property(D,red,pos)-1/6,object(D,block,countable,na,eq,1)-1/7,property(B,small,comp_than,D)-1/3,predicate(C,be,A,B)-1/2]))])",
            "drs([],[question(drs([A,B,C],[query(A,who)-1/1,property(C,small,sup)-1/4,object(C,agent,countable,na,eq,1)-1/5,predicate(B,be,A,C)-1/2]))])",
            "drs([],[question(drs([A,B],[query(A,who)-1/1,predicate(B,be,A,named('John'))-1/2]))])",
            "drs([],[question(drs([A,B,C,D],[query(A,which)-1/1,object(A,robot,countable,na,eq,1)-1/2,property(D,red,pos)-1/7,object(D,block,countable,na,eq,1)-1/8,property(B,small,comp_than,D)-1/4,predicate(C,be,A,B)-1/3]))])",
            "drs([],[question(drs([A,B,C,D],[query(A,which)-1/1,object(A,robot,countable,na,eq,1)-1/2,property(D,red,pos)-1/8,object(D,block,countable,na,eq,1)-1/9,property(B,small,pos_as,D)-1/5,predicate(C,be,A,B)-1/3]))])",
            "drs([],[question(drs([A,B],[query(A,which)-1/1,object(A,robot,countable,na,eq,1)-1/2,predicate(B,be,A,named('John'))-1/3]))])",
            "drs([],[command(drs([A,B,C],[object(C,apple,countable,na,eq,1)-1/5,object(B,table,countable,na,eq,1)-1/8,predicate(A,move,named('Sawyer'),C)-1/3,modifier_adv(A,slowly,pos)-1/9,modifier_pp(A,on,B)-1/6]))])",
            "drs([],[command(drs([A,B,C],[property(C,red,pos)-1/5,object(C,apple,countable,na,eq,1)-1/6,object(B,table,countable,na,eq,1)-1/9,predicate(A,move,named('Sawyer'),C)-1/3,modifier_pp(A,on,B)-1/7]))])",
            "drs([],[command(drs([A,B,C],[property(C,red,pos)-1/5,object(C,apple,countable,na,eq,1)-1/6,object(B,table,countable,na,eq,1)-1/9,predicate(A,move,named('Sawyer'),C)-1/3,modifier_adv(A,slowly,pos)-1/10,modifier_pp(A,on,B)-1/7]))])",
            "drs([],[command(drs([A,B,C],[property(C,red,pos)-1/5,object(C,apple,countable,na,eq,1)-1/6,object(B,table,countable,na,eq,1)-1/9,predicate(A,pick,named('Sawyer'),C)-1/3,modifier_adv(A,slowly,pos)-1/10,modifier_pp(A,on,B)-1/7]))])",
            "drs([],[command(drs([A,B,C],[property(C,red,pos)-1/5,object(C,apple,countable,na,eq,1)-1/6,object(B,table,countable,na,eq,1)-1/9,predicate(A,grasp,named('Sawyer'),C)-1/3,modifier_adv(A,slowly,pos)-1/10,modifier_pp(A,on,B)-1/7]))])",
            "drs([],[=>(drs([A,B,C],[relation(B,of,C)-1/4,object(B,robot,countable,na,eq,1)-1/3,predicate(A,run,B)-1/7,object(C,company,countable,na,eq,1)-1/6]),drs([D],[predicate(D,run,B)-1/14,modifier_adv(D,slowly,pos)-1/15]))])",
            "drs([],[=>(drs([A,B,C,D],[relation(C,of,D)-1/4,object(C,robot,countable,na,eq,1)-1/3,object(A,apple,countable,na,eq,1)-1/9,predicate(B,throw,C,A)-1/7,object(D,company,countable,na,eq,1)-1/6]),drs([E,F],[object(E,apple,countable,na,eq,1)-1/18,predicate(F,throw,C,E)-1/16,modifier_adv(F,slowly,pos)-1/19]))])",
            "drs([],[=>(drs([A,B,C,D],[relation(C,of,D)-1/4,object(C,robot,countable,na,eq,1)-1/3,object(A,apple,countable,na,eq,1)-1/10,property(A,red,pos)-1/9,predicate(B,throw,C,A)-1/7,modifier_adv(B,slowly,pos)-1/11,object(D,company,countable,na,eq,1)-1/6]),drs([E,F,G],[object(E,apple,countable,na,eq,1)-1/21,property(E,red,pos)-1/20,predicate(F,throw,C,E)-1/18,modifier_pp(F,under,G)-1/23,modifier_adv(F,slowly,pos)-1/22,object(G,table,countable,na,eq,1)-1/25]))])",
            "drs([],[=>(drs([A,B,C],[relation(B,of,C)-1/4,object(B,robot,countable,na,eq,1)-1/3,predicate(A,run,B)-1/7,object(C,company,countable,na,eq,1)-1/6]),drs([D],[predicate(D,run,B)-1/14,modifier_adv(D,slowly,pos)-1/15]))])",
            "drs([],[=>(drs([A,B,C,D],[relation(C,of,D)-1/4,object(C,robot,countable,na,eq,1)-1/3,object(A,apple,countable,na,eq,1)-1/9,predicate(B,throw,C,A)-1/7,object(D,company,countable,na,eq,1)-1/6]),drs([E,F],[object(E,apple,countable,na,eq,1)-1/18,predicate(F,throw,C,E)-1/16,modifier_adv(F,slowly,pos)-1/19]))])",
            "drs([],[=>(drs([A,B,C,D],[relation(C,of,D)-1/4,object(C,robot,countable,na,eq,1)-1/3,object(A,apple,countable,na,eq,1)-1/10,property(A,red,pos)-1/9,predicate(B,throw,C,A)-1/7,modifier_adv(B,slowly,pos)-1/11,object(D,company,countable,na,eq,1)-1/6]),drs([E,F,G],[object(E,apple,countable,na,eq,1)-1/21,property(E,red,pos)-1/20,predicate(F,throw,C,E)-1/18,modifier_pp(F,under,G)-1/23,modifier_adv(F,slowly,pos)-1/22,object(G,table,countable,na,eq,1)-1/25]))])",
            "drs([],[=>(drs([A,B,C],[object(A,agent,countable,na,eq,1)-1/6,predicate(B,be,named('John'),A)-1/4,predicate(C,run,named('John'))-1/7]),drs([D,E,F],[object(D,agent,countable,na,eq,1)-1/13,predicate(E,be,named('John'),D)-1/11,predicate(F,run,named('John'))-1/14,modifier_adv(F,slowly,pos)-1/15]))])",
            "drs([],[=>(drs([A,B,C,D],[object(A,agent,countable,na,eq,1)-1/6,predicate(B,be,named('John'),A)-1/4,object(C,apple,countable,na,eq,1)-1/9,predicate(D,throw,named('John'),C)-1/7]),drs([E,F,G,H],[object(E,agent,countable,na,eq,1)-1/15,predicate(F,be,named('John'),E)-1/13,object(G,apple,countable,na,eq,1)-1/18,predicate(H,throw,named('John'),G)-1/16,modifier_adv(H,slowly,pos)-1/19]))])",
            "drs([],[=>(drs([A,B,C,D],[object(A,agent,countable,na,eq,1)-1/6,predicate(B,be,named('John'),A)-1/4,object(C,apple,countable,na,eq,1)-1/10,property(C,red,pos)-1/9,predicate(D,throw,named('John'),C)-1/7,modifier_adv(D,slowly,pos)-1/11]),drs([E,F,G,H,I],[object(E,agent,countable,na,eq,1)-1/17,predicate(F,be,named('John'),E)-1/15,object(G,apple,countable,na,eq,1)-1/21,property(G,red,pos)-1/20,object(I,table,countable,na,eq,1)-1/25,predicate(H,throw,named('John'),G)-1/18,modifier_pp(H,under,I)-1/23,modifier_adv(H,slowly,pos)-1/22]))])",
            "drs([],[v(drs([A,B],[object(A,robot,countable,na,eq,1)-1/3,property(A,small,pos)-1/2,predicate(B,run,A)-1/4]),drs([C,D],[object(C,robot,countable,na,eq,1)-1/8,property(C,small,pos)-1/7,predicate(D,run,C)-1/9,modifier_adv(D,slowly,pos)-1/10]))])",
            "drs([],[v(drs([A,B,C],[object(A,robot,countable,na,eq,1)-1/3,property(A,small,pos)-1/2,object(B,apple,countable,na,eq,1)-1/6,predicate(C,throw,A,B)-1/4]),drs([D,E,F],[object(D,robot,countable,na,eq,1)-1/10,property(D,small,pos)-1/9,object(E,apple,countable,na,eq,1)-1/13,predicate(F,throw,D,E)-1/11,modifier_adv(F,slowly,pos)-1/14]))])",
            "drs([],[v(drs([A,B,C],[object(A,robot,countable,na,eq,1)-1/3,property(A,small,pos)-1/2,object(B,apple,countable,na,eq,1)-1/7,property(B,red,pos)-1/6,predicate(C,throw,A,B)-1/4,modifier_adv(C,slowly,pos)-1/8]),drs([D,E,F,G],[object(D,robot,countable,na,eq,1)-1/12,property(D,small,pos)-1/11,object(E,apple,countable,na,eq,1)-1/16,property(E,red,pos)-1/15,object(G,table,countable,na,eq,1)-1/20,predicate(F,throw,D,E)-1/13,modifier_pp(F,under,G)-1/18,modifier_adv(F,slowly,pos)-1/17]))])",
            "drs([],[v(drs([A,B],[object(A,robot,countable,na,eq,1)-1/3,property(A,small,pos)-1/2,predicate(B,run,A)-1/4]),drs([C],[object(C,apple,countable,na,eq,1)-1/9]))])",
            "drs([],[v(drs([A,B,C],[object(A,robot,countable,na,eq,1)-1/3,property(A,small,pos)-1/2,object(B,apple,countable,na,eq,1)-1/6,predicate(C,throw,A,B)-1/4]),drs([D],[object(D,apple,countable,na,eq,1)-1/11]))])",
            "drs([],[v(drs([A,B,C],[object(A,robot,countable,na,eq,1)-1/3,property(A,small,pos)-1/2,object(B,apple,countable,na,eq,1)-1/7,property(B,red,pos)-1/6,predicate(C,throw,A,B)-1/4,modifier_adv(C,slowly,pos)-1/8]),drs([D],[object(D,apple,countable,na,eq,3)-1/13]))])",
        ]
        parser = Lark(grammar_test_str, start="test_drs_statement")
        for i, input_ in enumerate(inputs_):
            try:
                result = parser.parse(input_)
            except:
                error_msg = "Sentence {}-th is in valid: {}".format(i, input_)
                self.fail(error_msg)


class Test_Rule_Root(unittest.TestCase):
    def test_drs_root(self):
        inputs_ = [

            "drs([A,B],[object(A,robot,countable,na,eq,1)-1/2,predicate(B,run,A)-1/3])",
            "drs([A,B],[object(A,robot,countable,na,eq,1)-1/2,predicate(B,run,A)-1/3,modifier_adv(B,slowly,pos)-1/4])",
            "drs([A,B],[object(A,apple,countable,na,eq,1)-1/4,predicate(B,throw,named('John'),A)-1/2])",
            "drs([A,B],[object(A,apple,countable,na,eq,1)-1/4,predicate(B,throw,named('John'),A)-1/2,modifier_adv(B,slowly,pos)-1/5])",
            "drs([A,B,C],[object(A,robot,countable,na,eq,1)-1/3,property(A,small,pos)-1/2,object(B,apple,countable,na,eq,1)-1/6,predicate(C,throw,A,B)-1/4,modifier_adv(C,slowly,pos)-1/7])",
            "drs([A,B,C],[object(A,robot,countable,na,eq,1)-1/3,property(A,small,pos)-1/2,object(B,apple,countable,na,eq,1)-1/7,property(B,red,pos)-1/6,predicate(C,throw,A,B)-1/4,modifier_adv(C,slowly,pos)-1/8])",
            "drs([A,B,C],[object(A,robot,countable,na,eq,1)-1/5,property(A,small,pos)-1/2,property(A,green,pos)-1/4,object(B,apple,countable,na,eq,1)-1/8,predicate(C,throw,A,B)-1/6])",
            "drs([A,B,C],[relation(A,of,named('John'))-1/2,object(A,robot,countable,na,eq,1)-1/4,object(B,apple,countable,na,eq,1)-1/7,predicate(C,throw,A,B)-1/5])",
            "drs([A,B,C],[relation(A,of,named('John'))-1/2,object(A,robot,countable,na,eq,1)-1/4,object(B,apple,countable,na,eq,1)-1/7,predicate(C,throw,A,B)-1/5,modifier_adv(C,slowly,pos)-1/8])",
            "drs([A,B,C],[relation(B,of,C)-1/3,object(B,robot,countable,na,eq,1)-1/2,predicate(A,run,B)-1/6,object(C,company,countable,na,eq,1)-1/5])",
            "drs([A,B,C],[relation(B,of,C)-1/3,object(B,robot,countable,na,eq,1)-1/2,predicate(A,run,B)-1/6,modifier_adv(A,slowly,pos)-1/7,object(C,company,countable,na,eq,1)-1/5])",
            "drs([A,B,C,D,E,F],[predicate(F,be,D,E)-1/4,object(E,agent,countable,na,eq,1)-1/6,object(D,robot,countable,na,eq,1)-1/2,object(A,apple,countable,na,eq,1)-1/10,property(A,red,pos)-1/9,object(C,table,countable,na,eq,1)-1/14,predicate(B,throw,D,A)-1/7,modifier_pp(B,under,C)-1/12,modifier_adv(B,slowly,pos)-1/11])",
            "drs([A,B,C,D],[predicate(D,be,B,C)-1/4,object(C,agent,countable,na,eq,1)-1/6,object(B,robot,countable,na,eq,1)-1/2,predicate(A,move,B)-1/7,modifier_adv(A,slowly,pos)-1/8])",
            "drs([A,B,C,D],[object(A,agent,countable,na,eq,1)-1/5,predicate(B,be,named('John'),A)-1/3,object(C,apple,countable,na,eq,1)-1/9,property(C,red,pos)-1/8,predicate(D,throw,named('John'),C)-1/6,modifier_adv(D,slowly,pos)-1/10])",
            "drs([A,B,C,D,E],[object(A,agent,countable,na,eq,1)-1/5,predicate(B,be,named('John'),A)-1/3,object(C,apple,countable,na,eq,1)-1/9,property(C,red,pos)-1/8,object(E,table,countable,na,eq,1)-1/13,predicate(D,throw,named('John'),C)-1/6,modifier_pp(D,under,E)-1/11,modifier_adv(D,slowly,pos)-1/10])",
            "drs([A,B,C],[object(C,robot,countable,na,eq,1)-1/2,object(A,apple,countable,kg,eq,3)-1/7,predicate(B,throw,C,A)-1/3,modifier_adv(B,slowly,pos)-1/8])",
            "drs([A,B,C],[object(C,robot,countable,na,eq,1)-1/2,object(A,apple,countable,kg,eq,3)-1/8,property(A,red,pos)-1/7,predicate(B,throw,C,A)-1/3,modifier_adv(B,slowly,pos)-1/9])",
            "drs([A,B,C],[object(C,robot,countable,na,eq,1)-1/2,object(A,metal,countable,pound,eq,3)-1/7,predicate(B,be,C,A)-1/3])",
            "drs([A],[object(A,robot,countable,na,eq,1)-1/2,can(drs([B,C],[object(B,apple,countable,na,eq,1)-1/7,property(B,red,pos)-1/6,predicate(C,throw,A,B)-1/4,modifier_adv(C,slowly,pos)-1/8]))])",
            "drs([A],[object(A,robot,countable,na,eq,1)-1/2,can(drs([B,C,D],[object(B,apple,countable,na,eq,1)-1/7,property(B,red,pos)-1/6,object(D,table,countable,na,eq,1)-1/11,predicate(C,throw,A,B)-1/4,modifier_pp(C,under,D)-1/9,modifier_adv(C,slowly,pos)-1/8]))])",
            "drs([],[-(drs([A],[object(A,apple,countable,na,eq,1)-1/4]))])",
            "drs([],[question(drs([A,B,C,D],[object(D,apple,countable,na,eq,1)-1/3,property(C,red,pos)-1/7,object(C,box,countable,na,eq,1)-1/8,property(A,small,comp_than,C)-1/4,predicate(B,be,D,A)-1/1]))])",
            "drs([],[question(drs([A,B,C,D],[object(D,apple,countable,na,eq,1)-1/3,property(C,red,pos)-1/8,object(C,box,countable,na,eq,1)-1/9,property(A,small,comp_than,C)-1/5,predicate(B,be,D,A)-1/1]))])",
            "drs([],[question(drs([A,B,C],[object(C,apple,countable,na,eq,1)-1/3,object(A,agent,countable,na,eq,1)-1/5,predicate(B,be,C,A)-1/1]))])",
            "drs([],[question(drs([A,B],[object(A,agent,countable,na,eq,1)-1/4,predicate(B,be,named('John'),A)-1/1]))])",
            "drs([],[question(drs([A,B],[query(A,who)-1/1,predicate(B,move,A)-1/3,modifier_adv(B,slowly,pos)-1/4]))])",
            "drs([],[question(drs([A,B],[query(A,who)-1/1,modifier_adv(B,slowly,pos)-1/3,predicate(B,move,A)-1/4]))])",
            "drs([],[question(drs([A,B,C,D],[query(A,who)-1/1,property(D,red,pos)-1/7,object(D,block,countable,na,eq,1)-1/8,property(B,small,pos_as,D)-1/4,predicate(C,be,A,B)-1/2]))])",
            "drs([],[question(drs([A,B,C,D],[query(A,who)-1/1,property(D,red,pos)-1/6,object(D,block,countable,na,eq,1)-1/7,property(B,small,comp_than,D)-1/3,predicate(C,be,A,B)-1/2]))])",
            "drs([],[question(drs([A,B,C],[query(A,who)-1/1,property(C,small,sup)-1/4,object(C,agent,countable,na,eq,1)-1/5,predicate(B,be,A,C)-1/2]))])",
            "drs([],[question(drs([A,B],[query(A,who)-1/1,predicate(B,be,A,named('John'))-1/2]))])",
            "drs([],[question(drs([A,B,C,D],[query(A,which)-1/1,object(A,robot,countable,na,eq,1)-1/2,property(D,red,pos)-1/7,object(D,block,countable,na,eq,1)-1/8,property(B,small,comp_than,D)-1/4,predicate(C,be,A,B)-1/3]))])",
            "drs([],[question(drs([A,B,C,D],[query(A,which)-1/1,object(A,robot,countable,na,eq,1)-1/2,property(D,red,pos)-1/8,object(D,block,countable,na,eq,1)-1/9,property(B,small,pos_as,D)-1/5,predicate(C,be,A,B)-1/3]))])",
            "drs([],[question(drs([A,B],[query(A,which)-1/1,object(A,robot,countable,na,eq,1)-1/2,predicate(B,be,A,named('John'))-1/3]))])",
            "drs([],[command(drs([A,B,C],[object(C,apple,countable,na,eq,1)-1/5,object(B,table,countable,na,eq,1)-1/8,predicate(A,move,named('Sawyer'),C)-1/3,modifier_adv(A,slowly,pos)-1/9,modifier_pp(A,on,B)-1/6]))])",
            "drs([],[command(drs([A,B,C],[property(C,red,pos)-1/5,object(C,apple,countable,na,eq,1)-1/6,object(B,table,countable,na,eq,1)-1/9,predicate(A,move,named('Sawyer'),C)-1/3,modifier_pp(A,on,B)-1/7]))])",
            "drs([],[command(drs([A,B,C],[property(C,red,pos)-1/5,object(C,apple,countable,na,eq,1)-1/6,object(B,table,countable,na,eq,1)-1/9,predicate(A,move,named('Sawyer'),C)-1/3,modifier_adv(A,slowly,pos)-1/10,modifier_pp(A,on,B)-1/7]))])",
            "drs([],[command(drs([A,B,C],[property(C,red,pos)-1/5,object(C,apple,countable,na,eq,1)-1/6,object(B,table,countable,na,eq,1)-1/9,predicate(A,pick,named('Sawyer'),C)-1/3,modifier_adv(A,slowly,pos)-1/10,modifier_pp(A,on,B)-1/7]))])",
            "drs([],[command(drs([A,B,C],[property(C,red,pos)-1/5,object(C,apple,countable,na,eq,1)-1/6,object(B,table,countable,na,eq,1)-1/9,predicate(A,grasp,named('Sawyer'),C)-1/3,modifier_adv(A,slowly,pos)-1/10,modifier_pp(A,on,B)-1/7]))])",
            "drs([],[=>(drs([A,B,C],[relation(B,of,C)-1/4,object(B,robot,countable,na,eq,1)-1/3,predicate(A,run,B)-1/7,object(C,company,countable,na,eq,1)-1/6]),drs([D],[predicate(D,run,B)-1/14,modifier_adv(D,slowly,pos)-1/15]))])",
            "drs([],[=>(drs([A,B,C,D],[relation(C,of,D)-1/4,object(C,robot,countable,na,eq,1)-1/3,object(A,apple,countable,na,eq,1)-1/9,predicate(B,throw,C,A)-1/7,object(D,company,countable,na,eq,1)-1/6]),drs([E,F],[object(E,apple,countable,na,eq,1)-1/18,predicate(F,throw,C,E)-1/16,modifier_adv(F,slowly,pos)-1/19]))])",
            "drs([],[=>(drs([A,B,C,D],[relation(C,of,D)-1/4,object(C,robot,countable,na,eq,1)-1/3,object(A,apple,countable,na,eq,1)-1/10,property(A,red,pos)-1/9,predicate(B,throw,C,A)-1/7,modifier_adv(B,slowly,pos)-1/11,object(D,company,countable,na,eq,1)-1/6]),drs([E,F,G],[object(E,apple,countable,na,eq,1)-1/21,property(E,red,pos)-1/20,predicate(F,throw,C,E)-1/18,modifier_pp(F,under,G)-1/23,modifier_adv(F,slowly,pos)-1/22,object(G,table,countable,na,eq,1)-1/25]))])",
            "drs([],[=>(drs([A,B,C],[relation(B,of,C)-1/4,object(B,robot,countable,na,eq,1)-1/3,predicate(A,run,B)-1/7,object(C,company,countable,na,eq,1)-1/6]),drs([D],[predicate(D,run,B)-1/14,modifier_adv(D,slowly,pos)-1/15]))])",
            "drs([],[=>(drs([A,B,C,D],[relation(C,of,D)-1/4,object(C,robot,countable,na,eq,1)-1/3,object(A,apple,countable,na,eq,1)-1/9,predicate(B,throw,C,A)-1/7,object(D,company,countable,na,eq,1)-1/6]),drs([E,F],[object(E,apple,countable,na,eq,1)-1/18,predicate(F,throw,C,E)-1/16,modifier_adv(F,slowly,pos)-1/19]))])",
            "drs([],[=>(drs([A,B,C,D],[relation(C,of,D)-1/4,object(C,robot,countable,na,eq,1)-1/3,object(A,apple,countable,na,eq,1)-1/10,property(A,red,pos)-1/9,predicate(B,throw,C,A)-1/7,modifier_adv(B,slowly,pos)-1/11,object(D,company,countable,na,eq,1)-1/6]),drs([E,F,G],[object(E,apple,countable,na,eq,1)-1/21,property(E,red,pos)-1/20,predicate(F,throw,C,E)-1/18,modifier_pp(F,under,G)-1/23,modifier_adv(F,slowly,pos)-1/22,object(G,table,countable,na,eq,1)-1/25]))])",
            "drs([],[=>(drs([A,B,C],[object(A,agent,countable,na,eq,1)-1/6,predicate(B,be,named('John'),A)-1/4,predicate(C,run,named('John'))-1/7]),drs([D,E,F],[object(D,agent,countable,na,eq,1)-1/13,predicate(E,be,named('John'),D)-1/11,predicate(F,run,named('John'))-1/14,modifier_adv(F,slowly,pos)-1/15]))])",
            "drs([],[=>(drs([A,B,C,D],[object(A,agent,countable,na,eq,1)-1/6,predicate(B,be,named('John'),A)-1/4,object(C,apple,countable,na,eq,1)-1/9,predicate(D,throw,named('John'),C)-1/7]),drs([E,F,G,H],[object(E,agent,countable,na,eq,1)-1/15,predicate(F,be,named('John'),E)-1/13,object(G,apple,countable,na,eq,1)-1/18,predicate(H,throw,named('John'),G)-1/16,modifier_adv(H,slowly,pos)-1/19]))])",
            "drs([],[=>(drs([A,B,C,D],[object(A,agent,countable,na,eq,1)-1/6,predicate(B,be,named('John'),A)-1/4,object(C,apple,countable,na,eq,1)-1/10,property(C,red,pos)-1/9,predicate(D,throw,named('John'),C)-1/7,modifier_adv(D,slowly,pos)-1/11]),drs([E,F,G,H,I],[object(E,agent,countable,na,eq,1)-1/17,predicate(F,be,named('John'),E)-1/15,object(G,apple,countable,na,eq,1)-1/21,property(G,red,pos)-1/20,object(I,table,countable,na,eq,1)-1/25,predicate(H,throw,named('John'),G)-1/18,modifier_pp(H,under,I)-1/23,modifier_adv(H,slowly,pos)-1/22]))])",
            "drs([],[v(drs([A,B],[object(A,robot,countable,na,eq,1)-1/3,property(A,small,pos)-1/2,predicate(B,run,A)-1/4]),drs([C,D],[object(C,robot,countable,na,eq,1)-1/8,property(C,small,pos)-1/7,predicate(D,run,C)-1/9,modifier_adv(D,slowly,pos)-1/10]))])",
            "drs([],[v(drs([A,B,C],[object(A,robot,countable,na,eq,1)-1/3,property(A,small,pos)-1/2,object(B,apple,countable,na,eq,1)-1/6,predicate(C,throw,A,B)-1/4]),drs([D,E,F],[object(D,robot,countable,na,eq,1)-1/10,property(D,small,pos)-1/9,object(E,apple,countable,na,eq,1)-1/13,predicate(F,throw,D,E)-1/11,modifier_adv(F,slowly,pos)-1/14]))])",
            "drs([],[v(drs([A,B,C],[object(A,robot,countable,na,eq,1)-1/3,property(A,small,pos)-1/2,object(B,apple,countable,na,eq,1)-1/7,property(B,red,pos)-1/6,predicate(C,throw,A,B)-1/4,modifier_adv(C,slowly,pos)-1/8]),drs([D,E,F,G],[object(D,robot,countable,na,eq,1)-1/12,property(D,small,pos)-1/11,object(E,apple,countable,na,eq,1)-1/16,property(E,red,pos)-1/15,object(G,table,countable,na,eq,1)-1/20,predicate(F,throw,D,E)-1/13,modifier_pp(F,under,G)-1/18,modifier_adv(F,slowly,pos)-1/17]))])",
            "drs([],[v(drs([A,B],[object(A,robot,countable,na,eq,1)-1/3,property(A,small,pos)-1/2,predicate(B,run,A)-1/4]),drs([C],[object(C,apple,countable,na,eq,1)-1/9]))])",
            "drs([],[v(drs([A,B,C],[object(A,robot,countable,na,eq,1)-1/3,property(A,small,pos)-1/2,object(B,apple,countable,na,eq,1)-1/6,predicate(C,throw,A,B)-1/4]),drs([D],[object(D,apple,countable,na,eq,1)-1/11]))])",
            "drs([],[v(drs([A,B,C],[object(A,robot,countable,na,eq,1)-1/3,property(A,small,pos)-1/2,object(B,apple,countable,na,eq,1)-1/7,property(B,red,pos)-1/6,predicate(C,throw,A,B)-1/4,modifier_adv(C,slowly,pos)-1/8]),drs([D],[object(D,apple,countable,na,eq,3)-1/13]))])",
        ]
        parser = Lark(grammar_test_str, start="test_drs_root")
        for i, input_ in enumerate(inputs_):
            try:
                result = parser.parse(input_)
            except:
                error_msg = "Sentence {}-th is in valid: {}".format(i, input_)
                self.fail(error_msg)


if __name__ == '__main__':
    unittest.main()
