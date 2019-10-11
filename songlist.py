import glob
import csv

names = glob.glob("*.mp3")
#Sample file name : 1_song-album.mp3
try:
    songarr = []
    
    for name in names:
        songmap = {}
        songname = "NA"
        movie = "NA"
        id = name.split("_")[0]
        if "-" in name.split("_")[1]:
            songname = name.split("_")[1].split("-")[0]
            movie = name.split("_")[1].split("-")[1].split(".")[0] 
        else:
            songname = name.split("_")[1].split(".")[0]
        songmap['id'] = id
        songmap['name'] = songname
        songmap['movie'] = movie
        songarr.append(songmap)
            
    with open('songs.csv', mode='w') as csv_file:
        fieldnames = ['id', 'name', 'movie']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        for song in songarr:
            writer.writerow(song)
except Exception as e:
    print(str(e))