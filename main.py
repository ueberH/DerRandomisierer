import discord
bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"{bot.user} ist online")

@bot.event
async def on_message(msg):
    if msg.author == bot.user:
        return
    else:

bot.run("MTI5ODcxMDI2NjU5ODY1ODA3OA.G1UXD5.dg5dFb9iOSn1VZgX2F3j6tKM2Z_g2wMX6_8lXs")