import requests
from colorama import Fore, Style, init

init(autoreset=True)

ascii_art = """
 _   __   ___   _ ___________   _____  _   _  _____ _____  _   __ ___________ 
| |  \ \ / / \ | |_   _| ___ \ /  __ \| | | ||  ___/  __ \| | / /|  ___| ___ |
| |   \ V /|  \| | | | | |_/ / | /  \/| |_| || |__ | /  \/| |/ / | |__ | |_/ /
| |    \ / | . ` | | | |    /  | |    |  _  ||  __|| |    |    \ |  __||    / 
| |____| | | |\  | | | | |\ \  | \__/\| | | || |___| \__/\| |\  \| |___| |\ \ 
\_____/\_/ \_| \_/ \_/ \_| \_|  \____/\_| |_/\____/ \____/\_| \_/\____/\_| \_|
                                                                              
                                                                              
 _             _          _                        _                          
| |           | |        | |                      | |                         
| |__  _   _  | |_  _____| | ____      ___   _  __| |                         
| '_ \| | | | | \ \/ / __| |/ /\ \ /\ / / | | |/ _` |                         
| |_) | |_| | | |>  < (__|   <  \ V  V /| |_| | (_| |                         
|_.__/ \__, | |_/_/\_\___|_|\_\  \_/\_/  \__, |\__,_|                         
        __/ |                             __/ |                               
       |___/                             |___/                                
"""

def is_username_claimed(username: str) -> bool:
    profile_url = f"https://lyntr.com/api/profile?handle={username}"
    feed_url = f"https://lyntr.com/api/feed?handle={username}"
    
    try:
        profile_response = requests.get(profile_url)
        if profile_response.status_code == 200:
            return True
        elif profile_response.status_code == 404:
            feed_response = requests.get(feed_url)
            if feed_response.status_code == 200:
                return True
            return False
        
        print(f"{Fore.YELLOW}Unexpected status code {profile_response.status_code} for username: {username}")
        return None
    
    except requests.RequestException as e:
        print(f"{Fore.RED}Request failed for username: {username} with exception {e}")
        return None

def check_usernames(usernames_list):
    results = {}
    for username in usernames_list:
        username = username.strip()
        claimed = is_username_claimed(username)
        if claimed is None:
            results[username] = "Error"
        elif claimed:
            results[username] = "Claimed"
        else:
            results[username] = "Unclaimed"
    return results

if __name__ == "__main__":
    print(Fore.CYAN + ascii_art + Style.RESET_ALL)

    usernames_file = input(f"{Fore.CYAN}Enter the path to the usernames file: {Style.RESET_ALL}")
    try:
        with open(usernames_file, 'r') as file:
            usernames_list = file.readlines()
    except FileNotFoundError:
        print(f"{Fore.RED}File {usernames_file} not found.")
        exit()

    results = check_usernames(usernames_list)
    
    with open("results.txt", "w") as file:
        for username, status in results.items():
            file.write(f"{username} - {status}\n")
    
    print(f"{Fore.GREEN}Username checking complete. Results saved to results.txt.")
