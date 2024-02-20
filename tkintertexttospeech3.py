from gtts import gTTS
import os
from tkinter import *

root =Tk()
c1=Canvas(root,height=300,width=400)
c1.pack()

def texttospeech():
    t=entry.get()
    language='hi'
    output=gTTS(text=t,lang='hi',slow=False)
    output.save("output.mp3")
    os.system("start output.mp3")

text=Label(text="TEXT TO SPEECH CONVERTER APP",font=30,fg='grey',bg="brown")
c1.create_window(200,100,window=text)
entry=Entry(root)
c1.create_window(200,180,window=entry)

button=Button(text="converter",command=texttospeech)
c1.create_window(200,230,window=button)


root.mainloop()