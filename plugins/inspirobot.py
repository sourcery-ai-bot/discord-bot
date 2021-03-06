import asyncio
import requests

from discord.ext import commands
from discord.ext.commands import Context

VERSION = "1.0b3"

class Inspirobot(commands.Cog):
    """Get inspirational images from the Inspirobot."""
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.name = "inspirobot"

    @commands.command(aliases=["ib", "inspire"])
    async def inspirobot(self, ctx: Context):
        """Step right up, get 'em while they're hot."""
        req = self.bot.loop.run_in_executor(
            None,
            lambda: requests.get("http://inspirobot.me/api?generate=true")
        )

        while not req.done():
            await asyncio.sleep(0.25)

        image = req.result()

        await ctx.send(image.text)

def setup(bot):
    bot.add_cog(Inspirobot(bot))
