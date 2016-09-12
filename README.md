# discord-bot
A Discord bot written in Python with discord.py.

## Commands
The following commands are currently supported by this bot:
* !rickroll \<channel\>: Joins 'channel', and begins playing Rick Astley's "Never Gonna Give You Up".
* !youtube \<url\> \<channel\>: Joins 'channel', and begins playing the audio of the YouTube video found at 'url'.
* !disconnect: Disconnects from the voice channel the bot is in.

## Requirements
The following packages are required to run the bot:
* Python 3.5 or higher.
* discord.py[voice]
* ffmpeg
* youtubedl
