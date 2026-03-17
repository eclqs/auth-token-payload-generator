# 🔐 auth Payload Generator

A small experimental Python project that simulates the generation of
**signup payloads** similar to what modern web applications send to
backend APIs.

The script generates: - Random **User IDs** - Nested **Access Tokens** -
**Authentication signatures** - **Login metadata** such as IP and
timestamp

This project is mainly useful for: - Learning how payload structures
work - Practicing token generation logic - Testing API payload
structures

------------------------------------------------------------------------

# 🚀 Features

✔ Secure random generation using `secrets`\
✔ Token transformations (Binary → Octal → Numeric)\
✔ Nested payload encoding using **Base64**\
✔ Hash verification using **MD5**\
✔ Automatic **IP detection**\
✔ Async-style structure using `asyncio`

------------------------------------------------------------------------

# 📦 Project Structure

    project/
    │
    ├── main.py        # Main script
    └── README.md      # Project documentation

------------------------------------------------------------------------

# ⚙️ Installation

Clone the repository:

``` bash
git clone https://github.com/eclqs/auth-token-payload-generator
cd auth-token-payload-generator
```

Install required dependency:

``` bash
pip install requests
```

------------------------------------------------------------------------

# ▶️ Usage

Run the script:

``` bash
python main.py
```

You will be asked to enter:

    Name
    Email
    Username
    Password

Example:

    Name >> John
    Email >> john@example.com
    Username >> john123
    Password >> strongpassword

The script will generate a **signup payload** containing authentication
tokens and metadata.

------------------------------------------------------------------------

# 🧠 How It Works

## 1️⃣ User ID Generation

The script generates a random token using:

    secrets.token_hex()

It then:

1.  Converts it to **binary**
2.  Extracts a dynamic chunk
3.  Converts it into a **6‑digit ID**

This method is loosely inspired by **TOTP dynamic truncation**.

------------------------------------------------------------------------

## 2️⃣ Access Token Generation

The function `gtok()` builds a chain of tokens.

Steps:

1.  Generate random values
2.  Encode them with **Base64**
3.  Convert to **octal**
4.  Transform to **binary**
5.  Pass through a pseudo-random transformation

Each token becomes a payload:

    {
     id,
     time,
     secret,
     verifier,
     data
    }

------------------------------------------------------------------------

## 3️⃣ Payload Chaining

Each payload contains another payload encoded in Base64.

Example:

    payload1
       ↓
    payload2
       ↓
    payload3

This simulates **nested authentication tokens**.

------------------------------------------------------------------------

# 📄 Example Output

``` json
{
 "id": 483921,
 "email": "john@example.com",
 "name": "John",
 "username": "john123",
 "timeOfLogin": 1710000000,
 "loginIp": "1.2.3.4",
 "place": "Unknown",
 "auth": {
   "accessToken": "...",
   "logincount": 1,
   "signature": "hex_signature"
 }
}
```

------------------------------------------------------------------------

# ⚠️ Disclaimer

This project is for **educational and research purposes only**.

It is **NOT intended for production authentication systems**.

Real authentication systems should use:

-   JWT
-   OAuth2
-   Secure key management
-   Cryptographically secure token validation

------------------------------------------------------------------------

# 👨‍💻 Author

Created by **SPARK (devSKO)**\
Cybersecurity enthusiast focused on: - API security - token analysis -
payload structures

------------------------------------------------------------------------

⭐ If you find this project interesting, consider giving it a star!
⭐ This Description is made by AI!
