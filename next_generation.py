
import multiprocessing

import os

import re

import nltk

import gensim.models.word2vec as w2v

from nltk.corpus import stopwords

import logging

from word_extractory import article_generator_text


class NextGen:

    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

    raw_corpus = None

    query = None

    topic2vec = None

    stop_words_additional = {'should', 'could', 'again', 'likewise', 'of course', 'like', 'as', 'too', 'would',
                             'around', 'provide', 'whatever', 'even', 'this', 'way', 'the'}


    def __init__(self, corpus, user_query):
        self.raw_corpus = corpus
        self.query = user_query

    def preprocessing(self):

        nltk.download('punkt')

        nltk.download('stopwords')

        tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

        raw_sentences = tokenizer.tokenize(self.raw_corpus)

        sentences = []

        stop_words = set(stopwords.words('english'))

        for raw_sentence in raw_sentences:
            if len(raw_sentence) > 0 and raw_sentence not in stop_words:
                sentences.append(self.sentence_to_wordlist(raw_sentence))

        return sentences


    def sentence_to_wordlist(self, raw):

        stop_words = set(stopwords.words('english'))

        clean = re.sub("[^a-zA-Z]"," ", raw)

        words = clean.split()

        filtered_words = list(filter(lambda x: x.lower() not in stop_words not in self.stop_words_additional, words))

        return filtered_words



    def train_model(self, sentences):

        num_of_features = 200

        min_word_count = 3

        num_processors = multiprocessing.cpu_count()

        context_size = 7

        downsampling = 1e-3

        seed = 1

        topic2vec = w2v.Word2Vec(
            sg=1,
            seed=seed,
            workers=num_processors,
            size=num_of_features,
            min_count=min_word_count,
            window=context_size,
            sample=downsampling
        )

        topic2vec.build_vocab(sentences)

        return topic2vec


    def save_model(topic2vec):
        if not os.path.exists("trained"):
            os.makedirs("trained")


    def process_query(self):

        self.get_model()

        next_generation_words = self.get_next_similarity()

        return next_generation_words


    def get_model(self):

        global topic2vec

        sentences = self.preprocessing()

        topic2vec = self.train_model(sentences)


    def get_next_similarity(self):

        global topic2vec

        filtered_queries = []

        splitted_query = self.query.split(' ')

        for word in splitted_query:
            try:
                filtered_queries.append(topic2vec.most_similar(word))
            except KeyError as e:
                self.process_invalid_query(self.query)
                filtered_queries.append(topic2vec.most_similar(word))

        word_to_rating = {}

        for query in filtered_queries[0]:
            if query[0] in word_to_rating:
                word_to_rating[query[0]] = word_to_rating[query[0]] * 2
            else:
                word_to_rating[query[0]] = query[1]

        ranked_words = sorted(word_to_rating, key=word_to_rating.get, reverse=True)

        for word in ranked_words:
            if len(word) < 3 or word.__contains__('ing'):
                ranked_words.remove(word)

        return ranked_words


    def process_invalid_query(self, word):

        new_text_base = article_generator_text(word, 10)

        self.raw_corpus = self.str_join(self.raw_corpus, ' ', new_text_base)

        print(self.raw_corpus)

        self.get_model()


    def str_join(*args):
        return ''.join(map(str, args))

    def check_relevant_words(self):
        global topic2vec
        output_total_words = self.process_generations()
        relevant_words = dict.fromkeys(output_total_words)
        for key in relevant_words:
            relevant_words[key] = 0
        for word in output_total_words:
            processed_word_list = topic2vec.most_similar(word)
            for other_word in processed_word_list:
                if other_word in output_total_words:
                    relevant_words[other_word] = relevant_words[other_word] + 1
        output_list = []
        relevant_words = sorted(relevant_words, key=relevant_words.get, reverse=True)
        for x in range(5):
            output_list.append(relevant_words[x])
        return output_list

    def convert_relevant_words_article(self):
        relevant_query_list = self.check_relevant_words()
        string_output = ""
        for word in relevant_query_list:
            string_output += str(word) + " "
        return article_generator_text(string_output, 1)

    def process_generations(self):
        set_total_words = set()
        for x in range(6):
            self.get_model()
            list_similar = self.get_next_similarity()
            self.mutated_query = list_similar[0]
            for word in list_similar:
                set_total_words.add(word)
        return list(set_total_words)
