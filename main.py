# APIラッパと非同期I/Oモジュールの読み込み
import discord
import asyncio

# クライアント接続オブジェクト
client = discord.Client()

# 配列宣言
sonano = ['そうなの', 'そーなの', 'ソウナノ', 'ソーナノ', 'ｿｳﾅﾉ', 'ｿｰﾅﾉ']
sonance = ['そうなん', 'そーなん', 'ソウナン', 'ソーナン', 'ｿｳﾅﾝ', 'ｿｰﾅﾝ']
daijobu = ['大丈夫', 'だいじょうぶ', 'だいじょぶ', 'ダイジョブ', 'だいじょーぶ', 'ダイジョーブ', 'ﾀﾞｲｼﾞｮﾌﾞ', 'ﾀﾞｲｼﾞｮｳﾌﾞ', 'ﾀﾞｲｼﾞｮｰﾌﾞ']

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

    await loop(message, sonano, 'ソーナノ', 'sonano.png')
    await loop(message, sonance, 'ソーナンス', 'sonance.png')
    await loop(message, daijobu, 'ダイジョーブ博士', 'daijobu.jpg')

async def loop(message, array, replyWord, replyImage):
    for word in array:
        if word in message.content:
            await client.send_file(message.channel, 'img/' + replyImage)
            await client.send_message(message.channel, replyWord)

client.run("NDYyOTA5ODE5NTc4MjIwNTQ0.DhouzA.V9JJgFkuFhsYOdViGJAUXaZl0oE")