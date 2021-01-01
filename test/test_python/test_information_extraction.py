import sys
from pathlib import Path
workspace_directory = Path(Path(__file__).parent.parent.parent)
sys.path.insert(0, str(workspace_directory))


import unittest
from scripts.drs.drs import (
    grammar_visualization_str,
    translate,
    visualizable_str,
    visualize,
    get_leaves,
    get_references,
    get_entities,
    get_valid_lexical,
    get_cname,
    get_conditions,
    get_objects,
    get_predicates,
    get_properties,
    get_modifier_adverbs,
    get_prepositions,
    get_queries,
    get_action_modifiers,
    get_noun_modifiers,
    get_relations,
    get_command_conditions,
    get_question_conditions,
    get_possibility_conditions,
    is_command_type,
    is_question_type,
    is_possibility_type,
    is_descriptive_type,
    get_main_predicate,
    get_subject_from_predicate,
    get_first_object_from_predicate,
    get_second_object_from_predicate,
    get_lexical_from_predicate,
    get_object_conditions_having_variable_x,
    get_object_conditions_information_having_variable_x,
    get_action_adverbs_having_variable_x,
    get_action_adverbs_information_having_variable_x,
    who_do_what,
    who_do_what_how
)
from lark import Lark


class Test_functional_methods(unittest.TestCase):
    def test_translate(self):
        inputs_ = [
            (
                "drs([],[=>(drs([A,B,C,D],[object(A,agent,countable,na,eq,1)-1/6,predicate(B,be,named('John'),A)-1/4,object(C,apple,countable,na,eq,1)-1/10,property(C,red,pos)-1/9,predicate(D,throw,named('John'),C)-1/7,modifier_adv(D,slowly,pos)-1/11]),drs([E,F,G,H,I],[object(E,agent,countable,na,eq,1)-1/17,predicate(F,be,named('John'),E)-1/15,object(G,apple,countable,na,eq,1)-1/21,property(G,red,pos)-1/20,object(I,table,countable,na,eq,1)-1/25,predicate(H,throw,named('John'),G)-1/18,modifier_pp(H,under,I)-1/23,modifier_adv(H,slowly,pos)-1/22]))])",
                "drs([],[(drs([A,B,C,D],[object(A,agent,countable,na,eq,1),predicate(B,be,named('John'),A),object(C,apple,countable,na,eq,1),property(C,red,pos),predicate(D,throw,named('John'),C),modifier_adv(D,slowly,pos)])->drs([E,F,G,H,I],[object(E,agent,countable,na,eq,1),predicate(F,be,named('John'),E),object(G,apple,countable,na,eq,1),property(G,red,pos),object(I,table,countable,na,eq,1),predicate(H,throw,named('John'),G),modifier_pp(H,under,I),modifier_adv(H,slowly,pos)]))])"
            ),
            (
                "drs([],[=>(drs([A,B,C],[relation(B,of,C)-1/4,object(B,robot,countable,na,eq,1)-1/3,predicate(A,run,B)-1/7,object(C,company,countable,na,eq,1)-1/6]),drs([D],[predicate(D,run,B)-1/14,modifier_adv(D,slowly,pos)-1/15]))])",
                "drs([],[(drs([A,B,C],[relation(B,of,C),object(B,robot,countable,na,eq,1),predicate(A,run,B),object(C,company,countable,na,eq,1)])->drs([D],[predicate(D,run,B),modifier_adv(D,slowly,pos)]))])"
            ),
            (
                "drs([],[v(drs([A,B],[object(A,robot,countable,na,eq,1)-1/3,property(A,small,pos)-1/2,predicate(B,run,A)-1/4]),drs([C,D],[object(C,robot,countable,na,eq,1)-1/8,property(C,small,pos)-1/7,predicate(D,run,C)-1/9,modifier_adv(D,slowly,pos)-1/10]))])",
                "drs([],[(drs([A,B],[object(A,robot,countable,na,eq,1),property(A,small,pos),predicate(B,run,A)])|drs([C,D],[object(C,robot,countable,na,eq,1),property(C,small,pos),predicate(D,run,C),modifier_adv(D,slowly,pos)]))])"
            ),
            (
                "drs([],[v(drs([A,B,C],[object(A,robot,countable,na,eq,1)-1/3,property(A,small,pos)-1/2,object(B,apple,countable,na,eq,1)-1/6,predicate(C,throw,A,B)-1/4]),drs([D,E,F],[object(D,robot,countable,na,eq,1)-1/10,property(D,small,pos)-1/9,object(E,apple,countable,na,eq,1)-1/13,predicate(F,throw,D,E)-1/11,modifier_adv(F,slowly,pos)-1/14]))])",
                "drs([],[(drs([A,B,C],[object(A,robot,countable,na,eq,1),property(A,small,pos),object(B,apple,countable,na,eq,1),predicate(C,throw,A,B)])|drs([D,E,F],[object(D,robot,countable,na,eq,1),property(D,small,pos),object(E,apple,countable,na,eq,1),predicate(F,throw,D,E),modifier_adv(F,slowly,pos)]))])"
            ),

        ]
        parser = Lark(grammar_visualization_str,
                      start="drs_root")
        for i, (input_, expect_) in enumerate(inputs_):

            result = parser.parse(input_)
            trans_ = translate(result)
            trans_ = [str(l) for l in trans_]
            trans_ = "".join(trans_)
            error_msg = "Sentence {}-th -- '{}'. Expect: \n<{}> /\n Actual: \n<{}>".format(
                i, input_, expect_, trans_)
            self.assertEqual(expect_, trans_, error_msg)


class Test_information_extraction(unittest.TestCase):
    def test_get_references(self):
        inputs_ = [

            (
                "drs([A,B],[object(A,robot,countable,na,eq,1)-1/2,predicate(B,run,A)-1/3])",
                set(['A', 'B'])
            ),
            (
                "drs([A,B],[object(A,robot,countable,na,eq,1)-1/2,predicate(B,run,A)-1/3,modifier_adv(B,slowly,pos)-1/4])",
                set(['A', 'B'])
            ),
            (
                "drs([A,B],[object(A,apple,countable,na,eq,1)-1/4,predicate(B,throw,named('John'),A)-1/2])",
                set(['A', 'B'])
            ),
            (
                "drs([A,B],[object(A,apple,countable,na,eq,1)-1/4,predicate(B,throw,named('John'),A)-1/2,modifier_adv(B,slowly,pos)-1/5])",
                set(['A', 'B'])
            ),
            (
                "drs([A,B,C],[object(A,robot,countable,na,eq,1)-1/3,property(A,small,pos)-1/2,object(B,apple,countable,na,eq,1)-1/6,predicate(C,throw,A,B)-1/4,modifier_adv(C,slowly,pos)-1/7])",
                set(["A", "B", "C"])
            ),
            (
                "drs([A,B,C],[object(A,robot,countable,na,eq,1)-1/3,property(A,small,pos)-1/2,object(B,apple,countable,na,eq,1)-1/7,property(B,red,pos)-1/6,predicate(C,throw,A,B)-1/4,modifier_adv(C,slowly,pos)-1/8])",
                set(["A", "B", "C"])
            ),
            (
                "drs([A,B,C],[object(A,robot,countable,na,eq,1)-1/5,property(A,small,pos)-1/2,property(A,green,pos)-1/4,object(B,apple,countable,na,eq,1)-1/8,predicate(C,throw,A,B)-1/6])",
                set(["A", "B", "C"])
            ),
            (
                "drs([A,B,C],[relation(A,of,named('John'))-1/2,object(A,robot,countable,na,eq,1)-1/4,object(B,apple,countable,na,eq,1)-1/7,predicate(C,throw,A,B)-1/5])",
                set(["A", "B", "C"])
            ),
            (
                "drs([A,B,C],[relation(A,of,named('John'))-1/2,object(A,robot,countable,na,eq,1)-1/4,object(B,apple,countable,na,eq,1)-1/7,predicate(C,throw,A,B)-1/5,modifier_adv(C,slowly,pos)-1/8])",
                set(["A", "B", "C"])
            ),
            (
                "drs([A,B,C],[relation(B,of,C)-1/3,object(B,robot,countable,na,eq,1)-1/2,predicate(A,run,B)-1/6,object(C,company,countable,na,eq,1)-1/5])",
                set(["A", "B", "C"])
            ),
            (
                "drs([A,B,C],[relation(B,of,C)-1/3,object(B,robot,countable,na,eq,1)-1/2,predicate(A,run,B)-1/6,modifier_adv(A,slowly,pos)-1/7,object(C,company,countable,na,eq,1)-1/5])",
                set(["A", "B", "C"])
            ),
            (
                "drs([A,B,C,D,E,F],[predicate(F,be,D,E)-1/4,object(E,agent,countable,na,eq,1)-1/6,object(D,robot,countable,na,eq,1)-1/2,object(A,apple,countable,na,eq,1)-1/10,property(A,red,pos)-1/9,object(C,table,countable,na,eq,1)-1/14,predicate(B,throw,D,A)-1/7,modifier_pp(B,under,C)-1/12,modifier_adv(B,slowly,pos)-1/11])",
                set(["A", "B", "C", "D", "E", "F"])
            ),
            (
                "drs([A,B,C,D],[predicate(D,be,B,C)-1/4,object(C,agent,countable,na,eq,1)-1/6,object(B,robot,countable,na,eq,1)-1/2,predicate(A,move,B)-1/7,modifier_adv(A,slowly,pos)-1/8])",
                set(["A", "B", "C", "D"])
            ),
            (
                "drs([A,B,C,D],[object(A,agent,countable,na,eq,1)-1/5,predicate(B,be,named('John'),A)-1/3,object(C,apple,countable,na,eq,1)-1/9,property(C,red,pos)-1/8,predicate(D,throw,named('John'),C)-1/6,modifier_adv(D,slowly,pos)-1/10])",
                set(["A", "B", "C", "D"])
            ),
            (
                "drs([A,B,C,D,E],[object(A,agent,countable,na,eq,1)-1/5,predicate(B,be,named('John'),A)-1/3,object(C,apple,countable,na,eq,1)-1/9,property(C,red,pos)-1/8,object(E,table,countable,na,eq,1)-1/13,predicate(D,throw,named('John'),C)-1/6,modifier_pp(D,under,E)-1/11,modifier_adv(D,slowly,pos)-1/10])",
                set(["A", "B", "C", "D", "E"])
            ),
            (
                "drs([A,B,C],[object(C,robot,countable,na,eq,1)-1/2,object(A,apple,countable,kg,eq,3)-1/7,predicate(B,throw,C,A)-1/3,modifier_adv(B,slowly,pos)-1/8])",
                set(["A", "B", "C"])
            ),
            (
                "drs([A,B,C],[object(C,robot,countable,na,eq,1)-1/2,object(A,apple,countable,kg,eq,3)-1/8,property(A,red,pos)-1/7,predicate(B,throw,C,A)-1/3,modifier_adv(B,slowly,pos)-1/9])",
                set(["A", "B", "C"])
            ),
            (
                "drs([A,B,C],[object(C,robot,countable,na,eq,1)-1/2,object(A,metal,countable,pound,eq,3)-1/7,predicate(B,be,C,A)-1/3])",
                set(["A", "B", "C"])
            ),
            (
                "drs([A],[object(A,robot,countable,na,eq,1)-1/2,can(drs([B,C],[object(B,apple,countable,na,eq,1)-1/7,property(B,red,pos)-1/6,predicate(C,throw,A,B)-1/4,modifier_adv(C,slowly,pos)-1/8]))])",
                set(["A", "B", "C"])
            ),
            (
                "drs([A],[object(A,robot,countable,na,eq,1)-1/2,can(drs([B,C,D],[object(B,apple,countable,na,eq,1)-1/7,property(B,red,pos)-1/6,object(D,table,countable,na,eq,1)-1/11,predicate(C,throw,A,B)-1/4,modifier_pp(C,under,D)-1/9,modifier_adv(C,slowly,pos)-1/8]))])",
                set(["A", "B", "C", "D"])
            ),
            (
                "drs([],[-(drs([A],[object(A,apple,countable,na,eq,1)-1/4]))])",
                set(["A"])
            ),
            (
                "drs([],[question(drs([A,B,C,D],[object(D,apple,countable,na,eq,1)-1/3,property(C,red,pos)-1/7,object(C,box,countable,na,eq,1)-1/8,property(A,small,comp_than,C)-1/4,predicate(B,be,D,A)-1/1]))])",
                set(["A", "B", "C", "D"])
            ),
            (
                "drs([],[question(drs([A,B,C,D],[object(D,apple,countable,na,eq,1)-1/3,property(C,red,pos)-1/8,object(C,box,countable,na,eq,1)-1/9,property(A,small,comp_than,C)-1/5,predicate(B,be,D,A)-1/1]))])",
                set(["A", "B", "C", "D"])
            ),
            (
                "drs([],[question(drs([A,B,C],[object(C,apple,countable,na,eq,1)-1/3,object(A,agent,countable,na,eq,1)-1/5,predicate(B,be,C,A)-1/1]))])",
                set(["A", "B", "C"])
            ),
            (
                "drs([],[question(drs([A,B],[object(A,agent,countable,na,eq,1)-1/4,predicate(B,be,named('John'),A)-1/1]))])",
                set(['A', 'B'])
            ),
            (
                "drs([],[question(drs([A,B],[query(A,who)-1/1,predicate(B,move,A)-1/3,modifier_adv(B,slowly,pos)-1/4]))])",
                set(['A', 'B'])
            ),
            (
                "drs([],[question(drs([A,B],[query(A,who)-1/1,modifier_adv(B,slowly,pos)-1/3,predicate(B,move,A)-1/4]))])",
                set(['A', 'B'])
            ),
            (
                "drs([],[question(drs([A,B,C,D],[query(A,who)-1/1,property(D,red,pos)-1/7,object(D,block,countable,na,eq,1)-1/8,property(B,small,pos_as,D)-1/4,predicate(C,be,A,B)-1/2]))])",
                set(["A", "B", "C", "D"])
            ),
            (
                "drs([],[question(drs([A,B,C,D],[query(A,who)-1/1,property(D,red,pos)-1/6,object(D,block,countable,na,eq,1)-1/7,property(B,small,comp_than,D)-1/3,predicate(C,be,A,B)-1/2]))])",
                set(["A", "B", "C", "D"])
            ),
            (
                "drs([],[question(drs([A,B,C],[query(A,who)-1/1,property(C,small,sup)-1/4,object(C,agent,countable,na,eq,1)-1/5,predicate(B,be,A,C)-1/2]))])",
                set(["A", "B", "C"])
            ),
            (
                "drs([],[question(drs([A,B],[query(A,who)-1/1,predicate(B,be,A,named('John'))-1/2]))])",
                set(['A', 'B'])
            ),
            (
                "drs([],[question(drs([A,B,C,D],[query(A,which)-1/1,object(A,robot,countable,na,eq,1)-1/2,property(D,red,pos)-1/7,object(D,block,countable,na,eq,1)-1/8,property(B,small,comp_than,D)-1/4,predicate(C,be,A,B)-1/3]))])",
                set(["A", "B", "C", "D"])
            ),
            (
                "drs([],[question(drs([A,B,C,D],[query(A,which)-1/1,object(A,robot,countable,na,eq,1)-1/2,property(D,red,pos)-1/8,object(D,block,countable,na,eq,1)-1/9,property(B,small,pos_as,D)-1/5,predicate(C,be,A,B)-1/3]))])",
                set(["A", "B", "C", "D"])
            ),
            (
                "drs([],[question(drs([A,B],[query(A,which)-1/1,object(A,robot,countable,na,eq,1)-1/2,predicate(B,be,A,named('John'))-1/3]))])",
                set(['A', 'B'])
            ),
            (
                "drs([],[command(drs([A,B,C],[object(C,apple,countable,na,eq,1)-1/5,object(B,table,countable,na,eq,1)-1/8,predicate(A,move,named('Sawyer'),C)-1/3,modifier_adv(A,slowly,pos)-1/9,modifier_pp(A,on,B)-1/6]))])",
                set(["A", "B", "C"])
            ),
            (
                "drs([],[command(drs([A,B,C],[property(C,red,pos)-1/5,object(C,apple,countable,na,eq,1)-1/6,object(B,table,countable,na,eq,1)-1/9,predicate(A,move,named('Sawyer'),C)-1/3,modifier_pp(A,on,B)-1/7]))])",
                set(["A", "B", "C"])
            ),
            (
                "drs([],[command(drs([A,B,C],[property(C,red,pos)-1/5,object(C,apple,countable,na,eq,1)-1/6,object(B,table,countable,na,eq,1)-1/9,predicate(A,move,named('Sawyer'),C)-1/3,modifier_adv(A,slowly,pos)-1/10,modifier_pp(A,on,B)-1/7]))])",
                set(["A", "B", "C"])
            ),
            (
                "drs([],[command(drs([A,B,C],[property(C,red,pos)-1/5,object(C,apple,countable,na,eq,1)-1/6,object(B,table,countable,na,eq,1)-1/9,predicate(A,pick,named('Sawyer'),C)-1/3,modifier_adv(A,slowly,pos)-1/10,modifier_pp(A,on,B)-1/7]))])",
                set(["A", "B", "C"])
            ),
            (
                "drs([],[command(drs([A,B,C],[property(C,red,pos)-1/5,object(C,apple,countable,na,eq,1)-1/6,object(B,table,countable,na,eq,1)-1/9,predicate(A,grasp,named('Sawyer'),C)-1/3,modifier_adv(A,slowly,pos)-1/10,modifier_pp(A,on,B)-1/7]))])",
                set(["A", "B", "C"])
            ),
            (
                "drs([],[=>(drs([A,B,C],[relation(B,of,C)-1/4,object(B,robot,countable,na,eq,1)-1/3,predicate(A,run,B)-1/7,object(C,company,countable,na,eq,1)-1/6]),drs([D],[predicate(D,run,B)-1/14,modifier_adv(D,slowly,pos)-1/15]))])",
                set(["A", "B", "C", "D"])
            ),
            (
                "drs([],[=>(drs([A,B,C,D],[relation(C,of,D)-1/4,object(C,robot,countable,na,eq,1)-1/3,object(A,apple,countable,na,eq,1)-1/9,predicate(B,throw,C,A)-1/7,object(D,company,countable,na,eq,1)-1/6]),drs([E,F],[object(E,apple,countable,na,eq,1)-1/18,predicate(F,throw,C,E)-1/16,modifier_adv(F,slowly,pos)-1/19]))])",
                set(["A", "B", "C", "D", "E", "F"])
            ),
            (
                "drs([],[=>(drs([A,B,C,D],[relation(C,of,D)-1/4,object(C,robot,countable,na,eq,1)-1/3,object(A,apple,countable,na,eq,1)-1/10,property(A,red,pos)-1/9,predicate(B,throw,C,A)-1/7,modifier_adv(B,slowly,pos)-1/11,object(D,company,countable,na,eq,1)-1/6]),drs([E,F,G],[object(E,apple,countable,na,eq,1)-1/21,property(E,red,pos)-1/20,predicate(F,throw,C,E)-1/18,modifier_pp(F,under,G)-1/23,modifier_adv(F,slowly,pos)-1/22,object(G,table,countable,na,eq,1)-1/25]))])",
                set(["A", "B", "C", "D", "E", "F", "G"])
            ),
            (
                "drs([],[=>(drs([A,B,C],[relation(B,of,C)-1/4,object(B,robot,countable,na,eq,1)-1/3,predicate(A,run,B)-1/7,object(C,company,countable,na,eq,1)-1/6]),drs([D],[predicate(D,run,B)-1/14,modifier_adv(D,slowly,pos)-1/15]))])",
                set(["A", "B", "C", "D"])
            ),
            (
                "drs([],[=>(drs([A,B,C,D],[relation(C,of,D)-1/4,object(C,robot,countable,na,eq,1)-1/3,object(A,apple,countable,na,eq,1)-1/9,predicate(B,throw,C,A)-1/7,object(D,company,countable,na,eq,1)-1/6]),drs([E,F],[object(E,apple,countable,na,eq,1)-1/18,predicate(F,throw,C,E)-1/16,modifier_adv(F,slowly,pos)-1/19]))])",
                set(["A", "B", "C", "D", "E", "F"])
            ),
            (
                "drs([],[=>(drs([A,B,C,D],[relation(C,of,D)-1/4,object(C,robot,countable,na,eq,1)-1/3,object(A,apple,countable,na,eq,1)-1/10,property(A,red,pos)-1/9,predicate(B,throw,C,A)-1/7,modifier_adv(B,slowly,pos)-1/11,object(D,company,countable,na,eq,1)-1/6]),drs([E,F,G],[object(E,apple,countable,na,eq,1)-1/21,property(E,red,pos)-1/20,predicate(F,throw,C,E)-1/18,modifier_pp(F,under,G)-1/23,modifier_adv(F,slowly,pos)-1/22,object(G,table,countable,na,eq,1)-1/25]))])",
                set(["A", "B", "C", "D", "E", "F", "G"])
            ),
            (
                "drs([],[=>(drs([A,B,C],[object(A,agent,countable,na,eq,1)-1/6,predicate(B,be,named('John'),A)-1/4,predicate(C,run,named('John'))-1/7]),drs([D,E,F],[object(D,agent,countable,na,eq,1)-1/13,predicate(E,be,named('John'),D)-1/11,predicate(F,run,named('John'))-1/14,modifier_adv(F,slowly,pos)-1/15]))])",
                set(["A", "B", "C", "D", "E", "F"])
            ),
            (
                "drs([],[=>(drs([A,B,C,D],[object(A,agent,countable,na,eq,1)-1/6,predicate(B,be,named('John'),A)-1/4,object(C,apple,countable,na,eq,1)-1/9,predicate(D,throw,named('John'),C)-1/7]),drs([E,F,G,H],[object(E,agent,countable,na,eq,1)-1/15,predicate(F,be,named('John'),E)-1/13,object(G,apple,countable,na,eq,1)-1/18,predicate(H,throw,named('John'),G)-1/16,modifier_adv(H,slowly,pos)-1/19]))])",
                set(["A", "B", "C", "D", "E", "F", "G", "H"])
            ),
            (
                "drs([],[=>(drs([A,B,C,D],[object(A,agent,countable,na,eq,1)-1/6,predicate(B,be,named('John'),A)-1/4,object(C,apple,countable,na,eq,1)-1/10,property(C,red,pos)-1/9,predicate(D,throw,named('John'),C)-1/7,modifier_adv(D,slowly,pos)-1/11]),drs([E,F,G,H,I],[object(E,agent,countable,na,eq,1)-1/17,predicate(F,be,named('John'),E)-1/15,object(G,apple,countable,na,eq,1)-1/21,property(G,red,pos)-1/20,object(I,table,countable,na,eq,1)-1/25,predicate(H,throw,named('John'),G)-1/18,modifier_pp(H,under,I)-1/23,modifier_adv(H,slowly,pos)-1/22]))])",
                set(["A", "B", "C", "D", "E", "F", "G", "H", "I"])
            ),
            (
                "drs([],[v(drs([A,B],[object(A,robot,countable,na,eq,1)-1/3,property(A,small,pos)-1/2,predicate(B,run,A)-1/4]),drs([C,D],[object(C,robot,countable,na,eq,1)-1/8,property(C,small,pos)-1/7,predicate(D,run,C)-1/9,modifier_adv(D,slowly,pos)-1/10]))])",
                set(['A', 'B', "C", "D"])
            ),
            (
                "drs([],[v(drs([A,B,C],[object(A,robot,countable,na,eq,1)-1/3,property(A,small,pos)-1/2,object(B,apple,countable,na,eq,1)-1/6,predicate(C,throw,A,B)-1/4]),drs([D,E,F],[object(D,robot,countable,na,eq,1)-1/10,property(D,small,pos)-1/9,object(E,apple,countable,na,eq,1)-1/13,predicate(F,throw,D,E)-1/11,modifier_adv(F,slowly,pos)-1/14]))])",
                set(["A", "B", "C", "D", "E", "F"])
            ),
            (
                "drs([],[v(drs([A,B,C],[object(A,robot,countable,na,eq,1)-1/3,property(A,small,pos)-1/2,object(B,apple,countable,na,eq,1)-1/7,property(B,red,pos)-1/6,predicate(C,throw,A,B)-1/4,modifier_adv(C,slowly,pos)-1/8]),drs([D,E,F,G],[object(D,robot,countable,na,eq,1)-1/12,property(D,small,pos)-1/11,object(E,apple,countable,na,eq,1)-1/16,property(E,red,pos)-1/15,object(G,table,countable,na,eq,1)-1/20,predicate(F,throw,D,E)-1/13,modifier_pp(F,under,G)-1/18,modifier_adv(F,slowly,pos)-1/17]))])",
                set(["A", "B", "C", "D", "E", "F", "G"])
            ),
            (
                "drs([],[v(drs([A,B],[object(A,robot,countable,na,eq,1)-1/3,property(A,small,pos)-1/2,predicate(B,run,A)-1/4]),drs([C],[object(C,apple,countable,na,eq,1)-1/9]))])",
                set(['A', 'B', "C"])
            ),
            (
                "drs([],[v(drs([A,B,C],[object(A,robot,countable,na,eq,1)-1/3,property(A,small,pos)-1/2,object(B,apple,countable,na,eq,1)-1/6,predicate(C,throw,A,B)-1/4]),drs([D],[object(D,apple,countable,na,eq,1)-1/11]))])",
                set(["A", "B", "C", "D"])
            ),
            (
                "drs([],[v(drs([A,B,C],[object(A,robot,countable,na,eq,1)-1/3,property(A,small,pos)-1/2,object(B,apple,countable,na,eq,1)-1/7,property(B,red,pos)-1/6,predicate(C,throw,A,B)-1/4,modifier_adv(C,slowly,pos)-1/8]),drs([D],[object(D,apple,countable,na,eq,3)-1/13]))])",
                set(["A", "B", "C", "D"])
            ),
        ]
        parser = Lark(grammar_visualization_str,
                      start="drs_root")
        for i, (input_, expect_) in enumerate(inputs_):
            try:
                result = parser.parse(input_)
                references = get_references(result)
                references_set = set(["".join(get_leaves(ref))
                                      for ref in references])

                mismatch_error_msg = "{} not equal with {}.\n At sentence {}-th: '{}'".format(
                    references_set, expect_, i, input_)
                self.assertEqual(references_set, expect_, mismatch_error_msg)
            except:
                error_msg = "Sentence {}-th is in valid: {}".format(i, input_)
                self.fail(error_msg)

    def test_get_entities(self):
        inputs_ = [

            (
                "drs([A,B],[object(A,robot,countable,na,eq,1)-1/2,predicate(B,run,A)-1/3])",
                set(['A', 'B'])
            ),
            (
                "drs([A,B],[object(A,robot,countable,na,eq,1)-1/2,predicate(B,run,A)-1/3,modifier_adv(B,slowly,pos)-1/4])",
                set(['A', 'B'])
            ),
            (
                "drs([A,B],[object(A,apple,countable,na,eq,1)-1/4,predicate(B,throw,named('John'),A)-1/2])",
                set(["A", "B", "named('John')"])
            ),
            (
                "drs([A,B],[object(A,apple,countable,na,eq,1)-1/4,predicate(B,throw,named('John'),A)-1/2,modifier_adv(B,slowly,pos)-1/5])",
                set(['A', 'B', "named('John')"])
            ),
            (
                "drs([A,B,C],[object(A,robot,countable,na,eq,1)-1/3,property(A,small,pos)-1/2,object(B,apple,countable,na,eq,1)-1/6,predicate(C,throw,A,B)-1/4,modifier_adv(C,slowly,pos)-1/7])",
                set(["A", "B", "C"])
            ),
            (
                "drs([A,B,C],[object(A,robot,countable,na,eq,1)-1/3,property(A,small,pos)-1/2,object(B,apple,countable,na,eq,1)-1/7,property(B,red,pos)-1/6,predicate(C,throw,A,B)-1/4,modifier_adv(C,slowly,pos)-1/8])",
                set(["A", "B", "C"])
            ),
            (
                "drs([A,B,C],[object(A,robot,countable,na,eq,1)-1/5,property(A,small,pos)-1/2,property(A,green,pos)-1/4,object(B,apple,countable,na,eq,1)-1/8,predicate(C,throw,A,B)-1/6])",
                set(["A", "B", "C"])
            ),
            (
                "drs([A,B,C],[relation(A,of,named('John'))-1/2,object(A,robot,countable,na,eq,1)-1/4,object(B,apple,countable,na,eq,1)-1/7,predicate(C,throw,A,B)-1/5])",
                set(["A", "B", "C", "named('John')"])
            ),
            (
                "drs([A,B,C],[relation(A,of,named('John'))-1/2,object(A,robot,countable,na,eq,1)-1/4,object(B,apple,countable,na,eq,1)-1/7,predicate(C,throw,A,B)-1/5,modifier_adv(C,slowly,pos)-1/8])",
                set(["A", "B", "C", "named('John')"])
            ),
            (
                "drs([A,B,C],[relation(B,of,C)-1/3,object(B,robot,countable,na,eq,1)-1/2,predicate(A,run,B)-1/6,object(C,company,countable,na,eq,1)-1/5])",
                set(["A", "B", "C"])
            ),
            (
                "drs([A,B,C],[relation(B,of,C)-1/3,object(B,robot,countable,na,eq,1)-1/2,predicate(A,run,B)-1/6,modifier_adv(A,slowly,pos)-1/7,object(C,company,countable,na,eq,1)-1/5])",
                set(["A", "B", "C"])
            ),
            (
                "drs([A,B,C,D,E,F],[predicate(F,be,D,E)-1/4,object(E,agent,countable,na,eq,1)-1/6,object(D,robot,countable,na,eq,1)-1/2,object(A,apple,countable,na,eq,1)-1/10,property(A,red,pos)-1/9,object(C,table,countable,na,eq,1)-1/14,predicate(B,throw,D,A)-1/7,modifier_pp(B,under,C)-1/12,modifier_adv(B,slowly,pos)-1/11])",
                set(["A", "B", "C", "D", "E", "F"])
            ),
            (
                "drs([A,B,C,D],[predicate(D,be,B,C)-1/4,object(C,agent,countable,na,eq,1)-1/6,object(B,robot,countable,na,eq,1)-1/2,predicate(A,move,B)-1/7,modifier_adv(A,slowly,pos)-1/8])",
                set(["A", "B", "C", "D"])
            ),
            (
                "drs([A,B,C,D],[object(A,agent,countable,na,eq,1)-1/5,predicate(B,be,named('John'),A)-1/3,object(C,apple,countable,na,eq,1)-1/9,property(C,red,pos)-1/8,predicate(D,throw,named('John'),C)-1/6,modifier_adv(D,slowly,pos)-1/10])",
                set(["A", "B", "C", "D", "named('John')"])
            ),
            (
                "drs([A,B,C,D,E],[object(A,agent,countable,na,eq,1)-1/5,predicate(B,be,named('John'),A)-1/3,object(C,apple,countable,na,eq,1)-1/9,property(C,red,pos)-1/8,object(E,table,countable,na,eq,1)-1/13,predicate(D,throw,named('John'),C)-1/6,modifier_pp(D,under,E)-1/11,modifier_adv(D,slowly,pos)-1/10])",
                set(["A", "B", "C", "D", "E", "named('John')"])
            ),
            (
                "drs([A,B,C],[object(C,robot,countable,na,eq,1)-1/2,object(A,apple,countable,kg,eq,3)-1/7,predicate(B,throw,C,A)-1/3,modifier_adv(B,slowly,pos)-1/8])",
                set(["A", "B", "C"])
            ),
            (
                "drs([A,B,C],[object(C,robot,countable,na,eq,1)-1/2,object(A,apple,countable,kg,eq,3)-1/8,property(A,red,pos)-1/7,predicate(B,throw,C,A)-1/3,modifier_adv(B,slowly,pos)-1/9])",
                set(["A", "B", "C"])
            ),
            (
                "drs([A,B,C],[object(C,robot,countable,na,eq,1)-1/2,object(A,metal,countable,pound,eq,3)-1/7,predicate(B,be,C,A)-1/3])",
                set(["A", "B", "C"])
            ),
            (
                "drs([A],[object(A,robot,countable,na,eq,1)-1/2,can(drs([B,C],[object(B,apple,countable,na,eq,1)-1/7,property(B,red,pos)-1/6,predicate(C,throw,A,B)-1/4,modifier_adv(C,slowly,pos)-1/8]))])",
                set(["A", "B", "C"])
            ),
            (
                "drs([A],[object(A,robot,countable,na,eq,1)-1/2,can(drs([B,C,D],[object(B,apple,countable,na,eq,1)-1/7,property(B,red,pos)-1/6,object(D,table,countable,na,eq,1)-1/11,predicate(C,throw,A,B)-1/4,modifier_pp(C,under,D)-1/9,modifier_adv(C,slowly,pos)-1/8]))])",
                set(["A", "B", "C", "D"])
            ),
            (
                "drs([],[-(drs([A],[object(A,apple,countable,na,eq,1)-1/4]))])",
                set(["A"])
            ),
            (
                "drs([],[question(drs([A,B,C,D],[object(D,apple,countable,na,eq,1)-1/3,property(C,red,pos)-1/7,object(C,box,countable,na,eq,1)-1/8,property(A,small,comp_than,C)-1/4,predicate(B,be,D,A)-1/1]))])",
                set(["A", "B", "C", "D"])
            ),
            (
                "drs([],[question(drs([A,B,C,D],[object(D,apple,countable,na,eq,1)-1/3,property(C,red,pos)-1/8,object(C,box,countable,na,eq,1)-1/9,property(A,small,comp_than,C)-1/5,predicate(B,be,D,A)-1/1]))])",
                set(["A", "B", "C", "D"])
            ),
            (
                "drs([],[question(drs([A,B,C],[object(C,apple,countable,na,eq,1)-1/3,object(A,agent,countable,na,eq,1)-1/5,predicate(B,be,C,A)-1/1]))])",
                set(["A", "B", "C"])
            ),
            (
                "drs([],[question(drs([A,B],[object(A,agent,countable,na,eq,1)-1/4,predicate(B,be,named('John'),A)-1/1]))])",
                set(['A', 'B', "named('John')"])
            ),
            (
                "drs([],[question(drs([A,B],[query(A,who)-1/1,predicate(B,move,A)-1/3,modifier_adv(B,slowly,pos)-1/4]))])",
                set(['A', 'B'])
            ),
            (
                "drs([],[question(drs([A,B],[query(A,who)-1/1,modifier_adv(B,slowly,pos)-1/3,predicate(B,move,A)-1/4]))])",
                set(['A', 'B'])
            ),
            (
                "drs([],[question(drs([A,B,C,D],[query(A,who)-1/1,property(D,red,pos)-1/7,object(D,block,countable,na,eq,1)-1/8,property(B,small,pos_as,D)-1/4,predicate(C,be,A,B)-1/2]))])",
                set(["A", "B", "C", "D"])
            ),
            (
                "drs([],[question(drs([A,B,C,D],[query(A,who)-1/1,property(D,red,pos)-1/6,object(D,block,countable,na,eq,1)-1/7,property(B,small,comp_than,D)-1/3,predicate(C,be,A,B)-1/2]))])",
                set(["A", "B", "C", "D"])
            ),
            (
                "drs([],[question(drs([A,B,C],[query(A,who)-1/1,property(C,small,sup)-1/4,object(C,agent,countable,na,eq,1)-1/5,predicate(B,be,A,C)-1/2]))])",
                set(["A", "B", "C"])
            ),
            (
                "drs([],[question(drs([A,B],[query(A,who)-1/1,predicate(B,be,A,named('John'))-1/2]))])",
                set(['A', 'B', "named('John')"])
            ),
            (
                "drs([],[question(drs([A,B,C,D],[query(A,which)-1/1,object(A,robot,countable,na,eq,1)-1/2,property(D,red,pos)-1/7,object(D,block,countable,na,eq,1)-1/8,property(B,small,comp_than,D)-1/4,predicate(C,be,A,B)-1/3]))])",
                set(["A", "B", "C", "D"])
            ),
            (
                "drs([],[question(drs([A,B,C,D],[query(A,which)-1/1,object(A,robot,countable,na,eq,1)-1/2,property(D,red,pos)-1/8,object(D,block,countable,na,eq,1)-1/9,property(B,small,pos_as,D)-1/5,predicate(C,be,A,B)-1/3]))])",
                set(["A", "B", "C", "D"])
            ),
            (
                "drs([],[question(drs([A,B],[query(A,which)-1/1,object(A,robot,countable,na,eq,1)-1/2,predicate(B,be,A,named('John'))-1/3]))])",
                set(['A', 'B', "named('John')"])
            ),
            (
                "drs([],[command(drs([A,B,C],[object(C,apple,countable,na,eq,1)-1/5,object(B,table,countable,na,eq,1)-1/8,predicate(A,move,named('Sawyer'),C)-1/3,modifier_adv(A,slowly,pos)-1/9,modifier_pp(A,on,B)-1/6]))])",
                set(["A", "B", "C", "named('Sawyer')"])
            ),
            (
                "drs([],[command(drs([A,B,C],[property(C,red,pos)-1/5,object(C,apple,countable,na,eq,1)-1/6,object(B,table,countable,na,eq,1)-1/9,predicate(A,move,named('Sawyer'),C)-1/3,modifier_pp(A,on,B)-1/7]))])",
                set(["A", "B", "C", "named('Sawyer')"])
            ),
            (
                "drs([],[command(drs([A,B,C],[property(C,red,pos)-1/5,object(C,apple,countable,na,eq,1)-1/6,object(B,table,countable,na,eq,1)-1/9,predicate(A,move,named('Sawyer'),C)-1/3,modifier_adv(A,slowly,pos)-1/10,modifier_pp(A,on,B)-1/7]))])",
                set(["A", "B", "C", "named('Sawyer')"])
            ),
            (
                "drs([],[command(drs([A,B,C],[property(C,red,pos)-1/5,object(C,apple,countable,na,eq,1)-1/6,object(B,table,countable,na,eq,1)-1/9,predicate(A,pick,named('Sawyer'),C)-1/3,modifier_adv(A,slowly,pos)-1/10,modifier_pp(A,on,B)-1/7]))])",
                set(["A", "B", "C", "named('Sawyer')"])
            ),
            (
                "drs([],[command(drs([A,B,C],[property(C,red,pos)-1/5,object(C,apple,countable,na,eq,1)-1/6,object(B,table,countable,na,eq,1)-1/9,predicate(A,grasp,named('Sawyer'),C)-1/3,modifier_adv(A,slowly,pos)-1/10,modifier_pp(A,on,B)-1/7]))])",
                set(["A", "B", "C", "named('Sawyer')"])
            ),
            (
                "drs([],[=>(drs([A,B,C],[relation(B,of,C)-1/4,object(B,robot,countable,na,eq,1)-1/3,predicate(A,run,B)-1/7,object(C,company,countable,na,eq,1)-1/6]),drs([D],[predicate(D,run,B)-1/14,modifier_adv(D,slowly,pos)-1/15]))])",
                set(["A", "B", "C", "D"])
            ),
            (
                "drs([],[=>(drs([A,B,C,D],[relation(C,of,D)-1/4,object(C,robot,countable,na,eq,1)-1/3,object(A,apple,countable,na,eq,1)-1/9,predicate(B,throw,C,A)-1/7,object(D,company,countable,na,eq,1)-1/6]),drs([E,F],[object(E,apple,countable,na,eq,1)-1/18,predicate(F,throw,C,E)-1/16,modifier_adv(F,slowly,pos)-1/19]))])",
                set(["A", "B", "C", "D", "E", "F"])
            ),
            (
                "drs([],[=>(drs([A,B,C,D],[relation(C,of,D)-1/4,object(C,robot,countable,na,eq,1)-1/3,object(A,apple,countable,na,eq,1)-1/10,property(A,red,pos)-1/9,predicate(B,throw,C,A)-1/7,modifier_adv(B,slowly,pos)-1/11,object(D,company,countable,na,eq,1)-1/6]),drs([E,F,G],[object(E,apple,countable,na,eq,1)-1/21,property(E,red,pos)-1/20,predicate(F,throw,C,E)-1/18,modifier_pp(F,under,G)-1/23,modifier_adv(F,slowly,pos)-1/22,object(G,table,countable,na,eq,1)-1/25]))])",
                set(["A", "B", "C", "D", "E", "F", "G"])
            ),
            (
                "drs([],[=>(drs([A,B,C],[relation(B,of,C)-1/4,object(B,robot,countable,na,eq,1)-1/3,predicate(A,run,B)-1/7,object(C,company,countable,na,eq,1)-1/6]),drs([D],[predicate(D,run,B)-1/14,modifier_adv(D,slowly,pos)-1/15]))])",
                set(["A", "B", "C", "D"])
            ),
            (
                "drs([],[=>(drs([A,B,C,D],[relation(C,of,D)-1/4,object(C,robot,countable,na,eq,1)-1/3,object(A,apple,countable,na,eq,1)-1/9,predicate(B,throw,C,A)-1/7,object(D,company,countable,na,eq,1)-1/6]),drs([E,F],[object(E,apple,countable,na,eq,1)-1/18,predicate(F,throw,C,E)-1/16,modifier_adv(F,slowly,pos)-1/19]))])",
                set(["A", "B", "C", "D", "E", "F"])
            ),
            (
                "drs([],[=>(drs([A,B,C,D],[relation(C,of,D)-1/4,object(C,robot,countable,na,eq,1)-1/3,object(A,apple,countable,na,eq,1)-1/10,property(A,red,pos)-1/9,predicate(B,throw,C,A)-1/7,modifier_adv(B,slowly,pos)-1/11,object(D,company,countable,na,eq,1)-1/6]),drs([E,F,G],[object(E,apple,countable,na,eq,1)-1/21,property(E,red,pos)-1/20,predicate(F,throw,C,E)-1/18,modifier_pp(F,under,G)-1/23,modifier_adv(F,slowly,pos)-1/22,object(G,table,countable,na,eq,1)-1/25]))])",
                set(["A", "B", "C", "D", "E", "F", "G"])
            ),
            (
                "drs([],[=>(drs([A,B,C],[object(A,agent,countable,na,eq,1)-1/6,predicate(B,be,named('John'),A)-1/4,predicate(C,run,named('John'))-1/7]),drs([D,E,F],[object(D,agent,countable,na,eq,1)-1/13,predicate(E,be,named('John'),D)-1/11,predicate(F,run,named('John'))-1/14,modifier_adv(F,slowly,pos)-1/15]))])",
                set(["A", "B", "C", "D", "E", "F", "named('John')"])
            ),
            (
                "drs([],[=>(drs([A,B,C,D],[object(A,agent,countable,na,eq,1)-1/6,predicate(B,be,named('John'),A)-1/4,object(C,apple,countable,na,eq,1)-1/9,predicate(D,throw,named('John'),C)-1/7]),drs([E,F,G,H],[object(E,agent,countable,na,eq,1)-1/15,predicate(F,be,named('John'),E)-1/13,object(G,apple,countable,na,eq,1)-1/18,predicate(H,throw,named('John'),G)-1/16,modifier_adv(H,slowly,pos)-1/19]))])",
                set(["A", "B", "C", "D", "E", "F", "G", "H", "named('John')"])
            ),
            (
                "drs([],[=>(drs([A,B,C,D],[object(A,agent,countable,na,eq,1)-1/6,predicate(B,be,named('John'),A)-1/4,object(C,apple,countable,na,eq,1)-1/10,property(C,red,pos)-1/9,predicate(D,throw,named('John'),C)-1/7,modifier_adv(D,slowly,pos)-1/11]),drs([E,F,G,H,I],[object(E,agent,countable,na,eq,1)-1/17,predicate(F,be,named('John'),E)-1/15,object(G,apple,countable,na,eq,1)-1/21,property(G,red,pos)-1/20,object(I,table,countable,na,eq,1)-1/25,predicate(H,throw,named('John'),G)-1/18,modifier_pp(H,under,I)-1/23,modifier_adv(H,slowly,pos)-1/22]))])",
                set(["A", "B", "C", "D", "E", "F", "G", "H", "I", "named('John')"])
            ),
            (
                "drs([],[v(drs([A,B],[object(A,robot,countable,na,eq,1)-1/3,property(A,small,pos)-1/2,predicate(B,run,A)-1/4]),drs([C,D],[object(C,robot,countable,na,eq,1)-1/8,property(C,small,pos)-1/7,predicate(D,run,C)-1/9,modifier_adv(D,slowly,pos)-1/10]))])",
                set(['A', 'B', "C", "D"])
            ),
            (
                "drs([],[v(drs([A,B,C],[object(A,robot,countable,na,eq,1)-1/3,property(A,small,pos)-1/2,object(B,apple,countable,na,eq,1)-1/6,predicate(C,throw,A,B)-1/4]),drs([D,E,F],[object(D,robot,countable,na,eq,1)-1/10,property(D,small,pos)-1/9,object(E,apple,countable,na,eq,1)-1/13,predicate(F,throw,D,E)-1/11,modifier_adv(F,slowly,pos)-1/14]))])",
                set(["A", "B", "C", "D", "E", "F"])
            ),
            (
                "drs([],[v(drs([A,B,C],[object(A,robot,countable,na,eq,1)-1/3,property(A,small,pos)-1/2,object(B,apple,countable,na,eq,1)-1/7,property(B,red,pos)-1/6,predicate(C,throw,A,B)-1/4,modifier_adv(C,slowly,pos)-1/8]),drs([D,E,F,G],[object(D,robot,countable,na,eq,1)-1/12,property(D,small,pos)-1/11,object(E,apple,countable,na,eq,1)-1/16,property(E,red,pos)-1/15,object(G,table,countable,na,eq,1)-1/20,predicate(F,throw,D,E)-1/13,modifier_pp(F,under,G)-1/18,modifier_adv(F,slowly,pos)-1/17]))])",
                set(["A", "B", "C", "D", "E", "F", "G"])
            ),
            (
                "drs([],[v(drs([A,B],[object(A,robot,countable,na,eq,1)-1/3,property(A,small,pos)-1/2,predicate(B,run,A)-1/4]),drs([C],[object(C,apple,countable,na,eq,1)-1/9]))])",
                set(['A', 'B', "C"])
            ),
            (
                "drs([],[v(drs([A,B,C],[object(A,robot,countable,na,eq,1)-1/3,property(A,small,pos)-1/2,object(B,apple,countable,na,eq,1)-1/6,predicate(C,throw,A,B)-1/4]),drs([D],[object(D,apple,countable,na,eq,1)-1/11]))])",
                set(["A", "B", "C", "D"])
            ),
            (
                "drs([],[v(drs([A,B,C],[object(A,robot,countable,na,eq,1)-1/3,property(A,small,pos)-1/2,object(B,apple,countable,na,eq,1)-1/7,property(B,red,pos)-1/6,predicate(C,throw,A,B)-1/4,modifier_adv(C,slowly,pos)-1/8]),drs([D],[object(D,apple,countable,na,eq,3)-1/13]))])",
                set(["A", "B", "C", "D"])
            ),
        ]

        parser = Lark(grammar_visualization_str,
                      start="drs_root")
        for i, (input_, expect_) in enumerate(inputs_):
            try:
                result = parser.parse(input_)
                references = get_entities(result)
                references_set = set(["".join(get_leaves(ref))
                                      for ref in references])

                mismatch_error_msg = "{} not equal with {}.\n At sentence {}-th: '{}'".format(
                    references_set, expect_, i, input_)
                self.assertEqual(references_set, expect_, mismatch_error_msg)
            except:
                error_msg = "Sentence {}-th is in valid: {}".format(i, input_)
                self.fail(error_msg)

    def test_get_valid_lexical(self):
        inputs_ = [
            (
                "object(A,robot,countable,na,eq,1)-1/2",
                set(["robot"])
            ),
            (
                "predicate(B,run,A)-1/3",
                set(["run"])
            ),
            (
                "object(A,robot,countable,na,eq,1)-1/2",
                set(["robot"])
            ),
            (
                "predicate(B,run,A)-1/3",
                set(["run"])
            ),
            (
                "modifier_adv(B,slowly,pos)-1/4",
                set(["slowly"])
            ),
            (
                "object(A,apple,countable,na,eq,1)-1/4",
                set(["apple"])
            ),
            (
                "predicate(B,throw,named('John'),A)-1/2",
                set(["throw"])
            ),
            (
                "object(A,apple,countable,na,eq,1)-1/4",
                set(["apple"])
            ),
            (
                "predicate(B,throw,named('John'),A)-1/2",
                set(["throw"])
            ),
            (
                "modifier_adv(B,slowly,pos)-1/5",
                set(["slowly"])
            ),
            (
                "object(A,robot,countable,na,eq,1)-1/3",
                set(["robot"])
            ),
            (
                "property(A,small,pos)-1/2",
                set(["small"])
            ),
            (
                "object(B,apple,countable,na,eq,1)-1/6",
                set(["apple"])
            ),
            (
                "predicate(C,throw,A,B)-1/4",
                set(["throw"])
            ),
            (
                "modifier_adv(C,slowly,pos)-1/7",
                set(["slowly"])
            ),
            (
                "object(A,robot,countable,na,eq,1)-1/3",
                set(["robot"])
            ),
            (
                "property(A,small,pos)-1/2",
                set(["small"])
            ),
            (
                "object(B,apple,countable,na,eq,1)-1/7",
                set(["apple"])
            ),
            (
                "property(B,red,pos)-1/6",
                set(["red"])
            ),
            (
                "predicate(C,throw,A,B)-1/4",
                set(["throw"])
            ),
            (
                "modifier_adv(C,slowly,pos)-1/8",
                set(["slowly"])
            ),
            (
                "object(A,robot,countable,na,eq,1)-1/5",
                set(["countable"])
            ),
            (
                "property(A,small,pos)-1/2",
                set(["small"])
            ),
            (
                "property(A,green,pos)-1/4",
                set(["green"])
            ),
            (
                "object(B,apple,countable,na,eq,1)-1/8",
                set(["apple"])
            ),
            (
                "predicate(C,throw,A,B)-1/6",
                set(["throw"])
            ),
            (
                "object(A,robot,countable,na,eq,1)-1/4",
                set(["robot"])
            ),
            (
                "object(B,apple,countable,na,eq,1)-1/7",
                set(["apple"])
            ),
            (
                "predicate(C,throw,A,B)-1/5",
                set(["throw"])
            ),
            (
                "object(A,robot,countable,na,eq,1)-1/4",
                set(["robot"])
            ),
            (
                "object(B,apple,countable,na,eq,1)-1/7",
                set(["apple"])
            ),
            (
                "predicate(C,throw,A,B)-1/5",
                set(["throw"])
            ),
            (
                "modifier_adv(C,slowly,pos)-1/8",
                set(["slowly"])
            ),
            (
                "object(B,robot,countable,na,eq,1)-1/2",
                set(["robot"])
            ),
            (
                "predicate(A,run,B)-1/6",
                set(["run"])
            ),
            (
                "object(C,company,countable,na,eq,1)-1/5",
                set(["company"])
            ),
            (
                "object(B,robot,countable,na,eq,1)-1/2",
                set(["robot"])
            ),
            (
                "predicate(A,run,B)-1/6",
                set(["run"])
            ),
            (
                "modifier_adv(A,slowly,pos)-1/7",
                set(["slowly"])
            ),
            (
                "object(C,company,countable,na,eq,1)-1/5",
                set(["company"])
            ),
            (
                "predicate(F,be,D,E)-1/4",
                set(["be"])
            ),
            (
                "object(E,agent,countable,na,eq,1)-1/6",
                set(["agent"])
            ),
            (
                "object(D,robot,countable,na,eq,1)-1/2",
                set(["robot"])
            ),
            (
                "object(A,apple,countable,na,eq,1)-1/10",
                set(["apple"])
            ),
            (
                "property(A,red,pos)-1/9",
                set(["red"])
            ),
            (
                "object(C,table,countable,na,eq,1)-1/14",
                set(["table"])
            ),
            (
                "predicate(B,throw,D,A)-1/7",
                set(["throw"])
            ),
            (
                "modifier_pp(B,under,C)-1/12",
                set(["under"])
            ),
            (
                "modifier_adv(B,slowly,pos)-1/11",
                set(["slowly"])
            ),
            (
                "predicate(D,be,B,C)-1/4",
                set(["be"])
            ),
            (
                "object(C,agent,countable,na,eq,1)-1/6",
                set(["agent"])
            ),
            (
                "object(B,robot,countable,na,eq,1)-1/2",
                set(["robot"])
            ),
            (
                "predicate(A,move,B)-1/7",
                set(["move"])
            ),
            (
                "modifier_adv(A,slowly,pos)-1/8",
                set(["slowly"])
            ),
            (
                "object(A,agent,countable,na,eq,1)-1/5",
                set(["agent"])
            ),
            (
                "predicate(B,be,named('John'),A)-1/3",
                set(["be"])
            ),
            (
                "object(C,apple,countable,na,eq,1)-1/9",
                set(["apple"])
            ),
            (
                "property(C,red,pos)-1/8",
                set(["red"])
            ),
            (
                "predicate(D,throw,named('John'),C)-1/6",
                set(["throw"])
            ),
            (
                "modifier_adv(D,slowly,pos)-1/10",
                set(["slowly"])
            ),
            (
                "object(A,agent,countable,na,eq,1)-1/5",
                set(["agent"])
            ),
            (
                "predicate(B,be,named('John'),A)-1/3",
                set(["be"])
            ),
            (
                "object(C,apple,countable,na,eq,1)-1/9",
                set(["apple"])
            ),
            (
                "property(C,red,pos)-1/8",
                set(["red"])
            ),
            (
                "object(E,table,countable,na,eq,1)-1/13",
                set(["table"])
            ),
            (
                "predicate(D,throw,named('John'),C)-1/6",
                set(["throw"])
            ),
            (
                "modifier_pp(D,under,E)-1/11",
                set(["under"])
            ),
            (
                "modifier_adv(D,slowly,pos)-1/10",
                set(["slowly"])
            ),
            (
                "object(C,robot,countable,na,eq,1)-1/2",
                set(["robot"])
            ),
            (
                "object(A,apple,countable,kg,eq,3)-1/7",
                set(["apple"])
            ),
            (
                "predicate(B,throw,C,A)-1/3",
                set(["throw"])
            ),
            (
                "modifier_adv(B,slowly,pos)-1/8",
                set(["slowly"])
            ),
            (
                "object(C,robot,countable,na,eq,1)-1/2",
                set(["robot"])
            ),
            (
                "object(A,apple,countable,kg,eq,3)-1/8",
                set(["apple"])
            ),
            (
                "property(A,red,pos)-1/7",
                set(["red"])
            ),
            (
                "predicate(B,throw,C,A)-1/3",
                set(["throw"])
            ),
            (
                "modifier_adv(B,slowly,pos)-1/9",
                set(["slowly"])
            ),
            (
                "object(C,robot,countable,na,eq,1)-1/2",
                set(["robot"])
            ),
            (
                "object(A,metal,countable,pound,eq,3)-1/7",
                set(["metal"])
            ),
            (
                "predicate(B,be,C,A)-1/3",
                set(["be"])
            ),
            (
                "object(A,robot,countable,na,eq,1)-1/2",
                set(["robot"])
            ),
            (
                "object(A,robot,countable,na,eq,1)-1/2",
                set(["robot"])
            ),
        ]
        parser = Lark(grammar_visualization_str,
                      start="atomic_condition")
        for i, (input_, expect_) in enumerate(inputs_):
            try:
                result = parser.parse(input_)
                references = get_valid_lexical(result)
                references_set = set(["".join(get_leaves(ref))
                                      for ref in references])

                mismatch_error_msg = "{} not equal with {}.\n At sentence {}-th: '{}'".format(
                    references_set, expect_, i, input_)
                # self.assertEqual(references_set, expect_, mismatch_error_msg)
            except:
                error_msg = "Sentence {}-th is in valid: {}".format(i, input_)
                self.fail(error_msg)

    def test_get_cname(self):
        inputs_ = [
            (
                "named('John')",
                set(["John"])
            ),
            (
                "named('Sawyer')",
                set(["Sawyer"])
            ),
        ]
        parser = Lark(grammar_visualization_str,
                      start="named_entity")
        for i, (input_, expect_) in enumerate(inputs_):
            try:
                result = parser.parse(input_)
                references = get_cname(result)
                references_set = set(["".join(get_leaves(ref))
                                      for ref in references])

                mismatch_error_msg = "{} not equal with {}.\n At sentence {}-th: '{}'".format(
                    references_set, expect_, i, input_)
                self.assertEqual(references_set, expect_, mismatch_error_msg)
            except:
                error_msg = "Sentence {}-th is in valid: {}".format(i, input_)
                self.fail(error_msg)

    def test_get_conditions(self):
        inputs_ = [
            (
                "[property(C,red,pos)-1/5,object(C,apple,countable,na,eq,1)-1/6,object(B,table,countable,na,eq,1)-1/9,predicate(A,move,named('Sawyer'),C)-1/3,modifier_pp(A,on,B)-1/7]",
                set([
                    "property(C,red,pos)-1/5",
                    "object(C,apple,countable,na,eq,1)-1/6",
                    "object(B,table,countable,na,eq,1)-1/9",
                    "predicate(A,move,named('Sawyer'),C)-1/3",
                    "modifier_pp(A,on,B)-1/7"
                ])
            )
        ]
        parser = Lark(grammar_visualization_str, start="conditions")
        for i, (input_, expect_) in enumerate(inputs_):
            result = parser.parse(input_)
            conditions = get_conditions(result)
            conditions = ["".join(get_leaves(c)) for c in conditions]
            conditions = set(conditions)

            error_msg = "Sentence {}-th: '{}'. Expect: <{}>/ Actual: <{}>".format(
                i, input_, expect_, conditions)
            self.assertEqual(expect_, conditions, error_msg)

    def test_get_objects(self):
        inputs_ = [
            (
                "[property(C,red,pos)-1/5,object(C,apple,countable,na,eq,1)-1/6,object(B,table,countable,na,eq,1)-1/9,predicate(A,move,named('Sawyer'),C)-1/3,modifier_pp(A,on,B)-1/7]",
                set([
                    "object(C,apple,countable,na,eq,1)",
                    "object(B,table,countable,na,eq,1)",
                ])
            )
        ]
        parser = Lark(grammar_visualization_str, start="conditions")
        for i, (input_, expect_) in enumerate(inputs_):
            result = parser.parse(input_)
            objects = get_objects(result)
            objects = ["".join(get_leaves(c)) for c in objects]
            objects = set(objects)

            error_msg = "Sentence {}-th: '{}'. Expect: <{}>/ Actual: <{}>".format(
                i, input_, expect_, objects)
            self.assertEqual(expect_, objects, error_msg)

    def test_get_predicates(self):
        inputs_ = [
            (
                "[property(C,red,pos)-1/5,object(C,apple,countable,na,eq,1)-1/6,object(B,table,countable,na,eq,1)-1/9,predicate(A,move,named('Sawyer'),C)-1/3,modifier_pp(A,on,B)-1/7]",
                set([
                    "predicate(A,move,named('Sawyer'),C)",
                ])
            )
        ]
        parser = Lark(grammar_visualization_str, start="conditions")
        for i, (input_, expect_) in enumerate(inputs_):
            result = parser.parse(input_)
            predicates = get_predicates(result)
            predicates = ["".join(get_leaves(c)) for c in predicates]
            predicates = set(predicates)

            error_msg = "Sentence {}-th: '{}'. Expect: <{}>/ Actual: <{}>".format(
                i, input_, expect_, predicates)
            self.assertEqual(expect_, predicates, error_msg)

    def test_get_properties(self):
        inputs_ = [
            (
                "[property(C,red,pos)-1/5,object(C,apple,countable,na,eq,1)-1/6,object(B,table,countable,na,eq,1)-1/9,predicate(A,move,named('Sawyer'),C)-1/3,modifier_pp(A,on,B)-1/7]",
                set([
                    "property(C,red,pos)",
                ])
            )
        ]
        parser = Lark(grammar_visualization_str, start="conditions")
        for i, (input_, expect_) in enumerate(inputs_):
            result = parser.parse(input_)
            properties = get_properties(result)
            properties = ["".join(get_leaves(c)) for c in properties]
            properties = set(properties)

            error_msg = "Sentence {}-th: '{}'. Expect: <{}>/ Actual: <{}>".format(
                i, input_, expect_, properties)
            self.assertEqual(expect_, properties, error_msg)

    def test_get_modifier_adverbs(self):
        inputs_ = [
            (
                "[object(D,robot,countable,na,eq,1)-1/10,property(D,small,pos)-1/9,object(E,apple,countable,na,eq,1)-1/13,predicate(F,throw,D,E)-1/11,modifier_adv(F,slowly,pos)-1/14]",
                set([
                    "modifier_adv(F,slowly,pos)",
                ])
            )
        ]
        parser = Lark(grammar_visualization_str, start="conditions")
        for i, (input_, expect_) in enumerate(inputs_):
            result = parser.parse(input_)
            adverbs = get_modifier_adverbs(result)
            adverbs = ["".join(get_leaves(c)) for c in adverbs]
            adverbs = set(adverbs)

            error_msg = "Sentence {}-th: '{}'. Expect: <{}>/ Actual: <{}>".format(
                i, input_, expect_, adverbs)
            self.assertEqual(expect_, adverbs, error_msg)

    def test_get_prepositions(self):
        inputs_ = [
            (
                "[property(C,red,pos)-1/5,object(C,apple,countable,na,eq,1)-1/6,object(B,table,countable,na,eq,1)-1/9,predicate(A,move,named('Sawyer'),C)-1/3,modifier_pp(A,on,B)-1/7]",
                set([
                    "modifier_pp(A,on,B)",
                ])
            )
        ]
        parser = Lark(grammar_visualization_str, start="conditions")
        for i, (input_, expect_) in enumerate(inputs_):
            result = parser.parse(input_)
            prepositions = get_prepositions(result)
            prepositions = ["".join(get_leaves(c)) for c in prepositions]
            prepositions = set(prepositions)

            error_msg = "Sentence {}-th: '{}'. Expect: <{}>/ Actual: <{}>".format(
                i, input_, expect_, prepositions)
            self.assertEqual(expect_, prepositions, error_msg)

    def test_get_queries(self):
        inputs_ = [
            (
                "[question(drs([A,B],[query(A,who)-1/1,predicate(B,move,A)-1/3,modifier_adv(B,slowly,pos)-1/4]))]",
                set([
                    "query(A,who)",
                ])
            )
        ]
        parser = Lark(grammar_visualization_str, start="conditions")
        for i, (input_, expect_) in enumerate(inputs_):
            result = parser.parse(input_)
            queries = get_queries(result)
            queries = ["".join(get_leaves(c)) for c in queries]
            queries = set(queries)

            error_msg = "Sentence {}-th: '{}'. Expect: <{}>/ Actual: <{}>".format(
                i, input_, expect_, queries)
            self.assertEqual(expect_, queries, error_msg)

    def test_get_action_modifiers(self):
        inputs_ = [
            (
                "[question(drs([A,B],[query(A,who)-1/1,predicate(B,move,A)-1/3,modifier_adv(B,slowly,pos)-1/4]))]",
                set([
                    "modifier_adv(B,slowly,pos)",
                ])
            )
        ]
        parser = Lark(grammar_visualization_str, start="conditions")
        for i, (input_, expect_) in enumerate(inputs_):
            result = parser.parse(input_)
            action_modifiers = get_action_modifiers(result)
            action_modifiers = ["".join(get_leaves(c))
                                for c in action_modifiers]
            action_modifiers = set(action_modifiers)

            error_msg = "Sentence {}-th: '{}'. Expect: <{}>/ Actual: <{}>".format(
                i, input_, expect_, action_modifiers)
            self.assertEqual(expect_, action_modifiers, error_msg)

    def test_get_noun_modifiers(self):
        inputs_ = [
            (
                "[=>(drs([A,B,C,D],[object(A,agent,countable,na,eq,1)-1/6,predicate(B,be,named('John'),A)-1/4,object(C,apple,countable,na,eq,1)-1/10,property(C,red,pos)-1/9,predicate(D,throw,named('John'),C)-1/7,modifier_adv(D,slowly,pos)-1/11]),drs([E,F,G,H,I],[object(E,agent,countable,na,eq,1)-1/17,predicate(F,be,named('John'),E)-1/15,object(G,apple,countable,na,eq,1)-1/21,property(G,red,pos)-1/20,object(I,table,countable,na,eq,1)-1/25,predicate(H,throw,named('John'),G)-1/18,modifier_pp(H,under,I)-1/23,modifier_adv(H,slowly,pos)-1/22]))]",
                set([
                    "property(C,red,pos)",
                    "property(G,red,pos)"
                ])
            )
        ]
        parser = Lark(grammar_visualization_str, start="conditions")
        for i, (input_, expect_) in enumerate(inputs_):
            result = parser.parse(input_)
            noun_modifiers = get_noun_modifiers(result)
            noun_modifiers = ["".join(get_leaves(c))
                              for c in noun_modifiers]
            noun_modifiers = set(noun_modifiers)

            error_msg = "Sentence {}-th: '{}'. Expect: <{}>/ Actual: <{}>".format(
                i, input_, expect_, noun_modifiers)
            self.assertEqual(expect_, noun_modifiers, error_msg)

    def test_get_relations(self):
        inputs_ = [
            (
                "[=>(drs([A,B,C],[relation(B,of,C)-1/4,object(B,robot,countable,na,eq,1)-1/3,predicate(A,run,B)-1/7,object(C,company,countable,na,eq,1)-1/6]),drs([D],[predicate(D,run,B)-1/14,modifier_adv(D,slowly,pos)-1/15]))]",
                set([
                    "relation(B,of,C)",
                ])
            )
        ]
        parser = Lark(grammar_visualization_str, start="conditions")
        for i, (input_, expect_) in enumerate(inputs_):
            result = parser.parse(input_)
            relations = get_relations(result)
            relations = ["".join(get_leaves(c))
                         for c in relations]
            relations = set(relations)

            error_msg = "Sentence {}-th: '{}'. Expect: <{}>/ Actual: <{}>".format(
                i, input_, expect_, relations)
            self.assertEqual(expect_, relations, error_msg)

    def test_get_command_conditions(self):
        inputs_ = [
            (
                "[command(drs([A,B,C],[object(C,apple,countable,na,eq,1)-1/5,object(B,table,countable,na,eq,1)-1/8,predicate(A,move,named('Sawyer'),C)-1/3,modifier_adv(A,slowly,pos)-1/9,modifier_pp(A,on,B)-1/6]))]",
                set([
                    "command(drs([A,B,C],[object(C,apple,countable,na,eq,1)-1/5,object(B,table,countable,na,eq,1)-1/8,predicate(A,move,named('Sawyer'),C)-1/3,modifier_adv(A,slowly,pos)-1/9,modifier_pp(A,on,B)-1/6]))",
                ])
            )
        ]
        parser = Lark(grammar_visualization_str, start="conditions")
        for i, (input_, expect_) in enumerate(inputs_):
            result = parser.parse(input_)
            commands = get_command_conditions(result)
            commands = ["".join(get_leaves(c))
                        for c in commands]
            commands = set(commands)

            error_msg = "Sentence {}-th: '{}'. Expect: <{}>/ Actual: <{}>".format(
                i, input_, expect_, commands)
            self.assertEqual(expect_, commands, error_msg)

    def test_get_question_conditions(self):
        inputs_ = [
            (
                "[question(drs([A,B,C,D],[query(A,which)-1/1,object(A,robot,countable,na,eq,1)-1/2,property(D,red,pos)-1/7,object(D,block,countable,na,eq,1)-1/8,property(B,small,comp_than,D)-1/4,predicate(C,be,A,B)-1/3]))]",
                set([
                    "question(drs([A,B,C,D],[query(A,which)-1/1,object(A,robot,countable,na,eq,1)-1/2,property(D,red,pos)-1/7,object(D,block,countable,na,eq,1)-1/8,property(B,small,comp_than,D)-1/4,predicate(C,be,A,B)-1/3]))"

                ])
            )
        ]
        parser = Lark(grammar_visualization_str, start="conditions")
        for i, (input_, expect_) in enumerate(inputs_):
            result = parser.parse(input_)
            questions = get_question_conditions(result)
            questions = ["".join(get_leaves(c))
                         for c in questions]
            questions = set(questions)

            error_msg = "Sentence {}-th: '{}'. Expect: <{}>/ Actual: <{}>".format(
                i, input_, expect_, questions)
            self.assertEqual(expect_, questions, error_msg)

    def test_get_question_conditions(self):
        inputs_ = [
            (
                "[question(drs([A,B,C,D],[query(A,which)-1/1,object(A,robot,countable,na,eq,1)-1/2,property(D,red,pos)-1/7,object(D,block,countable,na,eq,1)-1/8,property(B,small,comp_than,D)-1/4,predicate(C,be,A,B)-1/3]))]",
                set([
                    "question(drs([A,B,C,D],[query(A,which)-1/1,object(A,robot,countable,na,eq,1)-1/2,property(D,red,pos)-1/7,object(D,block,countable,na,eq,1)-1/8,property(B,small,comp_than,D)-1/4,predicate(C,be,A,B)-1/3]))"

                ])
            )
        ]
        parser = Lark(grammar_visualization_str, start="conditions")
        for i, (input_, expect_) in enumerate(inputs_):
            result = parser.parse(input_)
            questions = get_question_conditions(result)
            questions = ["".join(get_leaves(c))
                         for c in questions]
            questions = set(questions)

            error_msg = "Sentence {}-th: '{}'. Expect: <{}>/ Actual: <{}>".format(
                i, input_, expect_, questions)
            self.assertEqual(expect_, questions, error_msg)

    def test_get_possibility_conditions(self):
        inputs_ = [
            (
                "[object(A,robot,countable,na,eq,1)-1/2,can(drs([B,C],[object(B,apple,countable,na,eq,1)-1/7,property(B,red,pos)-1/6,predicate(C,throw,A,B)-1/4,modifier_adv(C,slowly,pos)-1/8]))]",
                set([
                    "can(drs([B,C],[object(B,apple,countable,na,eq,1)-1/7,property(B,red,pos)-1/6,predicate(C,throw,A,B)-1/4,modifier_adv(C,slowly,pos)-1/8]))"
                ])
            )
        ]
        parser = Lark(grammar_visualization_str, start="conditions")
        for i, (input_, expect_) in enumerate(inputs_):
            result = parser.parse(input_)
            possibilities = get_possibility_conditions(result)
            possibilities = ["".join(get_leaves(c))
                             for c in possibilities]
            possibilities = set(possibilities)

            error_msg = "Sentence {}-th: '{}'. Expect: <{}>/ Actual: <{}>".format(
                i, input_, expect_, possibilities)
            self.assertEqual(expect_, possibilities, error_msg)

    def test_types(self):
        inputs_ = [
            (
                "drs([A,B],[object(A,robot,countable,na,eq,1)-1/2,predicate(B,run,A)-1/3])",
                is_descriptive_type
            ),
            (
                "drs([A,B],[object(A,robot,countable,na,eq,1)-1/2,predicate(B,run,A)-1/3,modifier_adv(B,slowly,pos)-1/4])",
                is_descriptive_type
            ),
            (
                "drs([A,B],[object(A,apple,countable,na,eq,1)-1/4,predicate(B,throw,named('John'),A)-1/2])",
                is_descriptive_type
            ),
            (
                "drs([A,B],[object(A,apple,countable,na,eq,1)-1/4,predicate(B,throw,named('John'),A)-1/2,modifier_adv(B,slowly,pos)-1/5])",
                is_descriptive_type
            ),
            (
                "drs([A,B,C],[object(A,robot,countable,na,eq,1)-1/3,property(A,small,pos)-1/2,object(B,apple,countable,na,eq,1)-1/6,predicate(C,throw,A,B)-1/4,modifier_adv(C,slowly,pos)-1/7])",
                is_descriptive_type
            ),
            (
                "drs([A,B,C],[object(A,robot,countable,na,eq,1)-1/3,property(A,small,pos)-1/2,object(B,apple,countable,na,eq,1)-1/7,property(B,red,pos)-1/6,predicate(C,throw,A,B)-1/4,modifier_adv(C,slowly,pos)-1/8])",
                is_descriptive_type
            ),
            (
                "drs([A,B,C],[object(A,robot,countable,na,eq,1)-1/5,property(A,small,pos)-1/2,property(A,green,pos)-1/4,object(B,apple,countable,na,eq,1)-1/8,predicate(C,throw,A,B)-1/6])",
                is_descriptive_type
            ),
            (
                "drs([A,B,C],[relation(A,of,named('John'))-1/2,object(A,robot,countable,na,eq,1)-1/4,object(B,apple,countable,na,eq,1)-1/7,predicate(C,throw,A,B)-1/5])",
                is_descriptive_type
            ),
            (
                "drs([A,B,C],[relation(A,of,named('John'))-1/2,object(A,robot,countable,na,eq,1)-1/4,object(B,apple,countable,na,eq,1)-1/7,predicate(C,throw,A,B)-1/5,modifier_adv(C,slowly,pos)-1/8])",
                is_descriptive_type
            ),
            (
                "drs([A,B,C],[relation(B,of,C)-1/3,object(B,robot,countable,na,eq,1)-1/2,predicate(A,run,B)-1/6,object(C,company,countable,na,eq,1)-1/5])",
                is_descriptive_type
            ),
            (
                "drs([A,B,C],[relation(B,of,C)-1/3,object(B,robot,countable,na,eq,1)-1/2,predicate(A,run,B)-1/6,modifier_adv(A,slowly,pos)-1/7,object(C,company,countable,na,eq,1)-1/5])",
                is_descriptive_type
            ),
            (
                "drs([A,B,C,D,E,F],[predicate(F,be,D,E)-1/4,object(E,agent,countable,na,eq,1)-1/6,object(D,robot,countable,na,eq,1)-1/2,object(A,apple,countable,na,eq,1)-1/10,property(A,red,pos)-1/9,object(C,table,countable,na,eq,1)-1/14,predicate(B,throw,D,A)-1/7,modifier_pp(B,under,C)-1/12,modifier_adv(B,slowly,pos)-1/11])",
                is_descriptive_type
            ),
            (
                "drs([A,B,C,D],[predicate(D,be,B,C)-1/4,object(C,agent,countable,na,eq,1)-1/6,object(B,robot,countable,na,eq,1)-1/2,predicate(A,move,B)-1/7,modifier_adv(A,slowly,pos)-1/8])",
                is_descriptive_type
            ),
            (
                "drs([A,B,C,D],[object(A,agent,countable,na,eq,1)-1/5,predicate(B,be,named('John'),A)-1/3,object(C,apple,countable,na,eq,1)-1/9,property(C,red,pos)-1/8,predicate(D,throw,named('John'),C)-1/6,modifier_adv(D,slowly,pos)-1/10])",
                is_descriptive_type
            ),
            (
                "drs([A,B,C,D,E],[object(A,agent,countable,na,eq,1)-1/5,predicate(B,be,named('John'),A)-1/3,object(C,apple,countable,na,eq,1)-1/9,property(C,red,pos)-1/8,object(E,table,countable,na,eq,1)-1/13,predicate(D,throw,named('John'),C)-1/6,modifier_pp(D,under,E)-1/11,modifier_adv(D,slowly,pos)-1/10])",
                is_descriptive_type
            ),
            (
                "drs([A,B,C],[object(C,robot,countable,na,eq,1)-1/2,object(A,apple,countable,kg,eq,3)-1/7,predicate(B,throw,C,A)-1/3,modifier_adv(B,slowly,pos)-1/8])",
                is_descriptive_type
            ),
            (
                "drs([A,B,C],[object(C,robot,countable,na,eq,1)-1/2,object(A,apple,countable,kg,eq,3)-1/8,property(A,red,pos)-1/7,predicate(B,throw,C,A)-1/3,modifier_adv(B,slowly,pos)-1/9])",
                is_descriptive_type
            ),
            (
                "drs([A,B,C],[object(C,robot,countable,na,eq,1)-1/2,object(A,metal,countable,pound,eq,3)-1/7,predicate(B,be,C,A)-1/3])",
                is_descriptive_type
            ),
            (
                "drs([A],[object(A,robot,countable,na,eq,1)-1/2,can(drs([B,C],[object(B,apple,countable,na,eq,1)-1/7,property(B,red,pos)-1/6,predicate(C,throw,A,B)-1/4,modifier_adv(C,slowly,pos)-1/8]))])",
                is_possibility_type
            ),
            (
                "drs([A],[object(A,robot,countable,na,eq,1)-1/2,can(drs([B,C,D],[object(B,apple,countable,na,eq,1)-1/7,property(B,red,pos)-1/6,object(D,table,countable,na,eq,1)-1/11,predicate(C,throw,A,B)-1/4,modifier_pp(C,under,D)-1/9,modifier_adv(C,slowly,pos)-1/8]))])",
                is_possibility_type
            ),
            (
                "drs([],[-(drs([A],[object(A,apple,countable,na,eq,1)-1/4]))])",
                is_descriptive_type
            ),
            (
                "drs([],[question(drs([A,B,C,D],[object(D,apple,countable,na,eq,1)-1/3,property(C,red,pos)-1/7,object(C,box,countable,na,eq,1)-1/8,property(A,small,comp_than,C)-1/4,predicate(B,be,D,A)-1/1]))])",
                is_question_type
            ),
            (
                "drs([],[question(drs([A,B,C,D],[object(D,apple,countable,na,eq,1)-1/3,property(C,red,pos)-1/8,object(C,box,countable,na,eq,1)-1/9,property(A,small,comp_than,C)-1/5,predicate(B,be,D,A)-1/1]))])",
                is_question_type
            ),
            (
                "drs([],[question(drs([A,B,C],[object(C,apple,countable,na,eq,1)-1/3,object(A,agent,countable,na,eq,1)-1/5,predicate(B,be,C,A)-1/1]))])",
                is_question_type
            ),
            (
                "drs([],[question(drs([A,B],[object(A,agent,countable,na,eq,1)-1/4,predicate(B,be,named('John'),A)-1/1]))])",
                is_question_type
            ),
            (
                "drs([],[question(drs([A,B],[query(A,who)-1/1,predicate(B,move,A)-1/3,modifier_adv(B,slowly,pos)-1/4]))])",
                is_question_type
            ),
            (
                "drs([],[question(drs([A,B],[query(A,who)-1/1,modifier_adv(B,slowly,pos)-1/3,predicate(B,move,A)-1/4]))])",
                is_question_type
            ),
            (
                "drs([],[question(drs([A,B,C,D],[query(A,who)-1/1,property(D,red,pos)-1/7,object(D,block,countable,na,eq,1)-1/8,property(B,small,pos_as,D)-1/4,predicate(C,be,A,B)-1/2]))])",
                is_question_type
            ),
            (
                "drs([],[question(drs([A,B,C,D],[query(A,who)-1/1,property(D,red,pos)-1/6,object(D,block,countable,na,eq,1)-1/7,property(B,small,comp_than,D)-1/3,predicate(C,be,A,B)-1/2]))])",
                is_question_type
            ),
            (
                "drs([],[question(drs([A,B,C],[query(A,who)-1/1,property(C,small,sup)-1/4,object(C,agent,countable,na,eq,1)-1/5,predicate(B,be,A,C)-1/2]))])",
                is_question_type
            ),
            (
                "drs([],[question(drs([A,B],[query(A,who)-1/1,predicate(B,be,A,named('John'))-1/2]))])",
                is_question_type
            ),
            (
                "drs([],[question(drs([A,B,C,D],[query(A,which)-1/1,object(A,robot,countable,na,eq,1)-1/2,property(D,red,pos)-1/7,object(D,block,countable,na,eq,1)-1/8,property(B,small,comp_than,D)-1/4,predicate(C,be,A,B)-1/3]))])",
                is_question_type
            ),
            (
                "drs([],[question(drs([A,B,C,D],[query(A,which)-1/1,object(A,robot,countable,na,eq,1)-1/2,property(D,red,pos)-1/8,object(D,block,countable,na,eq,1)-1/9,property(B,small,pos_as,D)-1/5,predicate(C,be,A,B)-1/3]))])",
                is_question_type
            ),
            (
                "drs([],[question(drs([A,B],[query(A,which)-1/1,object(A,robot,countable,na,eq,1)-1/2,predicate(B,be,A,named('John'))-1/3]))])",
                is_question_type
            ),
            (
                "drs([],[command(drs([A,B,C],[object(C,apple,countable,na,eq,1)-1/5,object(B,table,countable,na,eq,1)-1/8,predicate(A,move,named('Sawyer'),C)-1/3,modifier_adv(A,slowly,pos)-1/9,modifier_pp(A,on,B)-1/6]))])",
                is_command_type
            ),
            (
                "drs([],[command(drs([A,B,C],[property(C,red,pos)-1/5,object(C,apple,countable,na,eq,1)-1/6,object(B,table,countable,na,eq,1)-1/9,predicate(A,move,named('Sawyer'),C)-1/3,modifier_pp(A,on,B)-1/7]))])",
                is_command_type
            ),
            (
                "drs([],[command(drs([A,B,C],[property(C,red,pos)-1/5,object(C,apple,countable,na,eq,1)-1/6,object(B,table,countable,na,eq,1)-1/9,predicate(A,move,named('Sawyer'),C)-1/3,modifier_adv(A,slowly,pos)-1/10,modifier_pp(A,on,B)-1/7]))])",
                is_command_type
            ),
            (
                "drs([],[command(drs([A,B,C],[property(C,red,pos)-1/5,object(C,apple,countable,na,eq,1)-1/6,object(B,table,countable,na,eq,1)-1/9,predicate(A,pick,named('Sawyer'),C)-1/3,modifier_adv(A,slowly,pos)-1/10,modifier_pp(A,on,B)-1/7]))])",
                is_command_type
            ),
            (
                "drs([],[command(drs([A,B,C],[property(C,red,pos)-1/5,object(C,apple,countable,na,eq,1)-1/6,object(B,table,countable,na,eq,1)-1/9,predicate(A,grasp,named('Sawyer'),C)-1/3,modifier_adv(A,slowly,pos)-1/10,modifier_pp(A,on,B)-1/7]))])",
                is_command_type
            ),
            (
                "drs([],[=>(drs([A,B,C],[relation(B,of,C)-1/4,object(B,robot,countable,na,eq,1)-1/3,predicate(A,run,B)-1/7,object(C,company,countable,na,eq,1)-1/6]),drs([D],[predicate(D,run,B)-1/14,modifier_adv(D,slowly,pos)-1/15]))])",
                is_descriptive_type
            ),
            (
                "drs([],[=>(drs([A,B,C,D],[relation(C,of,D)-1/4,object(C,robot,countable,na,eq,1)-1/3,object(A,apple,countable,na,eq,1)-1/9,predicate(B,throw,C,A)-1/7,object(D,company,countable,na,eq,1)-1/6]),drs([E,F],[object(E,apple,countable,na,eq,1)-1/18,predicate(F,throw,C,E)-1/16,modifier_adv(F,slowly,pos)-1/19]))])",
                is_descriptive_type
            ),
            (
                "drs([],[=>(drs([A,B,C,D],[relation(C,of,D)-1/4,object(C,robot,countable,na,eq,1)-1/3,object(A,apple,countable,na,eq,1)-1/10,property(A,red,pos)-1/9,predicate(B,throw,C,A)-1/7,modifier_adv(B,slowly,pos)-1/11,object(D,company,countable,na,eq,1)-1/6]),drs([E,F,G],[object(E,apple,countable,na,eq,1)-1/21,property(E,red,pos)-1/20,predicate(F,throw,C,E)-1/18,modifier_pp(F,under,G)-1/23,modifier_adv(F,slowly,pos)-1/22,object(G,table,countable,na,eq,1)-1/25]))])",
                is_descriptive_type
            ),
            (
                "drs([],[=>(drs([A,B,C],[relation(B,of,C)-1/4,object(B,robot,countable,na,eq,1)-1/3,predicate(A,run,B)-1/7,object(C,company,countable,na,eq,1)-1/6]),drs([D],[predicate(D,run,B)-1/14,modifier_adv(D,slowly,pos)-1/15]))])",
                is_descriptive_type
            ),
            (
                "drs([],[=>(drs([A,B,C,D],[relation(C,of,D)-1/4,object(C,robot,countable,na,eq,1)-1/3,object(A,apple,countable,na,eq,1)-1/9,predicate(B,throw,C,A)-1/7,object(D,company,countable,na,eq,1)-1/6]),drs([E,F],[object(E,apple,countable,na,eq,1)-1/18,predicate(F,throw,C,E)-1/16,modifier_adv(F,slowly,pos)-1/19]))])",
                is_descriptive_type
            ),
            (
                "drs([],[=>(drs([A,B,C,D],[relation(C,of,D)-1/4,object(C,robot,countable,na,eq,1)-1/3,object(A,apple,countable,na,eq,1)-1/10,property(A,red,pos)-1/9,predicate(B,throw,C,A)-1/7,modifier_adv(B,slowly,pos)-1/11,object(D,company,countable,na,eq,1)-1/6]),drs([E,F,G],[object(E,apple,countable,na,eq,1)-1/21,property(E,red,pos)-1/20,predicate(F,throw,C,E)-1/18,modifier_pp(F,under,G)-1/23,modifier_adv(F,slowly,pos)-1/22,object(G,table,countable,na,eq,1)-1/25]))])",
                is_descriptive_type
            ),
            (
                "drs([],[=>(drs([A,B,C],[object(A,agent,countable,na,eq,1)-1/6,predicate(B,be,named('John'),A)-1/4,predicate(C,run,named('John'))-1/7]),drs([D,E,F],[object(D,agent,countable,na,eq,1)-1/13,predicate(E,be,named('John'),D)-1/11,predicate(F,run,named('John'))-1/14,modifier_adv(F,slowly,pos)-1/15]))])",
                is_descriptive_type
            ),
            (
                "drs([],[=>(drs([A,B,C,D],[object(A,agent,countable,na,eq,1)-1/6,predicate(B,be,named('John'),A)-1/4,object(C,apple,countable,na,eq,1)-1/9,predicate(D,throw,named('John'),C)-1/7]),drs([E,F,G,H],[object(E,agent,countable,na,eq,1)-1/15,predicate(F,be,named('John'),E)-1/13,object(G,apple,countable,na,eq,1)-1/18,predicate(H,throw,named('John'),G)-1/16,modifier_adv(H,slowly,pos)-1/19]))])",
                is_descriptive_type
            ),
            (
                "drs([],[=>(drs([A,B,C,D],[object(A,agent,countable,na,eq,1)-1/6,predicate(B,be,named('John'),A)-1/4,object(C,apple,countable,na,eq,1)-1/10,property(C,red,pos)-1/9,predicate(D,throw,named('John'),C)-1/7,modifier_adv(D,slowly,pos)-1/11]),drs([E,F,G,H,I],[object(E,agent,countable,na,eq,1)-1/17,predicate(F,be,named('John'),E)-1/15,object(G,apple,countable,na,eq,1)-1/21,property(G,red,pos)-1/20,object(I,table,countable,na,eq,1)-1/25,predicate(H,throw,named('John'),G)-1/18,modifier_pp(H,under,I)-1/23,modifier_adv(H,slowly,pos)-1/22]))])",
                is_descriptive_type
            ),
            (
                "drs([],[v(drs([A,B],[object(A,robot,countable,na,eq,1)-1/3,property(A,small,pos)-1/2,predicate(B,run,A)-1/4]),drs([C,D],[object(C,robot,countable,na,eq,1)-1/8,property(C,small,pos)-1/7,predicate(D,run,C)-1/9,modifier_adv(D,slowly,pos)-1/10]))])",
                is_descriptive_type
            ),
            (
                "drs([],[v(drs([A,B,C],[object(A,robot,countable,na,eq,1)-1/3,property(A,small,pos)-1/2,object(B,apple,countable,na,eq,1)-1/6,predicate(C,throw,A,B)-1/4]),drs([D,E,F],[object(D,robot,countable,na,eq,1)-1/10,property(D,small,pos)-1/9,object(E,apple,countable,na,eq,1)-1/13,predicate(F,throw,D,E)-1/11,modifier_adv(F,slowly,pos)-1/14]))])",
                is_descriptive_type
            ),
            (
                "drs([],[v(drs([A,B,C],[object(A,robot,countable,na,eq,1)-1/3,property(A,small,pos)-1/2,object(B,apple,countable,na,eq,1)-1/7,property(B,red,pos)-1/6,predicate(C,throw,A,B)-1/4,modifier_adv(C,slowly,pos)-1/8]),drs([D,E,F,G],[object(D,robot,countable,na,eq,1)-1/12,property(D,small,pos)-1/11,object(E,apple,countable,na,eq,1)-1/16,property(E,red,pos)-1/15,object(G,table,countable,na,eq,1)-1/20,predicate(F,throw,D,E)-1/13,modifier_pp(F,under,G)-1/18,modifier_adv(F,slowly,pos)-1/17]))])",
                is_descriptive_type
            ),
            (
                "drs([],[v(drs([A,B],[object(A,robot,countable,na,eq,1)-1/3,property(A,small,pos)-1/2,predicate(B,run,A)-1/4]),drs([C],[object(C,apple,countable,na,eq,1)-1/9]))])",
                is_descriptive_type
            ),
            (
                "drs([],[v(drs([A,B,C],[object(A,robot,countable,na,eq,1)-1/3,property(A,small,pos)-1/2,object(B,apple,countable,na,eq,1)-1/6,predicate(C,throw,A,B)-1/4]),drs([D],[object(D,apple,countable,na,eq,1)-1/11]))])",
                is_descriptive_type
            ),
            (
                "drs([],[v(drs([A,B,C],[object(A,robot,countable,na,eq,1)-1/3,property(A,small,pos)-1/2,object(B,apple,countable,na,eq,1)-1/7,property(B,red,pos)-1/6,predicate(C,throw,A,B)-1/4,modifier_adv(C,slowly,pos)-1/8]),drs([D],[object(D,apple,countable,na,eq,3)-1/13]))])",
                is_descriptive_type
            ),
        ]
        parser = Lark(grammar_visualization_str, start="drs_root")
        for i, (input_, type_function_) in enumerate(inputs_):
            result = parser.parse(input_)

            error_msg = "Sentence {}-th: '{}' with type <{}>. Expect: <{}>".format(
                i, input_, type_function_.__name__, "True")
            is_correct_type = type_function_(result)
            self.assertTrue(is_correct_type, error_msg)


class Test_Information_Extraction_For_Predicate_Type(unittest.TestCase):
    def test_get_main_predicate(self):
        inputs_ = [
            (
                "drs([A,B],[object(A,robot,countable,na,eq,1)-1/2,predicate(B,run,A)-1/3])",
                set([
                    "predicate(B,run,A)"
                ])
            )
        ]
        parser = Lark(grammar_visualization_str, start="drs_root")
        for i, (input_, expect_) in enumerate(inputs_):
            result = parser.parse(input_)
            main_predicates = get_main_predicate(result)
            main_predicates = ["".join(get_leaves(c))
                               for c in main_predicates]
            main_predicates = set(main_predicates)

            error_msg = "Sentence {}-th: '{}'. Expect: <{}>/ Actual: <{}>".format(
                i, input_, expect_, main_predicates)
            self.assertEqual(expect_, main_predicates, error_msg)

    def test_get_subject_from_predicate(self):
        inputs_ = [
            (
                "predicate(B,run,A)",
                set([
                    "A"
                ])
            )
        ]
        parser = Lark(grammar_visualization_str, start="predicate_condition")
        for i, (input_, expect_) in enumerate(inputs_):
            result = parser.parse(input_)
            subject = get_subject_from_predicate(result)
            subject = ["".join(get_leaves(c))
                       for c in subject]
            subject = set(subject)

            error_msg = "Sentence {}-th: '{}'. Expect: <{}>/ Actual: <{}>".format(
                i, input_, expect_, subject)
            self.assertEqual(expect_, subject, error_msg)

    def test_get_first_object_from_predicate(self):
        inputs_ = [
            (
                "predicate(B,run,A)",
                set([

                ])
            ),
            (
                "predicate(D,throw,named('John'),C)",
                set([
                    "C"
                ])
            ),
            (
                "predicate(A,move,named('Sawyer'),C)",
                set([
                    "C"
                ])
            )
        ]
        parser = Lark(grammar_visualization_str, start="predicate_condition")
        for i, (input_, expect_) in enumerate(inputs_):
            result = parser.parse(input_)
            first_object = get_first_object_from_predicate(result)
            first_object = ["".join(get_leaves(c))
                            for c in first_object]
            first_object = set(first_object)

            error_msg = "Sentence {}-th: '{}'. Expect: <{}>/ Actual: <{}>".format(
                i, input_, expect_, first_object)
            self.assertEqual(expect_, first_object, error_msg)

    def test_get_second_object_from_predicate(self):
        inputs_ = [
            (
                "predicate(B,run,A,B,C)",
                set([
                    "C"
                ])
            ),
            (
                "predicate(D,throw,named('John'),C,named('Bob'))",
                set([
                    "named('Bob')"
                ])
            ),

        ]
        parser = Lark(grammar_visualization_str, start="predicate_condition")
        for i, (input_, expect_) in enumerate(inputs_):
            result = parser.parse(input_)
            second_object = get_second_object_from_predicate(result)
            second_object = ["".join(get_leaves(c))
                             for c in second_object]
            second_object = set(second_object)

            error_msg = "Sentence {}-th: '{}'. Expect: <{}>/ Actual: <{}>".format(
                i, input_, expect_, second_object)
            self.assertEqual(expect_, second_object, error_msg)

    def test_get_lexical_from_predicate(self):
        inputs_ = [
            (
                "predicate(B,run,A,B,C)",
                set([
                    "run"
                ])
            ),
            (
                "predicate(D,throw,named('John'),C,named('Bob'))",
                set([
                    "throw"
                ])
            ),

        ]
        parser = Lark(grammar_visualization_str, start="predicate_condition")
        for i, (input_, expect_) in enumerate(inputs_):
            result = parser.parse(input_)
            lexical_of_main_predicate = get_lexical_from_predicate(result)
            lexical_of_main_predicate = ["".join(get_leaves(c))
                                         for c in lexical_of_main_predicate]
            lexical_of_main_predicate = set(lexical_of_main_predicate)

            error_msg = "Sentence {}-th: '{}'. Expect: <{}>/ Actual: <{}>".format(
                i, input_, expect_, lexical_of_main_predicate)
            self.assertEqual(expect_, lexical_of_main_predicate, error_msg)

    def test_get_object_conditions_having_variable_x(self):
        inputs_ = [
            (
                "drs([A,B,C],[object(C,apple,countable,na,eq,1)-1/5,object(B,table,countable,na,eq,1)-1/8,predicate(A,move,named('Sawyer'),C)-1/3,modifier_adv(A,slowly,pos)-1/9,modifier_pp(A,on,B)-1/6])",
                "C",
                set([
                    "object(C,apple,countable,na,eq,1)"
                ])
            ),
            (
                "drs([A,B,C],[object(C,apple,countable,na,eq,1)-1/5,object(B,table,countable,na,eq,1)-1/8,predicate(A,move,named('Sawyer'),C)-1/3,modifier_adv(A,slowly,pos)-1/9,modifier_pp(A,on,B)-1/6])",
                "B",
                set([
                    "object(B,table,countable,na,eq,1)"
                ])
            ),

        ]
        parser = Lark(grammar_visualization_str, start="drs_root")
        for i, (input_, variable_, expect_) in enumerate(inputs_):
            result = parser.parse(input_)

            object_conditions = get_object_conditions_having_variable_x(
                result, variable_)
            object_conditions = ["".join(get_leaves(c))
                                 for c in object_conditions]
            object_conditions = set(object_conditions)

            error_msg = "Sentence {}-th: '{}'. Expect: <{}>/ Actual: <{}>".format(
                i, input_, expect_, object_conditions)
            self.assertEqual(expect_, object_conditions, error_msg)

    def test_get_object_conditions_information_having_variable_x(self):
        inputs_ = [
            (
                "drs([A,B,C],[object(C,apple,countable,na,eq,1)-1/5,object(B,table,countable,na,eq,1)-1/8,predicate(A,move,named('Sawyer'),C)-1/3,modifier_adv(A,slowly,pos)-1/9,modifier_pp(A,on,B)-1/6])",
                "C",
                set([
                    "apple"
                ])
            ),
            (
                "drs([A,B,C],[object(C,apple,countable,na,eq,1)-1/5,object(B,table,countable,na,eq,1)-1/8,predicate(A,move,named('Sawyer'),C)-1/3,modifier_adv(A,slowly,pos)-1/9,modifier_pp(A,on,B)-1/6])",
                "B",
                set([
                    "table"
                ])
            ),

        ]
        parser = Lark(grammar_visualization_str, start="drs_root")
        for i, (input_, variable_, expect_) in enumerate(inputs_):
            result = parser.parse(input_)

            object_lexical = get_object_conditions_information_having_variable_x(
                result, variable_)
            object_lexical = ["".join(get_leaves(c))
                              for c in object_lexical]
            object_lexical = set(object_lexical)

            error_msg = "Sentence {}-th: '{}'. Expect: <{}>/ Actual: <{}>".format(
                i, input_, expect_, object_lexical)
            self.assertEqual(expect_, object_lexical, error_msg)

    def test_get_action_modifiers_having_variable_x(self):
        inputs_ = [
            (
                "drs([A,B,C],[object(C,apple,countable,na,eq,1)-1/5,object(B,table,countable,na,eq,1)-1/8,predicate(A,move,named('Sawyer'),C)-1/3,modifier_adv(A,slowly,pos)-1/9,modifier_pp(A,on,B)-1/6])",
                "A",
                set([
                    "modifier_adv(A,slowly,pos)"
                ])
            ),
            (
                "drs([A,B,C],[object(C,apple,countable,na,eq,1)-1/5,object(B,table,countable,na,eq,1)-1/8,predicate(A,move,named('Sawyer'),C)-1/3,modifier_adv(A,slowly,pos)-1/9,modifier_pp(A,on,B)-1/6])",
                "A",
                set([
                    "modifier_adv(A,slowly,pos)"
                ])
            ),
            (
                "drs([A,B,C],[object(C,apple,countable,na,eq,1)-1/5,object(B,table,countable,na,eq,1)-1/8,predicate(A,move,named('Sawyer'),C)-1/3,modifier_adv(A,slowly,pos)-1/9,modifier_pp(A,on,B)-1/6])",
                "B",
                set([

                ])
            ),

        ]
        parser = Lark(grammar_visualization_str, start="drs_root")
        for i, (input_, variable_, expect_) in enumerate(inputs_):
            result = parser.parse(input_)

            adverbs = get_action_adverbs_having_variable_x(
                result, variable_)
            adverbs = ["".join(get_leaves(c))
                       for c in adverbs]
            adverbs = set(adverbs)

            error_msg = "Sentence {}-th: '{}'. Expect: <{}>/ Actual: <{}>".format(
                i, input_, expect_, adverbs)
            self.assertEqual(expect_, adverbs, error_msg)

    def test_get_action_adverbs_information_having_variable_x(self):
        inputs_ = [
            (
                "drs([A,B,C],[object(C,apple,countable,na,eq,1)-1/5,object(B,table,countable,na,eq,1)-1/8,predicate(A,move,named('Sawyer'),C)-1/3,modifier_adv(A,slowly,pos)-1/9,modifier_pp(A,on,B)-1/6])",
                "A",
                set([
                    "slowly"
                ])
            ),
            (
                "drs([A,B,C],[object(C,apple,countable,na,eq,1)-1/5,object(B,table,countable,na,eq,1)-1/8,predicate(A,move,named('Sawyer'),C)-1/3,modifier_adv(A,slowly,pos)-1/9,modifier_pp(A,on,B)-1/6])",
                "B",
                set([

                ])
            ),

        ]
        parser = Lark(grammar_visualization_str, start="drs_root")
        for i, (input_, variable_, expect_) in enumerate(inputs_):
            result = parser.parse(input_)

            adverbs = get_action_adverbs_information_having_variable_x(
                result, variable_)
            adverbs = set(adverbs)

            error_msg = "Sentence {}-th: '{}'. Expect: <{}>/ Actual: <{}>".format(
                i, input_, expect_, adverbs)
            self.assertEqual(expect_, adverbs, error_msg)

    def test_who_do_what_how(self):
        inputs_ = [
            (
                "drs([],[command(drs([A,B,C],[object(C,apple,countable,na,eq,1)-1/5,object(B,table,countable,na,eq,1)-1/8,predicate(A,move,named('Sawyer'),C)-1/3,modifier_adv(A,slowly,pos)-1/9,modifier_pp(A,on,B)-1/6]))])",
                ("Sawyer", "move", "apple")
            ),
            (
                "drs([],[command(drs([A,B,C],[property(C,red,pos)-1/5,object(C,apple,countable,na,eq,1)-1/6,object(B,table,countable,na,eq,1)-1/9,predicate(A,move,E,C)-1/3,modifier_pp(A,on,B)-1/7,object(E,apple,countable,na,eq,1)-1/6]))])",
                ("apple", "move", "apple")
            ),

        ]
        parser = Lark(grammar_visualization_str, start="drs_root")
        for i, (input_, expect_) in enumerate(inputs_):
            result = parser.parse(input_)

            result_tuple = who_do_what(result)

            error_msg = "Sentence {}-th: '{}'. Expect: <{}>/ Actual: <{}>".format(
                i, input_, expect_, result_tuple)
            self.assertEqual(expect_, result_tuple, error_msg)

    def test_who_do_what_how(self):
        inputs_ = [
            (
                "drs([],[command(drs([A,B,C],[object(C,apple,countable,na,eq,1)-1/5,object(B,table,countable,na,eq,1)-1/8,predicate(A,move,named('Sawyer'),C)-1/3,modifier_adv(A,slowly,pos)-1/9,modifier_pp(A,on,B)-1/6]))])",
                ("Sawyer", "move", "apple", None, "slowly")
            ),
            (
                "drs([],[command(drs([A,B,C],[property(C,red,pos)-1/5,object(C,apple,countable,na,eq,1)-1/6,object(B,table,countable,na,eq,1)-1/9,predicate(A,move,E,C)-1/3,modifier_pp(A,on,B)-1/7,object(E,apple,countable,na,eq,1)-1/6]))])",
                ("apple", "move", "apple", None, None)
            ),

        ]
        parser = Lark(grammar_visualization_str, start="drs_root")
        for i, (input_, expect_) in enumerate(inputs_):
            result = parser.parse(input_)

            result_tuple = who_do_what_how(result)

            error_msg = "Sentence {}-th: '{}'. Expect: <{}>/ Actual: <{}>".format(
                i, input_, expect_, result_tuple)
            self.assertEqual(expect_, result_tuple, error_msg)


if __name__ == '__main__':
    unittest.main()
