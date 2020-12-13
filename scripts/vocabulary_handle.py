#!/home/dangtran/Desktop/env/env_2/bin/python2
import rospy
from word_forms.word_forms import get_word_forms
from pattern.en import (
    referenced, article,
    pluralize, singularize,
    comparative, superlative,
    lemma, conjugate,
    PRESENT, PAST,
    INDICATIVE, IMPERATIVE, CONDITIONAL, SUBJUNCTIVE,
    PROGRESSIVE,
    SINGULAR, PLURAL,
    DEFINITE, INDEFINITE,
)
import dill
from nltk.corpus.reader import (
    CorpusReader,
    StreamBackedCorpusView
)
from nltk.corpus.reader.util import (
    read_line_block, concat
)
from nltk import (
    word_tokenize
)
from tqdm import tqdm
from vocab.unk_vocab import UnkVocab


class VocabularyStreamReader(StreamBackedCorpusView):
    def read_block(self, stream):
        block = []
        for line in read_line_block(stream):
            for word in word_tokenize(line):
                block.append(word)
        return block


class VocabularyPairStreamReader(StreamBackedCorpusView):
    def read_block(self, stream):
        block = []
        for line in read_line_block(stream):
            line = str(line).strip()
            line = line.split(" ")

            name = line[0].strip()
            type_ = line[1].strip()
            block.append((name, type_))
        return block


class VocabularyWholeLineStreamReader(StreamBackedCorpusView):
    def read_block(self, stream):
        block = []
        for line in read_line_block(stream):
            line = str(line).strip()
            block.append(line)
        return block


class BaseVocabulary(UnkVocab, object):
    def __init__(self, words=()):
        super(BaseVocabulary, self).__init__(words=words)

    def pluralize(self, word):
        '''
        Given base-form of the word, return back plural form of the word
        (For Noun only)
        Args:
            word (str): base-form of the word

        Raises:
            ValueError: The vocabulary does not contain the base-form
            ValueError: Can not find the base-form of the given word

        Returns:
            str: plural form of the word
        '''
        if word in self._word2index:
            return pluralize(word)
        else:
            try:
                base_form_word = lemma(word)
                if base_form_word in self._word2index:
                    return pluralize(base_form_word)
                else:
                    raise ValueError(
                        "Found the base-form for '{}': '{}'. But even the base-form not in vocabulary".format(word, base_form_word))
            except:
                raise ValueError(
                    "Can not found base-form for '{}'".format(word))

    def singularize(self, word):
        '''
        Given a base-form of noun, return a singular form
        (For Noun only)

        Args:
            word (str): base-form of noun

        Raises:
            ValueError: [description]
            ValueError: [description]

        Returns:
            str: singular form of noun
        '''
        if word in self._word2index:
            return singularize(word)
        else:
            try:
                base_form_word = lemma(word)
                if base_form_word in self._word2index:
                    return singularize(base_form_word)
                else:
                    raise ValueError(
                        "Found the base-form for '{}': '{}'. But even the base-form not in vocabulary".format(word, base_form_word))
            except:
                raise ValueError(
                    "Can not found base-form for '{}'".format(word))

    # - def add_article(self, word, definite=INDEFINITE):
    # -     if word in self._word2index:
    # -         return referenced(word, article=definite)
    # -     else:
    # -         try:
    # -             base_form_word = lemma(word)
    # -             if base_form_word in self._word2index:
    # -                 return referenced(base_form_word, article=definite)
    # -             else:
    # -                 raise (ValueError(
    # -                     "'{}'/'{}' - not in Vocabulary, can not add determiner for the noun".format(base_form_word, word)))
    # -         except:
    # -             raise (ValueError(
    # -                 "'{}'/'{}' - not in Vocabulary, can not add determiner for the noun".format(base_form_word, word)))

    def comparative(self, word):
        '''
        Given a base-form word (Adj), return back a comparative form

        Args:
            word (str): base-form of adj

        Raises:
            ValueError: [description]
            ValueError: [description]

        Returns:
            str: comparative form of adj
        '''
        if word in self._word2index:
            return comparative(word)
        else:
            try:
                base_form_word = lemma(word)
                if base_form_word in self._word2index:
                    return comparative(base_form_word)
                else:
                    raise ValueError(
                        "Found the base-form for '{}': '{}'. But even the base-form not in vocabulary".format(word, base_form_word))
            except:
                raise ValueError(
                    "Can not found base-form for '{}'".format(word))

    def superlative(self, word):
        '''
        Given a base-form word (Adj), return back a superlative form

        Args:
            word (str): base-form adj

        Raises:
            ValueError: [description]
            ValueError: [description]

        Returns:
            str: superlative form
        '''
        if word in self._word2index:
            return superlative(word)
        else:
            try:
                base_form_word = lemma(word)
                if base_form_word in self._word2index:
                    return superlative(base_form_word)
                else:
                    raise ValueError(
                        "Found the base-form for '{}': '{}'. But even the base-form not in vocabulary".format(word, base_form_word))
            except:
                raise ValueError(
                    "Can not found base-form for '{}'".format(word))

    def conjugate_singularize(self, word):
        '''
        Given a base-form word (Verb), return singularized form

        Args:
            word (str): base-form of verb

        Raises:
            ValueError: [description]
            ValueError: [description]

        Returns:
            str: singularized-form of verb
        '''
        if word in self._word2index:
            conj_word = conjugate(
                word, person=3, number=SINGULAR, mood=INDICATIVE, tense=PRESENT, parse=True)
            conj_word = conj_word.replace("'", "")  # * small hack
            return conj_word
        else:
            try:
                base_form_word = lemma(word)
                if base_form_word in self._word2index:
                    conj_word = conjugate(
                        base_form_word, person=3, number=SINGULAR, mood=INDICATIVE, tense=PRESENT, parse=True)
                    conj_word = conj_word.replace("'", "")  # * small hack
                    return conj_word
                else:
                    raise ValueError(
                        "Found the base-form for '{}': '{}'. But even the base-form not in vocabulary".format(word, base_form_word))
            except:
                raise ValueError(
                    "Can not found base-form for '{}'".format(word))

    def conjugate_gerund(self, word):
        '''
        Given a base-form word (Verb), return gerund form

        Args:
            word (str): base-form of verb

        Raises:
            ValueError: [description]
            ValueError: [description]

        Returns:
            str: Gerund form of verb
        '''
        if word in self._word2index:
            conj_word = conjugate(word, aspect=PROGRESSIVE,
                                  tense=PRESENT, parse=True)
            conj_word = conj_word.replace("'", "")  # * small hack
            return conj_word
        else:
            try:
                base_form_word = lemma(word)
                if base_form_word in self._word2index:
                    conj_word = conjugate(
                        base_form_word, aspect=PROGRESSIVE, tense=PRESENT, parse=True)
                    conj_word = conj_word.replace("'", "")  # * small hack
                    return conj_word
                else:
                    raise ValueError(
                        "Found the base-form for '{}': '{}'. But even the base-form not in vocabulary".format(word, base_form_word))
            except:
                raise ValueError(
                    "Can not found base-form for '{}'".format(word))

    def conjugate_ed(self, word):
        '''
        Given a base-form word (Verb), return back a ed-form

        Args:
            word (str): base-form of verb

        Raises:
            ValueError: [description]
            ValueError: [description]

        Returns:
            str: ed-form of verb
        '''
        if word in self._word2index:
            conj_word = conjugate(
                word, tense=PAST, mood=INDICATIVE, aspect=PROGRESSIVE, parse=True)
            conj_word = conj_word.replace("'", "")  # * small hack
            return conj_word
        else:
            try:
                base_form_word = lemma(word)
                if base_form_word in self._word2index:
                    conj_word = conjugate(base_form_word, tense=PAST,
                                          mood=INDICATIVE, aspect=PROGRESSIVE, parse=True)
                    conj_word = conj_word.replace("'", "")  # * small hack
                    return conj_word
                else:
                    raise ValueError(
                        "Found the base-form for '{}': '{}'. But even the base-form not in vocabulary".format(word, base_form_word))
            except:
                raise ValueError(
                    "Can not found base-form for '{}'".format(word))

    # def lookup(self, word):
    #     if word in self._word2index:
    #         return word
    #     else:
    #         try:
    #             base_form_word = lemma(word)
    #             print("here: {}".format(base_form_word))
    #             if base_form_word in self._word2index:
    #                 return word
    #             else:
    #                 print("Fail here")
    #                 return self.index2word(0)  # * return UNK
    #         except:
    #             return self.index2word(0)  # * return UNK

    @property
    def unknown(self):
        return self.index2word(0)


class VocabularyReader(CorpusReader):
    def __init__(self, root, fileids, encoding=None, tag_mapping_function=None):
        super(VocabularyReader, self).__init__(root, fileids,
                                               encoding=encoding, tag_mapping_function=tag_mapping_function)
        self._vocab = BaseVocabulary()
        self._vocab.word2index(list(self.words()), train=True)
        self._inverse_map = dict()

    @property
    def vocabulary(self):
        return self._vocab

    def lookup(self, word):
        if word in self._vocab._word2index:
            return word
        elif word in self._inverse_map.keys():
            return word
        else:
            try:
                base_word = lemma(word)
                if lemma(word) in self._vocab._word2index:
                    return lemma(word)
                elif lemma(word) in self._inverse_map.keys():
                    return lemma(word)
                else:
                    return self._vocab.index2word(0)
            except:
                return self._vocab.index2word(0)
        # elif lemma(word) in self._vocab._word2index:
        #     return lemma(word)
        # elif lemma(word) in self._inverse_map.keys():
        #     return lemma(word)
        # else:
        #     return self._vocab.index2word(0)

    def lemmatize(self, word):
        if word in self._vocab._word2index:
            return word
        elif word in self._inverse_map.keys():
            return self._inverse_map[word]
        elif lemma(word) in self._vocab._word2index:
            return lemma(word)
        elif lemma(word) in self._inverse_map.keys():
            return self._inverse_map[lemma(word)]
        else:
            return self._vocab.index2word(0)

    def words(self, fileids=None):
        if fileids is None:
            fileids = self._fileids
        elif isinstance(fileids, basestring):
            fileids = [fileids]
        return concat([VocabularyStreamReader(fileid, enc) for fileid, enc in self.abspaths(fileids, True)])

    def nouns(self):
        fileids = "Vocabulary_noun.txt"
        return concat([VocabularyStreamReader(fileid, enc) for fileid, enc in self.abspaths(fileids, True)])

    def mass_nouns(self):
        fileids = "Vocabulary_mass_noun.txt"
        return concat([VocabularyStreamReader(fileid, enc) for fileid, enc in self.abspaths(fileids, True)])

    def adjectives(self):
        fileids = "Vocabulary_adj.txt"
        return concat([VocabularyStreamReader(fileid, enc)
                       for fileid, enc in self.abspaths(fileids, True)])

    def verbs(self):
        fileids = "Vocabulary_verb.txt"
        return concat([VocabularyStreamReader(fileid, enc)
                       for fileid, enc in self.abspaths(fileids, True)])

    def preps(self):
        fileids = "Vocabulary_prep.txt"
        return concat([VocabularyStreamReader(fileid, enc)
                       for fileid, enc in self.abspaths(fileids, True)])

    def adverbs(self):
        fileids = "Vocabulary_adv.txt"
        return concat([VocabularyStreamReader(fileid, enc)
                       for fileid, enc in self.abspaths(fileids, True)])

    def measures(self):
        fileids = "Vocabulary_measure.txt"
        return concat([VocabularyStreamReader(fileid, enc)
                       for fileid, enc in self.abspaths(fileids, True)])

    def proper_nouns(self):
        fileids = "Vocabulary_proper_noun.txt"
        return concat([VocabularyPairStreamReader(fileid, enc)
                       for fileid, enc in self.abspaths(fileids, True)])

    def phrasal_verbs(self):
        fileids = "Vocabulary_phrasal_verb.txt"
        return concat([VocabularyPairStreamReader(fileid, enc)
                       for fileid, enc in self.abspaths(fileids, True)])

    def external_ace_rules(self):
        fileids = "External_rules.txt"

        return concat([VocabularyWholeLineStreamReader(fileid, enc)
                       for fileid, enc in self.abspaths(fileids, True)])

    def generate_ace_noun_rules(self):
        # - noun_sing_statement_list = []
        # - noun_plu_statement_list = []
        for noun in self.nouns():
            singular_noun = self.vocabulary.singularize(noun)
            plural_noun = self.vocabulary.pluralize(noun)
            noun_sing_statement = "noun_sg({}, {}, neutr).".format(
                singular_noun, noun)
            noun_plu_statement = "noun_pl({}, {}, neutr).".format(
                plural_noun, noun)

            self._inverse_map[singular_noun] = noun
            self._inverse_map[plural_noun] = noun

            yield noun_sing_statement
            yield noun_plu_statement
            # - noun_sing_statement_list.append(noun_sing_statement)
            # - noun_plu_statement_list.append(noun_plu_statement)

        # - return noun_sing_statement_list + noun_plu_statement_list
    def generate_ace_mass_noun_rules(self):
        for mass_noun in self.mass_nouns():
            mass_noun_statement = "noun_mass({}, {}, neutr).".format(
                mass_noun, mass_noun)
            yield mass_noun_statement

    def generate_ace_verb_rules(self):
        # for verb in self.verbs():
        # - bare_statemenet_list = []
        # - intransitive_sing_statement_list = []
        # - intransitive_plu_statement_list = []
        # - transitive_sing_statement_list = []
        # - transitive_plu_statement_list = []
        # - gerund_as_noun_sing_statement_list = []
        # - gerund_as_mass_noun_statement_list = []
        # - gerund_as_adj_statement_list = []
        # - ed_statement_list = []
        for verb in self.verbs():
            bare_word = verb
            gerund_word = self.vocabulary.conjugate_gerund(verb)
            singularize_verb_word = self.vocabulary.conjugate_singularize(verb)
            ed_word = self.vocabulary.conjugate_ed(verb)

            intransitive_sing_statement = "iv_finsg({}, {}).".format(
                singularize_verb_word, verb)
            intransitive_plu_statement = "iv_infpl({}, {}).".format(
                verb, verb
            )
            transitive_sing_statement = "tv_finsg({}, {}).".format(
                singularize_verb_word, verb
            )
            transitive_plu_statement = "tv_infpl({}, {}).".format(
                verb, verb
            )
            gerund_as_mass_noun_statement = "noun_mass({}, {}, neutr).".format(
                gerund_word, gerund_word
            )
            gerund_as_adj_statement = "adj_itr({}, {}).".format(
                gerund_word, gerund_word)
            gerund_as_noun_sing_statement = "noun_sg({}, {}).".format(
                gerund_word, gerund_word)
            ed_statement = "tv_pp({}, {}).".format(ed_word, verb)

            self._inverse_map[gerund_word] = verb
            self._inverse_map[singularize_verb_word] = verb
            self._inverse_map[ed_word] = verb

            yield intransitive_sing_statement
            yield intransitive_plu_statement
            yield transitive_sing_statement
            yield transitive_plu_statement
            yield gerund_as_mass_noun_statement
            yield gerund_as_noun_sing_statement
            yield gerund_as_adj_statement
            yield ed_statement
            # - intransitive_sing_statement_list.append(
            # -     intransitive_sing_statement)
            # - intransitive_plu_statement_list.append(
            # -     intransitive_plu_statement
            # - )
            # - transitive_sing_statement_list.append(
            # -     transitive_sing_statement
            # - )
            # - transitive_plu_statement_list.append(
            # -     transitive_plu_statement
            # - )
            # - gerund_as_mass_noun_statement_list.append(
            # -     gerund_as_mass_noun_statement
            # - )
            # - gerund_as_noun_sing_statement_list.append(
            # -     gerund_as_noun_sing_statement
            # - )
            # - gerund_as_adj_statement_list.append(
            # -     gerund_as_adj_statement
            # - )
            # - ed_statement_list.append(
            # -     ed_statement
            # - )

    def generate_ace_adj_rules(self):
        # - adj_statement_list = []
        # - adj_comp_statement_list = []
        # - adj_sup_statement_list = []
        # - adv_statement_list = []
        for adj in self.adjectives():
            bare_word = adj
            comparative_word = comparative(adj)
            if len(word_tokenize(comparative_word)) > 1:
                comparative_word = None

            superlative_word = superlative(adj)
            if len(word_tokenize(superlative_word)) > 1:
                superlative_word = None

            adverb = get_word_forms(adj)["r"]
            if len(adverb) == 0:
                adverb = None

            adj_statement = "adj_itr({}, {}).".format(adj, adj)
            yield adj_statement
            # - adj_statement_list.append(adj_statement)

            if comparative_word is not None:
                adj_comp_statement = "adj_itr_comp({}, {}).".format(
                    comparative_word, adj)

                self._inverse_map[comparative_word] = adj
                yield adj_comp_statement

                # - adj_comp_statement_list.append(adj_comp_statement)

            if superlative_word is not None:
                adj_sup_statement = "adj_itr_sup({}, {}).".format(
                    superlative_word, adj)

                self._inverse_map[superlative_word] = adj
                yield adj_sup_statement

                # - adj_sup_statement_list.append(adj_sup_statement)

            if adverb is not None:
                for adv in adverb:
                    adv_statement = "adv({}, {}).".format(adv, adv)

                    self._inverse_map[adv] = adj
                    yield adv_statement
                    # - adv_statement_list.append(adv_statement)
        # - return (adj_statement_list, adj_comp_statement_list, adj_sup_statement_list, adv_statement_list)

    def generate_ace_measure_rules(self):
        # - measure_sing_statement_list = []
        # - measure_plu_statement_list = []
        for measure in self.measures():
            measure_sing_statement = "mn_sg({}, {}).".format(measure, measure)
            measure_plu_statement = "mn_pl({}, {}).".format(measure, measure)
            yield measure_sing_statement
            yield measure_plu_statement
            # - measure_sing_statement_list.append(measure_sing_statement)
            # - measure_plu_statement_list.append(measure_plu_statement)

        # - return (measure_sing_statement_list, measure_plu_statement_list)

    def generate_ace_prep_rules(self):
        # - prep_statement_list = []
        for prep in self.preps():
            prep_statement = "prep({}, {}).".format(prep, prep)
            yield prep_statement
            # - prep_statement_list.append(prep_statement)
        # - return prep_statement_list

    def generate_ace_proper_rules(self):
        for proper_noun, type_ in self.proper_nouns():
            proper_noun_statement = "pn_sg('{}', '{}', {}).".format(
                proper_noun, proper_noun, type_)
            yield proper_noun_statement

    def generate_ace_phrasal_verb_rules(self):
        for verb, particle in self.phrasal_verbs():
            singularize_verb_word = self.vocabulary.conjugate_singularize(
                verb)
            phrasal_verb = verb+"_"+particle
            singularize_phrasal_verb = singularize_verb_word + "_" + particle
            self._vocab.word2index([phrasal_verb], train=True)

            self._inverse_map[phrasal_verb] = phrasal_verb
            self._inverse_map[singularize_phrasal_verb] = phrasal_verb

            intransitive_phrasal_verb_sing_statement = "iv_finsg({}, {}).".format(
                singularize_phrasal_verb, phrasal_verb
            )
            yield intransitive_phrasal_verb_sing_statement
            intransitive_phrasal_verb_plu_statement = "iv_infpl({}, {}).".format(
                phrasal_verb, phrasal_verb
            )
            yield intransitive_phrasal_verb_plu_statement
            transitive_phrasal_verb_sing_statement = "tv_finsg({}, {}).".format(
                singularize_phrasal_verb, phrasal_verb
            )
            yield transitive_phrasal_verb_sing_statement
            transitive_phrasal_verb_plu_statement = "tv_infpl({}, {}).".format(
                phrasal_verb, phrasal_verb
            )
            yield transitive_phrasal_verb_plu_statement

            # phrasal_verb_sing_statement = ""
    def generate_external_ace_rules(self):
        for rule in self.external_ace_rules():
            yield rule

    def generate_ace_all_rules(self):
        for statement in self.generate_ace_noun_rules():
            yield statement
        for statement in self.generate_ace_mass_noun_rules():
            yield statement
        for statement in self.generate_ace_verb_rules():
            yield statement
        for statement in self.generate_ace_phrasal_verb_rules():
            yield statement
        for statement in self.generate_ace_adj_rules():
            yield statement
        for statement in self.generate_ace_prep_rules():
            yield statement
        for statement in self.generate_ace_measure_rules():
            yield statement
        for statement in self.generate_ace_proper_rules():
            yield statement
        try:
            for statement in self.generate_external_ace_rules():
                yield statement
        except:
            pass

    def update_vocabulary(self):
        print("Vocabulary before updating: vocab -- {} / inverse -- {}".format(
            self.vocabulary, self._inverse_map))
        for statement in tqdm(self.generate_ace_all_rules()):
            pass
        print(
            "Vocabulary after updating: vocab -- {} / inverse -- {}".format(self.vocabulary, self._inverse_map))
        vocabulary_filename = "vocabulary.pkl"
        vocabulary_file = open(vocabulary_filename, "wb")
        dill.dump(reader, vocabulary_file)
        vocabulary_file.close()

    def create_ace_lexicon(self):
        filename = "clex_lexicon.pl"
        file_ = open(filename, "w")
        print ("Open file '{}'...".format(filename))

        print ("Saving...")
        for statement in tqdm(self.generate_ace_all_rules()):
            file_.write(statement + "\n")
        print ("Finish")

        file_.close()
        vocabulary_filename = "vocabulary.pkl"
        vocabulary_file = open(vocabulary_filename, "wb")
        dill.dump(reader, vocabulary_file)
        vocabulary_file.close()


if __name__ == "__main__":
    # * Call this function at "work_space/src/crl":
    # * $ python scripts/crl_node.py
    # reader = VocabularyReader("scripts/Vocabulary", "Voca.*\.txt")
    # reader.create_ace_lexicon()
    pass
