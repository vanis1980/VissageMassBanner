try:
    from concurrent.futures import ThreadPoolExecutor
    import random, time, os, httpx
    from colorama import Fore, Style
except ImportError:
    print("Error [!] -> Modules Are not installed")

token, guild = input("Token -> "), input("\nGuild ID -> ")


threads = []
apiv = [6, 7, 8, 9]
codes = [200, 201, 204]




def worker(user: str):
    try:
        response = httpx.put(
            "https://discord.com/api/v{}/guilds/{}/bans/{}".format(
                random.choice(apiv), guild, user
            ),
            headers={"Authorization": f"Bot {token}"},
        )
        if response.status_code in codes:
            print(
                f"{Fore.CYAN}{Style.BRIGHT} Succesfully Punished User --> {Fore.RESET}"
                + user
            )
        else:
            return worker(user)
    except (Exception):
        return worker(user)


def theadpool():
    with ThreadPoolExecutor() as executor:
        time.sleep(0.015)
        with open("members.txt") as f:
            Ids = f.readlines()
        for user in Ids:
            threads.append(executor.submit(worker, user))


if __name__ == "__main__":
    theadpool()
