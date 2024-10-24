# Important libraries
import os
import random
from pydoc import replace

from dotenv import load_dotenv

# Load secret .env file
load_dotenv('setup.env')
# Store credentials
dck = os.getenv('disco_key')

import discord

# Permissions
intent = discord.Intents.all()
intent.message_content = True
intent.members = True
bot = discord.Bot(intents=intent)


# Start Event
@bot.event
async def on_ready():
    print("Bot is ready.")
    # Message listener


@bot.event
async def on_message(msg):
    # Return when Message from Bot
    if msg.author == bot.user:
        return
    else:
        # Init Var for Parameter and ChannelNames
        bool_move = False
        str_ChannelNameToMove = ""
        str_ChannelName = ""
        splitString = ""

        if msg.content.startswith("!rnd"):
            if " -m " in msg.content:
                splitString = msg.content.split(" -m ")
                channelString = splitString[0].replace("!rnd ", "")
                bool_move = True
                str_ChannelNameToMove = splitString[1]
            else:
                channelString = msg.content.replace("!rnd ", "")
            channels = bot.get_all_channels()
            list_AllChannels = {}
            channelID = 0
            for channel in channels:
                list_AllChannels[channel.name] = channel.id
            try:
                SplitChannel = await bot.fetch_channel(list_AllChannels[channelString])
            except:
                await msg.channel.send(f"Voice Channel {channelString} leider nicht gefunden.")
            onlineMems = SplitChannel.members
            random.shuffle(onlineMems)
            team1 = []
            team2 = []
            team1.append("\n")
            team2.append("\n")
            for player in onlineMems:
                if onlineMems.index(player) < len(onlineMems) / 2:
                    team1.append(player.name)
                else:
                    team2.append(player.name)
                    if bool_move and vc.type.name == "voice" and (
                            msg.author.guild_permissions.administrator == True or msg.author.name == "sain0130" or msg.author.name == "kallistox"):
                        vc = bot.get_channel(list_AllChannels[str_ChannelNameToMove])
                        print(msg.author.guild_permissions.administrator)
                        await player.move_to(vc)
            print("Team 1:")
            print(team1)
            print("Team 2:")
            print(team2)
            strTeam1 = ""
            strTeam2 = ""
            for m in team1:
                strTeam1 += m + "\n"
            for m in team2:
                strTeam2 += m + "\n"
            await msg.channel.send(f"Team 1: {replace(strTeam1, "[", "")} \nTeam 2: {replace(strTeam2, "[", "")}")




        else:
            return


bot.run(dck)
