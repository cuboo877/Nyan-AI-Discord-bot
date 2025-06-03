import sqlite3
import discord
from discord.ext import commands
class SqlHelper:
    @classmethod
    async def init_db(cls):
        con = sqlite3.connect("chat_history.db")
        cursor = con.execute(
            '''
            CREATE TABLE IF NOT EXISTS Server (
                id BIGINT PRIMARY KEY,
                name TEXT
            );

            CREATE TABLE IF NOT EXISTS Channel (
                id BIGINT PRIMARY KEY,
                serverId BIGINT,
                FOREIGN KEY (serverId) REFERENCES Server(id)
            );

            CREATE TABLE IF NOT EXISTS Message (
                id BIGINT PRIMARY KEY,
                channelId BIGINT,
                author TEXT,
                time TEXT,
                content TEXT,
                FOREIGN KEY (channelId) REFERENCES Channel(id)
            );
            '''
        )
        con.commit()

    @classmethod
    async def add(cls, msg:discord.Message):
        