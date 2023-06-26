import os
from datetime import datetime

def create_event(date, topic, participants, transcription):
    # Parse the date string and reformat it
    date_object = datetime.strptime(date, "%Y-%m-%d")
    formatted_date = date_object.strftime("%B %d, %Y")

    event_filename = f"events/wpw-{date}.md"
    with open(event_filename, 'w') as file:
        file.write(f"## {topic}\n")
        file.write(f"**Date:** {formatted_date}\n")
        file.write(f"**Participants:** {participants}\n")
        file.write("\n")
        file.write(f"## Meeting Transcription\n")
        file.write(transcription)
    
    # Now, update the README.md file
    with open('README.md', 'a') as readme:
        readme.write(f"\n- **{formatted_date}** » [{topic}](events/wpw-{date}.md)")

# Use the function to create an event
create_event("2023-06-30", "Crypto Discussion", "Alice, Bob, Charlie", "This is a test event.")
