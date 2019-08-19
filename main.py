mmchannelid = 612819612727246860
token = "NjEwNTEwMjc5MjI2Mjk0Mjc1.XVn6fg.ha9wR2pJ_FRnYIMi4B7u4rurpbI"


import discord
from discord.ext import commands
import datetime


class Bot(commands.Bot):

    embedlist = []

    async def on_ready(self):
        print('Logged on as ', self.user)

    async def on_message(self, msg):
        # Adding DMs to modmail list
        if (msg.channel.type == discord.ChannelType.private) and (msg.author != self.user):
            self.add_to_embedlist(msg.author, msg.created_at, msg.content)
            await msg.channel.send("Your request has been received")

        await bot.process_commands(msg)

    
    # Add a message to the embed list.
    def add_to_embedlist(self, author, timestamp, msg):
        added = False
        for embed in self.embedlist:
            embedtime = embed[0] + datetime.timedelta(minutes=5)
            if embedtime > timestamp:
                embed[1].add_field(name="Message at {}".format(timestamp), value=msg)
                added = True
                break
        if not added:
            new_embed = discord.Embed().set_author(name=author)
            new_embed = new_embed.add_field(name="Message at {}".format(timestamp), value=msg)
            new_embed = (timestamp, new_embed)
            self.embedlist.append(new_embed)

bot = Bot("!")

@bot.command()
async def fetch(ctx):
    for embed in bot.embedlist:
        await ctx.send(embed=embed[1])

bot.run(token)