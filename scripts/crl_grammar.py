crl_grammar_str = """
Noun_Count -> NN
Noun_Count -> NNS

Proper_Noun -> NNP
Proper_Noun -> NNPS

Pronoun -> PRP

Noun_w_support -> Adj_phrase Noun_Count
Noun_w_support -> Noun_Count

Measure_Noun -> CD MN

# * Start of Adj
Adj_core -> JJ
Adj_core -> JJR
Adj_core -> JJS
Adj_core -> MORE JJ
Adj_core -> MOST JJ

Adj_phrase -> Adj_core
Adj_phrase -> Adj_core AND Adj_phrase

Adj_advance -> AS JJ  AS Noun_Phrase
Adj_advance -> JJR THAN Noun_Phrase
Adj_advance -> MORE JJ THAN Noun_Phrase
# * End of Adj

# * Start of Adv
Adv_core -> RB
Adv_core -> MORE RB
Adv_core -> MOST RB

Adv_phrase -> Adv_core
Adv_phrase -> Adv_core AND Adv_phrase
# * End of Adv

Gerund -> VBG

Quantified_Noun -> CD Noun_Count
Quantified_Noun -> CD Adj_phrase Noun_Count

Quantified_Noun -> CD Noun_Count VAR
Quantified_Noun -> CD Adj_phrase Noun_Count VAR
# * Start of Noun_Phrase
Noun_Phrase -> Proper_Noun
Noun_Phrase -> Pronoun
Noun_Phrase -> det Noun_w_support
Noun_Phrase -> Proper_Noun POS Noun_w_support
Noun_Phrase -> det Noun_w_support POS Noun_w_support

Noun_Phrase -> det Noun_w_support POS_of det Noun_w_support
Noun_Phrase -> det Noun_w_support POS_of Proper_Noun

Noun_Phrase -> Proper_Noun relative_clause
Noun_Phrase -> det Noun_w_support relative_clause

Noun_Phrase -> Measure_Noun
Noun_Phrase -> Measure_Noun POS_of Noun_w_support

Noun_Phrase -> Quantified_Noun

Noun_Phrase -> det Noun_w_support VAR
Noun_Phrase -> Proper_Noun POS Noun_w_support VAR
Noun_Phrase -> det Noun_w_support POS Noun_w_support VAR
Noun_Phrase -> det Noun_w_support VAR POS Noun_w_support
Noun_Phrase -> det Noun_w_support VAR POS Noun_w_support VAR

Noun_Phrase -> det Noun_w_support VAR POS_of det Noun_w_support
Noun_Phrase -> det Noun_w_support POS_of det Noun_w_support VAR
Noun_Phrase -> det Noun_w_support VAR POS_of det Noun_w_support VAR

Noun_Phrase -> det Noun_w_support POS_of Proper_Noun
Noun_Phrase -> det Noun_w_support VAR POS_of Proper_Noun

Noun_Phrase -> det Noun_w_support VAR relative_clause

Noun_Phrase -> Measure_Noun POS_of Noun_w_support VAR
# * End of Noun_Phrase

# * Start of Verb
Verb -> VBZ
Verb -> VB

Verb_core -> Verb
Verb_core -> Verb Noun_Phrase


# Verb_core -> Verb BY Noun_Phrase
# Verb_core -> Verb Noun_Phrase Noun_Phrase
Verb_core -> Noun_Phrase
Verb_core -> Adj_phrase
Verb_core -> Adj_advance
# * End of Verb

Preposition_Phrase -> IN Noun_Phrase

Verb_modifier -> Preposition_Phrase
Verb_modifier -> Preposition_Phrase Verb_modifier
Verb_modifier -> Adv_phrase
Verb_modifier -> Adv_phrase Verb_modifier


relative_clause_2 -> Verb_Phrase
relative_clause_2 -> Verb_Phrase and_relative_pronoun relative_clause_2
relative_clause_1 -> relative_clause_2
relative_clause_1 -> relative_clause_2 or_relative_pronoun relative_clause_1

relative_clause -> relative_pronoun relative_clause_1

and_relative_pronoun -> AND Wh_Pronoun
or_relative_pronoun -> OR Wh_Pronoun
relative_pronoun -> Wh_Pronoun

# * Start of Verb_Phrase
Verb_Phrase -> Verb_core
Verb_Phrase -> Verb_core Verb_modifier
Verb_Phrase -> Verb_modifier Verb_core
Verb_Phrase -> Verb_modifier Verb_core Verb_modifier

Verb_Phrase -> AUX Verb_core
Verb_Phrase -> MD Verb_core

Verb_Phrase -> AUX Verb_core Verb_modifier
Verb_Phrase -> Verb_modifier AUX Verb_core
Verb_Phrase -> Verb_modifier AUX Verb_core Verb_modifier

Verb_Phrase -> MD Verb_core Verb_modifier
Verb_Phrase -> MD Verb_modifier Verb_core
Verb_Phrase -> MD Verb_modifier Verb_core Verb_modifier

Verb_Phrase -> MD AUX Verb_core

Verb_Phrase -> MD AUX Verb_core Verb_modifier
Verb_Phrase -> Verb_modifier MD AUX Verb_core
Verb_Phrase -> Verb_modifier MD AUX Verb_core Verb_modifier

Verb_Phrase -> AUX_DO NOT Verb_core
Verb_Phrase -> AUX_DO NOT Verb_core Verb_modifier
Verb_Phrase -> AUX_DO NOT Verb_modifier Verb_core
Verb_Phrase -> AUX_DO NOT Verb_modifier Verb_core Verb_modifier

Verb_Phrase -> AUX NOT Verb_core
Verb_Phrase -> MD NOT Verb_core

Verb_Phrase -> AUX NOT Verb_core Verb_modifier
Verb_Phrase -> Verb_modifier AUX NOT Verb_core
Verb_Phrase -> Verb_modifier AUX NOT Verb_core Verb_modifier

Verb_Phrase -> MD NOT Verb_core Verb_modifier
Verb_Phrase -> MD NOT Verb_modifier Verb_core
Verb_Phrase -> MD NOT Verb_modifier Verb_core Verb_modifier


Verb_Phrase -> MD NOT AUX Verb_core

Verb_Phrase -> MD NOT AUX Verb_core Verb_modifier
Verb_Phrase -> Verb_modifier MD NOT AUX Verb_core
Verb_Phrase -> Verb_modifier MD NOT AUX Verb_core Verb_modifier

# * End of Verb_Phrase

VP_coord_2 -> Verb_Phrase AND VP_coord_2
VP_coord_2 -> Verb_Phrase

VP_coord_1 -> VP_coord_2 OR VP_coord_1
VP_coord_1 -> VP_coord_2


type_1_sentence -> Noun_Phrase VP_coord_1
type_2_sentence -> THERE AUX Noun_Phrase

# type_3_sentence -> "it" "is" "false" "that" type_1_sentence

# type_4_sentence -> Yes/No query
type_4_sentence -> AUX_DO Noun_Phrase Verb
type_4_sentence -> AUX_DO Noun_Phrase Verb Noun_Phrase

type_4_sentence -> AUX_DO Noun_Phrase Verb Verb_modifier
type_4_sentence -> AUX_DO Noun_Phrase Verb_modifier Verb

type_4_sentence -> AUX_DO Noun_Phrase Verb Noun_Phrase Verb_modifier
type_4_sentence -> AUX_DO Noun_Phrase Verb_modifier Verb Noun_Phrase


type_4_sentence -> AUX Noun_Phrase Adj_phrase
type_4_sentence -> AUX Noun_Phrase Noun_Phrase
type_4_sentence -> AUX Noun_Phrase Adj_advance

# type_5_sentence -> Wh-query

type_5_sentence_who -> WHO AUX_DO Verb
type_5_sentence_who -> WHO AUX_DO Verb Noun_Phrase

type_5_sentence_who -> WHO AUX_DO Verb Verb_modifier
type_5_sentence_who -> WHO AUX_DO Verb_modifier Verb

type_5_sentence_who -> WHO AUX_DO Verb Noun_Phrase Verb_modifier
type_5_sentence_who -> WHO AUX_DO Verb_modifier Verb Noun_Phrase

type_5_sentence_who -> WHO AUX Adj_phrase
type_5_sentence_who -> WHO AUX Adj_advance
type_5_sentence_who -> WHO AUX Noun_Phrase

type_5_sentence_which -> Which_Query_NP AUX_DO Verb
type_5_sentence_which -> Which_Query_NP AUX_DO Verb Noun_Phrase

type_5_sentence_which -> Which_Query_NP AUX_DO Verb Verb_modifier
type_5_sentence_which -> Which_Query_NP AUX_DO Verb_modifier Verb

type_5_sentence_which -> Which_Query_NP AUX_DO Verb Noun_Phrase Verb_modifier
type_5_sentence_which -> Which_Query_NP AUX_DO Verb_modifier Verb Noun_Phrase

type_5_sentence_which -> Which_Query_NP AUX Adj_phrase
type_5_sentence_which -> Which_Query_NP AUX Adj_advance
type_5_sentence_which -> Which_Query_NP AUX Noun_Phrase


Which_Query_NP -> WHICH Noun_w_support
Which_Query_NP -> WHICH Noun_w_support POS Noun_w_support
Which_Query_NP -> WHICH Noun_w_support POS_of Noun_w_support
Which_Query_NP -> WHICH Noun_w_support POS_of det Noun_w_support
Which_Query_NP -> WHICH Noun_w_support POS_of Proper_Noun
Which_Query_NP -> WHICH Noun_w_support relative_clause

type_5_sentence_where -> WHERE AUX_DO Noun_Phrase Verb
type_5_sentence_where -> WHERE AUX_DO Noun_Phrase Verb_modifier Verb
type_5_sentence_where -> WHERE AUX_DO Noun_Phrase Verb Noun_Phrase
type_5_sentence_where -> WHERE AUX_DO Noun_Phrase Verb_modifier Verb Noun_Phrase

type_5_sentence_where -> WHERE AUX Noun_Phrase


type_5_sentence_how -> HOW AUX_DO Noun_Phrase Verb
type_5_sentence_how -> HOW AUX_DO Noun_Phrase Verb Noun_Phrase

type_5_sentence_how -> HOW AUX_DO Noun_Phrase Verb_modifier Verb
type_5_sentence_how -> HOW AUX_DO Noun_Phrase Verb_modifier Verb Noun_Phrase

type_5_sentence_how -> HOW AUX Noun_Phrase

type_5_sentence -> type_5_sentence_who| type_5_sentence_which| type_5_sentence_where| type_5_sentence_how


type_6_sentence -> PLEASE VB
type_6_sentence -> PLEASE VB Noun_Phrase

type_6_sentence -> PLEASE VB Verb_modifier
type_6_sentence -> PLEASE Adv_phrase VB

type_6_sentence -> PLEASE Adv_phrase VB Noun_Phrase
type_6_sentence -> PLEASE VB Noun_Phrase Verb_modifier
type_6_sentence -> PLEASE Adv_phrase VB Noun_Phrase Verb_modifier

type_7_sentence -> IF type_1_sentence THEN type_1_sentence
type_7_sentence -> IF THERE AUX Noun_Phrase THEN THERE AUX Noun_Phrase

type_8_sentence -> VB
type_8_sentence -> VB Verb_modifier
type_8_sentence -> Adv_phrase VB
type_8_sentence -> Adv_phrase VB Verb_modifier

type_8_sentence -> VB Noun_Phrase
type_8_sentence -> VB Noun_Phrase Verb_modifier
type_8_sentence -> Adv_phrase VB Noun_Phrase
type_8_sentence -> Adv_phrase VB Noun_Phrase Verb_modifier

# simple_sentence -> type_1_sentence | type_2_sentence
# sentence_coord_2 -> simple_sentence
# sentence_coord_2 -> simple_sentence AND sentence_coord_2
# sentence_coord_1 -> sentence_coord_2
# sentence_coord_1 -> sentence_coord_2 OR sentence_coord_1
# sentence ->  sentence_coord_1 PERIOD

type_1_sentence_coord_2 -> type_1_sentence AND type_1_sentence_coord_2
type_1_sentence_coord_2 -> type_1_sentence | type_2_sentence


type_1_sentence_coord_1 -> type_1_sentence_coord_2
type_1_sentence_coord_1 -> type_1_sentence_coord_2 OR type_1_sentence_coord_1


sentence -> type_1_sentence PERIOD
sentence -> type_2_sentence PERIOD
sentence -> type_4_sentence QUESTION
sentence -> type_5_sentence QUESTION
sentence -> type_6_sentence EXCLAM
sentence -> type_6_sentence PERIOD
sentence -> type_7_sentence PERIOD
sentence -> type_8_sentence PERIOD
sentence -> type_8_sentence EXCLAM

sentence -> type_1_sentence_coord_1 PERIOD

S -> sentence

WP -> WHO | THAT
Wh_Pronoun -> WHO | THAT

det -> DET | NO

# - Start of -
Noun_Non_Count -> NN
Noun_Non_Count -> NNS

Noun_Non_Count_w_support -> Adj_phrase Noun_Non_Count
Noun_Non_Count_w_support -> Noun_Non_Count

Noun_Phrase -> Gerund
Noun_Phrase -> Noun_Non_Count_w_support
Noun_Phrase -> Measure_Noun POS_of Noun_Non_Count_w_support
Noun_Phrase -> Measure_Noun POS_of DET Noun_w_support
Noun_Phrase -> det Noun_w_support POS_of Noun_w_support

Adj_core -> Gerund
Adj_advance -> MUCH JJR THAN Noun_Phrase
Adj_advance -> MUCH MORE JJ THAN Noun_Phrase




# * Phrasal Verb
Verb_core -> Verb RP
Verb_core -> Verb RP Noun_Phrase
Verb_core -> Verb Noun_Phrase RP
Verb_core_w_gerund -> Gerund
Verb_core_w_gerund -> Gerund Noun_Phrase

Verb_core_w_to -> TO VB
Verb_core_w_to -> TO VB Noun_Phrase
type_2_sentence -> THERE AUX Noun_Phrase Preposition_Phrase


Verb_Phrase -> Verb Verb_core_w_gerund
Verb_Phrase -> Verb Verb_core_w_gerund Verb_modifier


Verb_Phrase -> Verb Verb_core_w_to
Verb_Phrase -> Verb Verb_core_w_to Verb_modifier
# - End of -

"""

POS_list = [
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
]
