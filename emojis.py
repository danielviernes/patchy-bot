

def getEmojiByName(guild, emojiName):

    emojiOutputString = "<:{}:{}>"

    for emoji in guild.emojis:
        if( emoji.name == emojiName ):
            emojiOutputString = emojiOutputString.format(emoji.name, emoji.id)

    return emojiOutputString

