import discord
import asyncio
from colorama import Fore, Style

async def delete_roles(guild):
    tasks = []
    for role in guild.roles:
        if role != guild.default_role:
            async def delete_role(role):
                try:
                    await role.delete()
                    print(f"{Fore.RED}[-] Deleted role: {role.name}{Style.RESET_ALL}")
                except discord.errors.Forbidden:
                    print(f"{Fore.RED}Unable to delete role: {role.name}.{Style.RESET_ALL}")
            tasks.append(delete_role(role))
    await asyncio.gather(*tasks)

async def create_roles(guild):
    num_roles = int(input(f"{Fore.LIGHTCYAN_EX}Enter the number of roles to create: {Style.RESET_ALL}"))
    role_name = input(f"{Fore.LIGHTCYAN_EX}Enter the name for the roles: {Style.RESET_ALL}")

    tasks = []
    for i in range(num_roles):
        async def create_role(i):
            try:
                await guild.create_role(name=f"{role_name}{i + 1}")
                print(f"{Fore.GREEN}[+] Created role: {role_name}{i + 1}{Style.RESET_ALL}")
            except discord.errors.Forbidden:
                print(f"{Fore.RED}Unable to create role: {role_name}{i + 1}.{Style.RESET_ALL}")
        tasks.append(create_role(i))
    await asyncio.gather(*tasks)
