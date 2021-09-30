from discord.ext import commands
import random
from discord.utils import get
import discord
import requests




intents= discord.Intents.default()

intents.members=True

bot = commands.Bot(command_prefix = '!',intents=intents)
# This is an event:
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")


@bot.command()
async def vbingo(ctx,x,y,free):
    outcomes = ['"Winning"', '"Pog"', '"Suck my dick"', '"Im carrying"', '"Why did you disconnect me"', 'being gay',
                '"Im reading manga"', 'Unintelligible swearing',
                'does not drop weapon to teammates even though he is Jeff Bezos in CS', '"Im so fucking good"',
                '"Im a god"', '"ez"', '"Im gonna rape you"', '"Im gonna rape your parents"', '"Im gonna shoot you"',
                '"Im gonna shoot your parents"', '"Shut up"',
                'Does not remember a thing he did or say literally a minute ago', '"Im NOT white"', '"Im white"',
                '"Im Brazilian"', '"Sheeeeeeeeesh"', 'Misspells other countries swear words', 'AFKs in game',
                'Tries to hit on a girl mid game but inevitably fails', '"1v1 me Nuketown"', '"You have Cold War?"',
                'Relentlessly mentions his PS4 account where he merely hit gold 3 years ago whenever someone criticises him',
                'Blames some random thing or someone for him performing bad',
                '"Fuck Hotpot bro Im never having that shit again"', '"This shit is so easy bro"',
                'Spawns by himself on R6 and drops the defuser']
    x=int(x)
    y=int(y)
    free=int(free)
    total = x * y
    totalfull = total - free
    chosenoutcomes = []
    for i in range(0, totalfull):
        choice = random.choice(outcomes)
        outcomes.remove(choice)
        chosenoutcomes.append(choice)

    for i in range(0, free):
        chosenoutcomes.append("Free!")
    maindict = {}

    for i in range(0, y):
        maindict[i] = []

    for n in range(0, x):
        currentlen = 0
        for i in range(0, y):
            finalchoice = random.choice(chosenoutcomes)
            chosenoutcomes.remove(finalchoice)
            if len(finalchoice) > currentlen:
                currentlen = len(finalchoice)
            maindict[i].append(finalchoice)
        # for i in range(0, y):
        #     while len(maindict[i][n]) < currentlen:
        #         maindict[i][n] = f"{maindict[i][n]} "
    embedVar = discord.Embed(title="Victor Bingo", description="Made by tms#9649, fueled by tex#6666", color=0x00ff00)

    for i in range(0,y):
        totalstring=""
        for n in range(0,x):
            totalstring=f"{totalstring}|{maindict[i][n]}"

        embedVar.add_field(name=totalstring, value=".", inline=False)
    await ctx.send(embed=embedVar)

bot.run("ODAxMDU3NDI3NTAzODQxMzAx.YAbI3Q.ChCOeCQm6XSsGvQUpdEXlrUtMbg")