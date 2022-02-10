import discord
import os
import requests
import json
from keepalive import keep_alive
from reactions import react_eggplant, react_pop
from discord.ext import commands



my_secret = os.environ['token']



client = commands.Bot(command_prefix = '**')

client.remove_command("help")


def get_meme():
  response = requests.get("https://meme-api.herokuapp.com/gimme/wholesomememes")
  json_data = json.loads(response.text)
  meme = json_data['preview'][3]
  return(meme)


@client.command(name='help')
async def hel(context):
  myEmbed = discord.Embed(title="", description="", color=0x0000FF)
  myEmbed.add_field(name="NSFW commands:", value="4k, anal, ass, boobs, kemonomimi, neko, pgif, pussy, yaoi", inline=False)
  myEmbed.add_field(name="Hentai commands:", value="hanal, hass, hboobs, hentai, hkitsune, hmidriff, hneko, holo", inline=False)
  myEmbed.add_field(name="Bot commands:", value="meme, ping", inline=False)
  myEmbed.set_footer(text="This is just a beta version!!!")
  myEmbed.set_author(name="Help Command", url="", icon_url="https://cdn.discordapp.com/attachments/941091409509896283/941345895998455859/170-1705433_47-images-about-cartoon-png-on-we-heart.png")
  await context.message.channel.send(embed=myEmbed)


@client.command(pass_content=True)
async def chnick(context, member: discord.Member, nick):
    await member.edit(nick=nick)
    await context.message.channel.send(f'Nickname was changed for {member.mention} ')
  

@client.command(name='ping')
async def ping(context):
  myEmbed = discord.Embed(title=f'{round(client.latency * 1000)} ms', color=0x00ff00)
  await context.message.channel.send(embed=myEmbed)




@client.command(name='version')
async def version(context):
  myEmbed = discord.Embed(title="BabyGotBytes BOT", description="This bot is in version 1.0 BETA", color=0x00ff00)
  myEmbed.add_field(name="Version Code:", value="v1.0.0", inline=False)
  myEmbed.add_field(name="Date Released:", value="February 10th, 2022", inline=False)
  myEmbed.set_footer(text="This bot can do crazy things!!!")
  myEmbed.set_author(name="Yajush Vyas", url="https://github.com/notsoocool", icon_url="https://cdn.discordapp.com/attachments/941091409509896283/941091918270562404/IMG_0124_jpg.JPG")
  await context.message.channel.send(embed=myEmbed)




@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))




@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith('**hey'):
    await message.channel.send('Hey sexy <3')
  if message.content.startswith('**meme'):
    meme = get_meme()
    await message.channel.send(meme)
  if("dick" in message.content.lower()):
    await react_eggplant(message)
    await message.channel.send("Suck my dick rn")
    return
  if("gupta" in message.content.lower()):
    await react_pop(message)
    await message.channel.send("Yeh gali kisne likh di XD")
    return
  await client.process_commands(message)



keep_alive()
client.run(my_secret)

