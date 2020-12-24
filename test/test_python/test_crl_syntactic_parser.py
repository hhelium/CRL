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
            "John throws an apple.",
            "John throws an apple slowly.",
            "A small robot throws an apple slowly.",
            "A small robot throws an red apple slowly.",
            "A small and green robot runs slowly.",
            "A small and green robot throws an apple.",
            "John 's robot throws an apple.",
            "John 's robot throws an apple slowly.",
            "The robot of the company runs.",
            "The robot of the company runs slowly.",
            "The robot which is an agent throws an red apple slowly under the table.",
            "The robot which is an agent moves slowly.",
            "John who is an agent throws an red apple slowly.",
            "John who is an agent throws an red apple slowly under the table.",
            "The robot throws 3 kg of apples slowly.",
            "The robot throws 3 kg of red apples slowly.",
            "The robot is 3 pound of metals.",
            "The robot is much smaller than the red box.",
            "The robot is much more small than the red box.",
            "The robot can throw an red apple slowly.",
            "The robot can throw an red apple slowly under the table.",
            "The robot can be much smaller than the red box.",
            "The robot can be much more small than the red box.",
            "The robot can be much smaller than the red box under the table.",
            "The robot can be much more small than the red box under the table.",
            "There is no apple.",
            "There is no apples on the table.",
            "Does the robot throw 3 kg of apple slowly?",
            "Does the robot throw 3 kg of red apple slowly?",
            "Is the apple smaller than the red box?",
            "Is the apple more small than the red box?",
            "Is the apple an agent?",
            "Is John an agent?",
            "Who does move slowly?",
            "Who does  slowly move?",
            "Who is as small as the red block?",
            "Who is smaller than the red block?",
            "Who is the smallest agent?",
            "Who is John?",
            "Which robot does throw 3 kg of red apple slowly?",
            "Which robot does throw 3 kg of red apple slowly under the table?",
            "which robot is smaller than the red block?",
            "which robot is as small as the red block?",
            "which robot is John?",
            "Where does the robot slowly throw 3 kg of red apple ?",
            "Where does the robot slowly under the table throw 3 kg of red apple ?",
            "Sawyer, move the apple on the table!",
            "Sawyer, move the apple on the table slowly!",
            "Sawyer, move the red apple on the table!",
            "Sawyer, move the red apple on the table slowly!",
            "Sawyer, pick the red apple on the table slowly!",
            "Sawyer, grasp the red apple on the table slowly!",
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
            "A small robot runs or a small robot runs slowly.",
            "A small robot throws an apple or a small robot throws an apple slowly.",
            "A small robot throws an red apple slowly or a small robot throws an red apple slowly under the table.",
            "A small robot runs or there is an apple.",
            "A small robot throws an apple or there is an apple.",
            "A small robot throws an red apple slowly or there are 3 apples.",
        ]
        for i, input_ in enumerate(inputs_):
            tokenized_sent = word_tokenize(input_)
            grammar = dynamic_crl_grammar(tokenized_sent)
            parser = BottomUpChartParser(grammar)
            result = parser.parse(tokenized_sent)
            print(result)


if __name__ == "__main__":
    unittest.main()
