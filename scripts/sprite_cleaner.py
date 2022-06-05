import os
import pathlib
import git #GitPython
import json
from os.path import exists


is_loud = True
max_count = 5
cwd = os.getcwd()
repo = git.Repo(cwd)
cmd_checkout = "git checkout -- "
cmd_clean = "git clean -f "


preference  = "preference"   # personally preferred
rejected    = "rejected"     # personally rejected
mistake     = "mistake"      # should be fixed
anomaly     = "anomaly"      # should be removed
supplement  = "supplement"   # personally added


all_categories = [preference, rejected, mistake, anomaly, supplement]


rejected_only = [preference, mistake, anomaly, supplement]
mistake_only = [preference, rejected, anomaly, supplement]
anomaly_only = [preference, rejected, mistake, supplement]
supplement_only = [preference, rejected, mistake, anomaly]


active_categories = all_categories


def delete(filepath:str):
    # repo.git.execute(f"rm {filepath}")
    if os.path.isfile(filepath):
        os.remove(filepath)


def git_clean(fusion_id):
    filename = fusion_id + ".png"
    filepath =  pathlib.Path(os.path.join(cwd, "CustomBattlers", filename)).as_posix()
    # git_command = cmd_clean + filepath
    # repo.git.execute(git_command)
    delete(filepath)


def git_checkout(fusion_id):
    filename = fusion_id + ".png"
    filepath =  pathlib.Path(os.path.join(cwd, "CustomBattlers", filename)).as_posix()
    git_command = cmd_checkout + filepath
    # repo.git.execute(git_command)
    os.system(git_command)
    

def handle_print(count, spritename):
    if count == 0:
        if is_loud:
            print(spritename, end='')
    elif count == max_count:
        if is_loud:
            print(", " + spritename, end='\n')
        count = -1
    else:
        if is_loud:
            print(", " + spritename, end='')
    return count + 1


def handle_git(category:str, spritename:str):
    if category == anomaly:
        git_clean(spritename)
    else:
        git_checkout(spritename)


def handle_sprites(category:str, sprites):
    count = 0
    print(category.upper())
    if category in active_categories:
        for spritename in sprites:
            count = handle_print(count, spritename)
            handle_git(category, spritename)
    print("\n")


def clean_custom_repo():
    with open("scripts/ignore_sprites.json") as json_file:
        print(" ")
        categories = json.load(json_file)
        for category, sprites in categories.items():
            handle_sprites(category, sprites)
        print("\nDONE")


if __name__ == "__main__":
    clean_custom_repo()