from json import load
import json
with open('slotinfofile.json') as file:
    data = load(file)
    for slot in data:
        for arr in data[slot]:
            arr[1] -= 20

    for slot in data:
        for arr in data[slot]:
            if arr[0][1] % 5 == 1:
                arr[0][1] -= 1

    writefile = open('newslotinfofile.json', 'w')
    writefile.write(json.dumps(data))
