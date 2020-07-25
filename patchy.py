import discord
from configuration import discordconfig as discordcfg
import webscraper
from enums import command_enums as commands
import sys

TOKEN = ''

try: 
    TOKEN = sys.argv[1]
    print("token: " + TOKEN) #debug
except IndexError:
    print( "Bot token is required (example command: 'python patchy.py <token>')")
    exit()

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await message.channel.send(msg)
        return

    if message.content.startswith('!patchy'):

        splitMessage = message.content.split(" ", 1)
        print(splitMessage)

        if( splitMessage[1] == 'hello' ):
            await message.channel.send('Hello {0.author.mention}'.format(message))
            return

        elif( splitMessage[1] == 'sino bobo?' ):
            await message.channel.send('Walang bobo sa server na to gago.')
            return

        elif( splitMessage[1] == 'sino mahal ni Pau?' ):
            await message.channel.send('Si <@512587968880312323>')
            return
        
        #commands for valorant
        elif( splitMessage[1].split()[0] == 'valorant' ): 

            splitMessage = message.content.split(" ")

            if( len(splitMessage) > 2 ): #check if there is a third command
                # --version, get latest game version only
                if( splitMessage[2] == commands.Valorant.LatestVersion.value ):
                    await message.channel.send('Ok, wait lang ssob...')
                    await message.channel.send(webscraper.getValorantVersion())
                    return

    await message.channel.send("Ha?")

client.run(TOKEN)