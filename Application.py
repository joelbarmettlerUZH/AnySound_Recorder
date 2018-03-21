from Screenshot import ScreenInfo
from Soundrecorder import Recorder
import time
import threading
import os
import random

class ScreenSound():
    def __init__(self):
        self._info = self.setNameFinder()
        self._recorder = Recorder()
        self._songs = []

    # Ask user to hover over top-left and bottom-right corner of screen part that holds the song name
    def setNameFinder(self):
        print("Hover still over top-left location where name is displayed for 1 second")
        x1, y1 = ScreenInfo.pickLocation()
        print("Hover still over bottom-right location where name is displayed for 1 second")
        x2, y2 = ScreenInfo.pickLocation()
        # Return 4 coordiantes
        return ScreenInfo((x1, y1, x2, y2))

    def recordSong(self, folder=""):
        # Identify song name
        songname = self._info.getText()
        # Rename song if already existent. Comment this line if you do not wish that behaviour.
        if os.path.isfile(songname+".mp3"):
            songname += " - Copy "+str(random.randint(10000,100000))
        # Start new thread that records the music
        print("Recording: "+songname)
        threading._start_new_thread(self._recorder.start, ())
        # Wait for a change in the songname to happen
        while(True):
            self._info.update()
            if songname != self._info.getText():
                break
            time.sleep(0.5)
        # Stop recording if change is detected
        self._recorder.stop()
        # Force entering other thread to stop the song
        time.sleep(0.01)
        # Song stopped, now save it to folder
        self._recorder.save(folder+songname)
        self._songs.append(songname)

    def recordFor(self, seconds, folder=""):
        #Record for X seconds all songs into folder.
        if not os.path.exists(folder):
            os.makedirs(folder)
        start = time.time()
        # Check whether X seconds have passed.
        while(time.time() - start < seconds):
            self.recordSong(folder)
        return self._songs

if __name__ == "__main__":
    s = ScreenSound()
    output_folder = "./records/"

    #Record songs
    print(s.recordFor(60*10, folder=output_folder))

    # Convert all songs from wav to mp3
    for song in os.listdir(output_folder):
        if song.endswith(".wav"):
            Recorder.wavTomp3(output_folder+song)