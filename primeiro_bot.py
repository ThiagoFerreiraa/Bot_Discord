import datetime
import requests
from asyncio import tasks
import discord
from discord import channel
from discord.ext import commands, tasks
from discord.ext.commands.core import command

# Prefixo que vai ser utilizado antes do comando (Exemplo "!play" no caso de musica)
bot = commands.Bot("!")


@bot.event
async def on_ready():
    print(f"Estou Pronto!! Estou conectado como {bot.user}")
    # current_time.start()


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if "palavrão" in message.content:
        await message.channel.send(f"Por favor, {message.author.name}, não ofenda os demais usuários !!")

        await message.delete()

    await bot.process_commands(message)


@bot.event
async def on_reaction_add(reaction, user):
    print(reaction.emoji)
    if reaction.emoji == "👍":
        role = user.guild.get_role(890954082146189353)
        await user.add_roles(role)
    elif reaction.emoji == "💩":
        role = user.guild.get_role(890954237029261372)
        await user.add_roles(role)


@bot.command(name="oi")
async def send_hellow(ctx):
    name = ctx.author.name

    response = "Olá, " + name

    await ctx.send(response)


@bot.command(name="calcular")
async def calculate_expression(ctx, *expression):
    expression = "".join(expression)
    response = eval(expression)

    await ctx.send("A resposta é: " + str(response))


@bot.command()
async def binance(ctx, coin, base):
    # URL API BINANCE: https://api.binance.com/api/v3/ticker/price?symbol=
    # BNB = coin | BTC = base
    try:
        response = requests.get(
            f"https://api.binance.com/api/v3/ticker/price?symbol={coin.upper()}{base.upper()}")

        data = response.json()
        price = data.get("price")
        if price:
            await ctx.send(f"O valor do par {coin.upper()}/{base.upper()} é {price}")
        else:
            await ctx.send(f"O par {coin.upper()}/{base.upper()} é invalido")
    except Exception as error:
        await ctx.send("Ops...deu algum erro!")
        print(error)


@bot.command(name="segredo")
async def secret(ctx):
    try:

        await ctx.author.send("Me siga no insta @thiagoferreiraa")
        await ctx.author.send("Me siga no insta @thiagoferreiraa")
        await ctx.author.send("Me siga no insta @thiagoferreiraa")
    except discord.errors.Forbidden:
        await ctx.send("Eii...não posso te contar o segredo se você não habilitar para receber mensagens no privado !! ;) (Opções > Privacidade)")


@bot.command(name="foto")
async def get_random_image(ctx):
    url_image = "https://picsum.photos/1920/1080"

    embed_image = discord.Embed(
        title="Resultado da busca de imagem",
        description="PS: A busca é totalmente aleatória",
        color=0x0000FF
    )

    embed_image.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)
    embed_image.set_footer(text="Feito por " + bot.user.name, icon_url=bot.user.avatar_url)

    embed_image.add_field(name="API", value="Usamos a API do https://picsum.photos/")
    embed_image.add_field(name="Parâmetros", value="{largura}/{altura}")
    embed_image.add_field(name="Exemplo", value=url_image,inline=False)

    embed_image.set_image(url=url_image)

    await ctx.send(embed=embed_image)


# @tasks.loop(hours=1)
# async def current_time():
#     now = datetime.datetime.now()

#     now = now.strftime("%d/%m/%Y às %H:%M:%S")

#     channel = bot.get_channel(884585184777887767)

#     await channel.send("Data atual: " + now)

bot.run("ODg0NTgzODQ0NTA5MDAzNzk3.YTam5w.5aaaOCAD7t3CTKlZlTLAQJ8Tnjw")
