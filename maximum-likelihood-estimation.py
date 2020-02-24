# Maximum Likelihood Estimation Example

# An intuitive way to estimate n-gram probabilities is called Maximum Likelihood Estimation or MLE. We get the MLE estimate for the parameters of an n-gram model by getting counts from a corpus, and normalizing the counts so that they lie between 0 and 1. For example, to compute a particular bigram probability of a word y given previous word x, we'll compute the count of the bigram C(xy) and normalize by the sum of all the bigrams that share the same first word x. We can simplify this equation, since the sum of all bigram counts that start with a given word w[n-1] must be equal to the unigram count for that word w[n-1].

# Let's work through an example using a mini-corpus of three sentences. We'll first need to augment each sentence with a special symbol <s> at the beginning of the sentence, to give us the bigram context of the first word. We'll also need a special end-symbol. </s>

# For probabilistic models, normalizing means dividing by some total count so that the resulting probabilities fall legally between 0 and 1.

# We need the end-symbol to make the bigram grammar a true probability distribution. Without an end-symbol, the sentence probabilities for all sentences of a given length would sum to one. This model would define an infinite set of probability distributions, with one distribution per sentence length.

from collections import Counter

sentences = ['I am Sam', 'Sam I am', 'I do not like green eggs and ham']
sentences = [['<s>'] + sentence.split() + ['</s>'] for sentence in sentences]

flatten = lambda l: [item for sublist in l for item in sublist]

unigram = flatten(sentences)
unigram_count = Counter(unigram)
# print(unigram_count)

bigram = [(sentence[i-1], sentence[i]) for sentence in sentences for i in range(1, len(sentence))]
bigram_count = Counter(bigram)
# print(bigram_count)

print('P(I|<s>) = ' + str(bigram_count[('<s>', 'I')] / unigram_count['<s>']))
print('P(Sam|<s>) = ' + str(bigram_count['<s>', 'Sam'] / unigram_count['<s>']))
print('P(am|I) = ' + str(bigram_count['I', 'am'] / unigram_count['I']))
print('P(</s>|Sam) = ' + str(bigram_count['Sam', '</s>'] / unigram_count['Sam']))
print('P(Sam|am) = ' + str(bigram_count['am', 'Sam'] / unigram_count['am']))
print('P(do|I) = ' + str(bigram_count['I', 'do'] / unigram_count['I']))
