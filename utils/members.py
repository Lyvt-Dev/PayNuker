import discord
import asyncio
from colorama import Fore, Style

async def ban_all_members(guild):
    ban_reason = input(f"{Fore.LIGHTCYAN_EX}Enter the ban reason: {Style.RESET_ALL}")
    tasks = []
    for member in guild.members:
        async def ban_member(member):
            try:
                await member.ban(reason=ban_reason)
                print(f"{Fore.RED}[-] Banned member: {member.name}#{member.discriminator} | Reason: {ban_reason}{Style.RESET_ALL}")
            except discord.errors.Forbidden:
                print(f"{Fore.RED}Unable to ban member: {member.name}#{member.discriminator}.{Style.RESET_ALL}")
        tasks.append(ban_member(member))
    await asyncio.gather(*tasks)

async def kick_all_members(guild):
    tasks = []
    for member in guild.members:
        async def kick_member(member):
            try:
                await member.kick(reason="Kicked by bot command")
                print(f"{Fore.RED}[-] Kicked member: {member.name}#{member.discriminator}{Style.RESET_ALL}")
            except discord.errors.Forbidden:
                print(f"{Fore.RED}Unable to kick member: {member.name}#{member.discriminator}.{Style.RESET_ALL}")
        tasks.append(kick_member(member))
    await asyncio.gather(*tasks)
