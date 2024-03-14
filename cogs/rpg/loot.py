from discord.ext import commands
from classes.repository import User
class Loot(commands.Cog):
  def __init__(self, client):
    self.client = client
  
  @commands.command()
  @commands.cooldown(1, 30, commands.BucketType.user)
  async def loot(self, ctx):
    user = User(ctx.author.id)
    print(user.get())
    await ctx.send("looteando")
    
async def setup(client):
  await client.add_cog(Loot(client))