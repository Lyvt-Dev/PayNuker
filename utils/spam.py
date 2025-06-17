import discord
import asyncio
from colorama import Fore, Style

async def ping_all(guild):
    tasks = []
    for channel in guild.text_channels:
        async def ping_channel(channel):
            try:
                await channel.send("@everyone")
                print(f"{Fore.YELLOW}[@] Pinged everyone in channel: {channel.name}{Style.RESET_ALL}")
            except discord.errors.Forbidden:
                print(f"{Fore.RED}Unable to ping in channel: {channel.name}.{Style.RESET_ALL}")
        tasks.append(ping_channel(channel))
    await asyncio.gather(*tasks)

async def message_spammer(guild):
    message = input(f"{Fore.LIGHTCYAN_EX}Enter the message to spam: {Style.RESET_ALL}")
    num_messages = int(input(f"{Fore.LIGHTCYAN_EX}Enter the number of messages per channel: {Style.RESET_ALL}"))

    tasks = []
    for channel in guild.text_channels:
        async def spam_channel(channel):
            for _ in range(num_messages):
                try:
                    await channel.send(message)
                    print(f"{Fore.GREEN}[+] Sent message in: {channel.name}{Style.RESET_ALL}")
                except discord.errors.Forbidden:
                    print(f"{Fore.RED}Unable to send message in: {channel.name}.{Style.RESET_ALL}")
        tasks.append(spam_channel(channel))
    await asyncio.gather(*tasks)
