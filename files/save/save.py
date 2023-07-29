import json


def save(App):
    data = default()

    # Write
    data["Night"] = App.menu.inNight
    data["Played"] = App.menu.played_once

    json_transform = json.dumps(data, indent=2)

    F = open("files/utils.txt", "w+")
    F.write(json_transform)
    F.close()

def default():
    data = {
        "Night":1,
        "Played":False
    }
    return data

def read(App):
    F = open("files/utils.txt", "r+")
    json_raw = F.readlines()
    # Read the file from json

    try:
        jsonstr = ""
        for i in range(len(json_raw)):
            jsonstr += json_raw[i].replace("\n", "")

        data = json.loads(jsonstr)

        print(data)
    except json.decoder.JSONDecodeError as e:
        data = default()

    F.close()

    return data

