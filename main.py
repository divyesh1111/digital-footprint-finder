import requests
from colorama import Fore, Style, init
from sites import SITES

init(autoreset=True)

def check_username(username):
    print(f"\n🔍 Searching digital footprint for: {username}\n")

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    found_count = 0

    for site, url in SITES.items():
        full_url = url.format(username)

        try:
            response = requests.get(full_url, headers=headers, timeout=5)

            # Most sites return 200 if profile exists
            if response.status_code == 200:
                print(Fore.GREEN + f"[FOUND] {site}: {full_url}")
                found_count += 1
            else:
                print(Fore.RED + f"[NOT FOUND] {site}")

        except requests.RequestException:
            print(Fore.YELLOW + f"[ERROR] Could not check {site}")

    print("\n" + "-" * 40)
    print(f"Total profiles found: {found_count}/{len(SITES)}")
    print("-" * 40)


def main():
    print("🌐 Digital Footprint Finder")
    print("=" * 35)

    username = input("Enter username to search: ").strip()
    check_username(username)


if __name__ == "__main__":
    main()
