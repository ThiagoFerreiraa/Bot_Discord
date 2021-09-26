from discord.ext import commands
from discord.ext.commands.core import Command


class Smarts(commands.Cog):
    """ Calculate infos """

    def __init__(self,bot):
        self.bot = bot

    #bot.command -> commands.command
    @commands.command(name="calcular")
    async def calculate_expression(self,ctx, *expression):
        expression = "".join(expression)
        response = eval(expression)

        await ctx.send("A resposta é: " + str(response))

def setup(bot):
    bot.add_cog(Smarts(bot))