import discord
from discord.ext import commands

from keep_alive import keep_alive
keep_alive()

import os

CHANNEL_NAME = "🐦┃листування"

TRACKED_GAMES = ["War Thunder", "World of Tanks Blitz", "World of Tanks", "Atomic Heart", "Escape from Tarkov", "RAGE Multiplayer", "World of Warships", "SnowRunner", "Crossout", "Warface", "MudRunner", "TLauncher", "Teardown", "Breathedge", "DCS World Steam Edition", "Stay Out", "Vector", "Cut the Rope", "BLOCKADE", "Hello Neighbor", "King's Bounty II", "Pathfinder: Wrath of the Righteous - Enhanced Edition", "Black Book", "Beholder", "CRSED: Cuisine Royale", "ONRAID", "Life is Feudal: MMO", "Dark Lord", "Sumoman", "BE-A Walker", "CubeOS", "Kingmakers", "BLOCKPOST MOBILE", "Whisper Trip", "CASE 2: Animatronics Survival", "FPV Kamikaze Drone", "JustAxe", "Norland", "Badland Bandits", "FIELD BREAKING", "Mini Golf Arena", "Gravulse", "Black Fire", "MannaRites", "MannaRites Gold", "World War Z", "Warhammer 40,000: Space Marine 2", "War Robots", "WorldBox - God Simulator", "Men of War II"]

intents = discord.Intents.default()
intents.members = True
intents.presences = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'{client.user} is Online :)')


@client.event
async def on_presence_update(before: discord.Member, after: discord.Member):
    channel = discord.utils.get(after.guild.text_channels, name=CHANNEL_NAME)
    if after.activities:
        for activity in after.activities:
            if activity.type == discord.ActivityType.playing and activity.name in TRACKED_GAMES:
                await channel.send(f'{after.mention}, Ви граєте у **{activity.name}**!\n:bangbang: ЦЯ ГРА ВІД РОСІЙСЬКОГО ВИДАВЦЯ АБО ВІД ГРОМАДЯН ВОРОЖИХ ДЛЯ УКРАЇНИ ДЕРЖАВ! Граючи в цю гру - ви підтримуєте і просуваєте проєкт, гроші від котрого надсилаються у рф та союзні для неї країни. :bangbang:')
                break
        

client.run(os.environ.get('TOKEN'))
