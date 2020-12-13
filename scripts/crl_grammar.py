crl_grammar = """
Noun_Count -> NN
Noun_Count -> NNS

Proper_Noun -> NNP
Proper_Noun -> NNPS

Pronoun -> PRP

Noun_w_support -> ADJP Noun_Count
Noun_w_support -> Noun_Count

Measure_Noun -> CD MN

# * Start of Adj
Adj_core -> JJ
Adj_core -> JJR
Adj_core -> JJS
Adj_core -> MORE JJ
Adj_core -> MOST JJ

ADJP -> Adj_core
ADJP -> Adj_core AND ADJP

Adj_advance -> AS JJ  AS NP
Adj_advance -> JJR THAN NP
Adj_advance -> MORE JJ THAN NP
# * End of Adj

# * Start of Adv
Adv_core -> RB
Adv_core -> MORE RB
Adv_core -> MOST RB

ADVP -> Adv_core
ADVP -> Adv_core AND ADVP
# * End of Adv

Gerund -> VBG

Quantified_Noun -> CD Noun_Count
Quantified_Noun -> CD ADJP Noun_Count

Quantified_Noun -> CD Noun_Count VAR
Quantified_Noun -> CD ADJP Noun_Count VAR
# * Start of NP
NP -> Proper_Noun
NP -> Pronoun
NP -> DET Noun_w_support
NP -> Proper_Noun POS Noun_w_support
NP -> DET Noun_w_support POS Noun_w_support

NP -> DET Noun_w_support POS_of DET Noun_w_support
NP -> DET Noun_w_support POS_of Proper_Noun

NP -> Proper_Noun relative_clause
NP -> DET Noun_w_support relative_clause

NP -> Measure_Noun
NP -> Measure_Noun POS_of Noun_w_support

NP -> Quantified_Noun

NP -> DET Noun_w_support VAR
NP -> Proper_Noun POS Noun_w_support VAR
NP -> DET Noun_w_support POS Noun_w_support VAR
NP -> DET Noun_w_support VAR POS Noun_w_support
NP -> DET Noun_w_support VAR POS Noun_w_support VAR

NP -> DET Noun_w_support VAR POS_of DET Noun_w_support
NP -> DET Noun_w_support POS_of DET Noun_w_support VAR
NP -> DET Noun_w_support VAR POS_of DET Noun_w_support VAR

NP -> DET Noun_w_support POS_of Proper_Noun
NP -> DET Noun_w_support VAR POS_of Proper_Noun

NP -> DET Noun_w_support VAR relative_clause

NP -> Measure_Noun POS_of Noun_w_support VAR
# * End of NP

# * Start of Verb
Verb -> VBZ
Verb -> VB

Verb_core -> Verb
Verb_core -> Verb NP


# Verb_core -> Verb BY NP
# Verb_core -> Verb NP NP
Verb_core -> NP
Verb_core -> ADJP
Verb_core -> Adj_advance
# * End of Verb

PP -> IN NP

Verb_modifier -> PP
Verb_modifier -> PP Verb_modifier
Verb_modifier -> ADVP
Verb_modifier -> ADVP Verb_modifier


relative_clause_2 -> VP
relative_clause_2 -> VP and_relative_pronoun relative_clause_2
relative_clause_1 -> relative_clause_2
relative_clause_1 -> relative_clause_2 or_relative_pronoun relative_clause_1

relative_clause -> relative_pronoun relative_clause_1

and_relative_pronoun -> AND WP
or_relative_pronoun -> OR WP
relative_pronoun -> WP

# * Start of VP
VP -> Verb_core
VP -> Verb_core Verb_modifier
VP -> Verb_modifier Verb_core
VP -> Verb_modifier Verb_core Verb_modifier

VP -> AUX Verb_core
VP -> MD Verb_core

VP -> AUX Verb_core Verb_modifier
VP -> Verb_modifier AUX Verb_core
VP -> Verb_modifier AUX Verb_core Verb_modifier

VP -> MD Verb_core Verb_modifier
VP -> MD Verb_modifier Verb_core
VP -> MD Verb_modifier Verb_core Verb_modifier

VP -> MD AUX Verb_core

VP -> MD AUX Verb_core Verb_modifier
VP -> Verb_modifier MD AUX Verb_core
VP -> Verb_modifier MD AUX Verb_core Verb_modifier

VP -> AUX_DO NOT Verb_core
VP -> AUX_DO NOT Verb_core Verb_modifier
VP -> AUX_DO NOT Verb_modifier Verb_core
VP -> AUX_DO NOT Verb_modifier Verb_core Verb_modifier

VP -> AUX NOT Verb_core
VP -> MD NOT Verb_core

VP -> AUX NOT Verb_core Verb_modifier
VP -> Verb_modifier AUX NOT Verb_core
VP -> Verb_modifier AUX NOT Verb_core Verb_modifier

VP -> MD NOT Verb_core Verb_modifier
VP -> MD NOT Verb_modifier Verb_core
VP -> MD NOT Verb_modifier Verb_core Verb_modifier


VP -> MD NOT AUX Verb_core

VP -> MD NOT AUX Verb_core Verb_modifier
VP -> Verb_modifier MD NOT AUX Verb_core
VP -> Verb_modifier MD NOT AUX Verb_core Verb_modifier

# * End of VP

VP_coord_2 -> VP AND VP_coord_2
VP_coord_2 -> VP

VP_coord_1 -> VP_coord_2 OR VP_coord_1
VP_coord_1 -> VP_coord_2


type_1_sentence -> NP VP_coord_1
type_2_sentence -> THERE AUX NP

# type_3_sentence -> "it" "is" "false" "that" type_1_sentence

# type_4_sentence -> Yes/No query
type_4_sentence -> AUX_DO NP Verb
type_4_sentence -> AUX_DO NP Verb NP

type_4_sentence -> AUX_DO NP Verb Verb_modifier
type_4_sentence -> AUX_DO NP Verb_modifier Verb

type_4_sentence -> AUX_DO NP Verb NP Verb_modifier
type_4_sentence -> AUX_DO NP Verb_modifier Verb NP


type_4_sentence -> AUX NP ADJP
type_4_sentence -> AUX NP NP
type_4_sentence -> AUX NP Adj_advance

# type_5_sentence -> Wh-query

type_5_sentence_who -> WHO AUX_DO Verb
type_5_sentence_who -> WHO AUX_DO Verb NP

type_5_sentence_who -> WHO AUX_DO Verb Verb_modifier
type_5_sentence_who -> WHO AUX_DO Verb_modifier Verb

type_5_sentence_who -> WHO AUX_DO Verb NP Verb_modifier
type_5_sentence_who -> WHO AUX_DO Verb_modifier Verb NP

type_5_sentence_who -> WHO AUX ADJP
type_5_sentence_who -> WHO AUX Adj_advance
type_5_sentence_who -> WHO AUX NP

type_5_sentence_which -> WHICH_QUERY_NP AUX_DO Verb
type_5_sentence_which -> WHICH_QUERY_NP AUX_DO Verb NP

type_5_sentence_which -> WHICH_QUERY_NP AUX_DO Verb Verb_modifier
type_5_sentence_which -> WHICH_QUERY_NP AUX_DO Verb_modifier Verb

type_5_sentence_which -> WHICH_QUERY_NP AUX_DO Verb NP Verb_modifier
type_5_sentence_which -> WHICH_QUERY_NP AUX_DO Verb_modifier Verb NP

type_5_sentence_which -> WHICH_QUERY_NP AUX ADJP
type_5_sentence_which -> WHICH_QUERY_NP AUX Adj_advance
type_5_sentence_which -> WHICH_QUERY_NP AUX NP


WHICH_QUERY_NP -> WHICH Noun_w_support
WHICH_QUERY_NP -> WHICH Noun_w_support POS Noun_w_support
WHICH_QUERY_NP -> WHICH Noun_w_support POS_of Noun_w_support
WHICH_QUERY_NP -> WHICH Noun_w_support POS_of DET Noun_w_support
WHICH_QUERY_NP -> WHICH Noun_w_support POS_of Proper_Noun
WHICH_QUERY_NP -> WHICH Noun_w_support relative_clause

type_5_sentence_where -> WHERE AUX_DO NP Verb
type_5_sentence_where -> WHERE AUX_DO NP Verb_modifier Verb
type_5_sentence_where -> WHERE AUX_DO NP Verb NP
type_5_sentence_where -> WHERE AUX_DO NP Verb_modifier Verb NP

type_5_sentence_where -> WHERE AUX NP


type_5_sentence_how -> HOW AUX_DO NP Verb
type_5_sentence_how -> HOW AUX_DO NP Verb NP

type_5_sentence_how -> HOW AUX_DO NP Verb_modifier Verb
type_5_sentence_how -> HOW AUX_DO NP Verb_modifier Verb NP

type_5_sentence_how -> HOW AUX NP

type_5_sentence -> type_5_sentence_who| type_5_sentence_which| type_5_sentence_where| type_5_sentence_how


type_6_sentence -> PLEASE VB
type_6_sentence -> PLEASE VB NP

type_6_sentence -> PLEASE VB Verb_modifier
type_6_sentence -> PLEASE ADVP VB

type_6_sentence -> PLEASE ADVP VB NP
type_6_sentence -> PLEASE VB NP Verb_modifier
type_6_sentence -> PLEASE ADVP VB NP Verb_modifier

type_7_sentence -> IF type_1_sentence THEN type_1_sentence
type_7_sentence -> IF THERE AUX NP THEN THERE AUX NP

type_8_sentence -> VB
type_8_sentence -> VB Verb_modifier
type_8_sentence -> ADVP VB
type_8_sentence -> ADVP VB Verb_modifier

type_8_sentence -> VB NP
type_8_sentence -> VB NP Verb_modifier
type_8_sentence -> ADVP VB NP
type_8_sentence -> ADVP VB NP Verb_modifier

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




IN -> 'to'
TO -> 'to'
WHO -> "Who"|"who"

WHICH -> "Which"|"which"

WHERE -> "Where"|"where"

HOW -> "How"|"how"
AND -> "and"
OR -> "or"
MORE -> "More"|"more"
MOST -> "Most"|"most"
AS -> "as"
THAN -> "than"
BY -> "by"
THERE -> "there" | "There"
QUESTION -> "?"

RP -> 'among' | 'over' | 'back' | 'one' | 'down' | 'as' | 'way' | 'through' | 'against' | 'in' | 'beyond' | 'open' | 'between' | 'out' | 'even' | 'aback' | 'from' | 'for' | 'away' | 'aside' | 'to' | 'behind' | 'above' | 'under' | 'forward' | 'before' | 'forth' | 'into' | 'towards' | 'around' | 'after' | 'upon' | 'along' | 'with' | 'by' | 'apart' | 'on' | 'about' | 'off' | 'ahead' | 'of' | 'past' | 'up' | 'together' | 'across' | 'below' | 'without' | 'toward' | 'onto' | 'round' | 'at'
VB -> 'do'
VBZ -> 'does'

PLEASE -> 'Please'|'please'

IF -> "If"|"if"
THEN -> "Then"|"then"

NOT -> "Not"|"not"

# - Start of -
Noun_Non_Count -> NN
Noun_Non_Count -> NNS

Noun_Non_Count_w_support -> ADJP Noun_Non_Count
Noun_Non_Count_w_support -> Noun_Non_Count

NP -> Gerund
NP -> Noun_Non_Count_w_support
NP -> Measure_Noun POS_of Noun_Non_Count_w_support
NP -> Measure_Noun POS_of DET Noun_w_support
NP -> DET Noun_w_support POS_of Noun_w_support

Adj_core -> Gerund
Adj_advance -> MUCH JJR THAN NP
Adj_advance -> MUCH MORE JJ THAN NP




# * Phrasal Verb
Verb_core -> Verb RP
Verb_core -> Verb RP NP
Verb_core -> Verb NP RP
Verb_core_w_gerund -> Gerund
Verb_core_w_gerund -> Gerund NP

Verb_core_w_to -> TO VB
Verb_core_w_to -> TO VB NP
type_2_sentence -> THERE AUX NP PP


VP -> Verb Verb_core_w_gerund
VP -> Verb Verb_core_w_gerund Verb_modifier


VP -> Verb Verb_core_w_to
VP -> Verb Verb_core_w_to Verb_modifier
# - End of -

"""

POS_list = [
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
]
