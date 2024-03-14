import discord
from classes.repository import User
class SelectViewTypeInventory(discord.ui.View):
    def __init__(self, ctx):
        super().__init__(timeout=30)
        self.add_item(SelectTypeInventory(ctx.author.id))

class SelectTypeInventory(discord.ui.Select):
    def __init__(self, id):
      self.id = id
      options = [
        discord.SelectOption(label="Armas", value="espada", description=f"Abra o inventário de armas"),
        discord.SelectOption(label="Armaduras", value="armors", description=f"Abra o inventário de armaduras")
        ]
      
      super().__init__(placeholder="Escolha um tipo de item para listar",max_values=1, min_values=1, options=options)

    async def callback(self, interaction: discord.Interaction):
        if self.id != interaction.user.id:
         return 
        
        user = User(self.id)
        user = user._get()
        if self.values[0] == "espada":
          embed = discord.Embed(title="Inventário de armas", description=f"inventario de {interaction.user.mention}")
          for i in user['inventory']['swords']:
            embed.add_field(name=i['name'], value=f"Tier: {i['tier']}\nDano: {i['dano']}\nValor: {i['valor']} 🪙", inline=False)
            await interaction.response.send_message(embed=embed, ephemeral=False)
      
        elif self.values[0] == "armors":    
          embed = discord.Embed(title="Inventário de armaduras", description=f"inventario de {interaction.user.mention}")
          for i in user['inventory']['armors']:
            embed.add_field(name=i['name'], value=f"Tier: {i['tier']}\Defesa: {i['defesa']}\nValor: {i['valor']} 🪙", inline=False)
            await interaction.response.send_message(embed=embed, ephemeral=False)