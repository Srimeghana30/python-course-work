#Assignment-1 YouTube Video Catalog System

# Task 1: Taking video metadata details as input
video_id = input("Enter Video ID: ") 
title = input("Enter Video Title: ")
uploader = input("Enter Uploader (Channel Name): ")
category = input("Enter Category (e.g., Music, Education, Vlog): ")
duration = float(input("Enter Video Duration (in minutes): "))

# Tuple for views and likes
views = int(input("Enter Number of Views: "))
likes = int(input("Enter Number of Likes: "))
stats = (views, likes)

# Set for tags
tags_input = input("Enter Tags (comma-separated): ")
tags = set(tag.strip() for tag in tags_input.split(","))

# Dict for monetization info
ad_type = input("Enter Ad Type (e.g., Skippable, Non-Skippable): ")
revenue_share = float(input("Enter Revenue Share Percentage: "))
monetization_info = {
    "Ad Type": ad_type,
    "Revenue Share": revenue_share
}

# Task 2: Display video information using formatting methods

# 1. Comma Separation
print("Video ID, Title, Uploader:", video_id, title, uploader, sep=", ")

# 2. Percentage Formatting
print("Revenue Share: %.1f%%" % monetization_info["Revenue Share"])

# 3. f-strings
print(f"\n Video Title: {title}")
print(f" Uploaded by: {uploader}")
print(f" Category: {category}")
print(f" Duration: {duration} minutes")
print(f" Stats: {stats[0]} views, {stats[1]} likes")
print(f" Tags: {','.join(tags)}")
print(f" Monetization: {monetization_info['Ad Type']} Ad")

# 4. .format() method
print("\n Summary:")
print("Video '{}' (ID: {}) by {} falls under '{}' category.".format(title, video_id, uploader, category))
print("It has {} views and {} likes.".format(stats[0], stats[1]))
print("Ad Type: {}, Revenue Share: {:.2f}%".format(monetization_info["Ad Type"], monetization_info["Revenue Share"]))
