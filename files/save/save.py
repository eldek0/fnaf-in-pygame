import json
import rsa

private_raw = ["-----BEGIN RSA PRIVATE KEY-----",
"MIIEqAIBAAKCAQEAmRzA8VgV0Y+8uHT/26o5T9lMtlIqWaWRixbXUxjOxlbUlFns",
"n/ec6G0rXxoq161Ib8To0bFEDzDz2Bu8nyMRRZDMHB8O4cYuUfcaCdcb9kOS7LZz",
"0SvHBuGq8OAkDibiBVaNj3AVHATeMBIfTAheTUJCPxtsy/2ZQMNGwVIPpseT1dHt",
"hDQsEpVQ0LoBaN2GUwFnxmFHNP5t6l/HsQf7NkJzfQfltf8S5Q3CCnTz/i3Uw3Jx",
"RYLhh/7F3Hk2mDJeUqKy4UWMeVxnmjNq/zPGODKa/n1OH20vgZHje8Ja0jcJDlu/",
"2rzTRbo5QNuko8kHNnc2tzVhb463qHeHMkehFwIDAQABAoIBAFb9IRl9RBglo8Dg",
"qCSzF5CoEo9bKzh3erMdLQTHCWNiHbCTTn6r/XeH3qZPhZu3lXn605OfNN20oDVd",
"vNJk6AEv/ObVNm1LXTGwRBjnH7nQNn9KQY7LYm4kdCwaDCIGMU97Fz4xHa0njtyc",
"zy8xafJW/LBB8pQK5lBj0FhiAB2N1p0CRQMq+C5pyIe2NbxPrp8aT/cuW9meCdjP",
"ImrICNgndln+Xf65rCBJfoRtn1Ckpx24ToiJzmow2VeIVBw3GWb75KY8RLVdtyyD",
"p3NiqeLtTWGPSUeA2GhvV2VaWFjbGWExAqF1NKW3gJl4J47g+K1nHU4KBxZje3VO",
"LBKbMlECgYkAqhf2hHh2wjL8AYqvM4qSx1GRONP3yMWn63CJSkQdBS71dXl8nGUD",
"jlxRwjVuiUrM+801KMSTteHJ/NIrPhXGN0OvZQBg/Yyr5saNrPX7IBvvRWdGT0OO",
"hKRMnEuIvmKN8WcpP64kzaas9bohulDlu+RLjEfYzeKrEOpwI05DXE4uYN+peoCI",
"pQJ5AOZxN4N9KBfnUs81TC0YT4/c2I8lRCuVvA49VN5Di9zOCAP1XHu5zHwBvS7l",
"Vz9n72vDHrnkaPiFZoB/j3kIrmTyiJ5ofFSeImvGj24hrulv5mL4PxCOKppFw0bn",
"hozqXo+FmsaHptAuzrbuVlvFqwC4MTWXxo0aCwKBiGSM4egRpnLK3Pq0Vznq0zYM",
"3AJyG+qOHeQqlJ5YgadMyUH23Vk+xclkfdiG6Z8zntXDy4ccHg3JOjTAsVt0V8bX",
"tlnIzY1VmVFFUv9KMngay2mF0aSN1TRIRBmo9V9Gt45bY6EHey4vN9PTgpi3tfdK",
"z/ZPirS7KFFJpZzZaSyp8vTFg1StoxkCeEY1UkOGWzPFL46f32CR2pOrJnOeWAGr",
"cgsolnXNQIx6XSjPlWjAt9NEOF5UU1unD+PWI8NhGrY09oDJ3G10vqVU21jf3plt",
"QHFzonlcW80VYazfk1844TP1c0Rj/7NpKHwzqW85HxKoYCSNwtPdCneCpsN8RWrx",
"9wKBiAzBIw5DmP8yDEUL0vieO/jb8vO52ABPlxKFHlUXm0du5WF9ADaotniJViBn",
"CgLW1SLRxCPTi7A7l3QsrNAgOrbjI8cvR603eS6091LjCSC9iis05lNtcz3Cm4/P",
"IjzrmOVFHmKLjBvDwgzJRvfNOQO0Vfcnd2qsbaMKj9jMAF73hrDii3ZAZmE=",
"-----END RSA PRIVATE KEY-----"]

# Transform private key to string
raw_prvt = ""
for line in private_raw:
    raw_prvt += line + "\n"

PRIVATE_KEY = rsa.PrivateKey.load_pkcs1(raw_prvt)
print(PRIVATE_KEY)

def save(App):
    data = default()

    # Write
    data["Night"] = App.menu.inNight
    data["Played"] = App.menu.played_once
    data["Custom"] = App.menu.custom_night_menu.completed_nights

    # Get key
    with open("public.pem", "r") as pk:
        raw_public_key = pk.read()

    PUBLIC_KEY = rsa.PublicKey.load_pkcs1(raw_public_key)

    json_transform = json.dumps(data, indent=2)

    with open("files/utils.txt", "wb") as f:
        f.write(
            rsa.encrypt(json_transform.encode(), PUBLIC_KEY)
            )

def default():
    data = {
        "Night":1,
        "Played":False
    }
    return data

def read(App):
    with open("files/utils.txt", "rb") as f:
        en = f.read()

    print(en)
    json_raw = rsa.decrypt(en, PRIVATE_KEY).decode("utf-8")
    print(json_raw)
    # Read the file from json

    try:
        jsonstr = ""
        for i in range(len(json_raw)):
            jsonstr += json_raw[i].replace("\n", "")

        data = json.loads(jsonstr)

        print(data)
    except json.decoder.JSONDecodeError as e:
        data = default()

    return data

