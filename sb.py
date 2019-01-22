from tkinter import Tk, Label, Button
import playsound

drive = 'C'
path = drive+r':\Users\jpwil\AppData\Local\Programs\Python\Python37\Scripts\myPythonScripts\soundBoard\soundClips'
headerSpacing ='                              '
soundsList = ['8675309','alright','anotherOne','aspen','blaster',
              'blessUp','byeFelicia','comeOnDown','crickets','dunDunDun',
              'ears','gotDamn','hawHaw','implication','marioOof','neat',
              'nerd','phrasing','playedYourself','rachel','thatsTheJoke',
              'wilson','zoinks']

class sbGUI:
    def __init__(self, master):
        self.master = master
        master.title("soundboard")

        self.label = Label(master, text=headerSpacing)
        self.label.grid(row=0, column=0)
        self.label = Label(master, text=headerSpacing)
        self.label.grid(row=0, column=1)
        self.label = Label(master, text=headerSpacing)
        self.label.grid(row=0, column=2)
        self.label = Label(master, text=headerSpacing)
        self.label.grid(row=0, column=3)
        self.label = Label(master, text=headerSpacing)
        self.label.grid(row=0, column=4)

        self.b0 = Button(master, text=soundsList[0], command=self.play0)
        self.b0.grid(row=1, column=0)
        self.b1 = Button(master, text=soundsList[1], command=self.play1)
        self.b1.grid(row=1, column=1)
        self.b2 = Button(master, text=soundsList[2], command=self.play2)
        self.b2.grid(row=1, column=2)
        self.b3 = Button(master, text=soundsList[3], command=self.play3)
        self.b3.grid(row=1, column=3)
        self.b4 = Button(master, text=soundsList[4], command=self.play4)
        self.b4.grid(row=1, column=4)

        self.b5 = Button(master, text=soundsList[5], command=self.play5)
        self.b5.grid(row=2, column=0)
        self.b6 = Button(master, text=soundsList[6], command=self.play6)
        self.b6.grid(row=2, column=1)
        self.b7 = Button(master, text=soundsList[7], command=self.play7)
        self.b7.grid(row=2, column=2)
        self.b8 = Button(master, text=soundsList[8], command=self.play8)
        self.b8.grid(row=2, column=3)
        self.b9 = Button(master, text=soundsList[9], command=self.play9)
        self.b9.grid(row=2, column=4)

        self.b10 = Button(master, text=soundsList[10], command=self.play10)
        self.b10.grid(row=3, column=0)
        self.b11= Button(master, text=soundsList[11], command=self.play11)
        self.b11.grid(row=3, column=1)
        self.b12 = Button(master, text=soundsList[12], command=self.play12)
        self.b12.grid(row=3, column=2)
        self.b13 = Button(master, text=soundsList[13], command=self.play13)
        self.b13.grid(row=3, column=3)
        self.b14 = Button(master, text=soundsList[14], command=self.play14)
        self.b14.grid(row=3, column=4)

        self.b15 = Button(master, text=soundsList[15], command=self.play15)
        self.b15.grid(row=4, column=0)
        self.b16= Button(master, text=soundsList[16], command=self.play16)
        self.b16.grid(row=4, column=1)
        self.b17 = Button(master, text=soundsList[17], command=self.play17)
        self.b17.grid(row=4, column=2)
        self.b18 = Button(master, text=soundsList[18], command=self.play18)
        self.b18.grid(row=4, column=3)
        self.b19 = Button(master, text=soundsList[19], command=self.play19)
        self.b19.grid(row=4, column=4)

        self.b20 = Button(master, text=soundsList[20], command=self.play20)
        self.b20.grid(row=5, column=0)
        self.b21= Button(master, text=soundsList[21], command=self.play21)
        self.b21.grid(row=5, column=1)
        self.b22 = Button(master, text=soundsList[22], command=self.play22)
        self.b22.grid(row=5, column=2)
        #self.b23 = Button(master, text=soundsList[23], command=self.play23)
        #self.b23.grid(row=5, column=3)
        #self.b24 = Button(master, text=soundsList[24], command=self.play24)
        #self.b24.grid(row=5, column=4)



    def play0(self):
        playsound.playsound(path+'\\'+soundsList[0]+'.mp3', True)
    def play1(self):
        playsound.playsound(path+'\\'+soundsList[1]+'.mp3', True)
    def play2(self):
        playsound.playsound(path+'\\'+soundsList[2]+'.mp3', True)
    def play3(self):
        playsound.playsound(path+'\\'+soundsList[3]+'.mp3', True)
    def play4(self):
        playsound.playsound(path+'\\'+soundsList[4]+'.mp3', True)

    def play5(self):
        playsound.playsound(path+'\\'+soundsList[5]+'.mp3', True)
    def play6(self):
        playsound.playsound(path+'\\'+soundsList[6]+'.mp3', True)
    def play7(self):
        playsound.playsound(path+'\\'+soundsList[7]+'.mp3', True)
    def play8(self):
        playsound.playsound(path+'\\'+soundsList[8]+'.mp3', True)
    def play9(self):
        playsound.playsound(path+'\\'+soundsList[9]+'.mp3', True)

    def play10(self):
        playsound.playsound(path+'\\'+soundsList[10]+'.mp3', True)
    def play11(self):
        playsound.playsound(path+'\\'+soundsList[11]+'.mp3', True)
    def play12(self):
        playsound.playsound(path+'\\'+soundsList[12]+'.mp3', True)
    def play13(self):
        playsound.playsound(path+'\\'+soundsList[13]+'.mp3', True)
    def play14(self):
        playsound.playsound(path+'\\'+soundsList[14]+'.mp3', True)

    def play15(self):
        playsound.playsound(path+'\\'+soundsList[15]+'.mp3', True)
    def play16(self):
        playsound.playsound(path+'\\'+soundsList[16]+'.mp3', True)
    def play17(self):
        playsound.playsound(path+'\\'+soundsList[17]+'.mp3', True)
    def play18(self):
        playsound.playsound(path+'\\'+soundsList[18]+'.mp3', True)
    def play19(self):
        playsound.playsound(path+'\\'+soundsList[19]+'.mp3', True)

    def play20(self):
        playsound.playsound(path+'\\'+soundsList[20]+'.mp3', True)
    def play21(self):
        playsound.playsound(path+'\\'+soundsList[21]+'.mp3', True)
    def play22(self):
        playsound.playsound(path+'\\'+soundsList[22]+'.mp3', True)
    def play23(self):
        playsound.playsound(path+'\\'+soundsList[23]+'.mp3', True)
    def play24(self):
        playsound.playsound(path+'\\'+soundsList[24]+'.mp3', True)



root = Tk()
my_gui = sbGUI(root)
root.mainloop()
