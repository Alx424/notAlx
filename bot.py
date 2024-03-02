import discord
import os
from dotenv import load_dotenv
load_dotenv()

import requests
import json

def get_meme():
  response = requests.get('https://meme-api.com/gimme')
  json_data = json.loads(response.text)
  return json_data['url']
def get_boredActivity():
  reponse = requests.get('https://www.boredapi.com/api/activity')
  json_data = json.loads(response.text)
  return json_data['activity']

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}'.format(self.user))
    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.content.startswith('$hello'):
            await message.channel.send('Hello there! How can I assist you? Type $commands to see a list of commands.')
        if message.content.startswith('$commands'):
            await message.channel.send('$hello - greet the bot \n $commands - a list of commands \n $meme - show a random meme')
        if message.content.startswith('$meme'):
            await message.channel.send(get_meme())
        if message.content.startswith('$bored'):
            await message.channel.send(get_boredActivity())
intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(os.environ["BOT_TOKEN"])

