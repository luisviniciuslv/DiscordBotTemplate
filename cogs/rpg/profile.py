import discord
from discord.ext import commands
from classes.repository import User
class Profile(commands.Cog):
  def __init__(self, client):
    self.client = client
  
  @commands.command()
  async def profile(self, ctx, member: discord.Member=None):
    if member == None:
      member = ctx.author
    print(member.id)
    user = User(member.id)
    user = user._get()
    embed = discord.Embed(title="Inventário de armas", description=f"{ctx.author.mention}")
    espada = user['sword']
    armadura = user['armor']
    embed.add_field(name='Espada equipada', value=f"Nome: {espada['name']} Tier: {espada['tier']}\nDano: {espada['dano']}\nValor: {espada['valor']} 🪙", inline=False)
    embed.add_field(name='Armadura equipada', value=f"Nome: {armadura['name']} Tier: {armadura['tier']}\nDefesa: {armadura['defesa']}\nValor: {armadura['valor']} 🪙", inline=False)
    await ctx.send(embed=embed)
      
    
async def setup(client):
  await client.add_cog(Profile(client))