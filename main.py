import os
import sys
import json
import asyncio
from colorama import Fore, Style, init
from utils import roles, members, spam, admin, invites, channels

os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))
init(autoreset=True)

CONFIG_PATH = "data/config.json"
try:
    with open(CONFIG_PATH, "r") as f:
        config = json.load(f)
except Exception as e:
    print(f"{Fore.RED}[ERROR] Failed to load config.json: {e}")
    input("Press ENTER to exit...")
    sys.exit(1)

token = config.get("token", "").strip()
prefix = config.get("prefix", "!")
owner = config.get("owner", "Unknown")

bot_user = "Not logged in"
logged_in = False
total_guilds = 0
total_members = 0
selected_guild = None  # Für Zugriff im Menü


def save_token(new_token):
    config["token"] = new_token
    with open(CONFIG_PATH, "w") as f:
        json.dump(config, f, indent=2)


def print_banner(current_token):
    import shutil
    global bot_user, total_guilds, total_members

    os.system("cls" if os.name == "nt" else "clear")
    width = shutil.get_terminal_size().columns

    ascii_title = [
        "██████╗  █████╗ ██╗   ██╗    ███╗   ██╗██╗   ██╗██╗  ██╗███████╗██████╗",
        "██╔══██╗██╔══██╗╚██╗ ██╔╝    ████╗  ██║██║   ██║██║ ██╔╝██╔════╝██╔══██╗",
        "██████╔╝███████║ ╚████╔╝     ██╔██╗ ██║██║   ██║█████╔╝ █████╗  ██████╔╝",
        "██╔═══╝ ██╔══██║  ╚██╔╝      ██║╚██╗██║██║   ██║██╔═██╗ ██╔══╝  ██╔══██╗",
        "██║     ██║  ██║   ██║       ██║ ╚████║╚██████╔╝██║  ██╗███████╗██║  ██║",
        "╚═╝     ╚═╝  ╚═╝   ╚═╝       ╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝"
    ]

    for line in ascii_title:
        print(Fore.MAGENTA + line.center(width) + Style.RESET_ALL)

    print()
    print(Fore.CYAN + "Author: _.calmly".center(width))
    print("Version: 1.1.4 (Latest)".center(width))
    print("GitHub: https://github.com/Lyvt-Dev/PayNuker".center(width))
    print()
    print(Fore.GREEN + "[i] config.json loaded successfully".center(width) if current_token else Fore.RED + "[i] No token found in config.json".center(width))
    print()
    print(Fore.LIGHTBLACK_EX + "═" * width + Style.RESET_ALL)
    print()
    print(Fore.WHITE + f"Logged in as: {bot_user}".center(width))
    print(f"Prefix: {prefix}".center(width))
    print(f"Total servers: {total_guilds}".center(width))
    print(f"Total members: {total_members}".center(width))
    print()
    print(Fore.LIGHTBLACK_EX + "═" * width + Style.RESET_ALL)


def print_banner_head(current_token):
    import shutil
    os.system("cls" if os.name == "nt" else "clear")
    width = shutil.get_terminal_size().columns

    ascii_title = [
        "██████╗  █████╗ ██╗   ██╗    ███╗   ██╗██╗   ██╗██╗  ██╗███████╗██████╗",
        "██╔══██╗██╔══██╗╚██╗ ██╔╝    ████╗  ██║██║   ██║██║ ██╔╝██╔════╝██╔══██╗",
        "██████╔╝███████║ ╚████╔╝     ██╔██╗ ██║██║   ██║█████╔╝ █████╗  ██████╔╝",
        "██╔═══╝ ██╔══██║  ╚██╔╝      ██║╚██╗██║██║   ██║██╔═██╗ ██╔══╝  ██╔══██╗",
        "██║     ██║  ██║   ██║       ██║ ╚████║╚██████╔╝██║  ██╗███████╗██║  ██║",
        "╚═╝     ╚═╝  ╚═╝   ╚═╝       ╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝"
    ]

    for line in ascii_title:
        print(Fore.MAGENTA + line.center(width) + Style.RESET_ALL)

    print()
    print(Fore.CYAN + "Author: _.calmly".center(width))
    print("Version: 1.1.4 (Latest)".center(width))
    print("GitHub: https://github.com/Lyvt-Dev/PayNuker".center(width))
    print()
    print(Fore.GREEN + "[i] config.json loaded successfully".center(width) if current_token else Fore.RED + "[i] No token found in config.json".center(width))
    print()
    print(Fore.LIGHTBLACK_EX + "═" * width + Style.RESET_ALL)


async def show_menu(guild, token):

    print_banner_head(token)
    print(Fore.YELLOW + "Available Tools:")
    print("1. Delete all Channels")
    print("2. Create Channels")
    print("3. Delete all Roles")
    print("4. Create Roles")
    print("5. Spammer")
    print("6. Free Admin")
    print("7. Create Invite Link")
    print("8. Kick all Members")
    print("9. Ban all Members")
    print("10. Full Nuke")
    print("0. Back")
    print("-" * 60)

    choice = input(Fore.CYAN + "Select a tool: ")

    if choice == "1":
        await channels.delete_channels(guild)
    elif choice == "2":
        await channels.create_channels(guild)
    elif choice == "3":
        await roles.delete_roles(guild)
    elif choice == "4":
        await roles.create_roles(guild)
    elif choice == "5":
        await spam.message_spammer(guild)
    elif choice == "6":
        await admin.free_admin(guild)
    elif choice == "7":
        await invites.create_invite_link(guild)
    elif choice == "8":
        await members.kick_all_members(guild)
    elif choice == "9":
        await members.ban_all_members(guild)
    elif choice == "10":
        await admin.full_nuke(guild)
    elif choice == "0":
        return
    else:
        print(Fore.RED + "Invalid input.")



async def get_and_start_bot(token):
    global bot_user, logged_in, total_guilds, total_members
    import discord
    from discord.ext import commands

    intents = discord.Intents.all()
    bot = commands.Bot(command_prefix=prefix, intents=intents)

    @bot.event
    async def on_ready():
        global bot_user, logged_in, total_guilds, total_members
        bot_user = f"{bot.user.name}#{bot.user.discriminator}"
        logged_in = True
        total_guilds = len(bot.guilds)
        total_members = sum(g.member_count or 0 for g in bot.guilds)
        await bot.close()

    try:
        await bot.start(token)
    except discord.LoginFailure:
        print(Fore.RED + "[ERROR] Invalid bot token!")
        input("Press ENTER to exit...")
        sys.exit(1)
    except Exception as e:
        print(Fore.RED + f"[CRASH] {e}")
        input("Press ENTER to exit...")
        sys.exit(1)

    return bot


# Main loop
async def main_loop():
    global token, selected_guild

    if not token:
        print_banner(token)
        input(Fore.CYAN + ">>> Press ENTER to continue...")
        token = input(Fore.CYAN + "Enter your bot token: ").strip()
        save_token(token)

    import discord
    from discord.ext import commands

    intents = discord.Intents.all()
    bot = commands.Bot(command_prefix=prefix, intents=intents)

    @bot.event
    async def on_ready():
        global selected_guild, bot_user, total_guilds, total_members
        bot_user = f"{bot.user.name}#{bot.user.discriminator}"
        total_guilds = len(bot.guilds)
        total_members = sum(g.member_count or 0 for g in bot.guilds)

        print_banner(token)

        for i, g in enumerate(bot.guilds):
            print(f"{i}: {g.name} (ID: {g.id})")

        index = input(Fore.CYAN + "Select guild by number: ")
        try:
            selected_guild = bot.guilds[int(index)]
            print(Fore.GREEN + f"Selected: {selected_guild.name}")
        except:
            print(Fore.RED + "Invalid guild selection.")
            await bot.close()
            return

        while True:
            command = input(Fore.CYAN + ">>> ").strip().lower()
            if command == "exit":
                print(Fore.YELLOW + "Goodbye!")
                break
            elif command == "!":
                await show_menu(selected_guild, token)
            else:
                print(Fore.RED + "Unknown command. Type '!' for menu or 'exit' to quit.")

        await bot.close()

    await bot.start(token)


if __name__ == "__main__":
    try:
        asyncio.run(main_loop())
    except Exception as e:
        import traceback
        print(Fore.RED + "[CRASH] An error occurred:")
        traceback.print_exc()
        input("Press ENTER to exit...")
