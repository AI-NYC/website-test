import os
import argparse
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
    with open('README.md', 'r+') as readme:
        content = readme.read()
        position = content.find("## WPW Events")
        position = content.find('\n', position) + 1
        line_to_insert = f"- **{date}** » [{topic}](events/wpw-{date}.md)\n"
        content = content[:position] + line_to_insert + content[position:]
        readme.seek(0)
        readme.write(content)

def get_summary(transcription):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    chunks = [transcription[i:i + 4090] for i in range(0, len(transcription), 4090)]
    full_summary = ""
    for chunk in chunks:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a video meeting assistant."},
                {"role": "user", "content": f"Summarize the video meeting text into a list of topics and takes discussed, with links if any: {chunk}"},
            ]
        )
        full_summary += response['choices'][0]['message']['content']
    return full_summary

def format_date(date):
    date_object = datetime.strptime(date, "%Y-%m-%d")
    return date_object.strftime("%B %d, %Y")

def create_event(transcription_path):
    date = input("Enter the date of the meeting (YYYY-MM-DD): ")
    topic = input("Enter the topic of the meeting: ")
    participants = input("Enter the attendees of the meeting (comma-separated): ")

    with open(transcription_path, 'r') as file:
        transcription = file.read()

    formatted_date = format_date(date)
    summary = get_summary(transcription)
    create_event_file(formatted_date, topic, participants, transcription, summary)
    update_readme(formatted_date, topic)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Summarize a meeting transcription.')
    parser.add_argument('transcription_path', type=str, help='The path to the meeting transcription file.')
    args = parser.parse_args()
    create_event(args.transcription_path)
