from transformers import pipeline
import csv
with open("AIproject/comments.csv", "r", encoding="utf-8") as file:
    lines = [line.strip() for line in file.readlines()]
classifier = pipeline("sentiment-analysis")
for line in lines:
    res = classifier(line)
    print(res)
    print("\n")


