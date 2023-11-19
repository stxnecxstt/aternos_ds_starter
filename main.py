import discord
from discord.ext import commands
from python_aternos import Client
import asyncio
atclient = Client()
atclient.login('xTich', 'artyom_belous')
aternos = atclient.account
servs = aternos.list_servers()
myserv = servs[0]
canBeStarted = bool
admins = [575327633420714004]

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def atblock(ctx):
    myserv.fetch()
    if ctx.author.id in admins:
        global canBeStarted
        canBeStarted = False
        await ctx.send('<@' + str(ctx.author.id) + '>' + "      *** Теперь сервер не может быть запущен")
    else:
        await ctx.send('<@' + str(ctx.author.id) + '>' + "      *** Это команда только для администраторов, вы не являетесь администратором")

@bot.command()
async def atunblock(ctx):
    myserv.fetch()
    if ctx.author.id in admins:
        global canBeStarted
        canBeStarted = True
        await ctx.send('<@' + str(ctx.author.id) + '>' + "      *** Теперь сервер снова может быть запущен :)")
    else:
        await ctx.send('<@' + str(ctx.author.id) + '>' + "      *** Это команда только для администраторов, вы не являетесь администратором")

@bot.command()
async def atstart(ctx):
    if canBeStarted:
        try:
            myserv.start()
        except:
            pass

        while True:
            myserv.fetch()
            if myserv.status == 'online':
                await ctx.send('<@' + str(ctx.author.id) + '>' + "      *** Сервер запущен!" + "\n  Ip - " + myserv.address)
                break
            await asyncio.sleep(3)
    else:
        await ctx.send('<@' + str(ctx.author.id) + '>' + "      *** Сервер не может быть запущен :((")

@bot.command()
async def atstatus(ctx):
    myserv.fetch()
    await ctx.send(' <@' + str(ctx.author.id) + '>' + "  ***     Сервер  " + myserv.status + " \n  Ip -  " + myserv.address + " \n   Может быть запущен? -  " + str(canBeStarted))


bot.run('MTE3NTEyMTAwNzU0NDEyMzQ4Mg.GebmXG.BFq7btyrlcZOD0ra2qcmhr91tWm4kFZEvEU-6M')