from discord.ext import commands


class Reactions(commands.Cog):
    """ Show  """

    def __init__(self, bot):
        self.bot = bot

    #bot.event -> Commands.cog.listener()
    @commands.Cog.listener()
    async def on_reaction_add(self,reaction, user):
        print(reaction.emoji)
        if reaction.emoji == "👍":
            role = user.guild.get_role(890954082146189353)
            await user.add_roles(role)
        elif reaction.emoji == "💩":
            role = user.guild.get_role(890954237029261372)
            await user.add_roles(role)


def setup(bot):
    bot.add_cog(Reactions(bot))
