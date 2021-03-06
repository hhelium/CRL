import sys
from pathlib import Path
workspace_directory = Path(Path(__file__).parent.parent.parent)
sys.path.insert(0, str(workspace_directory))

from scripts.crl.crl_grammar import (
    dynamic_crl_grammar
)

from scripts.crl.syntactic_parser import (
    BottomUpChartParser
)

from nltk import (
    word_tokenize
)

import unittest


class Test_Syntactic_Parser(unittest.TestCase):
    def test_parser(self):
        inputs_ = [
            "A robot runs.",
            "A robot runs slowly.",
            "A robot throws an apple.",
            "A robot throws an apple slowly.",
            "A robot throws an red apple slowly.",
            "A robot throws an small and red apple slowly.",
            "A robot throws an small and red apple slowly under the table.",
            "A robot under the table throws  an small and red apple slowly .",
            "A robot moves slowly.",
            "The robot can capture the red apple on the table.",

            "John runs.",
            "John runs slowly.",
            "John throws an apple.",
            "John throws an apple slowly.",
            "John throws an red apple slowly.",
            "John throws an red apple slowly under the table.",
            "John moves slowly.",


            "She runs.",
            "She runs slowly.",
            "She throws an apple.",
            "She throws an apple slowly.",
            "She throws an red apple slowly.",
            "She throws an red apple slowly under the table.",
            "She moves slowly.",


            "A small robot runs.",
            "A small robot runs slowly.",
            "A small robot throws an apple.",
            "A small robot throws an apple slowly.",
            "A small robot throws an red apple slowly.",
            "A small robot throws an red apple slowly under the table.",
            "A small robot moves slowly.",

            "A small and green robot runs.",
            "A small and green robot runs slowly.",
            "A small and green robot throws an apple.",
            "A small and green robot throws an apple slowly.",
            "A small and green robot throws an red apple slowly.",
            "A small and green robot throws an red apple slowly under the table.",
            "A small and green robot moves slowly.",

            "John 's robot runs.",
            "John 's robot runs slowly.",
            "John 's robot throws an apple.",
            "John 's robot throws an apple slowly.",
            "John 's robot throws an red apple slowly.",
            "John 's robot throws an red apple slowly under the table.",
            "John 's robot moves slowly.",


            "John 's small robot runs.",
            "John 's small robot runs slowly.",
            "John 's small robot throws an apple.",
            "John 's small robot throws an apple slowly.",
            "John 's small robot throws an red apple slowly.",
            "John 's small robot throws an red apple slowly under the table.",
            "John 's small robot moves slowly.",


            "The company 's robot runs.",
            "The company 's robot runs slowly.",
            "The company 's robot throws an apple.",
            "The company 's robot throws an apple slowly.",
            "The company 's robot throws an red apple slowly.",
            "The company 's robot throws an red apple slowly under the table.",
            "The company 's robot moves slowly.",


            "The robot of the company runs.",
            "The robot of the company runs slowly.",
            "The robot of the company throws an apple.",
            "The robot of the company throws an apple slowly.",
            "The robot of the company throws an red apple slowly.",
            "The robot of the company throws an red apple slowly under the table.",
            "The robot of the company moves slowly.",


            "The robot of company runs.",
            "The robot of company runs slowly.",
            "The robot of company throws an apple.",
            "The robot of company throws an apple slowly.",
            "The robot of company throws an red apple slowly.",
            "The robot of company throws an red apple slowly under the table.",
            "The robot of company moves slowly.",

            "The robot which is an agent runs.",
            "The robot which is an agent runs slowly.",
            "The robot which is an agent throws an apple.",
            "The robot which is an agent throws an apple slowly.",
            "The robot which is an agent throws an red apple slowly.",
            "The robot which is an agent throws an red apple slowly under the table.",
            "The robot which is an agent moves slowly.",


            "John who is an agent runs.",
            "John who is an agent runs slowly.",
            "John who is an agent throws an apple.",
            "John who is an agent throws an apple slowly.",
            "John who is an agent throws an red apple slowly.",
            "John who is an agent throws an red apple slowly under the table.",
            "John who is an agent moves slowly.",



            "The robot runs.",
            "The robot runs slowly.",
            "The robot throws 3 kg of apple.",
            "The robot throws 3 kg of apple slowly.",
            "The robot throws 3 kg of red apple slowly.",
            "The robot throws 3 kg of red apple slowly under the table.",
            "The robot moves slowly.",


            "The robot is a agent.",
            "The robot is 3 pound.",
            "The robot is 3 pound of metal.",

            "The robot is small.",
            "The robot is small and red.",
            "The robot is as small as the box.",
            "The robot is smaller than the red box.",
            "The robot is more small than the red box.",
            "The robot is much smaller than the red box.",
            "The robot is much more small than the red box.",


            "The robot can run.",
            "The robot should run slowly.",
            "The robot may throw an apple.",
            "The robot might throw an apple slowly.",
            "The robot can throw an red apple slowly.",
            "The robot can throw an red apple slowly under the table.",
            "The robot can move slowly.",


            "The robot can be small.",
            "The robot can be small and red.",
            "The robot can be as small as the box.",
            "The robot can be smaller than the red box.",
            "The robot can be more small than the red box.",
            "The robot can be much smaller than the red box.",
            "The robot can be much more small than the red box.",


            "The robot can be small under the table.",
            "The robot can be small and red under the table.",
            "The robot can be as small as the box under the table.",
            "The robot can be smaller than the red box under the table.",
            "The robot can be more small than the red box under the table.",
            "The robot can be much smaller than the red box under the table.",
            "The robot can be much more small than the red box under the table.",


            "There is an apple.",
            "There is 3 kg of apples.",
            "There is no apple.",
            "There is no apples on the table.",
            "There is no apples under the chair.",

            "Does the robot move?",
            "Does the robot move slowly?",
            "Does the robot  slowly move?",
            "Does the robot run?",
            "Does the robot run slowly?",
            "Does the robot throw 3 kg of apple?",
            "Does the robot throw 3 kg of apple slowly?",
            "Does the robot throw 3 kg of red apple slowly?",
            "Does the robot throw 3 kg of red apple slowly under the table?",
            "Does the robot move slowly?",

            "Is the red apple small?",
            "Is the apple smaller than the red box?",
            "Is the apple more small than the red box?",
            "Is the apple much more small than the red box?",
            "Is the apple as small as the red block?",
            "Is the apple small and red?",

            "Is the apple an agent?",
            "Is John an agent?",
            "Is John an robot?",


            "Who does move?",
            "Who does move slowly?",
            "Who does  slowly move?",
            "Who does run?",
            "Who does run slowly?",
            "Who does throw 3 kg of apple?",
            "Who does throw 3 kg of apple slowly?",
            "Who does throw 3 kg of red apple slowly?",
            "Who does throw 3 kg of red apple slowly under the table?",


            "Who is small?",
            "Who is smart?",
            "Who is small and red?",
            "Who is as small as the red block?",
            "Who is smaller than the red block?",
            "Who is much smaller than the red block?",


            "Who is the robot?",
            "Who is the agent?",
            "Who is the smallest agent?",
            "Who is John?",


            "Which robot does move?",
            "Which robot does move slowly?",
            "Which robot does  slowly move?",
            "Which robot does run?",
            "Which robot does run slowly?",
            "Which robot does throw 3 kg of apple?",
            "Which robot does throw 3 kg of apple slowly?",
            "Which robot does throw 3 kg of red apple slowly?",
            "Which robot does throw 3 kg of red apple slowly under the table?",


            "Which robot is small?",
            "Which robot is small and red?",
            "which robot is smaller than the red block?",
            "which robot is as small as the red block?",

            "which robot is an agent?",
            "which robot is John?",
            "which robot is John 's parent?",


            "Where does the robot move?",
            "Where does the robot slowly run?",
            "Where does the robot under the table run?",
            "Where does the robot throw 3 kg of apple?",
            "Where does the robot slowly throw 3 kg of apple ?",
            "Where does the robot slowly throw 3 kg of red apple ?",
            "Where does the robot slowly under the table throw 3 kg of red apple ?",

            "Where is an apple?",
            "Where is the robot?",


            "How does robot move?",
            "How does robot  slowly move?",
            "How does robot run?",
            "How does robot throw 3 kg of apple?",
            "How does robot slowly throw 3 kg of apple ?",
            "How does robot slowly throw 3 kg of red apple ?",
            "How does robot slowly under the table throw 3 kg of red apple?",


            "How is the robot?",
            "How is the apple?",

            "There are 3 apples.",
            "There are 3 beautiful apples.",
            "There are 3 beautiful and red apples.",
            "The robot moves 3 beautiful and red apples.",

            "A robot runs or hides.",
            "A robot runs slowly or hides.",
            "A robot throws an apple or hides.",
            "A robot throws an apple slowly or hides.",
            "A robot throws an red apple slowly or moves an beer.",
            "A robot under the table throws an small and red apple slowly or moves an beer .",


            "A robot runs and hides.",
            "A robot runs slowly and hides.",
            "A robot throws an apple and hides.",
            "A robot throws an apple slowly and hides.",
            "A robot throws an red apple slowly and moves an beer.",
            "A robot under the table throws an small and red apple slowly and moves an beer .",


            "if a robot runs then a robot runs slowly.",
            "if a robot throws an apple then a robot throws an apple slowly.",
            "if a robot throws an red apple slowly then a robot throws an small and red apple slowly.",
            "if a robot throws an small and red apple slowly under the table then a robot under the table throws an small and red apple slowly .",
            "if a robot moves slowly then the robot can capture the red apple on the table.",

            "if John runs then John runs slowly.",
            "if John throws an apple then John throws an apple slowly.",
            "if John throws an red apple slowly then John throws an red apple slowly under the table.",


            "if a small robot runs then a small robot runs slowly.",
            "if a small robot throws an apple then a small robot throws an apple slowly.",
            "if a small robot throws an red apple slowly then a small robot throws an red apple slowly under the table.",


            "if a small and green robot runs then a small and green robot runs slowly.",
            "if a small and green robot throws an apple then a small and green robot throws an apple slowly.",
            "if a small and green robot throws an red apple slowly then a small and green robot throws an red apple slowly under the table.",


            "if John 's robot runs then John 's robot runs slowly.",
            "if John 's robot throws an apple then John 's robot throws an apple slowly.",
            "if John 's robot throws an red apple slowly then John 's robot throws an red apple slowly under the table.",

            "if John 's small robot runs then John 's small robot runs slowly.",
            "if John 's small robot throws an apple then John 's small robot throws an apple slowly.",
            "if John 's small robot throws an red apple slowly then John 's small robot throws an red apple slowly under the table.",


            "if the robot of the company runs then the robot of the company runs slowly.",
            "if the robot of the company throws an apple then the robot of the company throws an apple slowly.",
            "if the robot of the company throws an red apple slowly then the robot of the company throws an red apple slowly under the table.",


            "if the robot of the company runs then the robot of the company runs slowly.",
            "if the robot of the company throws an apple then the robot of the company throws an apple slowly.",
            "if the robot of the company throws an red apple slowly then the robot of the company throws an red apple slowly under the table.",

            "if the robot who is an agent runs then the robot who is an agent runs slowly.",
            "if the robot who is an agent throws an apple then the robot who is an agent throws an apple slowly.",
            "if the robot who is an agent throws an red apple slowly then the robot who is an agent throws an red apple slowly under the table.",


            "if John who is an agent runs then John who is an agent runs slowly.",
            "if John who is an agent throws an apple then John who is an agent throws an apple slowly.",
            "if John who is an agent throws an red apple slowly then John who is an agent throws an red apple slowly under the table.",


            "if the robot runs then the robot runs slowly.",
            "if the robot throws 3 kg of apples then the robot throws 3 kg of apples slowly.",
            "if the robot throws 3 kg of red apples slowly then the robot throws 3 kg of red apples slowly under the table.",


            "if the robot is a agent then the robot is 3 pound.",
            "if the robot is 3 pound of metal then the robot runs.",

            "if the robot is small then the robot is small and red.",
            "if the robot is as small as the box then the robot is smaller than the red box.",
            "if the robot is much smaller than the red box then the robot is much more small than the red box.",


            "if the robot can run then the robot should run slowly.",
            "if the robot may throw an apple then the robot might throw an apple slowly.",
            "if the robot can throw an red apple slowly then the robot can throw an red apple slowly under the table.",

            "if there is an apple then there is 3 kg of apples.",
            "if there is no apple then there is no car.",
            "There is no apples under the chair.",


            "if a robot runs or hides then a robot runs slowly or hides.",
            "if a robot throws an apple or hides then a robot throws an apple slowly or hides.",
            "if a robot throws an red apple slowly or moves an beer then a robot under the table throws an small and red apple slowly or moves an beer .",


            "A robot does not run.",
            "A robot does not run slowly.",
            "A robot does not throw an apple.",
            "A robot does not throw an apple slowly.",
            "A robot does not throw an red apple slowly.",
            "A robot does not throw an small and red apple slowly.",
            "A robot does not throw an small and red apple slowly under the table.",
            "A robot does not under the table throw  an small and red apple slowly .",


            "The robot is not small.",
            "The robot is not small and red.",
            "The robot is not as small as the box.",
            "The robot is not smaller than the red box.",
            "The robot is not more small than the red box.",
            "The robot is not much smaller than the red box.",
            "The robot is not much more small than the red box.",

            "The robot can not capture the red apple on the table.",
            "The robot can not run.",
            "The robot should not run slowly.",
            "The robot may not throw an apple.",
            "The robot can not throw an red apple slowly.",
            "The robot can not throw an red apple slowly under the table.",
            "The robot can not move slowly.",


            "The robot can not be small.",
            "The robot can not be small and red.",
            "The robot can not be as small as the box.",
            "The robot can not be smaller than the red box.",
            "The robot can not be more small than the red box.",
            "The robot can not be much smaller than the red box.",
            "The robot can not be much more small than the red box.",


            "A robot runs or a robot runs slowly.",
            "A robot throws an apple or a robot throws an apple slowly.",
            "A robot throws an small and red apple slowly under the table or a robot under the table throws  an small and red apple slowly .",
            "A robot moves slowly or the robot can capture the red apple on the table.",


            "John runs or John runs slowly.",
            "John throws an apple or John throws an apple slowly.",
            "John throws an red apple slowly or John throws an red apple slowly under the table.",


            "A small robot runs or a small robot runs slowly.",
            "A small robot throws an apple or a small robot throws an apple slowly.",
            "A small robot throws an red apple slowly or a small robot throws an red apple slowly under the table.",


            "A small robot runs or there is an apple.",
            "A small robot throws an apple or there is an apple.",
            "A small robot throws an red apple slowly or there are 3 apples.",


            "The robot puts the surface on the top of the table.",
            "The robot grasps the leg X.",
            "The robot moves the leg X perpendicularly with the surface.",

            "The robot grasps 3 apples X.",
            "The robot X is small.",


            "The robot avoids running.",
            "The robot avoids throwing the apple.",
            "The robot enjoys cooking.",

            "The robot tries to solve the problem.",
            "The robot asks the users to enter the input.",

            "Please move.",
            "Please move an apple on the table!",
            "Please move an apple on the table.",

            "There are 3 kg of the apple.",

            "Grasp the leg X.",
            "Slowly grasp the leg X.",
            "Slowly and carefully grasp the leg X.",

            "Grasp the leg X under the table.",
            "Grasp the leg X under the table slowly.",


            "Please move.",
            "Please move an apple on the table!",
            "Please move an apple on the table.",

            "Move the leg X perpendicularly with the surface.",
            "Rotate the leg X.",

            "Insert the leg X.",
        ]
        for i, input_ in enumerate(inputs_):
            tokenized_sent = word_tokenize(input_)

            grammar = dynamic_crl_grammar(tokenized_sent)
            parser = BottomUpChartParser(grammar)
            result = parser.parse(tokenized_sent)

            error_msg = "Can not parse the sentence {}-th: <{}>\nUse parser's trace to analyze the error.".format(
                i, tokenized_sent)
            self.assertNotEqual(result, None, error_msg)


if __name__ == "__main__":
    unittest.main()
