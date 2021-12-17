import os
import pathlib
import git
import json
from pathlib import Path


cwd = os.getcwd()
repo = git.Repo(cwd)
git_checkout = "git checkout -q -- "


def discard_changes(fusion_id):
    filename = fusion_id + ".png"
    filepath =  pathlib.Path(os.path.join(cwd, "CustomBattlers", filename)).as_posix()
    git_command = git_checkout + filepath
    print(fusion_id)
    repo.git.execute(git_command)


def clean_repo():
    # I prefer the alt instead of the official version 
    with open("scripts/ignore_sprites.json") as json_file:
        sprites = json.load(json_file)
        print(" ")
        for sprite in sprites:
            # print(sprite)
            discard_changes(sprite)
        print("\nDONE")


if __name__ == "__main__":
    clean_repo()
