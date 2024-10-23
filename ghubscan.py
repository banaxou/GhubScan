import os,requests,fade
os.system('cls' if os.name == 'nt' else 'clear') 
R = "\033[0m"
red = "\033[31m"
green = "\033[32m"

v = ['code by ovax','https://github.com/banaxou']
ve = "v1.0"
ba = f"""
 ▄▄ •  ▄ .▄▄• ▄▌▄▄▄▄· .▄▄ ·  ▄▄·  ▄▄▄·  ▐ ▄ 
▐█ ▀ ▪██▪▐██▪██▌▐█ ▀█▪▐█ ▀. ▐█ ▌▪▐█ ▀█ •█▌▐█
▄█ ▀█▄██▀▐██▌▐█▌▐█▀▀█▄▄▀▀▀█▄██ ▄▄▄█▀▀█ ▐█▐▐▌
▐█▄▪▐███▌▐▀▐█▄█▌██▄▪▐█▐█▄▪▐█▐███▌▐█ ▪▐▌██▐█▌
·▀▀▀▀ ▀▀▀ · ▀▀▀ ·▀▀▀▀  ▀▀▀▀ ·▀▀▀  ▀  ▀ ▀▀ █▪


       {green}{ve}{R}                 {red}{v[0]}{R} | {green}{v[1]}{R} 
                        
"""
print(fade.purplepink(ba))
user = input(f"[{red}+{R}] {green}Enter GitHub username{R}: ")

try:

    apix = requests.get(f"https://api.github.com/users/{user}")
    re = requests.get(f"https://api.github.com/users/{user}/events/public")

    if apix.status_code == 200:
        if re.status_code == 200:
            print(f"{green}request 200{R}")
            data = re.json()
            email_found = False
            w = 50
            print("Scanning...")

            for event in data:
                if 'payload' in event and 'commits' in event['payload']:
                    for commit in event['payload']['commits']:
                        if 'author' in commit and 'email' in commit['author']:
                            email = commit['author']['email']
                            print(f"╔{'═' * w}╗")
                            print(f"{red}email:{R} {email}")
                            email_found = True
                            break
                if email_found:
                    break
            

            data = apix.json()
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
            print(f"╚{'═' * w}╝")

        if not email_found:
            print(f"{red}Email not found.{R}")
    
    elif apix.status_code == 404:
        print(f"{red}User not found.{R}")
    else:
        print(f"Response: {apix.status_code} ;(")

except requests.RequestException as e:
    print(f"{red}Network error: {e}{R}")
