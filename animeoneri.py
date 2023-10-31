import discord
import random

from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def korku(ctx): 
    korku = ["death note","chainsaw man","ansatsu kyoushitsu","wotaku ni koi wa muzukashii","tokyo ghoul","devilman crybaby","another","kakegurui","akame ga kill!","the promise neverland","mieruko_chan","angels of death","high rise invasion","junji ıto collection"]
    anime=random.choice(korku)
    await ctx.send(anime)

@bot.command()
async def romantik(ctx): 
    romantik = ["kaguya sama: love is war","nana","monogatari","watashi no shiwase na kekko","sasaki and miyano","kamisama hajimemashita","my dress up darling","horimia",]
    anime=random.choice(romantik)
    await ctx.send(anime)

@bot.command()
async def aksiyon(ctx):
    aksiyon = ["tokyo reverangers","attack on titan","jujutsu kaisen","demon slayer:kimetsuno yaiba","hunter x hunter","one piece","ansatsu kyoushitsu","lycoris recoil","bungou stray dogs wan"]
    anime=random.choice(aksiyon)
    await ctx.send(anime)

@bot.command()
async def komedi(ctx):
   komedi =["saiki kusuo","yahari ore no seishun love comedy","kaguya_sama:love is war","haikyuu","spy x family","bunny girl senpai"]
   anime=random.choice(komedi)
   await ctx.send(anime)


@bot.command()
async def dram(ctx): 
     dram = ["banana fish","anohana","sky8 the ınfinity","violet evergraden","wonder egg priority"]
     anime=random.choice(dram)
     await ctx.send(anime)


bot.run('')

