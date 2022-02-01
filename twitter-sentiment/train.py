from nltk.stem import LancasterStemmer
import pandas as pd


def read_data(file_path: str,
              delimiter: str = ",",
              headers: bool = True) -> pd.DataFrame:
    if headers:
        return pd.read_csv(file_path, sep=delimiter)
    return pd.read_csv(file_path, sep=delimiter, header=None)


data_frame = read_data("twitter-sentiment/data/Tweets.csv")
tweets_frame = data_frame["text"]
tweets_list = tweets_frame.to_numpy().flatten().tolist()
words = []


def clean_text(text: str) -> str:
    letters = list(" qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM")
    for symbol in text:
        if symbol not in letters:
            text = text.replace(symbol, "")
    return text


for tweet in [clean_text(tweet).split(" ") for tweet in tweets_list]:

    words += [word.strip() for word in tweet
              if word != "" and "http" not in word and not word.isdigit()]

lancaster = LancasterStemmer()
stemmed_words = list(set([lancaster.stem(word) for word in words]))

print(stemmed_words)
