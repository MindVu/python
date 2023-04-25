from TikTokApi import TikTokApi
import csv

# TikTok video URL
url = 'https://www.tiktok.com/@thokhoakyanh/video/7224335838434413829?_t=8bhauNj9nIv&_r=1'

# Initialize TikTokAPI instance
api = TikTokApi()

# Get video ID
video_id = api.get_Video_By_Url(url, return_bytes = 0, custom_verifyFp="")

# Get video info
video_info = api.get_Video_By_Id(video_id)

# Extract top 20 comments
comments = video_info['itemInfos']['commentList'][:20]

# Write comments to CSV file
with open('comments.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Author', 'Text', 'Likes', 'Timestamp'])
    for comment in comments:
        author = comment['author']['uniqueId']
        text = comment['text']
        likes = comment['diggCount']
        timestamp = comment['createTime']
        writer.writerow([author, text, likes, timestamp])
