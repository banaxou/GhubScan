---
# 🔎 GhubScan - OSINT Tool  1.4 
<img src="https://github.com/user-attachments/assets/6835a86e-c167-4622-ad7e-ce13b1884422" alt="banner">

<a href="https://github.com/banaxou/GhubScan /stargazers"><img src="https://img.shields.io/github/stars/banaxou/GhubScan" alt="Stars Badge"/></a>
<a href="https://github.com/banaxou/awesome-github-profile-readme/network/members"><img src="https://img.shields.io/github/forks/banaxou/GhubScan" alt="Forks Badge"/></a>
---
<img src="https://github.com/user-attachments/assets/157de8d0-a6e8-4385-a79c-890dbfe73960" width="320px" height="320">


**GhubScan** is an OSINT tool specifically designed to collect public information about GitHub users. This tool utilizes GitHub's public APIs to extract various data about a user, including: 

- 📧 **Email|old email**
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
pip install gub
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
- [gitbash](https://git-scm.com/downloads)
```bash
git config --global user.email "id+name@users.noreply.github.com"
git config --global user.email
git log
```
---

## **🪷 ghubscan by ovax**
