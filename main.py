import instaloader
import csv

username = "joe_mama2833"
password = "mothaiba"
link = input("Search link: ")
link.split("/")[-2]
L = instaloader.Instaloader()

L.context.login(username, password)


post = instaloader.Post.from_shortcode(L.context, shortcode=link.split("/")[-2])

comments = post.get_comments()


 #Save comments to a CSV file
with open('comments.csv', 'w', newline='', encoding='utf-8-sig') as file:
     writer = csv.writer(file)
     writer.writerow(['Comment'])
     for comment in comments:
         writer.writerow([comment.text])