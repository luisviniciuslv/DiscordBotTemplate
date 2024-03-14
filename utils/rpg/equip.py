import discord
from classes.repository import User

class SelectViewEquip(discord.ui.View):
  def __init__(self, ctx, swordORarmor):
    super().__init__(timeout=30)
    self.add_item(SelectEquip(ctx.author.id, swordORarmor))

class SelectEquip(discord.ui.Select):
  def __init__(self, id, swordORarmor):
    self.swordORarmor = swordORarmor
    user = User(id)
    user = user._get()
    itens = user['inventory'][swordORarmor]
    options = [] 
    for item in itens:
      options.append(discord.SelectOption(label=item['name'], value=item['_id'], description=f"Equipar {item['name']}"))
    super().__init__(placeholder="Escolha um item para equipar",max_values=1,min_values=1,options=options)

  async def callback(self, interaction: discord.Interaction):
    if self.id != interaction.user.id:
      return

    user = User(self.id)
    user = user._get()
    item = user['inventory'][self.swordORarmor][self.values[0]]

    user['inventory'][self.swordORarmor].remove(item)
    user['inventory'][self.swordORarmor].append(user[self.swordORarmor])
    user[self.swordORarmor] = item

    await interaction.response.send_message(f"Item equipado com sucesso!", ephemeral=False)