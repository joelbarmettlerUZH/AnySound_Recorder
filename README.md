# AnySound Recorder

Record any music that you can  hear! There are a lot of services that do not allow you to download their music: Internet Radio, Spotify and so on. But this can be really annoying when you want to load music onto devices that do not support these services or have no active internet connection. AnySound Recorder solves this problem for you!

The main advantages of AnySound:

- Records everything that your can listen to on your computer
- Starts a new record every time a new song starts
- Names the songs automatically and sorts them into folders
- Record music for hours even when you are not at your computer
- Automatically converts your recordings to a simple MP3 format
- Works for YouTube, Spotify, DI.FM, SoundCloud and many more!

# Setup
Let's quickly walk over the steps that are needed in order to run AnySound Recorder.

## Install dependencies
AnySound uses a text recognition software called Tesseract which you will need to run AnySound. Click [here](https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-setup-3.05.01.exe) to download and install tesseract. Make sure to include the language English and to install it at the default location. Otherwise, you will need to change the installation path later on. 

You will need some other third party modules. Install them via pip:

```sh
pip instlal pyscreenshot
pip install cv2
pip install PIL
pip install pytesseract
pip install pyaudio
pip install wave
```

## Fork the GitHub Repo

Fork this github repository or download the files. To run the python script, open the Command promt in the downloaded/forked folder and run:

```sh
python Application.py
```

### Modify tesseract path (optional)
If you have not installed tesseract at the default location *(C://Program Files (x86)/Tesseract_OCR)*, then make sure to change the path to your installation directory in the *Screenshot.py* file. 

```python
# Line 56
pytesseract.tesseract_cmd = 'C:\\YOUR\\INSTALLATION\\PATH\\Tesseract_OCR\\tesseract.exe'
```

## Set the Windows standard audio input
Next, we need to define the windows output sound as its input sound as well in order to record it. This is easy: Play some sound that you like (we will need it to recognize whether we have chosen the right audio input). Then, right-click on the *windows sound icon* and chose *Recording Devices*. One of these devices displayed here is your soundcard. Per default - either no device is selected or your microphone/headset/webcam. Right-Click on one of the devices and chose *activate*. If you have hit the right device, you will immediatelly see green soundbars right next to it, indicating your windows now "hears" what you play. 

# Using the application
Let's give it a try!

Create a new Python script in the same folder as the forked/downloaded respository and import application:
```Python
from Application import ScreenSound
```

Now we first have to create a new Screensound entity. The entity will ask you to mark the region of your display where your songname is displayed. When you run your application, you will see a bunch of nubmers floating down your command promt. This is your current mouse cursor position. You now need to move it to the top-left corner of the region where your Songname is located on the screen. For most applicatins like spotify, DI.FM or SoundCloud, this is at the bottom of the screen. Move to the right location (make sure to exlude everything except the written text) and keep the cursor still for a seconds. When the command promt asks you to now mark the second position, move your cursor to the bottom-right of the text. Keep it still again. Voilà, you successfully market a square that contains your song information which AnySound can extract and use to name your sounds accordingly. 
```python
s = ScreenSound()
```
![Demo](https://github.com/joelbarmettlerUZH/AnySound_Recorder/raw/master/Resources/AnySound_Demo.gif)

Cool! Now we are ready to go. Specify the folder where you want your songs to be stored in, then call *recordFor* to record for X seconds into your specified output folder. Here, I record for 7 hours over night. 

```python
output_folder = "./records/"
s.recordFor(60 * 60 * 7, output_folder)
```

Make sure that you keep your screen turned on and the view on the songname unblocked. Then hit play to make the music play (you only have to leave the windows sound on, feel free to mute your loudspeakers when you do not want to listen to the music the whole night).

Lastly, add the command to convert your recorded songs from **.wav** into **.mp3** with the following statement:

```python
for song in os.listdir(output_folder):
    if song.endswith(".wav"):
        Recorder.wavTomp3(output_folder+song)
```

Note that the the *ffmpeg.exe* file that is responsible for converting wav to mp3 is downloaded from their official website [ffmpeg.org](https://www.ffmpeg.org/) and released under the GNU License 2.1. 

Note that you are only allowed to download music which has no copyright, such as the music that I downloaded as a demonstration. You can find it [here](https://github.com/joelbarmettlerUZH/AnySound_Recorder/tree/master/records).

License
----

MIT License

Copyright (c) 2018 Joel Barmettler

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.















