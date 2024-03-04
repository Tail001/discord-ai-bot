import google.generativeai as genai
import discord
import os


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-pro')

chat = model.start_chat(history=[])
#client 是我們與 Discord 連結的橋樑，intents 是我們要求的權限
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

allowed_target = {
    "檔案暫存小天地":["測試用頻道"]
}

setting = open("set.txt", "r")

def generate_response(message):
    message = setting.read() + message
    response = chat.send_message(message)
    return response.text

#調用event函式庫
@client.event
#當機器人完成啟動時
async def on_ready():
    print('目前登入身份：',client.user)
    game = discord.Game('努力中')
    await client.change_presence(status=discord.Status.idle, activity=game)
    
@client.event
#當有訊息時
async def on_message(message):
    #排除自己的訊息，避免陷入無限循環
    if message.author == client.user:
        return
        
    server_name = message.guild.name
    if server_name in allowed_target:
        allowed_channels = allowed_target[server_name]
        if message.channel.name in allowed_channels:
            if client.user.mentioned_in(message):
                res = generate_response(message.content)    
                await message.channel.send(res)


client.run(os.getenv("DISCORD_TOKEN")) 