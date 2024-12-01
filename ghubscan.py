import os,requests,time,fade


# code by ovax
red = "\033[91m"
green = "\033[92m"
R = "\033[0m"  
w = 50

agent = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
# im tired
def idéfix(agent):

    you = input(f"[{red}+{R}] {green}Enter GitHub user ID{R}: ") or "181485458"
    r = requests.get(f"https://api.github.com/user/{you}", headers=agent)
    
    
    if r.status_code == 200:
        data = r.json()
        print(f"╔{'═' * w}╗")
        for key, value in data.items():
            print(f"{red}{key.capitalize()}:{R} {value}")
        input(f"╚{'═' * w}╝")
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
         input(f"{red}Error: {r.status_code}{R}")



def emailkaykobémé(agent):
    email = input(f"[{red}+{R}] {green}Enter email to search on GitHub {R}: ") 

    if not email:
        print(f"{red}Email is not found{R}")
        return
    try:
        response = requests.get(f"https://api.github.com/search/commits?q=author-email:{email}", headers=agent, params={'per_page': 10})

        if response.status_code == 200:
            cdata = response.json()

            if cdata['total_count'] > 0:
                susers = set()  

                for it in cdata['items']:
                    
                    if 'author' in it:
                        user_id = it['author']['id']
                        login = it['author']['login']
                        avatar_url = it['author']['avatar_url']
                        html_url = it['author']['html_url']

                        if user_id not in susers:
                            susers.add(user_id)  
                            print(f"╔{'═' * w}╗")
                            print(f"{red}User ID:{R} {user_id}")
                            print(f"{red}Pseudo:{R} {login}")
                            print(f"{red}Email:{R} {email}")
                            print(f"{red}Avatar URL:{R} {avatar_url}")
                            print(f"{red}Profile URL:{R} {html_url}")
                            input(f"╚{'═' * w}╝")
                            os.system('cls' if os.name == 'nt' else 'clear')
            else:
                input(f"{red}No email found {R}")
                os.system('cls' if os.name == 'nt' else 'clear')
        else:
            input(f"{red}Error: {response.status_code}{R}")

    except requests.RequestException as e:
        input(f"{red}Network error: {e}{R}")

def user_info(agent):
    os.system('cls' if os.name == 'nt' else 'clear')
    R = "\033[0m"
    red = "\033[31m"
    green = "\033[32m"

    v = ['code by ovax', 'https://github.com/banaxou', "v1.3"]

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
        print(f"{green}Scanning..{R}")

        apix = requests.get(f"https://api.github.com/users/{user}", headers=agent, timeout=10)
        re = requests.get(f"https://api.github.com/users/{user}/events/public", headers=agent, timeout=10)

        if apix.status_code == 200:
            print(f"{green}Request 200 - {R}")

            data = apix.json()
            email_found = False
            w = 50
            emails = set()

            if re.status_code == 200:
                event_data = re.json()

                if event_data:
                    for event in event_data:
                        if event["type"] == "PushEvent":
                            for commit in event["payload"]["commits"]:
                                email = commit["author"]["email"]
                                emails.add(email)

                    if emails:
                        first = next(iter(emails))
                        print(f"{red}List old/emails:{R}")
                        for email in emails:
                            if email != first:
                                print(f"{red}old/email:{R} {email}")
                    else:
                        print(f"{red}email not found{R}")
                else:
                    print(f"{red}Error: {R} No events data found")
                    return user

            user_info = {
                'Pseudo': data.get('login', 'Not found'),
                'Icon': data.get('avatar_url', 'Not found'),
                'URL': data.get('html_url', 'Not found'),
                'Name': data.get('name', 'Not found'),
                'Type': data.get('type', 'Not found'),
                'ID': data.get('id', 'Not found'),
                'Node ID': data.get('node_id', 'Not found'),
                'Bio': data.get('bio', 'Not found'),
                'Blog': data.get('blog', 'Not found'),
                'Location': data.get('location', 'Not found'),
                'Following': data.get('following', 'Not found'),
                'Followers': data.get('followers', 'Not found'),
                'Created at': data.get('created_at', 'Not found'),
                'Updated at': data.get('updated_at', 'Not found'),
                'Repositories': data.get('public_repos', 'Not found'),
                'Public Gists': data.get('public_gists', 'Not found'),
                'Twitter': data.get('twitter_username', 'Not found'),
            }

            print(f"╔{'═' * w}╗")
            print(f"{green}Email account:{R} {first}")
            for key, value in user_info.items():
                print(f"{red}{key}:{R} {value}")
            print(f"╚{'═' * 50}╝")

            repos_url = f"https://api.github.com/users/{user}/repos?per_page=5"
            repos_data = requests.get(repos_url, headers=agent, timeout=10).json()
            print(f"\n{green}Public Repositories{R}:")
            for repo in repos_data:
                print(f"- {repo['name']} - {repo['html_url']}")

            gists_url = f"https://api.github.com/users/{user}/gists?per_page=5"
            gists_data = requests.get(gists_url, headers=agent, timeout=10).json()
            print(f"\n{green}Public Gists{R}:")
            for gist in gists_data:
                print(f"- {gist['description']} - {gist['html_url']}")

            follo_url = f"https://api.github.com/users/{user}/followers?per_page=5"
            follo_data = requests.get(follo_url, headers=agent, timeout=10).json()
            print(f"\n{green}Followers{R}:")
            for follower in follo_data:
                print(f"- {follower['login']} - {follower['html_url']}")

            follo_url = f"https://api.github.com/users/{user}/following?per_page=5"
            follo_data = requests.get(follo_url, headers=agent, timeout=10).json()
            print(f"\n{green}Following{R}:")
            for following in follo_data:
                print(f"- {following['login']} - {following['html_url']}")

            or_url = f"https://api.github.com/users/{user}/orgs"
            or_data = requests.get(or_url, headers=agent, timeout=10).json()
            print(f"\n{green}Organizations{R}:")
            if not or_data:
                input(f"{red}No organizations found{R}")

            for org in or_data:
                org_url = org.get('html_url', 'Not found')
                input(f"- {org['login']} - {org_url}")

            twitter_user = data.get('twitter_username', None)
            if twitter_user:
                input(f"\n{green}Twitter Profile: {R}https://x.com/{twitter_user}")
        
        else:
            print(f"{red}API error: {apix.status_code}{R}")
    
    except requests.RequestException as e:
        input(f"{red}Network error: {e}{R}")
        
def menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    R = "\033[0m"
    red = "\033[31m"
    green = "\033[32m"

    agent = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
    }

    v = ['code by ovax', 'https://github.com/banaxou', "v1.3", "1", "2", "3","4","0"]

    ba = f"""
         ▄▄ •  ▄ .▄▄• ▄▌▄▄▄▄· .▄▄ ·  ▄▄·  ▄▄▄·  ▐ ▄      
        ▐█ ▀ ▪██▪▐██▪██▌▐█ ▀█▪▐█ ▀. ▐█ ▌▪▐█ ▀█ •█▌▐█    {R}{v[3]} [ {red}user github{R}  ] 
        ▄█ ▀█▄██▀▐██▌▐█▌▐█▀▀█▄▄▀▀▀█▄██ ▄▄▄█▀▀█ ▐█▐▐▌    {R}{v[4]} [ {red}email github{R} ]
        ▐█▄▪▐███▌▐▀▐█▄█▌██▄▪▐█▐█▄▪▐█▐███▌▐█ ▪▐▌██▐█▌    {R}{v[5]} [ {red}id github{R}    ]    
        ·▀▀▀▀ ▀▀▀ · ▀▀▀ ·▀▀▀▀  ▀▀▀▀ ·▀▀▀  ▀  ▀ ▀▀ █▪                                       {R}({v[6]} {red}clear{R})
                                                                                           {R}({v[7]} {red}exit{R})
           {green}{v[2]}{R}                 {red}{v[0]}{R} | {green}{v[1]}{R}
     """
    
    while True:
        print(fade.purplepink(ba))
        inp = input(f"[{red}+{R}] {green}Enter choice{R}: ").lower()

        if inp == "1":
            user_info(agent=agent)
        elif inp == "2":
            emailkaykobémé(agent=agent)
        elif inp == "3":
            idéfix(agent=agent)
        elif inp == "4":
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            print(f"{red} invalid {R}")
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')

menu()
