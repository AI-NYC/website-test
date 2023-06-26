# Crypto NYC

Welcome to Crypto NYC! We have a variety of events. Check them out below:

## WPW Events

- **June 26, 2023** » [Tempalte](events/template.md)
- **June 30, 2023** » [Crypto Discussion](events/wpw-2023-06-30.md)

## How to update this repo

The content in this repo is generated automatically. We run otter.ai in our meetings to transcribe them. The transcription is then summarized with GPT 3.5 and pushed into this repo:
![Meeting AI Agent](https://github.com/EtnaLabs/website-test/assets/540035/6fb33d35-3f92-4565-aa11-5c904c20da86.png)

### How to run the summarizer

1. Clone this repo, then install the requirements

```bash
poetry install
```

2. Run the summarizer script with the path to the transcription file as a command-line argument:
```bash
poetry run python summarizer.py ~/Downloads/your-transcription.txt
```
The script will prompt you for the following information:
- Date of the meeting (in YYYY-MM-DD format)
- Topic of the meeting
- Attendees of the meeting (comma-separated)
After you provide this information, the script will update the README.md and generate an event file.

3. Commit the changes and push them to the repo:
```bash
git add .
git commit -m "Add new event"
git push
```