import discord
from discord import app_commands, Interaction
from discord.ext import commands

from modules.main import defaultEmbed


class MainCog(commands.Cog, name='main'):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='about', description='有關優奈')
    async def about(self, interaction: Interaction):
        embed = defaultEmbed(title="優奈 • March 7th Bot",
                             description="**優奈**是由綾霞製作的機器人")
        embed.set_author(name="優奈", url="https://github.com/Ayaakaa/March-7th-Bot",
                         icon_url="https://i.imgur.com/Zp9bgVN.jpeg")
        embed.set_image(url="https://i.imgur.com/sU7bXs1.jpeg")
        embed.set_footer(text=f"優奈 v{self.bot.version} - by 綾霞 Ayaakaa")
        await interaction.response.send_message(embed=embed)
    
    @commands.Cog.listener()
    async def on_message(self, msg: discord.Message):
        tuple1 = ('優奈：','Yuna：',)
        tuple2 = ('優奈:','Yuna:',)
        if msg.author.id == 831883841417248778 and msg.content[0:3] in tuple1 or msg.content[0:3] in tuple2 or msg.content[0:4] in tuple1 or msg.content[0:4] in tuple2:
            global text
            if msg.content[0:3] or msg.content[0:4] in tuple1: text = msg.content.split('：')[1]
            elif msg.content[0:3] or msg.content[0:4] in tuple2: text = msg.content.split(': ')[1]
            else: return
            if msg.reference != None or msg.reference is not None:
                reply_id = msg.reference.message_id
                await msg.delete()
                reply_message = await msg.channel.fetch_message(reply_id)
                await reply_message.reply(text)
            else:
                await msg.delete()
                await msg.channel.send(text)
        
async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(MainCog(bot))