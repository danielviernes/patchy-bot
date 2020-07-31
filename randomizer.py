import random

items = []

def getItems():
    return items

def add( item ):
    items.append( item )

def remove( itemNumber ):
    items.pop( itemNumber-1 )

def clear(): 
    items.clear()

def getRandomItem():
    try:
        return items[ random.randint( 0, len(items)-1 ) ]
    except (IndexError, ValueError):
        return "List is empty.\nFor a list of commands, use `!patchy randomize help`"

def getPrettyList():

    if( len( items ) < 1 ):
        return "List is empty.\nFor a list of commands, use `!patchy randomize help`"

    prettyStr = "Randomizer items:\n\n"
    itemFormat = '{}. {}\n'
    ctr = 1

    for item in items:
        prettyStr += itemFormat.format( ctr, item )
        ctr += 1

    return prettyStr

def help():
    formatStr = 'Add an item/start a list:\n`{}`\n\n'
    formatStr += 'Remove an item from the list:\n`{}`\n\n'
    formatStr += 'Show list items:\n`{}`\n\n'
    formatStr += 'Get a random item from the list:\n`{}`\n\n'
    formatStr += 'Clear items from the list:\n`{}`\n\n'

    return formatStr.format( '!patchy randomize add <item>',
    '!patchy randomize remove <item number>',
    '!patchy randomize list',
    '!patchy randomize',
    '!patchy randomize clear' )
