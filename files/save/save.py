import json
import rsa
from files.save.key import private_raw

# Transform private key to string
raw_prvt = ""
for line in private_raw:
    raw_prvt += line + "\n"

PRIVATE_KEY = rsa.PrivateKey.load_pkcs1(raw_prvt)

def save(App):
    """data = default()

    # Write
    data["Night"] = App.menu.inNight
    data["Played"] = App.menu.played_once
    data["Custom"] = App.menu.custom_night_menu.completed_nights
    data["Cutscenes"] = App.menu.cutscenes_data

    # Get key
    with open("public.pem", "r") as pk:
        raw_public_key = pk.read()

    PUBLIC_KEY = rsa.PublicKey.load_pkcs1(raw_public_key)

    json_transform = json.dumps(data, indent=2)

    with open("files/utils.txt", "wb") as f:
        f.write(
            rsa.encrypt(json_transform.encode(), PUBLIC_KEY)
            )"""
    pass

def default():
    data = {
        "Night":1,
        "Played":False,
        "Custom":[
            False, False, False, False, False,
            False, False, False, False, False
        ],
        "Cutscenes":[False, False, False, False]
        #,"Minigames":[False, False]
    }
    return data

def check_if_minigames_data_is_in_file(App, data):
    # TODO
    """ Minigames are not aveliable in version 1.0.05 and below,"""
    """ so the files must be updated correctly if that's the case."""
    if "minigames" in data.keys():
        print("is")
    else:
        print("not, updating")
        defa = default()
        data["Minigames"] = defa["Minigames"]

    print(data)
    return data


def read(App):
    # Create the file if it does not exist
    """with open("files/utils.txt", "wb") as f:
        f.close()"""

    with open("files/utils.txt", "rb") as f:
        en = f.read()

    try:
        json_raw = rsa.decrypt(en, PRIVATE_KEY).decode("utf-8")
    except rsa.pkcs1.DecryptionError:
        print("A DECRIPTION ERROR HAPPENED, RESETTING GAME VALUES")
        return None
    
    # Read the file from json

    try:
        jsonstr = ""
        for i in range(len(json_raw)):
            jsonstr += json_raw[i].replace("\n", "")

        data = json.loads(jsonstr)

        print(data)
    except json.decoder.JSONDecodeError as e:
        data = default()

    #data = check_if_minigames_data_is_in_file(App, data)

    return data

