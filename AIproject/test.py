import csv
import googleapiclient.discovery
import googleapiclient.errors

DEVELOPER_KEY = ""
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

youtube = googleapiclient.discovery.build(
    YOUTUBE_API_SERVICE_NAME, 
    YOUTUBE_API_VERSION, 
    developerKey=DEVELOPER_KEY
)

video_id = "F0BBMvSMMlg"

try:
    comments = []
    
    # Call the API to retrieve the first 20 comments
    response = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        textFormat="plainText",
        maxResults=20
    ).execute()
    
    # Extract the comment text from the API response
    for item in response["items"]:
        comment = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
        comments.append(comment)

    # Write the comments to a CSV file
    with open('comments.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Comment"])
        for comment in comments:
            writer.writerow([comment])

    print(f"{len(comments)} comments saved to comments.csv")

except googleapiclient.errors.HttpError as error:
    print(f"An error occurred: {error}")