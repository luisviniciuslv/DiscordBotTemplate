from discord.ext import commands

class OnError(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
      if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f"Puxa, você está cansado...\nAguarde {round(error.retry_after, 2)} para lootear novamente!")
      else:
         raise error       

async def setup(client):
    await client.add_cog(OnError(client))
