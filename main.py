import shutil
from os import walk

# Script permettant de déplacer les fichiers afin de mettre de l'ordre

files_image = []
files_videos = []
files_rar = []
files_son = []

path_download = '/Users/alexa/Downloads'
path_image = '/Users/alexa/Downloads/Image'
path_videos = '/Users/alexa/Downloads/Vidéos'
path_rar = '/Users/alexa/Downloads/fichiers rar'
path_sound = '/Users/alexa/Downloads/son'

listeFichiers = []

for (repertoire, sousRepertoires, fichiers) in walk(path_download):
    listeFichiers.extend(fichiers)

    print(fichiers)
    for x in fichiers:
        if '.jpg' in x or '.png' in x or '.ico' in x or '.gif' in x:
            files_image.append('/Users/alexa/Downloads/' + x)

    for x in fichiers:
        if '.mkv' in x or '.mp4' in x or '.avi' in x or '.mov' in x:
            files_videos.append('/Users/alexa/Downloads/' + x)

    for x in fichiers:
        if '.rar' in x or '.zip' in x or '.7z' in x or '.tar.gz' in x:
            files_rar.append('/Users/alexa/Downloads/' + x)

    for x in fichiers:
        if '.flac' in x or '.mp3' in x or '.wav' in x or '.ogg' in x or '.aac' in x:
            files_son.append('/Users/alexa/Downloads/' + x)
    break
    # Enlever le break pour trier même les sous répertoires

for file in files_image:
    shutil.move(file, path_image)

for file in files_videos:
    shutil.move(file, path_videos)

for file in files_rar:
    shutil.move(file, path_rar)

for file in files_son:
    shutil.move(file, path_sound)
