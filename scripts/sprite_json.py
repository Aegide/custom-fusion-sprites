from os import listdir
from os.path import isfile, join
import json


path_custom = "CustomBattlers"
json_file_name = "scripts/aegide_sprites.json"


def is_sprite(element):
    return isfile(join(path_custom, element)) and element.endswith(".png")


def build_json():
    fusions = []
    for element in listdir(path_custom):
        if is_sprite(element):
            fusions.append(element[:-4])
            print(element[:-4])
    json_str = json.dumps(fusions, separators=(',\n', ': '))
    json_file = open(json_file_name, "w")
    json_file.write(json_str)
    json_file.close()


if __name__ == '__main__':
    build_json()
