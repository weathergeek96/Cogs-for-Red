import os
from discord.ext import commands
from .utils.dataIO import dataIO
import aiohttp
import asyncio
import json

class json:
    """testing json"""
    
    waitingResponse = ""

    def __init__(self, bot):
        self.bot = bot
        self.file_path = "data/friendcode/latest.json"
        self.system = dataIO.load_json(self.file_path)
        
    def __unload(self):
        self.session.close()

    def save_enabled(self):
        fileIO('data/friendcode/latest.json', 'save', self.enabled)
       
    @commands.command(pass_context=True)
    async def json(self, ctx):
        """gets JSON file and announces the data from Nookipedia Discord API"""
        search = "https://nookipedia.com/network/discord-api.php?action=get&user_id=191340394485645312&user_display=Jake"
        async with aiohttp.ClientSession() as session:
            async with session.get(search) as r:
                result = await r.json()
                await self.bot.say("INFORMATION!!! " + result['user_id'])
            


def setup(bot):
    bot.add_cog(json(bot))
