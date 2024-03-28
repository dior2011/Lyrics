from tkinter import *
import tkinter.messagebox as mb
import json
import requests

def extract_lyrics(artist, song):
   
    artist_name = artist
    song_name = song.lower()
    link = 'https://api.lyrics.ovh/v1/'+artist_name.replace(' ', '%20')+'/'+song_name.replace(' ', '%20')
    req = requests.get(link)
    json_data = json.loads(req.content)
    try:
        lyrics = json_data['lyrics']
        
        with open(f"{artist_name}-{song_name}.txt", "w") as txt:
            txt.write(lyrics)
        return lyrics

    except:
        return "Qo'shiq topilmadi!"

