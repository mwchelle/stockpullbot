import discord
import stockpull

async def send_message(message, user_message):
    try:
        stock = stockpull.find_stock(user_message)
        await message.channel.send(stock)   
    except Exception as e:
        print(e)


def run_bot():
    TOKEN = 'MTA2MjU4NjAyNTcxODg1Mzc3Mw.GbCp1Y.Xyjj2IMN1n_AO5Sd8rgnsvUN0F5WqtuzKOye5k'
    intents=discord.Intents.default()
    intents.message_content=True
    client=discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!') 
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return     
        username=str(message.author)
        user_message=str(message.content)
        channel=str(message.channel)

        print(f'{username} said: "{user_message}" ({channel})')
        await send_message(message, user_message)

    client.run(TOKEN)
