from discord.ext import commands
import requests

class Criptos(commands.Cog):
    """ Calculate criptos price """

    def __init__(self,bot):
        self.bot = bot

    #bot.command -> commands.command
    @commands.command()
    async def binance(self,ctx, coin, base):
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
        


def setup(bot):
    bot.add_cog(Criptos(bot))