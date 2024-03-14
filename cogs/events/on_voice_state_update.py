import discord
from discord.ext import commands
import asyncio

class VoiceStateUpdate(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.Cog.listener()
  async def on_voice_state_update(self, member, before, after):
    try:
      vc_after = after.channel
      vc = await vc_after.connect()
      vc.play(discord.FFmpegPCMAudio(source='./olhaeleae.mp3'))
      await asyncio.sleep(2)
      await vc.disconnect()

    except:
      pass

async def setup(client):
  await client.add_cog(VoiceStateUpdate(client))