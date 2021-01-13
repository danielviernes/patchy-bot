from discord.ext import commands as discord
import sys,os,random
import webscraper
from enums import command_enums as commands
from enums import nicknames
import emojis
import giphy
import randomizer


TOKEN = ''

try: 
    TOKEN = os.getenv('PATCHY_TKN')
except (IndexError, TypeError):
    print( "Bot token is required (example command: 'python patchy.py <token>')")
    exit()

description = '''A bot for Paymayan Disord server'''
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

@bot.command()
async def motivate(ctx):
    queryList = ['mina', 'tzuyu', 'sana', 'nayeon', 'dahyun', 'dubu', 'jihyo', 'momo', 'jeongyeon', 'chaeyoung', 'kpop']
    query = '{} {}'.format( 'twice', queryList[random.randint( 0, len(queryList)-1 )] )
    await ctx.send( giphy.getRandomGif( query ) )

@bot.command()
async def randomize(ctx):
    '''Format: !patchy todo <username>'''
    subCommand = ''

    try:
        subCommand = ctx.message.content.split(" ")[2].lower()
    except IndexError:
        ''' runs '!patchy randomize', no sub-command '''
        await ctx.send( '{emoji} {item}'.format( emoji="<:game_die:738692861481975838>", item=randomizer.getRandomItem() ) )
        return
    
    if( subCommand == 'add' ):

        item = ''

        try:
            item = ctx.message.content.split(" ", 3)[3]
        except IndexError:
            await ctx.send( "No item to add\nFor a list of commands, use `!patchy randomize help`" )
            return

        randomizer.add(item)

        await ctx.send( randomizer.getPrettyList() )

    elif( subCommand == 'list' ):
        
        await ctx.send( randomizer.getPrettyList() )

    elif( subCommand == 'remove' ):

        try:
            itemNumber = int(ctx.message.content.split(" ")[3])
        except IndexError:
            await ctx.send( "No item to remove.\nFor a list of commands, use `!patchy randomize help`" )
            return
        except ValueError:
            await ctx.send( "Add the number of the item to remove.\nFor a list of commands, use `!patchy randomize help`" )
            return

        randomizer.remove(itemNumber)
        await ctx.send( randomizer.getPrettyList() )

    elif( subCommand == 'clear' ):
        
        randomizer.clear()

    elif( subCommand == 'help' ):

        await ctx.send( randomizer.help() )

bot.run(TOKEN)