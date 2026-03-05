---
# 🔎 GhubScan - OSINT Tool  1.4 it's coming in a few hours
<img src="https://github.com/user-attachments/assets/6835a86e-c167-4622-ad7e-ce13b1884422" alt="banner">

<a href="https://github.com/banaxou/GhubScan /stargazers"><img src="https://img.shields.io/github/stars/banaxou/GhubScan" alt="Stars Badge"/></a>
<a href="https://github.com/banaxou/awesome-github-profile-readme/network/members"><img src="https://img.shields.io/github/forks/banaxou/GhubScan" alt="Forks Badge"/></a>
---

**GhubScan** is an OSINT tool specifically designed to collect public information about GitHub users. This tool utilizes GitHub's public APIs to extract various data about a user, including: 

- 📧 **Email | old email (commits)**
- 🆔 **User ID**
- 📝 **Name**
- 🔑 **Username**
- 🔗 **Link to GitHub profile**
- 📂 **Number of repositories**
- 👥 **Number of followers**
- 👤 **Number of following users**

![gh](https://github.com/user-attachments/assets/103acd43-1908-4a44-9a3f-21e4ed7be00c)

GhubScan relies on GitHub's **public APIs** [API 1](https://api.github.com/users/usergithub/events/public) and [API 2](https://api.github.com/users/usergithub) to extract this information. It allows for quick and efficient OSINT operations on GitHub profiles.

## 🖥️ Install Python  
- 🐍 **[Download Python](https://www.python.org/downloads/)**
- ```bash
  git clone https://github.com/banaxou/GhubScan/
  cd GhubScan
  bash start.sh or start.bat
  python ghubscan.py
  ```
## 🟢 Usage 
- [pypi gub](https://pypi.org/project/gub/)
```sh
pip install gub ( 1.3 bug ) 
```

You can also install GhubScan from GitHub:

```sh
git clone https://github.com/banaxou/GhubScan/
```

---
### Commands

- Get user information:
  ```sh
  gub -u username
  ```

- Search by email:
  ```sh
  gub -e email@example.com
  ```

- Get user info by ID:
  ```sh
  gub -id 123456
  ```

- Help command:
  ```sh
  gub -h
  ```

---

| Platform      | Availability         | 
|---------------|----------------------|
| **Linux**     | ✅ Available          |                
| **Windows**   | ✅ Available          | 
| **Termux**    | ✅ Available          | 

---

## ❓ How to Mask Your Information?

*(To hide your information, you need to have a noreply email on GitHub, which looks like this: ID+name@users.noreply.github.com)*  
Your email address will appear in the API as soon as you have posted two repositories
[docs](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-email-preferences/setting-your-commit-email-address)

## install git
- github > Settings > emails (Keep my email addresses private )
or
- [gitbash](https://git-scm.com/downloads)
```bash
git config --global user.email "id+name@users.noreply.github.com"
git config --global user.email
git log
```
## 🌸 Contribute

**Issues and PRs are welcome !**  
Want to suggest an improvement or help with code? Open an issue or pull request 
---
## ❤️ Donate

Your support helps keep this tool alive and open source!

<h1>Ethereum</h1>
<img src="https://upload.wikimedia.org/wikipedia/commons/0/05/Ethereum_logo_2014.svg" width="20">  

[0x4cc818bc2C4291CEa8117D9F8D8417EE054fEA58](https://etherscan.io/address/0x4cc818bc2C4291CEa8117D9F8D8417EE054fEA58)

---
‎<h1>sol</h1>
<img src="https://raw.githubusercontent.com/trustwallet/assets/master/blockchains/solana/info/logo.png" width="20">

[BVMkqwkMjtTNmD5spKayhYeb6JUfmReGxGaD4kcetXp2](https://solscan.io/account/BVMkqwkMjtTNmD5spKayhYeb6JUfmReGxGaD4kcetXp2)

> **Ghubscan 1.4**
---

