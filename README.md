# kaggle-twitter-sentiment
Analyze how travelers in February 2015 expressed their feelings on Twitter

<br/><br/>

## Data set:
14 640 tweets with sentiment: neutral, positive or negative

![sentiment](https://user-images.githubusercontent.com/67274837/153897294-8397a8cd-423d-45fb-820f-a748653a55ca.png)

<br/><br/>

## Data preparation:
![image](https://user-images.githubusercontent.com/67274837/153902974-058f974b-2ddc-4cbe-a66f-8d2ccc104978.png)

### 1. Cleaning data
    Deleting hashtags, web page urls, numbers, emoticons etc.
    From:
      "@VirginAmerica help, left expensive headphones on flight 89 IAD to LAX today. Seat 2A. No one answering L&amp;F number at LAX!"
    To:
      ['help', 'left', 'expensive', 'headphones', 'on', 'flight', 'IAD', 'to', 'LAX', 'today', 'Seat', 'A', 'No', 'one', 'answering', 'LampF', 'number', 'at', 'LAX']

### 2. Lemmatization
    The goal of lemmatization is to reduce related word forms to a common base form.
    For example:
      Playing -> Play
      Plays   -> Play
      Played  -> Play
    From:
      ['help', 'left', 'expensive', 'headphones', 'on', 'flight', 'IAD', 'to', 'LAX', 'today', 'Seat', 'A', 'No', 'one', 'answering', 'LampF', 'number', 'at', 'LAX']
    To:
      ['help', 'left', 'expend', 'headphon', 'on', 'flight', 'iad', 'to', 'lax', 'today', 'seat', 'a', 'no', 'on', 'answ', 'lampf', 'numb', 'at', 'lax']

### 3. Creating bag of words
    List of all lemmatized words in all tweets.
    Example:
      ['malcom', 'throne', 'gopatriot', 'awhil', 'plu', 'servicelook', 'screens', 'surveyemail', 'muc', 'acarlcom', 'banan', 'pia', 'waitin', 
      'forev', 'pricew', 'minno', 'bitchy',     'delh', 'havin', 'dee', 'cxp', 'daynot', 'woe', 'onal', 'ho', 'lord', 'cxldprotection', 'phoneon', 
      'tast', 'delinqu', 'lindsey', 'wop', 'thrown', 'ahhhhh', 'spf', 'nw', ... ]

### 4. Tokenization
    Changing tweets into vectors with 0 and 1.
    1 if word from bag of words exist in tweet, 0 when not exist.
    From:
      ['help', 'left', 'expend', 'headphon', 'on', 'flight', 'iad', 'to', 'lax', 'today', 'seat', 'a', 'no', 'on', 'answ', 'lampf', 'numb', 'at', 'lax']
    To:
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ... ]

### 5. Column normalization
    Normalization of tweets by columns (by the words from the bag of words)

<br/><br/>

## Data Classification:

| Place | Classifier | Accuracy |
| -- | -- | -- |
| 1 | Bernoulli Naive Bayes | 0.78 |
| 2 | Random Forest | 0.76 |
| 3 | Multi-layer Perceptron classifier | 0.73 |
| 4 | Logistic Regression | 0.67 |
| 5 | Gaussian  Naive Bayes | 0.4 |

![acc_time](https://user-images.githubusercontent.com/67274837/153903290-b0da4f29-09ba-4719-9697-6e4143845fe4.png)
