import os
import openai
from datetime import datetime

def create_event_file(date, topic, participants, transcription, summary):
    event_filename = f"events/wpw-{date}.md"
    with open(event_filename, 'w') as file:
        file.write(f"## {topic}\n")
        file.write(f"**Date:** {date}\n")
        file.write(f"**Participants:** {participants}\n")
        file.write("\n")
        file.write(f"## Summary\n")
        file.write(summary)

def update_readme(date, topic):
    with open('README.md', 'a') as readme:
        readme.write(f"\n- **{date}** » [{topic}](events/wpw-{date}.md)")

def get_summary(transcription):
    openai.api_key = 'your-api-key'
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Summarize the following meeting transcription: {transcription}"},
        ]
    )
    return response['choices'][0]['message']['content']

def format_date(date):
    date_object = datetime.strptime(date, "%Y-%m-%d")
    return date_object.strftime("%B %d, %Y")

def create_event(date, topic, participants, transcription):
    formatted_date = format_date(date)
    summary = get_summary(transcription)
    create_event_file(formatted_date, topic, participants, transcription, summary)
    update_readme(formatted_date, topic)

# Use the function to create an event
create_event("2023-06-30", "Crypto Discussion", "Alice, Bob, Charlie", "This is a test event.")
