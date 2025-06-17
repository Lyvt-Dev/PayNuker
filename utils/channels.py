import discord
import asyncio
from colorama import Fore, Style

async def delete_channels(guild):
    tasks = []
    for channel in guild.channels:
        async def delete_channel(c):
            try:
                await c.delete()
                print(f"{Fore.RED}[-] Deleted channel: {c.name}{Style.RESET_ALL}")
            except discord.errors.Forbidden:
                print(f"{Fore.RED}Unable to delete channel: {c.name}.{Style.RESET_ALL}")
        tasks.append(delete_channel(channel))
    await asyncio.gather(*tasks)


async def create_channels(guild):
    num_channels = int(input("Number of channels (max. 400): "))
    channel_name = input("Channel name: ")
    channel_type = input("Type (1: Voice, 2: Text): ")

    if channel_type == "1":
        ch_type = discord.ChannelType.voice
    else:
        ch_type = discord.ChannelType.text

    tasks = []
    for i in range(num_channels):
        async def create_channel(index):
            name = f"{channel_name}"
            try:
                if ch_type == discord.ChannelType.voice:
                    await guild.create_voice_channel(name)
                else:
                    await guild.create_text_channel(name)
                print(f"{Fore.GREEN}[+] Created channel: {name}{Style.RESET_ALL}")
            except discord.errors.Forbidden:
                print(f"{Fore.RED}Unable to create channel: {name}.{Style.RESET_ALL}")
        tasks.append(create_channel(i))
    await asyncio.gather(*tasks)