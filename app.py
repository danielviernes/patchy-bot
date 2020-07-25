import discord
from configuration import discordconfig as discordcfg
import webscraper
from enums import command_enums as commands

TOKEN = discordcfg.patchy['token']

print("token: " + TOKEN)

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await message.channel.send(msg)
        return

    elif message.content.startswith('!patchy'):

        splitMessage = message.content.split(" ", 1)
        print(splitMessage)

        if( splitMessage[1] is None):
            return

        elif( splitMessage[1] == 'sino bobo?' ):
            await message.channel.send('Walang bobo sa server na to gago.')

        elif( splitMessage[1] == 'sino mahal ni Pau?' ):
            await message.channel.send('Si <@512587968880312323>')
        
        elif( splitMessage[1].split()[0] == 'valorant' ): #commands for valorant

            splitMessage = message.content.split(" ")

            if( len(splitMessage) > 2 ): #check if there is a third command
                # --version, get latest game version only
                if( splitMessage[2] == commands.Valorant.LatestVersion.value ):
                    await message.channel.send('Ok, wait lang ssob...')
                    await message.channel.send(webscraper.getValorantVersion())
                    return

    await message.channel.send("Ha?")

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)