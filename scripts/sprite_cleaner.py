import os
import pathlib
import git
import json
from pathlib import Path


cwd = os.getcwd()
repo = git.Repo(cwd)
cmd_checkout = "git checkout -q -- "
cmd_clean = "git clean -f "


preference  = "preference"   # personnal design preference
mistake     = "mistake"      # should be fixed
anomaly     = "anomaly"      # should be removed
active_categories = [preference, mistake, anomaly]


def git_clean(fusion_id):
    filename = fusion_id + ".png"
    filepath =  pathlib.Path(os.path.join(cwd, "CustomBattlers", filename)).as_posix()
    git_command = cmd_clean + filepath
    repo.git.execute(git_command)


def git_checkout(fusion_id):
    filename = fusion_id + ".png"
    filepath =  pathlib.Path(os.path.join(cwd, "CustomBattlers", filename)).as_posix()
    git_command = cmd_checkout + filepath
    repo.git.execute(git_command)


def handle_sprites(category, sprites):
    if category in active_categories:
        for sprite in sprites:
            print(sprite)
            if(category == anomaly):
                git_clean(sprite)
            else:
                git_checkout(sprite)


def clean_repo():
    # I prefer the alt instead of the official version 
    with open("scripts/ignore_sprites.json") as json_file:
        print(" ")
        categories = json.load(json_file)
        for category, sprites in categories.items():
            handle_sprites(category, sprites)
        print("\nDONE")


if __name__ == "__main__":
    clean_repo()
