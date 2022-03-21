import os
import pathlib
import git
import json
from pathlib import Path



is_loud = True
max_count = 5
cwd = os.getcwd()
repo = git.Repo(cwd)
cmd_checkout = "git checkout -q -- "
cmd_clean = "git clean -f "


preference  = "preference"   # personnally prefered
rejected    = "rejected"     # personnally rejected
mistake     = "mistake"      # should be fixed
anomaly     = "anomaly"      # should be removed
supplement  = "supplement"   # personnally added

# active_categories = [preference, rejected, mistake, anomaly, supplement]
active_categories = [preference, rejected, mistake, anomaly, supplement]
# active_categories = [anomaly] # mistake


def delete(filepath):
    try:
        repo.git.execute(f"rm {filepath}")
    except Exception as e:
        pass


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
    repo.git.execute(git_command)


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
    if(category == anomaly):
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