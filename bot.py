import os
from decouple import config
from discord.ext import commands

# Prefixo que vai ser utilizado antes do comando (Exemplo "!play" no caso de musica)
bot = commands.Bot("!")

def load_cogs(bot):
    bot.load_extension("meneger")
    # bot.load_extension("tasks.dates")

    for file in os.listdir("commands"):
        if file.endswith(".py"):
            cog = file[:-3]
            print(cog)
            bot.load_extension(f"commands.{cog}")

load_cogs(bot)


TOKEN = config("TOKEN")
bot.run(TOKEN)
