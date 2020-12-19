grammar_test_str = '''
    // Root DRS
    test_drs_root: drs_root
    drs_root: drs_statement

    test_complex_condition: complex_condition

    complex_condition: NEG OPEN_CIRCLE_BRACKET drs_statement CLOSE_CIRCLE_BRACKET
                | DISJUNCT OPEN_CIRCLE_BRACKET drs_statement SEP drs_statement CLOSE_CIRCLE_BRACKET
                | IMPLICATION OPEN_CIRCLE_BRACKET drs_statement SEP drs_statement CLOSE_CIRCLE_BRACKET
                | COMMAND OPEN_CIRCLE_BRACKET drs_statement CLOSE_CIRCLE_BRACKET
                | POSSIBILITY OPEN_CIRCLE_BRACKET drs_statement CLOSE_CIRCLE_BRACKET
                | QUESTION OPEN_CIRCLE_BRACKET drs_statement CLOSE_CIRCLE_BRACKET

    // complex_condition: neg
    test_drs_statement: drs_statement
    test_domain: domain
    test_conditions: conditions
    test_condition: condition
    test_atomic_condition: atomic_condition


    drs_statement: DRS OPEN_CIRCLE_BRACKET domain SEP conditions CLOSE_CIRCLE_BRACKET
    domain: OPEN_SQUARE_BRACKET (VAR SEP)* VAR? CLOSE_SQUARE_BRACKET
    conditions: OPEN_SQUARE_BRACKET (condition SEP)* condition? CLOSE_SQUARE_BRACKET
    condition: atomic_condition
            | complex_condition

    atomic_condition: object_condition SID_TID
            | property_condition SID_TID
            | relation_condition SID_TID
            | predicate_condition SID_TID
            | modifier_adv_condition SID_TID
            | modifier_pp_condition SID_TID
            | query_condition SID_TID

    // Test grammar rule
    test_object_condition: object_condition
    test_property_condition: property_condition
    test_relation_condition: relation_condition
    test_predicate_condition: predicate_condition
    test_modifier_adv_condition: modifier_adv_condition
    test_modifier_pp_condition: modifier_pp_condition
    test_query_condition: query_condition

    object_condition: OBJECT OPEN_CIRCLE_BRACKET VAR SEP VALID_LEXICON SEP QUANTITY_PROPERTY SEP UNIT_PROPERTY SEP OPERATOR_PROPERTY SEP COUNT_PROPERTY CLOSE_CIRCLE_BRACKET
    property_condition: PROPERTY OPEN_CIRCLE_BRACKET VAR SEP VALID_LEXICON SEP PROPERTY_DEGREE_PROPERTY CLOSE_CIRCLE_BRACKET
        | PROPERTY OPEN_CIRCLE_BRACKET VAR SEP VALID_LEXICON SEP PROPERTY_DEGREE_PROPERTY SEP VAR CLOSE_CIRCLE_BRACKET
    relation_condition: RELATION OPEN_CIRCLE_BRACKET VAR SEP OF SEP var_or_named_entity CLOSE_CIRCLE_BRACKET
    predicate_condition: PREDICATE OPEN_CIRCLE_BRACKET VAR SEP VALID_LEXICON SEP var_or_named_entity CLOSE_CIRCLE_BRACKET
        | PREDICATE OPEN_CIRCLE_BRACKET VAR SEP VALID_LEXICON SEP var_or_named_entity SEP var_or_named_entity CLOSE_CIRCLE_BRACKET
    modifier_adv_condition: MODIFIER_ADV OPEN_CIRCLE_BRACKET VAR SEP VALID_LEXICON SEP ADV_DEGREE_PROPERTY CLOSE_CIRCLE_BRACKET
    modifier_pp_condition: MODIFIER_PP OPEN_CIRCLE_BRACKET VAR SEP VALID_LEXICON  SEP VAR CLOSE_CIRCLE_BRACKET
    query_condition: QUERY OPEN_CIRCLE_BRACKET VAR SEP QUERY_WH_WORD CLOSE_CIRCLE_BRACKET

    // Test
    test_var_or_named_entity: var_or_named_entity
    var_or_named_entity: VAR | named_entity


    // Test lexicon rule
    test_property_degree_property: PROPERTY_DEGREE_PROPERTY
    test_adv_degree_property: ADV_DEGREE_PROPERTY
    test_count_property: COUNT_PROPERTY
    test_operator_property: OPERATOR_PROPERTY
    test_unit_property: UNIT_PROPERTY
    test_quantity_property: QUANTITY_PROPERTY
    test_valid_lexicon: VALID_LEXICON
    test_object: OBJECT
    test_property: PROPERTY
    test_relation: RELATION
    test_predicate: PREDICATE
    test_modifier_adv: MODIFIER_ADV
    test_modifier_pp: MODIFIER_PP
    test_query: QUERY
    test_query_wh_word: QUERY_WH_WORD
    test_neg: NEG
    test_named_entity: named_entity
    test_disjunct: DISJUNCT
    test_implication: IMPLICATION
    test_command: COMMAND
    test_possibility: POSSIBILITY
    test_question: QUESTION
    test_open_circle_bracket: OPEN_CIRCLE_BRACKET
    test_close_circle_bracket: CLOSE_CIRCLE_BRACKET
    test_open_square_bracket: OPEN_SQUARE_BRACKET
    test_close_square_bracket: CLOSE_SQUARE_BRACKET
    test_drs: DRS
    test_sid_tid: SID_TID
    test_named: NAMED
    test_single_quote: SINGLE_QUOTE
    test_variable: VAR
    test_sep: SEP


    named_entity: NAMED OPEN_CIRCLE_BRACKET SINGLE_QUOTE CNAME SINGLE_QUOTE CLOSE_CIRCLE_BRACKET

    // Sentence ID, Term ID
    ADV_DEGREE_PROPERTY: "pos" | "comp" | "sup"
    PROPERTY_DEGREE_PROPERTY: "pos_as"| "pos" | "comp_than"| "comp" | "sup"
    COUNT_PROPERTY: "na"|INT
    OPERATOR_PROPERTY: "eq" | "geq" | "greater" | "leq" | "less" | "exactly" | "na"
    UNIT_PROPERTY: "na" | WORD
    QUANTITY_PROPERTY: "dom"|"mass"|"countable"
    VALID_LEXICON: CNAME
    OBJECT: "object"
    PROPERTY: "property"
    RELATION: "relation"
    PREDICATE: "predicate"
    MODIFIER_ADV: "modifier_adv"
    MODIFIER_PP: "modifier_pp"
    NAMED: "named"
    SINGLE_QUOTE: "'"
    QUERY: "query"
    QUERY_WH_WORD: "who" | "what" | "which" | "how" | "where" | "when"
    NEG: "-"

    DISJUNCT: "v"
    IMPLICATION: "=>"
    COMMAND: "command"
    POSSIBILITY: "may" | "can" | "should" | "must"
    QUESTION: "question"
    OPEN_CIRCLE_BRACKET: "("
    CLOSE_CIRCLE_BRACKET: ")"
    OPEN_SQUARE_BRACKET: "["
    CLOSE_SQUARE_BRACKET: "]"
    DRS: "drs"|"DRS"
    SID_TID: "-" INT "/" INT
    VAR: UCASE_LETTER DIGIT*
    SEP: ","

    // Some special keywords:
    test_of: OF
    OF: "of"

    %import common.DIGIT
    %import common.UCASE_LETTER
    %import common.INT
    %import common.CNAME
    %import common.WORD
    %import common.WS
    %ignore WS
'''

