
from lib.music_tracker import *
from lib.music_track import *

#As a user
#So that I can keep track of my music listening
#I want to add tracks I've listened to and see a list of them.

# add tracks I've listened to to a track history

def test_add_track():
    track_1 = Track("Purple Rain", "Prince", 1984)
    track_2 = Track("Hello", "Adele", 2015)
    music_tracker = MusicTracker()
    music_tracker.add_track(track_1)
    music_tracker.add_track(track_2)
    assert music_tracker.track_history == ["Purple Rain", "Prince", 1984, "Hello", "Adele", 2015]

# return a track history in a list
def test_return_track_history():
    music_tracker = MusicTracker()
    music_tracker.add_track("Hello by Adele")
    music_tracker.add_track("Believe by Cher")
    assert music_tracker.return_track_history() == "Today you have listened to: Hello by Adele, Believe by Cher"


