
import boto3
import re
import emoji
import nltk
nltk.download('words')
words = set(nltk.corpus.words.words())

def retrieve_data(dynamodb=None):

    if not dynamodb:
        dynamodb = boto3.resource("dynamodb")

    table = dynamodb.Table("Tweets")
    response = table.scan()
    data = response['Items']

    for item in data :
        record = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) |(\w+:\/\/\S+)", " ", item['tweet']).split())
       # with open("tweets.txt" , "a") as file:
        #    file.write(record+"\n")
        cleaner_data(item['tweet'])
        #print(record)


def cleaner_data(tweet):
    tweet = re.sub("@[A-Za-z0-9]+", "", tweet)  # Remove @ sign
    tweet = re.sub(r"(?:\@|http?\://|https?\://|www)\S+", "", tweet)  # Remove http links
    tweet = " ".join(tweet.split())
    tweet = ''.join(c for c in tweet if c not in emoji.UNICODE_EMOJI)  # Remove Emojis
    tweet = tweet.replace("#", "").replace("_", " ")  # Remove hashtag sign but keep the text
    #tweet = " ".join(w for w in nltk.wordpunct_tokenize(tweet) \
    #                if w.lower() in words or not w.isalpha())
    print(tweet)


if __name__ == '__main__':
    retrieve_data()