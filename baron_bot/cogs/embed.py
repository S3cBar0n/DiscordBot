# Libraries
# Imports our discord and discord commands libraries
import discord
from discord.ext import commands


# This references the client we created within our bot.py and passes it into the cog
class Embed(commands.Cog):
    def __init__(self, client):
        self.client = client  # this allows us to access the client within our cog

    # Test Embed
    @commands.command()
    async def embedtest(self, ctx):
        embed = discord.Embed(
            colour=discord.Colour.teal(),
            title="Test Title",
            description="This is the test description"
        )

        embed.set_author(name="Author", icon_url="")
        embed.set_image(url="")
        embed.set_thumbnail(url="")
        embed.add_field(name="ping", value="Bot now says pong!", inline=False)
        embed.add_field(name="Test field #2", value="This is test field #2!", inline=False)
        embed.add_field(name="Test field #3", value="This is test field #3!", inline=False)
        embed.set_footer(text="This is my footer!")

        await ctx.send(embed=embed)

    # Embedded Help command
    @commands.command(pass_context=True, aliases=["help"])
    async def helpcmd(self, ctx):
        author = ctx.message.author

        embed_help = discord.Embed(
            colour=discord.Colour.orange()
        )

        embed_help.set_author(name="Baron Bot Commands:\nBot prefix = !")
        embed_help.add_field(name="!help", value="This command displays helpful and common commands.", inline=False)
        embed_help.add_field(name="!8ball", value="This command allows you to ask an 8ball a question!", inline=False)
        embed_help.add_field(name="!about", value="This command simply displays the creator of the bot!", inline=False)
        embed_help.add_field(name="!addrole", value="This command allows you to give yourself or another user a role!",
                             inline=False)
        embed_help.add_field(name="!dumb", value="This command sends a silly message about this bot", inline=False)
        embed_help.add_field(name="!joke", value="This returns a dad joke", inline=False)
        embed_help.add_field(name="!meme", value="Returns a random meme from a meme page", inline=False)
        embed_help.add_field(name="!nextmonth", value="This shows how many days until the start of the next month!",
                             inline=False)
        embed_help.add_field(name="!ping", value="This displays how long it is taking the bot to read commands!",
                             inline=False)
        embed_help.add_field(name="!summer", value="This command calculates how many days until Summer Vacation!",
                             inline=False)
        embed_help.add_field(name="Music Commands:",
                             value="!join or !j - This command join's the bot to the current voice channel, this is the first step in playing a song!\n"
                                   "!leave or !l - This command makes the bot leave the current voice channel!\n"
                                   "!play or !pl - This commands allows you to post a link to a song you want to play! Only works after the join command is used!\n"
                                   "!pause or !pa - This pauses the current song!\n"
                                   "!resume or !r - This resumes a paused song!\n"
                                   "!queue or !q - This command allows you to post a link to play a song and adds it to the next available queue position!\n"
                                   "!next or !n - This plays the next song in the queue!\n"
                                   "!stop or !s - This stops and removes the current song from playing, as well as clears the current queue!\n"
                                   "!volume or !v - This command changes the current volume % of the music the bot is playing!")

        await author.send(embed=embed_help)


# This function allows us to connect this cog to our bot
def setup(client):
    client.add_cog(Embed(client))
