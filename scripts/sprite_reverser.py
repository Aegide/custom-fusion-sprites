from os import listdir, mkdir
from os.path import isfile, join, exists
from shutil import copyfile

path_custom = "CustomBattlers"
path_reverse = "CustomBattlersReverse"
path_json = "json"
fusions = []


def revert_sprite(sprite):
    fusion_name = sprite[:-4].split(".")
    if len(fusion_name)==2:
        reverse_fusion_name = fusion_name[1] + "." + fusion_name[0]
        fusions.append(reverse_fusion_name)
        copyfile(join(path_custom, sprite), join(path_reverse, "r"+reverse_fusion_name+".png"))
        print(reverse_fusion_name)
    else:
        print(fusion_name)


def is_sprite(element):
    return isfile(join(path_custom, element)) and element.endswith(".png")


def revert_element(element):
    if is_sprite(element):
        revert_sprite(element)


def revert_sprites():
    for element in listdir(path_custom):
        revert_element(element)


if __name__ == '__main__':
    if not exists(path_reverse):
        mkdir(path_reverse)
    revert_sprites()
