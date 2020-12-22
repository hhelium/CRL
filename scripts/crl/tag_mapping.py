"""
# @ Our valid POS tags:
    "NN", "NNS",
    "NNP", "NNPS",
    "PRP",
    "POS_of", "POS",
    "CD", "MN",
    "DET",
    "VBZ", "VB", "VBN", "VBG", "MD",
    "JJ", "JJR", "JJS", "MOST", "MORE", "AND", "OR",
    "THAN", "AS",
    "RB", "RBR", "RBS",
    "BY", "TO",
    "IN",
    "AUX", "AUX_DO",
    "WHO", "WHERE", "WHICH", "HOW",
    "WP", "WDT",
    "THERE",
    "PERIOD", "QUESTION", "EXCLAM",

    "RP",
    "PREP",
    "VAR",
    "PLEASE"
"""

spacy_tag2our_tag = {
    "DT": "DET",
    ".": "PERIOD",
    "-LRB-": "LRB",
    "-RRB-": "RRB",
    ",": "COMMA",
    "`": "QUOTE",
    ";": "SEMI_COLON",
    ":": "COLON",
    "PRP$": "POS_pronoun",
    "CC": "AND"
}

other_tag2our_tag = spacy_tag2our_tag
