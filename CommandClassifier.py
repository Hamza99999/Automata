from nltk import NaiveBayesClassifier
from nltk.tokenize import word_tokenize
import csv


ALL_WORDS  = None
CLASSIFIER = None


def init():
	global ALL_WORDS
	global CLASSIFIER
	training_data = []

	file          = open("training_data.csv", 'rb') # Training data
	reader        = csv.reader(file)

	for row in reader:
		training_data.append((row[0], row[1]))

	file.close()

	ALL_WORDS      = set(word.lower() for passage in training_data for word in 
		                 word_tokenize(passage[0]))
	trainig_object = [({word: (word in word_tokenize(x[0])) for word in 
		                ALL_WORDS}, x[1]) for x in training_data]
	CLASSIFIER     = NaiveBayesClassifier.train(trainig_object)


def decode_command(command):
	global ALL_WORDS
	global CLASSIFIER

	test_sent_features = {word.lower(): (word in word_tokenize(
						  command.lower())) for word in ALL_WORDS}
	return CLASSIFIER.classify(test_sent_features)