import discord
from discord.ext import commands
import os
from .utils.dataIO import dataIO
import aiohttp
import asyncio
import json
from __main__ import send_cmd_help


class acPlayerInfo:
    """The ACPICS (Animal Crossing Player Info Card System)!"""
    #setup
    def __init__(self, bot):
        self.bot = bot
    
    #******** setting up command GPC *********
    #*****************************************
    @commands.command(pass_context=True)
    async def gpc(self, ctx, user: discord.Member):
        """Retrieves player information, including friendcode and dreamcode."""
        #setting up local vars
        userName = user.display_name #.display_name gets either the .nick or .name of user
        api_get = "https://nookipedia.com/network/discord-api.php?action=get&user_id=" + str(user.id) + "&user_display=" + str(userName)
        
        async with aiohttp.ClientSession() as session: #connects to server
            async with session.get(api_get) as r: #gets user card
                result = await r.json()
                if result == False: #check to confirm user profile exist
                    await self.bot.say("This user has not set up their profile!")
                else:
                    #setting vars
                    author = ctx.message.author
                    description = ("About My Animal Crossing Town!")
                    playerName = result["user_display"]
                    friendCode = result["user_friendcode"]
                    dreamCode = result["user_dreamcode"]
                    townName = result["user_town"]
                    footer_text = "Hi. I am a footer text. I look small when displayed."
                    #setting up the embed
                    embed = discord.Embed(colour=0x67AC42, description=description) # Can use discord.Colour() as well
                    embed.set_thumbnail(url=user.avatar_url)
                    embed.title = "Nookipedia Player Card for " + playerName
                    embed.add_field(name="Friend Code", value=friendCode) # Can add multiple fields.
                    embed.add_field(name="Dream Code", value=dreamCode) # Can add multiple fields.
                    embed.add_field(name="Town Name", value=townName) # Can add multiple fields.
                    await self.bot.say(embed=embed) #say embed

    #********** Setting up command SPC **************
    #************************************************
    @commands.command(pass_context=True)
    async def spc(self, ctx, friendcode, dreamcode, townname):
        """Intial Playercard Set Up. Use quotes around values with spaces."""
        #setting up local vars
        user = ctx.message.author
        user_id = user.id
        playerName = user.display_name
        api_set = "https://nookipedia.com/network/discord-api.php?action=set&user_id=" + str(user_id) + "&user_display=" + str(playerName) + "&user_friendcode=" + str(friendcode) + "&user_dreamcode=" + str(dreamcode) + "&user_town=" + str(townname)
        
        async with aiohttp.ClientSession() as session: #connecting with server
            async with session.get(api_set) as r:
                await self.bot.say(str(r)) #saying confirmation
    
    #*********** Setting the command group for updating card ************
    #********************************************************************
    @commands.group(name="upc", pass_context=True)
    async def _upc(self, ctx):
        """Use this command to update a field on your card!"""
        if ctx.invoked_subcommand is None:
            await send_cmd_help(ctx)

    #subcommand to update friendcode only
    @_upc.command(pass_context=True)
    async def friendcode(self, ctx, friendcode):
        #setting local vars
        user = ctx.message.author
        user_id = user.id
        playerName = user.display_name
        api_set = "https://nookipedia.com/network/discord-api.php?action=set&user_id=" + str(user_id) + "&user_display=" + str(playerName) + "&user_friendcode=" + str(friendcode)
        
        async with aiohttp.ClientSession() as session: #connecting with server
            async with session.get(api_set) as r:
                await self.bot.say(str(r))
    
    #subcommand to update dreamcode only
    @_upc.command(pass_context=True)
    async def dreamcode(self, ctx, dreamcode):
        #setting local vars
        user = ctx.message.author
        user_id = user.id
        playerName = user.display_name
        api_set = "https://nookipedia.com/network/discord-api.php?action=set&user_id=" + str(user_id) + "&user_display=" + str(playerName) + "&user_dreamcode=" + str(dreamcode)
        
        async with aiohttp.ClientSession() as session: #connecting with server
            async with session.get(api_set) as r:
                await self.bot.say(str(r))
    
    #subcommand to update townName only
    @_upc.command(pass_context=True)
    async def townName(self, ctx, townName):
        #setting local vars
        user = ctx.message.author
        user_id = user.id
        playerName = user.display_name
        api_set = "https://nookipedia.com/network/discord-api.php?action=set&user_id=" + str(user_id) + "&user_display=" + str(playerName) + "&user_town=" + str(townName)
        
        async with aiohttp.ClientSession() as session: #connecting with server
            async with session.get(api_set) as r:
                await self.bot.say(str(r))

def setup(bot):
    bot.add_cog(acPlayerInfo(bot))
