from textblob import TextBlob
import csv

# Open the CSV file and read the comments into a list
with open("comments.csv", "r", encoding="utf-8") as file:
    lines = [line.strip() for line in file.readlines()]

# Define a function to perform sentiment analysis using TextBlob
def get_sentiment(line):
    blob = TextBlob(line)
    polarity = blob.sentiment.polarity
    if polarity > 0.1:
        return "positive"
    elif polarity < -0.1:
        return "negative"
    else:
        return "neutral"

# Loop through the lines and print the sentiment of each line
for line in lines:
    sentiment = get_sentiment(line)
    print(f"{line}: {sentiment}")
