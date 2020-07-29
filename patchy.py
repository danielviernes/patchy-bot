from discord.ext import commands as discord
import webscraper
from enums import command_enums as commands
from enums import nicknames
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

@bot.command()
async def todo(ctx):
    '''Format: !patchy todo <username>'''
    username = ctx.message.content.split(" ")[2].lower()

    todoCtr = 1
    msg = "{name}'s To-do list\n\n"
    todoItemFormat = "{number}. {emoji} {todo}\n"

    if( username in nicknames.Jaemy._value2member_map_ ):
        msg = msg.format(name=username)
        for todo in nicknames.Jaemy.todo():
            msg += todoItemFormat.format(number=todoCtr, emoji="<:x:737658641837981746>", todo=todo)
            todoCtr += 1
    else:
        msg = 'Wala, lalaro na yan'


    await ctx.send( msg )


bot.run(TOKEN)