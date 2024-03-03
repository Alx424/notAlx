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
  response = requests.get('https://www.boredapi.com/api/activity')
  json_data = json.loads(response.text)
  return json_data['activity']
def get_AstronomyPicOfTheDay():
    response = requests.get('https://api.nasa.gov/planetary/apod?api_key=CovdJv0F7rn2uFCfcwEv7WBwqOOg5GZBsvUDxCCz')
    json_data = json.loads(response.text)
    return '# Astronomical Picture Of the Day\n## ' + json_data['title'] + '\n' + json_data['url'] + '\n' + json_data['explanation'] + ''
def get_darkhumour():
    response = requests.get('https://v2.jokeapi.dev/joke/Dark?blacklistFlags=nsfw,religious,political,racist,sexist,explicit')
    json_data = json.loads(response.text)
    return json_data['insult']

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}'.format(self.user))
    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.content.startswith('$hello'):
            await message.channel.send('Hello there! How can I assist you? Type $help to see a list of commands.')
        if message.content.startswith('$help'):
            await message.channel.send('$hello - greet the bot \n$help - a list of commands \n$meme - show a random meme \n$bored - a random activity to do when you\'re bored \n$apod - shows the astronomical picture of the day from NASA\n$darkhumour - gives a random dark joke')
        if message.content.startswith('$meme'):
            await message.channel.send(get_meme())
        if message.content.startswith('$bored'):
            await message.channel.send(get_boredActivity())
        if message.content.startswith('$apod'):
            await message.channel.send(get_AstronomyPicOfTheDay())
        if message.content.startswith('$darkhumour'):
            await message.channel.send(get_darkhumour)
intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(os.environ["BOT_TOKEN"])

