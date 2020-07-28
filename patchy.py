from discord.ext import commands as discord
import webscraper
from enums import command_enums as commands
import sys
import emojis

TOKEN = ''

try: 
    TOKEN = sys.argv[1]
except IndexError:
    print( "Bot token is required (example command: 'python patchy.py <token>')")
    exit()

description = '''A bot for checking patch notes'''
bot = discord.Bot(command_prefix='!patchy ', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def hello(ctx):
    await ctx.send('Hello {0.author.mention}'.format(ctx.message))

@bot.command()
async def valorant(ctx):
    splitMessage = ctx.message.content.split(" ")

    if( len(splitMessage) > 2 ): #check if there is a third command
        # --version, get latest game version only
        if( splitMessage[2] == commands.Valorant.LatestVersion.value ):
            await ctx.send('Ok, wait lang ssob...')
            await ctx.send(webscraper.getValorantVersion())
            return
    else:
        await ctx.send(webscraper.getValorantPatchNotes())
        return

@bot.command()
async def sino(ctx):
    splitMessage = ctx.message.content.split(" ", 1)
    print(splitMessage)

    if( splitMessage[1] == 'sino bobo?' ):
        await ctx.send('Walang bobo sa server na to gago.')
        return

    elif( splitMessage[1] == 'sino mahal ni Pau?' ):
        await ctx.send(
            emojis.getEmojiByName(ctx.message.guild, 'jaem2') + " " +
            emojis.getEmojiByName(ctx.message.guild, 'jaem') + " " +
            emojis.getEmojiByName(ctx.message.guild, 'jaem2') + " " +
            emojis.getEmojiByName(ctx.message.guild, 'jaem')) 
        return

    else:
        await ctx.send( '\'Di ko alam yan' )

bot.run(TOKEN)