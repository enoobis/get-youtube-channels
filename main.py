import os
import requests
import json

# Define the API key for the YouTube Data API
api_key = os.environ['API_KEY']

# Define the parameters for the search request
params = {
    "part": "snippet",
    "q": "python projects",
    "type": "channel",
    "maxResults": 50,
    "key": api_key
}

# Send the search request
response = requests.get("https://www.googleapis.com/youtube/v3/search", params=params)

# Get the JSON data from the response
data = response.json()

# Open a text file for writing
with open("youtube_channels.txt", "w") as file:
    # Loop through the results
    for item in data["items"]:
        # Get the channel ID
        channel_id = item["snippet"]["channelId"]

        # Define the parameters for the channel statistics request
        params = {
            "part": "statistics",
            "id": channel_id,
            "key": api_key
        }

        # Send the channel statistics request
        response = requests.get("https://www.googleapis.com/youtube/v3/channels", params=params)

        # Get the JSON data from the response
        channel_data = response.json()

        # Get the number of subscribers
        subscribers = channel_data["items"][0]["statistics"]["subscriberCount"]

        # Check if the number of subscribers is less than 1000
        if int(subscribers) < 100:
            # Write the channel name, number of subscribers, and link to the text file
            file.write(item["snippet"]["channelTitle"] + " " + subscribers + " " + "https://www.youtube.com/channel/" + channel_id + "\n")