import secrets as s
import base64
import hashlib
import json
import time
import requests
import asyncio

def guserid(name="Null",password="Null"):
    tok = s.token_hex(16)
    binary = ''.join(format(ord(c), '08b') for c in tok)
    data = int(binary,2).to_bytes(len(binary)//8,'big')
    offset = data[-1] & 0x0F
    chunk = data[offset:offset+4]
    num = int.from_bytes(chunk,'big') & 0x7fffffff
    code = num % 1000000
    return code + int(str((len(name)/len(password[s.randbelow(4):]))).split(".")[0]) - s.randbelow(99)
def gtok():
    def bitonum(b: str):
        n = int(b, 2)
        a = 65537
        c = 12345
        m = 1 << len(b)
        x = (n * a + c) % m
        return x, len(b)
    toks = []
    for x in range(16):
        ttok = base64.b64encode(s.token_hex(1).encode()).decode().replace("=","")
        p = " ".join(format(b, "o") for b in ttok.encode("utf-8"))
        binary = ''.join(format(ord(c), '08b') for c in p)
        num, l = bitonum(binary)
        fstok = f"{num}.{l}"
        toks.append(fstok)
    payloads = []
    for tok in toks:
        vtok = tok.encode().hex()
        temp = hashlib.md5("".join(toks).encode()).hexdigest()
        payload = {"id":tok ,"time":s.randbelow(122244),"secret":temp,"verifier":vtok ,"data":"$payload$"}
        payloads.append(payload)
    for i in range(len(payloads)-1, -1, -1):
        if i == len(payloads)-1:
            npayload = ""
        else:
            npayload = base64.b64encode(str(payloads[i+1]).encode()).decode()
        payloads[i]["data"] = npayload

    return json.dumps(payloads[0])

async def signup():
    name = input("Name >> ")
    email = input("Email >> ")
    if not "@" in email:
        print("Enter a valid Email")
        signup()
    username = input("Username >> ")
    password =  input("Password >> ")
    if password == None:
        print("Password cannot be empty")
    elif len(password) < 6:
        print("Password must be at least 6 characters long")
    else:
        ipdata = requests.get("https://api.ipify.org?format=json").json()
        ip = ipdata["ip"]
        placeinfo = f"{ipdata.get('country')}, {ipdata.get('city')}"
        userid = guserid()
        sign = s.token_hex(64)
        acctok = gtok()
        payload = {
              "id": userid,
              "email": email,
              "name": name,
              "username": username,
              "timeOfLogin": int(time.time()),
              "loginIp": ip,
              "place": placeinfo,
              "auth": {
                "accessToken": acctok,
                "logincount": 1,
                "signature": sign
              }
            }
        return payload
asyncio.run(signup())
