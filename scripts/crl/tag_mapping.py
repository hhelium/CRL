"""
# @ Our valid POS tags:

    # * Our POS tags:
    "WHICH",
    "WHO",
    "WHERE",
    "HOW",
    "THAT",
    "AND",
    "OR",
    "AS",
    "THAN",
    "MUCH",
    "MORE",
    "MOST",
    "BY",
    "THERE",
    "PLEASE",
    "IF",
    "THEN",
    "QUESTION",
    "EXCLAM",
    "PERIOD",
    "COMMA",
    "COLON",
    "IN",
    "POS_of",
    "AUX",
    "AUX_DO",
    "NOT",
    "NO",
    "DET",
    "MN",
    "VAR",

    # * Spacy POS tags:
    "NN",
    "NNS",
    "NNP",
    "NNPS",
    "PRP",
    "VB",
    "VBZ ",
    "IN",
    "MD",
    "CD ",
    "JJ",
    "JJR",
    "JJS ",
    "RB",
    "POS",
"""


spacy_tag2our_tag = {
    "DT": "DET",
    "-LRB-": "LRB",
    "-RRB-": "RRB",
    "`": "QUOTE",
    ";": "SEMI_COLON",
    "PRP$": "POS_pronoun",
}

other_tag2our_tag = spacy_tag2our_tag

