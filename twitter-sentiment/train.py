from sklearn.preprocessing import StandardScaler
from nltk.stem import LancasterStemmer
import pandas as pd


def read_data(file_path: str,
              delimiter: str = ",",
              headers: bool = True) -> pd.DataFrame:
    if headers:
        return pd.read_csv(file_path, sep=delimiter)
    return pd.read_csv(file_path, sep=delimiter, header=None)


def clean_sentence(text: str) -> str:
    letters = list(" qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM")
    for symbol in text:
        if symbol not in letters:
            text = text.replace(symbol, "")
    return text


def clean_sentences(sentences_list: list[str]) -> list[list[str]]:
    """
    Input:
     * sentences_list: list[str] - list of sentences

    Output:
     * list[list[str]] - list of cleansed sentences (without special symbols)

    Example:
        Input: ["Hello my World!",
                "How are you?"]

        Output: [["Hello", "my", "World"],
                 ["How", "are", "you"]]
    """
    cleansed_sentences = []
    for tweet in [clean_sentence(tweet).split(" ")
                  for tweet in sentences_list]:

        cleansed_sentence = [word.strip() for word in tweet
                             if
                             word != "" and
                             "http" not in word and
                             not word.isdigit()]

        cleansed_sentences.append(cleansed_sentence)

    return cleansed_sentences


def flat_lists(sentences_list: list[list[str]]) -> list[str]:
    words = []
    for sentence in sentences_list:
        words += sentence
    return words


def lemmatization_sentence(sentence: list[str],
                           lancaster: LancasterStemmer) -> list[str]:

    return [lancaster.stem(word) for word in sentence]


# [ take tweets ]
data_frame = read_data("twitter-sentiment/data/Tweets.csv")
# tweets_frame = data_frame["text"]
# tweets_sentiment_frame = data_frame["airline_sentiment"]
# tweets_list = tweets_frame.to_numpy().flatten().tolist()
# tweets_sentiment_list = tweets_sentiment_frame.to_numpy().flatten().tolist()
#
data_frame = data_frame[["text", "airline_sentiment"]]
print(data_frame)

data_frame["text"] = clean_sentences(data_frame["text"])
print(data_frame)

cleansed_words = flat_lists(data_frame["text"])
lancaster = LancasterStemmer()
stemmed_words = lemmatization_sentence(cleansed_words, lancaster)
bag_of_words = list(set(stemmed_words))
print(bag_of_words)


def sentence_coding(sentence: list[str],
                    bag_of_words: list[str]) -> list[bool]:
    # 1 - word occurs in the bag of words
    # 0 - word does not appear in the sentence
    return [1 if word in sentence else 0 for word in bag_of_words]


def sentences_coding(sentences: list[list[str]],
                     bag_of_words: list[str]) -> list[bool]:
    return [sentence_coding(sentence, bag_of_words) for sentence in sentences]


# [ change words for numbers ]
temp_data_frame = pd.DataFrame(
    sentences_coding(data_frame["text"], bag_of_words)
    )

data_frame = temp_data_frame.join(data_frame["text"])
print(data_frame)

# the_cleansed_sentences = clean_sentences(tweets_list)
# cleansed_words = flat_lists(the_cleansed_sentences)

# # [ lemmatization ]
# lancaster = LancasterStemmer()
# stemmed_words = lemmatization_sentence(cleansed_words, lancaster)
# bag_of_words = list(set(stemmed_words))


# def sentence_coding(sentence: list[str],
#                     bag_of_words: list[str]) -> list[bool]:
#     return [1 if word in sentence else 0 for word in bag_of_words]


# # [ change words for numbers ]
# # 1 - word occurs in the bag of words
# # 0 - word does not appear in the sentence
# coded_sentences = []
# for row in the_cleansed_sentences:
#     row = lemmatization_sentence(row, lancaster)
#     coded_sentences.append(sentence_coding(row, bag_of_words))

# # [ change sentiment for numbers ]
# # 1 - neutral
# # 2 - positive
# # 3 - negative
# coded_sentiments = []
# for sentiment in tweets_sentiment_list:
#     if sentiment == "neutral":
#         coded_sentiments.append(1)
#     elif sentiment == "positive":
#         coded_sentiments.append(2)
#     elif sentiment == "negative":
#         coded_sentiments.append(3)

# print("Neutral tweets: ", coded_sentiments.count(1))
# print("Positive tweets:", coded_sentiments.count(2))
# print("Negative tweets:", coded_sentiments.count(3))
# scaler = StandardScaler()
