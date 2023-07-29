# -*- coding: utf-8 -*-
"""
Created on Tue May 25 18:06:21 2021

@author: shrey
"""

#Creating GUI with tkinter
import tkinter
from tkinter import *
import chat
import speech_recognition as s
from google_trans_new import google_translator


translator = google_translator()

def send():
    msg = EntryBox.get("1.0",'end-1c').strip()
    #translator = google_translator()
    language = translator.detect(msg)[1]
    print(language)
    translate = translator.translate(msg, lang_tgt='eng')
    EntryBox.delete("0.0",END)

    if msg != '':
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, "You: " + msg + '\n\n')
        ChatLog.config(foreground="#442265", font=("Verdana", 12 ))
        msg=translate
    
        res = chat.chatbot_response(msg)
        if language == "marathi":
            res = translator.translate(res, lang_tgt='mr')
            
        if language == "hindi":
            res = translator.translate(res, lang_tgt='hi')
        
        print("res "+res)
        ChatLog.insert(END, "Bot: " + res + '\n\n')
            
        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)
        


def takeQuery():
    sr = s.Recognizer()
    sr.pause_threshold = 0.5
    print("your bot is listening try to speak")
    with s.Microphone() as m:
        try:
            print("listen")
            audio = sr.listen(m)
          #  query=format(sr.recognize(audio))
            query = sr.recognize_google(audio, language='eng-in')
            print(query)
            EntryBox.delete("0.0", END)
            EntryBox.insert(END, query)
            send()
        except Exception as e:
            print(e)
            print("not recognized")



base = Tk()
base.title("Chatbot")
base.geometry("400x500")
base.resizable(width=FALSE, height=FALSE)

#Create Chat window
ChatLog = Text(base, bd=0, bg="white", height="8", width="50", font="Arial",)

ChatLog.config(state=DISABLED)

#Bind scrollbar to Chat window
scrollbar = Scrollbar(base, command=ChatLog.yview, cursor="heart")
ChatLog['yscrollcommand'] = scrollbar.set

#Create Button to send message
SendButton = Button(base, font=("Verdana",12,'bold'), text="Send", width="12", height=5,
                    bd=0, bg="#32de97", activebackground="#3c9d9b",fg='#ffffff',
                    command= send )

#Create the box to enter message
EntryBox = Text(base, bd=0, bg="white",width="29", height="5", font="Arial")
#EntryBox.bind("<Return>", send)


AudioButton = Button(base, font=("Verdana",12,'bold'), text="Speak", width="12", height=5,
                    bd=0, bg="#32de97", activebackground="#3c9d9b",fg='#ffffff',
                    command= takeQuery )

#Place all components on the screen
scrollbar.place(x=376,y=6, height=386)
ChatLog.place(x=6,y=6, height=386, width=370)
EntryBox.place(x=128, y=401, height=90, width=265)
SendButton.place(x=6, y=401, height=45)
AudioButton.place(x=6, y=447, height=45, width=122)

#t = threading.Thread(target=takeQuery)
#t.start()



base.mainloop()
