import discord
from discord.ext import commands
from config import TOKEN
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def nasılsın(ctx):
    await ctx.send(f'iyiyim sen nasılsın')

@bot.command()
async def ensevdiğinbilgisayar(ctx):
    await ctx.send(f'macbook air imac 1999')

@bot.command()
async def ensevdiğinşarkı(ctx):
    await ctx.send(f'Nothing Else Matters by Metalica')

@bot.command()
async def botseniçokseviyorum(ctx):
    await ctx.send(f'bende seni')

@bot.command()
async def üzüldüm(ctx):
    await ctx.send(f'üzülme mutlu ol')

@bot.command()
async def ensevdiğintelefonne(ctx):
    await ctx.send(f'iphone 3gs 5s 17pro')

@bot.command()
async def ensevdiğinipodne(ctx):
    await ctx.send(f'nano 4 ve classic 5, 7')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)


@bot.command()
async def umut(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

bot.run(TOKEN)
