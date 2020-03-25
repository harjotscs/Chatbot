from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *
import pyttsx3 as py
import speech_recognition as srm
import threading

tk = Tk()
frame = Frame(tk)
engine = py.init()

voices = engine.getProperty('voices')
print(voices)
engine.setProperty('voice', voices[1].id)

tk.geometry('500x800')
tk.configure(bg="#212121")
tk.title('Beast')
chatbot = ChatBot('Beast')

conversation = [
    'what is your name',
    'My name is Beast',
    'What can you do',
    'I can assist you regarding placements',
    'which companies are coming for placements',
    'Microsoft Amazon Google',
    'Average Package Amazon',
    '28 LPA',
    'Average Package Microsoft',
    '42 LPA',
    'Average Package TCS',
    '5 LPA',
    'Average Package Cognizant',
    '6 LPA',
    'Average Package Bosch',
    '7 LPA',
    'Amazon Criteria',
    '7 CGPA, No Re Appears, No Backlogs'
    'TCS Criteria',
    '7 CGPA, No Re Appears, No Backlogs'
    'Microsoft Criteria',
    '7 CGPA, No Re Appears, No Backlogs',
]

trainer = ListTrainer(chatbot)
trainer.train(conversation)


def getQuery():
    sr = srm.Recognizer()
    sr.pause_threshold = 1
    print("Ready To Answer Please Ask Your Query")
    with srm.Microphone() as m:

        try:
            audio = sr.listen(m)
            query = sr.recognize_google(audio, language='eng-in')
            print(query)
            input.delete(0, END)
            input.insert(0, query)
            responses()
        except Exception as e:
            print(e)
            print('Not Recognised')


def speak(word):
    engine.say(word)
    engine.runAndWait()


def responses():
    query = input.get()
    # reply='hi'
    reply = chatbot.get_response(query)
    chat.insert(END, 'User=>' + str(query))
    chat.insert(END, 'Beast=>' + str(reply))
    speak(reply)
    input.delete(0, END)
    chat.yview(END)


def submit(onEnter):
    response.invoke()


tk.bind('<Return>', submit)

logoDecryption = PhotoImage(file='logo.png')
logo = Label(tk, image=logoDecryption, width=250, height=250)
logo.pack(padx=5, pady=5)

scrollbar = Scrollbar(frame)
scrollbar.pack(side=RIGHT, fill=Y)
chat = Listbox(frame, width=80, height=14, bg='#212121', font='stencil 14',fg='gray', yscrollcommand=scrollbar.set)
chat.pack(side=LEFT, fill=BOTH, pady=10)
frame.pack()


input = Entry(tk, font='amazobitaemostrovfine 20', fg='gray',bg='#212121')
input.insert(0, 'please speak or Enter your Query')
input.pack(fill=X, pady=5)
response = Button(tk, font='amazobitaemostrovfine 20', fg='gray',bg='#212121', text='Ask Your Query', command=responses)
response.pack()


def repeatListen():
    while True:
        print('run me')
        getQuery()


t = threading.Thread(target=repeatListen)
t.start()

tk.mainloop()