import shutil
import tkinter.font as font
from os import walk
from pathlib import Path
from tkinter import *

# Script permettant de déplacer les fichiers afin de mettre de l'ordre

root = Tk()

root.title("SteelFiles Management")
root.resizable(width=False, height=False)

window_width = 650
window_height = 680

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_cordinate = int((screen_width / 2) - (window_width / 2))  # Permet de mettre la fenêtre au milieu
y_cordinate = int((screen_height / 2) - (window_height / 2))

root.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")

background = PhotoImage(file='assets/doc6.png')
root.iconbitmap("assets/logoo.ico")

label1 = Label(root, image=background)
label1.place(x=-2, y=-2)

vide = Frame(None).grid(row=0, pady=60)


# root.overrideredirect(1)

# ----------------------------------


text_color = 'black'
color_bg = '#e8c292'

font_entry = font.Font(size=12, family='ArialBlack', weight='bold')

path_label1 = Label(root, text='Déplacer depuis', bg=color_bg)
path_label1['font'] = font_entry
path_tri = Entry(root, borderwidth=3, width=30, fg=text_color, bg=color_bg)

# Path de base (Downloads)
downloads_path = (str(Path.home() / "Downloads").replace("\\", "/") + '/')
image_path = (str(Path.home() / "Images").replace("\\", "/") + '/')
music_path = (str(Path.home() / "Music").replace("\\", "/") + '/')
video_path = (str(Path.home() / "Videos").replace("\\", "/") + '/')

path_tri.insert(END, downloads_path)

# path_tri.insert(END, path)
path_tri['font'] = font_entry

path_label1.grid(column=0, row=1, ipadx=5, pady=15, padx=40)
path_tri.grid(column=1, row=1, ipadx=5, pady=5)

# ------------------------------------

files_image = []
files_videos = []
files_rar = []
files_son = []
files_doctexte = []

listeFichiers = []

Entry_sound = Entry(root, width=30, borderwidth=3, fg=text_color, bg=color_bg)
Entry_sound['font'] = font_entry
path_label2 = Label(root, text='Dossier de destination', bg=color_bg)
path_label2['font'] = font_entry

Entry_image = Entry(root, width=30, borderwidth=3, fg=text_color, bg=color_bg)
Entry_image['font'] = font_entry
path_label3 = Label(root, text='Dossier de destination', bg=color_bg)
path_label3['font'] = font_entry

Entry_video = Entry(root, width=30, borderwidth=3, fg=text_color, bg=color_bg)
Entry_video['font'] = font_entry
path_label4 = Label(root, text='Dossier de destination', bg=color_bg)
path_label4['font'] = font_entry

Entry_doctexte = Entry(root, width=30, borderwidth=3, fg=text_color, bg=color_bg)
Entry_doctexte['font'] = font_entry
path_label5 = Label(root, text='Dossier de destination', bg=color_bg)
path_label5['font'] = font_entry

# -------------------------------------------

checked_audio = IntVar()
checked_image = IntVar()
checked_video = IntVar()
checked_doctexte = IntVar()


def active_check():
    if checked_audio.get() == 1:
        Entry_sound.grid(row=3, column=1)
        path_label2.grid(column=0, row=3, ipadx=10, pady=5)
    elif checked_audio.get() == 0:
        Entry_sound.grid_forget()
        path_label2.grid_forget()

    if checked_image.get() == 1:
        Entry_image.grid(row=5, column=1)
        path_label3.grid(column=0, row=5, ipadx=10, pady=5)
    elif checked_image.get() == 0:
        Entry_image.grid_forget()
        path_label3.grid_forget()

    if checked_video.get() == 1:
        Entry_video.grid(row=7, column=1)
        path_label4.grid(column=0, row=7, ipadx=10, pady=5)
    elif checked_video.get() == 0:
        Entry_video.grid_forget()
        path_label4.grid_forget()

    if checked_doctexte.get() == 1:
        Entry_doctexte.grid(row=9, column=1)
        path_label5.grid(row=9, column=0, ipadx=10, pady=5)
    elif checked_doctexte.get() == 0:
        Entry_doctexte.grid_forget()
        path_label5.grid_forget()


tri_sound = Checkbutton(root, text='Déplacer les fichiers audio',
                        onvalue=1, offvalue=0, variable=checked_audio, command=active_check, bg=color_bg)
tri_sound['font'] = font_entry
tri_sound.grid(row=2, column=1, pady=10, ipadx=20)

# --------------------------------------------

tri_image = Checkbutton(root, text='Déplacer les fichiers image',
                        onvalue=1, offvalue=0, variable=checked_image, command=active_check, bg=color_bg)
tri_image['font'] = font_entry
tri_image.grid(row=4, column=1, pady=10, ipadx=20)

tri_video = Checkbutton(root, text='Déplacer les fichiers vidéos',
                        onvalue=1, offvalue=0, variable=checked_video, command=active_check, bg=color_bg)
tri_video['font'] = font_entry
tri_video.grid(row=6, column=1, pady=10, ipadx=20)

tri_doctexte = Checkbutton(root, text='Déplacerles fichiers textes',
                           onvalue=1, offvalue=0, variable=checked_doctexte, command=active_check, bg=color_bg)
tri_doctexte['font'] = font_entry
tri_doctexte.grid(row=8, column=1, pady=10, ipadx=20)

format_sound = ['.flac', '.mp3', '.wav', '.ogg', '.aac']
format_image = ['.jpg', '.gif', '.png', '.PNG', '.ico', '.webp', '.jpeg']
format_video = ['.mp4', '.avi', '.mkv', '.mov', '.webm', '.mpeg']
format_doctexte = ['.txt', '.pdf', '.doc', '.ppt', '.pps', '.rtf', '.xml']


# ---------------------------------------

def enable_trie():
    global listeFichiers, fichiers, file

    n = 0
    path_base = Entry.get(path_tri)
    path_sound = Entry.get(Entry_sound)
    path_image = Entry.get(Entry_image)
    path_videos = Entry.get(Entry_video)
    path_doctexte = Entry.get(Entry_doctexte)

    for (repertoire, sousRepertoires, fichiers) in walk(path_base):
        listeFichiers.extend(fichiers)
        print(fichiers)

        for x in fichiers:

            if checked_audio.get() == 1:
                for n in range(len(format_sound)):
                    if format_sound[n] in x:
                        files_son.append(path_base + x)
                        n += 1

            if checked_image.get() == 1:
                for n in range(len(format_image)):
                    if format_image[n] in x:
                        files_image.append(path_base + x)
                        n += 1

            if checked_video.get() == 1:
                for n in range(len(format_video)):
                    if format_video[n] in x:
                        files_videos.append(path_base + x)
                        n += 1

            if checked_doctexte.get() == 1:
                for n in range(len(format_doctexte)):
                    if format_doctexte[n] in x:
                        files_doctexte.append(path_base + x)
                        n += 1

            '''if '.rar' in x or '.zip' in x or '.7z' in x or '.tar.gz' in x:
                files_rar.append('/Users/alexa/Downloads/' + x)'''

        break
        # Enlever le break pour trier même les sous répertoires

    print(f'----------------\n'
          f'> {len(files_son)} fichiers images ont été déplacés')

    print(f'----------------\n'
          f'> {len(files_image)} fichiers audios ont été déplacés')

    print(f'----------------\n'
          f'> {len(files_videos)} fichiers vidéos ont été déplacés')

    print(f'----------------\n'
          f'> {len(files_doctexte)} fi'
          f'chiers documents/textes ont été déplacés')

    for file in files_image:
        shutil.move(file, path_image)

    for file in files_son:
        shutil.move(file, path_sound)

    for file in files_videos:
        shutil.move(file, path_videos)

    for file in files_doctexte:
        shutil.move(file, path_doctexte)

    '''for file in files_rar:
        shutil.move(file, path_rar)'''


# ---------------------------------------------------------

Entry_image.insert(END, image_path)
Entry_sound.insert(END, music_path)
Entry_video.insert(END, video_path)

submit = Button(root, text='Start', command=enable_trie, width=20, bg=color_bg, borderwidth=3)
submit.grid(row=12, column=1, pady=20, padx=140)
submit['font'] = font_entry

root.mainloop()
