import discord
from discord.ext import commands

def main():
    bot = commands.Bot(command_prefix='!')
    bot.load_extension('voice_bot')

    token = 'your_token_here'

    bot.run(token)
    
if __name__ == "__main__":
    main()
