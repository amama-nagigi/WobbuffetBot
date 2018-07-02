# モジュールの読み込み
import discord
import asyncio
import configparser
import re
import jaconv

# 正規表現の作成
sonano = re.compile(r'ソ(ウ|ー+)ナノ')
sonance = re.compile(r'ソ(ウ|ー+)ナン')
daijobu = re.compile(r'(大|ダイ|デ(エ|ー)+)(丈|(ジョ(ウ?|ー*)))(夫|ブ)')

# コンフィグファイルの読み込み
inifile = configparser.ConfigParser()
inifile.read('./config.ini', 'UTF-8')
token = inifile.get('settings', 'token')

# クライアント接続オブジェクト
client = discord.Client()

# 起動時の処理
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

# 誰かが発言した時の処理
@client.event
async def on_message(message):
    if message.author.bot:
        return

    await match(message, sonano, 'ソーナノ', 'sonano.png')
    await match(message, sonance, 'ソーナンス', 'sonance.png')
    await match(message, daijobu, 'ダイジョーブ博士', 'daijobu.jpg')

async def match(message, regex, replyWord, replyImage):
    m = regex.search(jaconv.hira2kata(jaconv.h2z(message.content)))
    if m:
        await client.send_file(message.channel, 'img/' + replyImage)
        await client.send_message(message.channel, replyWord)

client.run(token)