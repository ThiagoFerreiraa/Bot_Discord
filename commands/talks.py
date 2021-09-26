from discord.ext import commands
import discord

class Talks(commands.Cog):
    """ Talks with user """

    def __init__(self, bot):
        self.bot = bot

    #bot.command -> commands.command 
    @commands.command(name="oi")
    async def send_hellow(self, ctx):
        name = ctx.author.name

        response = "Olá, " + name

        await ctx.send(response)

    @commands.command(name="segredo")
    async def secret(self,ctx):
        try:

            await ctx.author.send("Me siga no insta @thiagoferreiraa")
            await ctx.author.send("Me siga no insta @thiagoferreiraa")
            await ctx.author.send("Me siga no insta @thiagoferreiraa")
        except discord.errors.Forbidden:
            await ctx.send("Eii...não posso te contar o segredo se você não habilitar para receber mensagens no privado !! ;) (Opções > Privacidade)")


def setup(bot):
    bot.add_cog(Talks(bot))
