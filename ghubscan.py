import os,requests,fade

os.system('cls' if os.name == 'nt' else 'clear')
R = "\033[0m"
red = "\033[31m"
green = "\033[32m"

v = ['code by ovax', 'https://github.com/banaxou',"v1.1"]


ba = f"""
 ▄▄ •  ▄ .▄▄• ▄▌▄▄▄▄· .▄▄ ·  ▄▄·  ▄▄▄·  ▐ ▄ 
▐█ ▀ ▪██▪▐██▪██▌▐█ ▀█▪▐█ ▀. ▐█ ▌▪▐█ ▀█ •█▌▐█
▄█ ▀█▄██▀▐██▌▐█▌▐█▀▀█▄▄▀▀▀█▄██ ▄▄▄█▀▀█ ▐█▐▐▌
▐█▄▪▐███▌▐▀▐█▄█▌██▄▪▐█▐█▄▪▐█▐███▌▐█ ▪▐▌██▐█▌
·▀▀▀▀ ▀▀▀ · ▀▀▀ ·▀▀▀▀  ▀▀▀▀ ·▀▀▀  ▀  ▀ ▀▀ █▪


       {green}{v[2]}{R}                 {red}{v[0]}{R} | {green}{v[1]}{R}
"""
print(fade.purplepink(ba))
user = input(f"[{red}+{R}] {green}Enter GitHub username{R}: ")

try:
    apix = requests.get(f"https://api.github.com/users/{user}")
    
    if apix.status_code == 200:
        print(f"{green}Request 200 - {R}")
        data = apix.json()
        w = 50
        print(f"╔{'═' * w}╗")
        user_info = {
            'Pseudo': data.get('login', 'Not found'),
            'Icon': data.get('avatar_url', 'Not found'),
            'URL': data.get('html_url', 'Not found'),
            'Name': data.get('name', 'Not found'),
            'Type': data.get('type', 'Not found'),
            'ID': data.get('id', 'Not found'),
            'Location': data.get('location', 'Not found'),
            'Following': data.get('following', 'Not found'),
            'Followers': data.get('followers', 'Not found'),
            'Created at': data.get('created_at', 'Not found'),
            'Updated at': data.get('updated_at', 'Not found'),
            'Repositories': data.get('public_repos', 'Not found'),
            'Public Gists': data.get('public_gists', 'Not found'),
            'Twitter': data.get('twitter_username', 'Not found'),
        }

        for key, value in user_info.items():
            print(f"{red}{key}:{R} {value}")
        
        print(f"╚{'═' * 50}╝")
        
        repos_url = f"https://api.github.com/users/{user}/repos?per_page=5"
        repos_data = requests.get(repos_url).json()

        print(f"\n{green}Public Repositories{R}:")
        for repo in repos_data:
            print(f"- {repo['name']} - {repo['html_url']}")

        gists_url = f"https://api.github.com/users/{user}/gists?per_page=5"
        gists_data = requests.get(gists_url).json()

        print(f"\n{green}Public Gists{R}:")
        for gist in gists_data:
            print(f"- {gist['description']} - {gist['html_url']}")

        follo_url = f"https://api.github.com/users/{user}/followers?per_page=5"
        follo_data = requests.get(follo_url).json()

        print(f"\n{green}Followers{R}:")
        for follower in follo_data:
            print(f"- {follower['login']} - {follower['html_url']}")  

        follo_url = f"https://api.github.com/users/{user}/following?per_page=5"
        follo_data = requests.get(follo_url).json()

        print(f"\n{green}Following{R}:")
        for following in follo_data:
            print(f"- {following['login']} - {following['html_url']}")  


        or_url = f"https://api.github.com/users/{user}/orgs"
        or_data = requests.get(or_url).json()

        print(f"\n{green}Organizations{R}:")
        if not or_data:
            print(f"{red}No organizations found{R}")
        for org in or_data:

            org_url = org.get('html_url', 'Not found')
            print(f"- {org['login']} - {org_url}")

        twitter_user = data.get('twitter_username', None)
        if twitter_user:
            print(f"\n{green}Twitter Profile: {R}https://x.com/{twitter_user}")

    else:
        print(f"{red}API error: {apix.status_code}{R}")

except requests.RequestException as e:
    print(f"{red}Network error: {e}{R}")
