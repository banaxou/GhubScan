import os, requests, time, fade, json, re

# code by ovax & copilot github (ONLY FOR THIS TOOL !)

red = "\033[91m"
green = "\033[92m"
yellow = "\033[93m"
R = "\033[0m"
w = 60

CONFIG_FILE = "config.json"

def strip_ansi(text):
    ansi_escape = re.compile(r'\033\[[0-9;]*m')
    return ansi_escape.sub('', text)

def safe_box_line(content, width=60, indent=0):
    clean_content = strip_ansi(content)
    padding = max(0, width - len(clean_content) - indent - 2)
    return f"│ {' ' * indent}{content}" + " " * padding + "│"

def safe_box_line_no_indent(content, width=60):
    clean_content = strip_ansi(content)
    padding = max(0, width - len(clean_content) - 2)
    return f"│ {content}" + " " * padding + "│"


def load_config():
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, 'r') as f:
                return json.load(f)
        except:
            pass
    return {"api": ""}

def save_config(config):
    try:
        with open(CONFIG_FILE, 'w') as f:
            json.dump(config, f, indent=4)
        return True
    except:
        return False

def get_headers():
    """Get headers with API key if available"""
    config = load_config()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    }
    
    api_key = config.get("api")
    if api_key:
        headers['Authorization'] = f'token {api_key}'
    
    return headers

def manage_api_key():
    """Manage GitHub API key"""
    os.system('cls' if os.name == 'nt' else 'clear')
    
    ba = f"""
 ▄▄ •  ▄ .▄▄• ▄▌▄▄▄▄· .▄▄ ·  ▄▄·  ▄▄▄·  ▐ ▄ 
▐█ ▀ ▪██▪▐██▪██▌▐█ ▀█▪▐█ ▀. ▐█ ▌▪▐█ ▀█ •█▌▐█
▄█ ▀█▄██▀▐██▌▐█▌▐█▀▀█▄▄▀▀▀█▄██ ▄▄▄█▀▀█ ▐█▐▐▌
▐█▄▪▐███▌▐▀▐█▄█▌██▄▪▐█▐█▄▪▐█▐███▌▐█ ▪▐▌██▐█▌
·▀▀▀▀ ▀▀▀ · ▀▀▀ ·▀▀▀▀  ▀▀▀▀ ·▀▀▀  ▀  ▀ ▀▀ █▪

            {red}API KEY MANAGEMENT{R}
    """
    print(fade.purplepink(ba))
    
    config = load_config()
    current_key = config.get("api", "")
    
    if current_key:
        masked_key = current_key[:8] + "*" * (len(current_key) - 12) + current_key[-4:] if len(current_key) > 12 else "****"
        print(f"\n{green}Current API Key:{R} {masked_key}\n")
    else:
        print(f"\n{yellow}No API key configured{R}\n")
    
    print(f"{green}[{R}1{green}]{R} Add/Update API Key")
    print(f"{green}[{R}2{green}]{R} Remove API Key")
    print(f"{green}[{R}3{green}]{R} Test API Key")
    print(f"{green}[{R}0{green}]{R} Back to menu\n")
    
    choice = input(f"[{red}+{R}] {green}Enter choice{R}: ").strip()
    
    if choice == "1":
        print(f"\n{yellow}Get your API key from: https://github.com/settings/tokens{R}")
        print(f"{yellow}Generate new token (classic){R}\n")
        new_key = input(f"[{red}+{R}] {green}Enter GitHub API Key{R}: ").strip()
        
        if new_key:
            config['api'] = new_key
            if save_config(config):
                print(f"\n{green}✓ API Key saved successfully{R}")
            else:
                print(f"\n{red}✗ Failed to save API Key{R}")
        else:
            print(f"\n{red}✗ No API Key provided{R}")
        
        input(f"\nPress Enter to continue...")
    
    elif choice == "2":
        if current_key:
            confirm = input(f"\n{red}Remove API Key? (y/n):{R} ").strip().lower()
            if confirm == 'y':
                config['api'] = ''
                if save_config(config):
                    print(f"\n{green}✓ API Key removed{R}")
                else:
                    print(f"\n{red}✗ Failed to remove API Key{R}")
            input(f"\nPress Enter to continue...")
        else:
            print(f"\n{yellow}No API Key to remove{R}")
            input(f"\nPress Enter to continue...")
    
    elif choice == "3":
        if current_key:
            print(f"\n{yellow}Testing API Key...{R}")
            headers = get_headers()
            try:
                r = requests.get("https://api.github.com/rate_limit", headers=headers, timeout=10)
                if r.status_code == 200:
                    data = r.json()
                    rate = data.get('rate', {})
                    limit = rate.get('limit', 0)
                    remaining = rate.get('remaining', 0)
                    print(f"\n{green}✓ API Key is valid!{R}")
                    print(f"{green}Rate Limit:{R} {remaining}/{limit} requests remaining")
                else:
                    print(f"\n{red}✗ API Key is invalid (Status: {r.status_code}){R}")
            except Exception as e:
                print(f"\n{red}✗ Error testing API Key: {e}{R}")
            input(f"\nPress Enter to continue...")
        else:
            print(f"\n{yellow}No API Key configured{R}")
            input(f"\nPress Enter to continue...")

def check_rate_limit(headers):
    try:
        r = requests.get("https://api.github.com/rate_limit", headers=headers, timeout=5)
        if r.status_code == 200:
            data = r.json()
            rate = data.get('rate', {})
            limit = rate.get('limit', 0)
            remaining = rate.get('remaining', 0)
            
            if remaining < 10:
                print(f"{red}⚠ Warning: Only {remaining}/{limit} API requests remaining{R}")
            else:
                print(f"{green}API Requests: {remaining}/{limit} remaining{R}")
    except:
        pass

def get_followers(user, headers):
    try:
        url = f"https://api.github.com/users/{user}/followers?per_page=30"
        r = requests.get(url, headers=headers, timeout=10)
        if r.status_code == 200:
            return [f.get("login", "Unknown") for f in r.json()]
    except:
        pass
    return []

def get_following(user, headers):
    try:
        url = f"https://api.github.com/users/{user}/following?per_page=30"
        r = requests.get(url, headers=headers, timeout=10)
        if r.status_code == 200:
            return [f.get("login", "Unknown") for f in r.json()]
    except:
        pass
    return []

def get_organizations(user, headers):
    """Get list of organizations"""
    orgs = []
    try:
        url = f"https://api.github.com/users/{user}/orgs"
        r = requests.get(url, headers=headers, timeout=10)
        if r.status_code == 200:
            data = r.json()
            for org in data:
                orgs.append(org.get('login', 'Unknown'))
    except:
        pass
    return orgs

def booste_email(user, headers, owner_email=None, max_repo_pages=10, max_commit_pages=5):
    emails_by_repo = {}
    total_commits_scanned = 0
    email_found = False

    print(f"{yellow}Scanning repositories...{R}")

    for page in range(1, max_repo_pages + 1):
        if email_found:
            break

        repos_url = f"https://api.github.com/users/{user}/repos"
        params = {"per_page": 100, "page": page, "type": "owner", "sort": "updated"}

        try:
            r = requests.get(repos_url, headers=headers, params=params, timeout=10)
            if r.status_code != 200:
                break
            data = r.json()
        except:
            break

        if not isinstance(data, list) or not data:
            break

        for repo in data:
            if email_found:
                break

            repo_owner = repo.get("owner", {}).get("login", "")
            if repo_owner.lower() != user.lower():
                continue

            repo_name = repo.get("name")
            emails_by_repo.setdefault(repo_name, set())

            print(f"  └─ Scanning {repo_name}...", end="\r")

            for commits_page in range(1, max_commit_pages + 1):
                commits_url = f"https://api.github.com/repos/{user}/{repo_name}/commits"
                params_c = {"per_page": 100, "page": commits_page}

                try:
                    rc = requests.get(commits_url, headers=headers, params=params_c, timeout=10)
                    if rc.status_code != 200:
                        break
                    commits_data = rc.json()
                except:
                    break

                if not isinstance(commits_data, list) or not commits_data:
                    break

                for commit in commits_data:
                    total_commits_scanned += 1
                    author_obj = commit.get("author")
                    commit_author = commit.get("commit", {}).get("author", {})

                    if author_obj and isinstance(author_obj, dict):
                        author_login = author_obj.get("login", "").lower()
                        if author_login == repo_owner.lower():
                            email = commit_author.get("email")
                            if email and "noreply.github.com" not in email.lower():
                                emails_by_repo[repo_name].add(email)

                                if owner_email and email.lower() == owner_email.lower():
                                    email_found = True
                                    print(f"{green}✓ Found owner email in {repo_name}!{R}")
                                    break

                if email_found:
                    break

    print(f"{green}✓ Scanned {total_commits_scanned} commits{R}")
    return emails_by_repo, total_commits_scanned


def user_info(headers):
    os.system('cls' if os.name == 'nt' else 'clear')
    v = ['code by ovax', 'https://github.com/banaxou', "v1.4"]

    ba = f"""
 ▄▄ •  ▄ .▄▄• ▄▌▄▄▄▄· .▄▄ ·  ▄▄·  ▄▄▄·  ▐ ▄ 
▐█ ▀ ▪██▪▐██▪██▌▐█ ▀█▪▐█ ▀. ▐█ ▌▪▐█ ▀█ •█▌▐█
▄█ ▀█▄██▀▐██▌▐█▌▐█▀▀█▄▄▀▀▀█▄██ ▄▄▄█▀▀█ ▐█▐▐▌
▐█▄▪▐███▌▐▀▐█▄█▌██▄▪▐█▐█▄▪▐█▐███▌▐█ ▪▐▌██▐█▌
·▀▀▀▀ ▀▀▀ · ▀▀▀ ·▀▀▀▀  ▀▀▀▀ ·▀▀▀  ▀  ▀ ▀▀ █▪

       {green}{v[2]}{R}                 {red}{v[0]}{R} | {green}{v[1]}{R}
 """
    print(fade.purplepink(ba))

    check_rate_limit(headers)

    user = input(f"\n[{red}+{R}] {green}Enter GitHub username{R}: ").strip()
    if not user:
        return

    print(f"[{red}*{R}] Starting scan for: {user}{R}\n")

    print(f"{yellow}Fetching user profile...{R}")
    try:
        apix = requests.get(f"https://api.github.com/users/{user}", headers=headers, timeout=10)
        apix.raise_for_status()
        data = apix.json()
    except Exception as e:
        print(f"{red}Unable to retrieve profile: {e}{R}")
        data = {}

    owner_email = None
    if data.get('email') and "noreply.github.com" not in data.get('email', "").lower():
        owner_email = data['email']

    try:
        emails_by_repo, total_scanned = booste_email(user, headers, owner_email=owner_email)
    except Exception as e:
        print(f"{red}Email scan error: {e}{R}")
        emails_by_repo, total_scanned = {}, 0

    owner_emails = set()
    for repo, emails in emails_by_repo.items():
        owner_emails.update(emails)

    account_email = data.get('email')
    has_public_account_email = account_email and "noreply.github.com" not in account_email.lower()

    print(f"\n╭{'─'*59}╮")
    print(safe_box_line_no_indent(f"{red}[{R}EMAILS LINKED TO OWNER{red}]{R}", w))
    print(f"├{'─'*59}┤")
    if owner_emails:
        for e in sorted(owner_emails):
            print(safe_box_line(f"{green}{e}{R}", w, indent=2))
    else:
        msg = "No linked email found in commits (public)"
        print(safe_box_line(f"{yellow}{msg}{R}", w, indent=2))
    print(f"╰{'─'*59}╯")

    if has_public_account_email:
        match = "yes" if account_email in owner_emails else "no"
        print(f"{green}Public account email:{R} {account_email}    {green}Match?{R} {match}\n")
    else:
        print(f"{yellow}No public email on profile\n{R}")

    print(f"\n╭{'─'*59}╮")
    print(safe_box_line_no_indent(f"{red}[{R}PROFILE SUMMARY{red}]{R}", w))
    print(f"├{'─'*59}┤")
    summary_fields = [
        ("Username", data.get('login', 'Not found')),
        ("Name", data.get('name', 'Not found')),
        ("ID", data.get('id', 'Not found')),
        ("Bio", data.get('bio', 'Not found')),
        ("Location", data.get('location', 'Not found')),
        ("Company", data.get('company', 'Not found')),
        ("Blog", data.get('blog', 'Not found')),
        ("Repositories", data.get('public_repos', 'Not found')),
        ("Public Gists", data.get('public_gists', 'Not found')),
        ("Followers", data.get('followers', 'Not found')),
        ("Following", data.get('following', 'Not found')),
        ("Twitter", data.get('twitter_username', 'Not found')),
        ("URL", data.get('html_url', 'Not found')),
        ("Created at", data.get('created_at', 'Not found')),
    ]
    for key, value in summary_fields:
        line = f"{red}{key}:{R} {value}"
        print(safe_box_line_no_indent(line, w))
    print(f"╰{'─'*59}╯")

    print(f"\n╭{'─'*59}╮")
    print(safe_box_line_no_indent(f"{red}[{R}REPOSITORIES{red}]{R}", w))
    print(f"├{'─'*59}┤")
    try:
        repos_url = f"https://api.github.com/users/{user}/repos?per_page=50"
        repos_data = requests.get(repos_url, headers=headers, timeout=10).json()
        
        repos_affichees = 0
        for repo in repos_data[:50]:
            repo_name = repo.get('name')
            if repo_name not in emails_by_repo:
                continue
            
            repos_affichees += 1
            stars = repo.get('stargazers_count', 0)
            lang = repo.get('language', 'N/A') or 'N/A'
            name = repo.get('full_name', repo.get('name', ''))
  
            main_content = f"★{stars:4d} | {lang:12s} | {name}"
            print(safe_box_line(main_content, w, indent=2))
  
            for e in sorted(emails_by_repo.get(repo_name, set())):
                email_content = f"↳ {e}"
                print(safe_box_line(email_content, w, indent=4))
        
        if repos_affichees == 0:
            empty_msg = f"{yellow}No repository scanned{R}"
            print(safe_box_line(empty_msg, w, indent=2))
    except Exception as e:
        print(safe_box_line(f"{red}Error retrieving repos: {e}{R}", w, indent=2))
    print(f"╰{'─'*59}╯")


    print(f"\n╭{'─'*59}╮")
    print(safe_box_line_no_indent(f"{red}[{R}FOLLOWERS{red}]{R}", w))
    print(f"├{'─'*59}┤")
    followers = get_followers(user, headers)
    if followers:
        for follower in followers[:10]:
            print(safe_box_line(f"• {follower}", w, indent=2))
    else:
        print(safe_box_line(f"{yellow}No followers found{R}", w, indent=2))
    print(f"╰{'─'*59}╯")

    print(f"\n╭{'─'*59}╮")
    print(safe_box_line_no_indent(f"{red}[{R}FOLLOWING{red}]{R}", w))
    print(f"├{'─'*59}┤")
    following = get_following(user, headers)
    if following:
        for follow in following[:10]:
            print(safe_box_line(f"• {follow}", w, indent=2))
    else:
        print(safe_box_line(f"{yellow}No following found{R}", w, indent=2))
    print(f"╰{'─'*59}╯")

    print(f"\n╭{'─'*59}╮")
    print(safe_box_line_no_indent(f"{red}[{R}ORGANIZATIONS{red}]{R}", w))
    print(f"├{'─'*59}┤")
    orgs = get_organizations(user, headers)
    if orgs:
        for org in orgs:
            print(safe_box_line(f"• {org}", w, indent=2))
    else:
        print(safe_box_line(f"{yellow}No organizations found{R}", w, indent=2))
    print(f"╰{'─'*59}╯")

    # save
    timestamp = int(time.time()) 
    os.makedirs("output", exist_ok=True)
    json_path = f"output/{user}_{timestamp}.json"
    txt_path = f"output/{user}_{timestamp}.txt"

    full_data = {
        "profile": data,
        "emails_by_repo": {repo: list(emails) for repo, emails in emails_by_repo.items()},
        "followers": followers,
        "following": following,
        "organizations": orgs
    }

    with open(json_path, "w", encoding="utf-8") as json_f:
        json.dump(full_data, json_f, indent=4)

    with open(txt_path, "w", encoding="utf-8") as txt_f:
        txt_f.write(f"GitHub Profile of {user}\n")
        txt_f.write("=" * 60 + "\n\n")
        for k, v in data.items():
            txt_f.write(f"{k}: {v}\n")
        txt_f.write("\nEmails by repository:\n")
        txt_f.write("-" * 60 + "\n")
        for repo, emails in emails_by_repo.items():
            txt_f.write(f"{repo}:\n")
            for e in emails:
                txt_f.write(f"  {e}\n")
        txt_f.write("\nFollowers:\n")
        txt_f.write("-" * 60 + "\n")
        for follower in followers:
            txt_f.write(f"  {follower}\n")
        txt_f.write("\nFollowing:\n")
        txt_f.write("-" * 60 + "\n")
        for follow in following:
            txt_f.write(f"  {follow}\n")
        txt_f.write("\nOrganizations:\n")
        txt_f.write("-" * 60 + "\n")
        for org in orgs:
            txt_f.write(f"  {org}\n")

    print(f"\n{green}✓ Data has been saved in {json_path} and {txt_path}{R}")
    input("\nPress Enter to continue...")


def idéfix(headers):
    user_id = input(f"[{red}+{R}] {green}Enter GitHub User ID{R}: ") or "181485458"
    r = requests.get(f"https://api.github.com/user/{user_id}", headers=headers)

    if r.status_code == 200:
        data = r.json()

        print(f"\n╭{'─'*59}╮")
        print(safe_box_line_no_indent(f"{red}[{R}GITHUB ID INFO{red}]{R}", w))
        print(f"├{'─'*59}┤")

        allowed_fields = [
            "login",
            "id",
            "node_id",
            "avatar_url",
            "html_url",
            "type",
            "site_admin",
            "name",
            "company",
            "blog",
            "location",
            "email",
            "hireable",
            "bio",
            "twitter_username",
            "public_repos",
            "public_gists",
            "followers",
            "following",
            "created_at",
            "updated_at"
        ]

        for key in allowed_fields:
            if key in data:
                value = data.get(key)
                line = f"{red}{key.capitalize()}:{R} {value}"
                print(safe_box_line_no_indent(line, w))

        print(f"╰{'─'*59}╯")
        input("\nPress Enter to continue...")

    else:
        print(f"{red}Error: {r.status_code} | User ID not found{R}")
        time.sleep(2)


def emailkaykobémé(headers):
    email = input(f"[{red}+{R}] {green}Enter email{R}: ")

    if not email:
        print(f"{red}Email not found{R}")
        return
    try:
        response = requests.get(f"https://api.github.com/search/commits?q=author-email:{email}", headers=headers, params={'per_page': 10})

        if response.status_code == 200:
            cdata = response.json()

            if cdata['total_count'] > 0:
                susers = set()

                for it in cdata['items']:
                    if 'author' in it and it['author']:
                        user_id = it['author']['id']
                        login = it['author']['login']
                        avatar_url = it['author']['avatar_url']
                        html_url = it['author']['html_url']

                        if user_id not in susers:
                            susers.add(user_id)
                            print(f"\n╭{'─'*59}╮")
                            print(safe_box_line_no_indent(f"{red}[{R}EMAIL INFO{red}]{R}", w))
                            print(f"├{'─'*59}┤")
                            info_lines = [
                                ("User ID", user_id),
                                ("Username", login),
                                ("Email", email),
                                ("Avatar URL", avatar_url),
                                ("Profile URL", html_url),
                            ]
                            for k, v in info_lines:
                                line = f"{red}{k}:{R} {v}"
                                print(safe_box_line_no_indent(line, w))
                            print(f"╰{'─'*59}╯")
                            input("\nPress Enter to continue...")
            else:
                print(f"{red}No email found{R}")
                time.sleep(2)
        else:
            print(f"{red}Error: {response.status_code}{R}")
            time.sleep(2)

    except requests.RequestException as e:
        print(f"{red}Network error: {e}{R}")
        time.sleep(2)


def menu():
    os.system('cls' if os.name == 'nt' else 'clear')

    v = ['code by ovax', 'https://github.com/banaxou', "v1.4", "1", "2", "3", "4", "5", "0"]

    ba = f"""
         ▄▄ •  ▄ .▄▄• ▄▌▄▄▄▄· .▄▄ ·  ▄▄·  ▄▄▄·  ▐ ▄      
        ▐█ ▀ ▪██▪▐██▪██▌▐█ ▀█▪▐█ ▀. ▐█ ▌▪▐█ ▀█ •█▌▐█    {R}{v[3]} [ {red}GitHub user{R}   ] 
        ▄█ ▀█▄██▀▐██▌▐█▌▐█▀▀█▄▄▀▀▀█▄██ ▄▄▄█▀▀█ ▐█▐▐▌    {R}{v[4]} [ {red}GitHub email{R}  ]
        ▐█▄▪▐███▌▐▀▐█▄█▌██▄▪▐█▐█▄▪▐█▐███▌▐█ ▪▐▌██▐█▌    {R}{v[5]} [ {red}GitHub ID{R}     ]
        ·▀▀▀▀ ▀▀▀ · ▀▀▀ ·▀▀▀▀  ▀▀▀▀ ·▀▀▀  ▀  ▀ ▀▀ █▪    {R}{v[6]} [ {red}API key config{R}]
                                                                                           
                                                                                           {R}({v[8]} {red}exit{R})
           {green}{v[2]}{R}                 {red}{v[0]}{R} | {green}{v[1]}{R}
     """

    while True:
        print(fade.purplepink(ba))
        
        config = load_config()
        headers = get_headers()
        
        if config.get("api"):
            check_rate_limit(headers)
        else:
            print(f"\n{yellow}⚠ No API Key (limited to 60 req/hour){R}")
        
        inp = input(f"\n[{red}+{R}] {green}Enter choice{R}: ").lower()

        if inp == "1":
            user_info(headers=headers)
        elif inp == "2":
            emailkaykobémé(headers=headers)
        elif inp == "3":
            idéfix(headers=headers)
        elif inp == "4":
            manage_api_key()
        elif inp == "0":
            print(f"{red}code by ovax ;){R}")
            time.sleep(2)
            break
        else:
            time.sleep(2)
        
        os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    menu()
