from discord.ext import commands
from utils.rpg.inventory import SelectViewTypeInventory

class Inventory(commands.Cog):
  def __init__(self, client):
    self.client = client
  
  @commands.hybrid_command(
    name="inventario",
    description="Saia para lootear e encontre itens.",
    aliases=["inv", "i"]
  ) 
  async def inv(self, ctx):
    print("inv")
    view = SelectViewTypeInventory(ctx)
    await ctx.send(view=view)
    
async def setup(client):
  await client.add_cog(Inventory(client))
  