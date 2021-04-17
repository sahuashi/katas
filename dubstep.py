def song_decoder(song):
    decoded = song.replace("WUB", " ").strip()
    return ' '.join(decoded.split())