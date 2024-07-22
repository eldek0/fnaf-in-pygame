import json
import rsa
from files.save.key import private_raw

# Transform private key to string
raw_prvt = ""
for line in private_raw:
    raw_prvt += line + "\n"

PRIVATE_KEY = rsa.PrivateKey.load_pkcs1(bytes(raw_prvt, "utf-8"))

def save(App):
    data = default()

    # Write
    
    data["Night"] = App.menu.inNight
    data["Played"] = App.menu.played_once
    data["Custom"] = App.menu.custom_night_menu.completed_nights
    data["Cutscenes"] = App.menu.cutscenes_data
    data["Ctrl"] = App.ctrl_adv
    data["RealTime"] = App.menu.passed_real_time
    

    # Get key
    with open("public.pem", "r") as pk:
        raw_public_key = pk.read()

    PUBLIC_KEY = rsa.PublicKey.load_pkcs1(raw_public_key)

    if App.debug:
        json_transform = json.dumps(data, indent=2)
    else:
        json_transform = json.dumps(data)
    with open("files/utils.txt", "wb") as f:
        if not App.debug:
            f.write(
                rsa.encrypt(json_transform.encode(), PUBLIC_KEY)
                )
        else:
            f.write( # Without encryption
                json_transform.encode()
                )

def default():
    data = {
        "Night":1,
        "Played":False,
        "Custom":[
            False, False, False, False, False,
            False, False, False, False, False
        ],
        "Cutscenes":[False, False, False, False],
        "Ctrl":False,
        "RealTime":False
    }
    return data

def check_if_data_is_in_file(App, data):
    """ Some features are not aveliable in version 1.0.05 and below,"""
    """ so the files must be updated correctly if that's the case."""
    to_check = ["Ctrl", "RealTime"]
    for check in to_check:
        if not check in list(data.keys()):
            print("not, updating")
            defa = default()
            data[check] = defa[check]
        
    return data

def get_decrypted_file(read:bytes):
    try:
        json_raw = rsa.decrypt(read, PRIVATE_KEY).decode("utf-8")
    except rsa.pkcs1.DecryptionError:
        print("A DECRIPTION ERROR HAPPENED, RESETTING GAME VALUES")
        return None

    #json_raw = rsa.decrypt(read, PRIVATE_KEY)

        
    return json_raw

def read(App):
    with open("files/utils.txt", "rb") as f:
        en = f.read()
    
    print(en)

    if App.debug:
        try:
            json_raw = en.decode("utf-8") # Without encryption
        except UnicodeDecodeError:
            json_raw = get_decrypted_file(en)

    else:
        json_raw = get_decrypted_file(en)

    # Read the file from json
    try:
        jsonstr = ""
        for i in range(len(json_raw)):
            jsonstr += json_raw[i].replace("\n", "")

        data = json.loads(jsonstr)

        print(data)
    except json.decoder.JSONDecodeError:
        data = default()
    except Exception as e:
        print(f"An unexpected error happened: {e}")
        data = default()

    data = check_if_data_is_in_file(App, data)

    return data

