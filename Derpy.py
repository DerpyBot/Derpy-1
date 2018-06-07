import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord.voice_client import VoiceClient
import asyncio
import time
Client = discord.Client()
client = commands.Bot(command_prefix = ">")
#startup_extension = ["Music"]

@client.event
async def on_ready():
    print("De DerpyBot is er weer klaar voor!")
    print("Made By Pidenk AKA Pink")
    await client.change_presence(game=discord.Game(name='> a.u.b. help'))

#class Main_Commands():
       # def __init__(self, bot):
        # self.bot = bot

#@client.event
#async def on_member_join(memer):
#    welkomchannel = member.server.default_channel
#    await client.send_message(welkomchannel, "Welkom".format(member.mention, member.server.name))

#@cleint.event
#async def on_member_remove(member):
#    welkomchannel = member.server.default_channel
#   await client.send_message(welkomchannel, )

@client.event
async def on_message(message):
#kan verschillen
    if message.content == "> video":
        video = discord.Object("451119837456891904")
        await client.send_message(video, "@everyone **Check hier de nieuwe video:** https://www.youtube.com/watch?v=4gtq_54o5Wc&feature=push-u-sub&attr_tag=saGATtPTA7YAfDkN-6&has_verified=1")
    if message.content == "> a.u.b. help":
        await client.send_message(message.channel, "**Bekijk alle commands op:** https://derpderp-bot.webnode.nl/commands/")
    if message.content == "> aub help":
        await client.send_message(message.channel, "**Bekijk alle commands op:** https://derpderp-bot.webnode.nl/commands/")
    if message.content == "> shop":
        await client.send_message(message.channel, "**Check de site:** https://derpycommunity.webnode.nl/")
    if message.content == "> IP":
        await client.send_message(message.channel, "**DerpyGames:** DerpyGames.g-s.nu")
    if message.content == "> site":
        await client.send_message(message.channel, "**Check de site:** https://derpycommunity.webnode.nl/")
    if message.content == "> remix":
        await client.send_message(message.channel, "**Alle Derp Remixes:** https://www.youtube.com/playlist?list=PL5qfmunB_Gs178RBvgARYPmtS6R_7NT2E")
    if message.content == "> YT":
        await client.send_message(message.channel, "**Ons YouTube Kanaal:** https://www.youtube.com/channel/UCb1kRvyY8d1LJj6s7T5P9BQ")
    if message.content == "> YouTube":
        await client.send_message(message.channel, "**Ons YouTube Kanaal:** https://www.youtube.com/channel/UCb1kRvyY8d1LJj6s7T5P9BQ")
    if message.content == "> moderator help":
        moderator = discord.Object("452444325301977088")
        await client.send_message(moderator, "**De Moderator commands:** https://derpderp-bot.webnode.nl/commands/")
#GEKKE COMMANDS
    if message.content == "Hoi":
        await client.send_message(message.channel, "**Hallo**")
    if message.content == "lol":
        await client.send_message(message.channel, ":joy:")
    if message.content == "Lol":
        await client.send_message(message.channel, ":joy:")
    if message.content == "LOL":
        await client.send_message(message.channel, ":joy:")
    if message.content == "Tackle":
        await client.send_message(message.channel, "NEIN Tackle NEIN")
    if message.content == "WTF":
        await client.send_message(message.channel, "**Rustig, ik hoop voor je dat er geen moderator online is want hier staat een flinke straf op, doe dit aub niet vaker.**")
    if message.content == "wtf":
        await client.send_message(message.channel, "**Rustig, ik hoop voor je dat er geen moderator online is want hier staat een flinke straf op, doe dit aub niet vaker.**")
    if message.content == "Wtf":
        await client.send_message(message.channel, "**Rustig, ik hoop voor je dat er geen moderator online is want hier staat een flinke straf op, doe dit aub niet vaker.**")
    if message.content == "The Derp?":
        await client.send_message(message.channel, "**Hij is nu aan het derpen, ergens op de wereld en heeft geen tijd voor kippetjes**")
    if message.content == "TheDerp?":
        await client.send_message(message.channel, "**Hij is nu aan het derpen, ergens op de wereld en heeft geen tijd voor kippetjes**")
    if message.content == "Kip":
        await client.send_message(message.channel, "**Dat is precies waar ik ook aan dacht** :chicken:")
    if message.content == "moscow":
        await client.send_message(message.channel, "https://www.youtube.com/watch?v=NvS351QKFV4")
    if message.content == "NEIN":
        await client.send_message(message.channel, "https://www.youtube.com/watch?v=xoMgnJDXd3k")
    if message.content == "omg":
        await client.send_message(message.channel, ":scream:")
    if message.content == "Omg":
        await client.send_message(message.channel, ":scream:")
    if message.content == "OMG":
        await client.send_message(message.channel, ":scream:")

        
#    if message.content == "> giveaway":
#        polls = discord.Object("448224922565869568")
#       await client.send_message(polls, "@everyone **Wil jij een minecraft account winnen? Stem dan hieronder**")

#    for extension in startup_extensions:
#        try:
 #           bot.load_extension(extension)
 #       except Exception as e:
#                exc = "{}: {}".format(type(e).__name__, e)
#                print("Het is niet gelukt om het te laden {}\n{}".format(extension, exc))


        
    

client.run("NDUxMDEwNDQ5NTQ3MTk4NDY2.De7jzw.3NNXPBqoZ2ekxUBy6Sosrh8JEJA")
