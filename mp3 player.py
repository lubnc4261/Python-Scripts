from tkinter import *
from tkinter import filedialog
from pygame import mixer

class MusicPlayer:
    def __init__(self, window ):
        window.geometry('450x350'); window.title('Simple Mp3 Player'); window.resizable(0,0)
        Load = Button(window, text = 'Laden',  width = 10, font = ('Times', 10), command = self.load)
        Play = Button(window, text = 'Abspielen',  width = 10,font = ('Times', 10), command = self.play)
        Pause = Button(window,text = 'Pausieren',  width = 10, font = ('Times', 10), command = self.pause)
        Stop = Button(window ,text = 'Stoppen',  width = 10, font = ('Times', 10), command = self.stop)
        Load.place(x=100,y=20);Play.place(x=210,y=20);Pause.place(x=320,y=20);Stop.place(x=210,y=60)
        self.music_file = False
        self.playing_state = False
        
    def load(self):
        self.music_file = filedialog.askopenfilename()
        
    def play(self):
        if self.music_file:
            mixer.init()
            mixer.music.load(self.music_file)
            mixer.music.play()
            
    def pause(self):
        if not self.playing_state:
            mixer.music.pause()
            self.playing_state = True
        else:
            mixer.music.unpause()
            self.playing_state = False
            
    def stop(self):
        mixer.music.stop()

window = Tk()
app = MusicPlayer(window)
window.mainloop()
