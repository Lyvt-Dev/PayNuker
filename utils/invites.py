import discord
from colorama import Fore, Style

async def create_invite_link(guild):
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).create_instant_invite:
            try:
                invite = await channel.create_invite(max_age=0, max_uses=0, unique=True)
                print(f"{Fore.LIGHTGREEN_EX}[+] Invite Link for {guild.name}: {invite.url}{Style.RESET_ALL}")
                return
            except discord.Forbidden:
                print(f"{Fore.RED}[-] No permission in {channel.name}{Style.RESET_ALL}")
    print(f"{Fore.RED}[-] Could not create an invite link. No suitable channel found.{Style.RESET_ALL}")
