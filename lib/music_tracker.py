from music_track import *

class MusicTracker:

    def __init__(self):
        self.track_history = []

    def add_track(self, track):
        self.track_history.append(track)

    def return_track_history(self):
        songs = ", ".join(self.track_history.title)
        return f"Today you have listened to: {songs}"

weds_music = MusicTracker()
track_1 = Track("Disco Inferno", "50 Cent", 2005)
track_2 = Track("Hotel California", "The Eagles", 1976)
weds_music.add_track(track_1)
weds_music.add_track(track_2)
print(weds_music.track_history)
print(weds_music.return_track_history())
