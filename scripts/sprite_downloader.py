# https://github.com/nsadawi/Download-Large-File-From-Google-Drive-Using-Python
# https://stackoverflow.com/a/54577565


import requests
import os
from zipfile import ZipFile


def download_file_from_google_drive(id, destination):
    URL = f"https://docs.google.com/uc?confirm=XWPY&export=download&id={id}"
    session = requests.Session()
    response = session.get(URL, stream = True)
    save_response_content(response, destination)    


def save_response_content(response, destination):
    CHUNK_SIZE = 32768
    with open(destination, "wb") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk:
                f.write(chunk)


def unzip_file(source, destination):
    try:
        with ZipFile(source, 'r') as archive:
            archive.extractall(destination)
    except:
        print("\n", "NOT AN ARCHIVE", "\n")
        os.remove(source)


if __name__ == "__main__":


    file_id = None
    archive_path = os.path.join(os.getcwd(), "tmp", "archive.zip")
    folder_path = os.path.join(os.getcwd(), "tmp")

    print(">> START")
    download_file_from_google_drive(file_id, archive_path)
    print(">> DOWNLOADED")
    unzip_file(archive_path, folder_path)
    print(">> END")