import sys
from pathlib import Path
workspace_directory = Path(Path(__file__).parent.parent.parent)
sys.path.insert(0, str(workspace_directory))


import unittest
from scripts.drs import (
    grammar_visualization_str,
    translate,
    visualizable_str,
    visualize,
    get_leaves,
    get_references,
    get_entities,
    get_valid_lexical,
    get_cname
)
from lark import Lark


class Test_functional_methods(unittest.TestCase):
    def test_translate(self):
        inputs_ = [
            "drs([],[=>(drs([A,B,C,D],[object(A,agent,countable,na,eq,1)-1/6,predicate(B,be,named('John'),A)-1/4,object(C,apple,countable,na,eq,1)-1/10,property(C,red,pos)-1/9,predicate(D,throw,named('John'),C)-1/7,modifier_adv(D,slowly,pos)-1/11]),drs([E,F,G,H,I],[object(E,agent,countable,na,eq,1)-1/17,predicate(F,be,named('John'),E)-1/15,object(G,apple,countable,na,eq,1)-1/21,property(G,red,pos)-1/20,object(I,table,countable,na,eq,1)-1/25,predicate(H,throw,named('John'),G)-1/18,modifier_pp(H,under,I)-1/23,modifier_adv(H,slowly,pos)-1/22]))])",
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
        parser = Lark(grammar_visualization_str,
                      start="drs_root")
        for i, input_ in enumerate(inputs_):
            try:
                result = parser.parse(input_)
                drs_visualizable_str = visualizable_str(result)
            except:
                error_msg = "Sentence {}-th is in valid: {}".format(i, input_)
                self.fail(error_msg)


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


if __name__ == '__main__':
    unittest.main()
