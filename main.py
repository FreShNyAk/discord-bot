import discord
import os
from keep_alive import keep_alive
keep_alive()


CHANNEL_NAME = "🐦┃листування"

TRACKED_GAMES = ["War Thunder", "World of Tanks Blitz", "World of Tanks", 
                 "Atomic Heart", "Escape from Tarkov", "RAGE Multiplayer", 
                 "World of Warships", "SnowRunner", "Crossout", 
                 "Warface", "MudRunner", "TLauncher", 
                 "Teardown", "Breathedge", "DCS World Steam Edition", 
                 "Stay Out", "Vector", "Cut the Rope", 
                 "BLOCKADE", "Hello Neighbor", "King's Bounty II", 
                 "Pathfinder: Wrath of the Righteous - Enhanced Edition", "Black Book", "Beholder", 
                 "CRSED: Cuisine Royale", "ONRAID", "Life is Feudal: MMO", 
                 "Dark Lord", "Sumoman", "BE-A Walker", 
                 "CubeOS", "Kingmakers", "BLOCKPOST MOBILE", 
                 "Whisper Trip", "CASE 2: Animatronics Survival", 
                 "FPV Kamikaze Drone", "JustAxe", "Norland", 
                 "Badland Bandits", "FIELD BREAKING", "Mini Golf Arena", 
                 "Gravulse", "Black Fire", "MannaRites", 
                 "MannaRites Gold", "World War Z", "Warhammer 40,000: Space Marine 2", 
                 "War Robots", "WorldBox - God Simulator", "Men of War II",
                 "Moon Samurai", "One-Eyed Likho", "Age of Water",
                 "Technotopia", "Woodo", "Writer's Rush",
                 "Heads Will Roll", "Weird Hero", "No Time To Live",
                 "Knock Harder", "Twilight Wars", "Heads Will Roll: Reforged",
                 "The Mildew Children", "The Mildew Children: Chapter 1", "Reflection of Mine",
                 "Fearmonium", "CREAM SODA CLUB", "Jet Racing Extreme: The First Encounter",
                 "The Witch's Cauldron", "Armor Attack", "DR LIVESEY ROM AND DEATH EDITION",
                 "STALCRAFT", "Conqueror's Blade", "Voidtrain",
                 "Warhammer 40,000: Rogue Trader", "CarX Drift Racing Online", "Partisans 1941",
                 "Potion Craft: Alchemist Simulator", "City Car Driving", "Deadside",
                 "IL-2 Sturmovik: Battle of Stalingrad", "Quasimorph", "Graveyard Keeper",
                 "Wall World", "Ghost Watchers", "Terminator: Dark Fate - Defiance",
                 "Global City", "Men of War: Assault Squad 2", "Punch Club 2: Fast Forward",
                 "Stoneshard", "The Wild Eight", "Panzar",
                 "Mighty Party", "HighFleet", "Pathfinder: Kingmaker - Enhanced Plus Edition",
                 "Iratus: Lord of the Dead", "Loop Hero", "Warface: Clutch",
                 "The Life and Suffering of Sir Brante", "Beholder 2", "Beholder 3",
                 "Caliber", "Punch Club", "Anvil Saga",
                 "Craft The World", "War Selection", "Hand Simulator",
                 "Fly Corp", "HudSight - custom crosshair overlay", "Tiny Bunny",
                 "Heroes of Might & Magic V", "Cartel Tycoon", "I Am Future: Cozy Apocalypse Survival",
                 "Milk outside a bag of milk outside a bag of milk", "Despot's Game: Dystopian Battle Simulator", "Train Valley 2",
                 "SANYA", "Outcast Tales: The First Journey", "Noch",
                 "Evil Snowmen 2", "Fading Afternoon", "Bus World",
                 "Galaxy Pass Station", "Pathogenesis: Overcome", "Black Skylands",
                 "Metro Simulator 2", "The Bookwalker: Thief of Tales", "Mondealy",
                 "Daydream: Forgotten Sorrow", "Romance Club - Stories I Play", "Psebay",
                 "Golden Light", "DRAKE", "CyberCorp",
                 "Bogatyr", "Grimshade", "Leviathan: the Cargo — Ongoing series",
                 "Leviathan: The Last Day of the Decade", "Sea Legends", "Time Hacker",
                 "AGAINST", "STRIDE", "Chernobyl: Origins",
                 "Kidnapped Girl", "Grimgrad", "DarkHouse",
                 "IKO 39", "Reclusive", "Hamlet or the Last Game without MMORPG Features, Shaders and Product Placement",
                 "The Franz Kafka Videogame"]

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
                await channel.send(f'{after.mention}, Ви граєте у **{activity.name}**!\n\n:bangbang: ЦЯ ГРА ВІД РОСІЙСЬКОГО ВИДАВЦЯ АБО ВІД ГРОМАДЯН ВОРОЖИХ ДЛЯ УКРАЇНИ ДЕРЖАВ! :bangbang:\n:bangbang: Граючи в цю гру - ви підтримуєте і просуваєте проєкт, гроші від котрого надсилаються у рф та союзні для неї країни. :bangbang:')
                break


client.run(os.environ.get('TOKEN'))
