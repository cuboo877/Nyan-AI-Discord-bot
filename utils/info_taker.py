import discord
from discord.ext import commands
class InfoTaker:
    @classmethod
    def get_serverName(cls,  ctx:commands.Context):
        return ctx.message.guild.name

    @classmethod
    def get_channelName(cls, ctx:commands.Context):
        return ctx.channel.name

    @classmethod
    def get_serverIconURL(cls, ctx:commands.Context):
        if ctx.guild.icon:
            return ctx.guild.icon.url
        return None