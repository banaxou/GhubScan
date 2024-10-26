# 🔎 GhubScan - OSINT Tool 
<img src="https://github.com/user-attachments/assets/157de8d0-a6e8-4385-a79c-890dbfe73960" width="320px" height="320">


**GhubScan** is an OSINT tool specifically designed to collect public information about GitHub users. This tool utilizes GitHub's public APIs to extract various data about a user, including: 

- 📧 **Email**
- 🆔 **User ID**
- 📝 **Name**
- 🔑 **Username**
- 🔗 **Link to GitHub profile**
- 📂 **Number of repositories**
- 👥 **Number of followers**
- 👤 **Number of following users**
  
![ghubscan](https://github.com/user-attachments/assets/474f35b3-ddd0-435d-b26e-05abac005fd6)

GhubScan relies on GitHub's **public APIs** [API 1](https://api.github.com/users/usergithub/events/public) and [API 2](https://api.github.com/users/usergithub) to extract this information. It allows you to retrieve a user's email along with other important data. This tool is useful for OSINT research or for getting an overview of publicly accessible information via a user’s GitHub profile

---

## ❓ How to Mask Your Information?

*(To hide your information, you need to have a noreply email on GitHub, which looks like this: ID+name@users.noreply.github.com)*  
Your email address will appear in the API as soon as you have posted two repositories
## install git
- [gitbash](https://git-scm.com/downloads)
```bash
git config --global user.email "id+name@users.noreply.github.com"
git config --global user.email
git log
```
---

## 🖥️ Install Python  
- 🐍 **[Download Python](https://www.python.org/downloads/)**
- ``` bash
  git clone https://github.com/banaxou/GhubScan/
  pip install fade
  cd GhubScan
  python ghubscan.py
  ```
---

| Platform      | Availability         | 
|---------------|----------------------|
| **Linux**     | ✅ Available          |                
| **Windows**   | ✅ Available          | 
| **Termux**    | ✅ Available          | 


---
## **🪷 ghubscan by ovax**
