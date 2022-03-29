from tkinter import Toplevel, PhotoImage, END, NORMAL, DISABLED, Tk, Text, VERTICAL

from tkinter import *
from tkinter.ttk import Progressbar, Label, Button, Frame
import pyttsx3
from pygame import mixer

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # 0 index = male voice

mixer.init()

mixer.music.load('kbc.mp3')
mixer.music.play(-1)


def select(event):
    callButton.place_forget()
    progressbarA.place_forget()
    progressbarB.place_forget()
    progressbarC.place_forget()
    progressbarD.place_forget()

    progressbarLabelA.place_forget()
    progressbarLabelB.place_forget()
    progressbarLabelC.place_forget()
    progressbarLabelD.place_forget()

    b = event.widget  # which button is getting pressed
    value = b['text']  # it will give the text value

    for i in range(15):
        if value == correct_answers[i]:
            if value == correct_answers[14]:
                def close():
                    root2.destroy()
                    root.destroy()

                def playagain():
                    lifeline50Button.config(state=NORMAL, image=image50)
                    audiencePoleButton.config(state=NORMAL, image=audiencePole)
                    phoneLifelineButton.config(state=NORMAL, image=phoneImage)
                    root2.destroy()
                    questionArea.delete(1.0, END)
                    questionArea.insert(END, questions[0])

                    optionButton1.config(text=first_option[0])
                    optionButton2.config(text=second_option[0])
                    optionButton3.config(text=third_option[0])
                    optionButton4.config(text=fourth_option[0])

                    amountlabel.config(image=amountimage)

                mixer.music.stop()
                mixer.music.load('kbcwon.mp3')
                mixer.music.play()

                root2 = Toplevel()
                root2.overrideredirect(True)
                root2.config(bg='black')
                root2.geometry('500x400+140+30')
                root2.title('u won o pounds')
                imgLabel = Label(root2, image=centerImage, bd=0)
                imgLabel.pack(pady=30)

                winlabel = Label(root2, text='Yor won', font=('arial', 40, 'bold'), bg='black', fg='white')
                winlabel.pack()

                playagainButton = Button(root2, text='play Again', font=('arial', 20, 'bold'), bg='black', fg='white',
                                         activebackground='black', activeforeground='white', bd=0, cursor='hand2',
                                         command=playagain)
                playagainButton.pack()

                closeButton = Button(root2, text='Close', font=('arial', 20, 'bold'), bg='black', fg='white',
                                     activebackground='black', activeforeground='white', bd=0, cursor='hand2',
                                     command=close)
                closeButton.pack()

                happyimage = PhotoImage(file='happy.png')
                sadLabel = Label(root2, image=happyimage, bg='black')
                sadLabel.place(x=30, y=280)

                sadLabel1 = Label(root2, image=happyimage, bg='black')
                sadLabel1.place(x=400, y=280)

                root2.mainloop()
                break

            questionArea.delete(1.0, END)
            questionArea.insert(END, questions[i + 1])

            optionButton1.config(text=first_option[i + 1])
            optionButton2.config(text=second_option[i + 1])
            optionButton3.config(text=third_option[i + 1])
            optionButton4.config(text=fourth_option[i + 1])
            amountlabel.config(image=amountImages[i])

        if value not in correct_answers:
            def close():
                root1.destroy()
                root.destroy()

            def tryagain():
                lifeline50Button.config(state=NORMAL, image=image50)
                audiencePoleButton.config(state=NORMAL, image=audiencePole)
                phoneLifelineButton.config(state=NORMAL, image=phoneImage)
                root1.destroy()

                questionArea.delete(1.0, END)
                questionArea.insert(END, questions[0])

                optionButton1.config(text=first_option[0])
                optionButton2.config(text=second_option[0])
                optionButton3.config(text=third_option[0])
                optionButton4.config(text=fourth_option[0])

                amountlabel.config(image=amountimage)

            root1 = Toplevel()
            root1.overrideredirect(True)
            root1.config(bg='black')
            root1.geometry('500x400+140+30')
            root1.title('u won o pounds')
            imgLabel = Label(root1, image=centerImage, bd=0)
            imgLabel.pack(pady=30)

            loselabel = Label(root1, text='Yor Lose', font=('arial', 40, 'bold'), bg='black', fg='white')
            loselabel.pack()

            tryagainButton = Button(root1, text='Try Again', font=('arial', 20, 'bold'), bg='black', fg='white',
                                    activebackground='black', activeforeground='white', bd=0, cursor='hand2',
                                    command=tryagain)
            tryagainButton.pack()

            closeButton = Button(root1, text='Close', font=('arial', 20, 'bold'), bg='black', fg='white',
                                 activebackground='black', activeforeground='white', bd=0, cursor='hand2',
                                 command=close)
            closeButton.pack()

            sadimage = PhotoImage(file='sad.png')
            sadlabel = Label(root1, image=sadimage, bg='black')
            sadlabel.place(x=30, y=280)
            sadlabel1 = Label(root1, image=sadimage, bg='black')
            sadlabel1.place(x=400, y=280)

            root1.mainloop()
            break


def lifeline50():
    lifeline50Button.config(image=image50X, state=DISABLED)
    if questionArea.get(1.0, 'end-1c') == questions[0]:
        optionButton1.config(text='')
        optionButton3.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[1]:
        optionButton2.config(text='')
        optionButton3.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[2]:
        optionButton1.config(text='')
        optionButton3.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[3]:
        optionButton3.config(text='')
        optionButton4.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[4]:
        optionButton4.config(text='')
        optionButton1.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[5]:
        optionButton2.config(text='')
        optionButton4.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[6]:
        optionButton3.config(text='')
        optionButton1.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[7]:
        optionButton2.config(text='')
        optionButton3.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[8]:
        optionButton4.config(text='')
        optionButton3.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[9]:
        optionButton1.config(text='')
        optionButton4.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[10]:
        optionButton1.config(text='')
        optionButton3.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[11]:
        optionButton1.config(text='')
        optionButton4.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[12]:
        optionButton1.config(text='')
        optionButton3.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[13]:
        optionButton2.config(text='')
        optionButton3.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[14]:
        optionButton2.config(text='')
        optionButton3.config(text='')


def audiencePoleLifeline():
    audiencePoleButton.config(image=audiencePoleX, state=DISABLED)
    progressbarA.place(x=580, y=190)
    progressbarB.place(x=620, y=190)
    progressbarC.place(x=660, y=190)
    progressbarD.place(x=7000, y=190)

    progressbarLabelA.place(x=580, y=320)
    progressbarLabelB.place(x=620, y=320)
    progressbarLabelC.place(x=660, y=320)
    progressbarLabelD.place(x=700, y=320)

    if questionArea.get(1.0, 'end-1c') == questions[0]:
        progressbarA.config(value=30)
        progressbarB.config(value=50)
        progressbarC.config(value=60)
        progressbarD.config(value=80)

    if questionArea.get(1.0, 'end-1c') == questions[1]:
        progressbarA.config(value=30)
        progressbarB.config(value=50)
        progressbarC.config(value=60)
        progressbarD.config(value=80)

    if questionArea.get(1.0, 'end-1c') == questions[2]:
        progressbarA.config(value=30)
        progressbarB.config(value=90)
        progressbarC.config(value=60)
        progressbarD.config(value=60)

    if questionArea.get(1.0, 'end-1c') == questions[3]:
        progressbarA.config(value=80)
        progressbarB.config(value=50)
        progressbarC.config(value=60)
        progressbarD.config(value=45)

    if questionArea.get(1.0, 'end-1c') == questions[4]:
        progressbarA.config(value=30)
        progressbarB.config(value=50)
        progressbarC.config(value=90)
        progressbarD.config(value=80)

    if questionArea.get(1.0, 'end-1c') == questions[5]:
        progressbarA.config(value=90)
        progressbarB.config(value=50)
        progressbarC.config(value=60)
        progressbarD.config(value=30)

    if questionArea.get(1.0, 'end-1c') == questions[6]:
        progressbarA.config(value=30)
        progressbarB.config(value=50)
        progressbarC.config(value=60)
        progressbarD.config(value=80)

    if questionArea.get(1.0, 'end-1c') == questions[7]:
        progressbarA.config(value=30)
        progressbarB.config(value=90)
        progressbarC.config(value=60)
        progressbarD.config(value=20)

    if questionArea.get(1.0, 'end-1c') == questions[8]:
        progressbarA.config(value=90)
        progressbarB.config(value=50)
        progressbarC.config(value=60)
        progressbarD.config(value=70)

    if questionArea.get(1.0, 'end-1c') == questions[9]:
        progressbarA.config(value=30)
        progressbarB.config(value=50)
        progressbarC.config(value=80)
        progressbarD.config(value=60)

    if questionArea.get(1.0, 'end-1c') == questions[10]:
        progressbarA.config(value=30)
        progressbarB.config(value=50)
        progressbarC.config(value=60)
        progressbarD.config(value=80)

    if questionArea.get(1.0, 'end-1c') == questions[11]:
        progressbarA.config(value=30)
        progressbarB.config(value=90)
        progressbarC.config(value=60)
        progressbarD.config(value=70)

    if questionArea.get(1.0, 'end-1c') == questions[12]:
        progressbarA.config(value=30)
        progressbarB.config(value=80)
        progressbarC.config(value=60)
        progressbarD.config(value=50)

    if questionArea.get(1.0, 'end-1c') == questions[13]:
        progressbarA.config(value=30)
        progressbarB.config(value=50)
        progressbarC.config(value=60)
        progressbarD.config(value=80)

    if questionArea.get(1.0, 'end-1c') == questions[14]:
        progressbarA.config(value=80)
        progressbarB.config(value=50)
        progressbarC.config(value=60)
        progressbarD.config(value=30)


def phoneLifeline():
    mixer.music.load('calling.mp3')
    mixer.music.play()
    callButton.place(x=70, y=260)
    phoneLifelineButton.config(image=phoneImageX, state=DISABLED)
    callButton.config(image=callimage)


def phoneclick():
    mixer.music.load('kbc.mp3')
    mixer.music.play(-1)
    mixer.music.set_volume(0)
    for i in range(15):
        if questionArea.get(1.0, 'end-1c') == questions[i]:
            engine.say(f'The answer is {correct_answers[i]}')
            engine.runAndWait()


correct_answers = ["Ganesha", "Four", "Sept 8", "Brazil", "Malayalam", "Jainism", "Oct 14",
                   "Suhagan", "Tamil Nadu", "Aryabhatta", "Rabdi", "Chaitra", "Madurai", "Gandhi",
                   "Id-ul-Zuha"]

questions = ["Which of the following gods is also known as ‘Gauri Nandan’?",
             "In the game of ludo the discs or tokens are of how many colours?",
             "International Literacy Day is observed on?",
             "Where was the BRICS summit held in 2014?",
             "The language of Lakshadweep , a union territory of India is",
             "Bahubali festival is related to",
             "Which day is observed as the World's Standards Day?",
             "Which of these terms can only be used for women?",
             "Pongal is a popular festival of which state?",
             "The value of Pi was first given by",
             "Milk is the main ingredients of which of these desserts?",
             "The first month of Saka year is",
             "Meenakshi Temple is in?",
             "Complete the name of this bilateral test cricket series played between India and South Africa: "
             "___________ Mandela Series",
             "The festival celebrated to commemorate the ordeal of Islamics is"]

first_option = ["Agni", "One", "Nov 28", "Brazil", "Tamil", "Jainism", "Dec 2", "Dirghaayu",
                "Tamil Nadu", "Bhaskara", "Petha", "Vaisakh", "Puri", "Nehru",
                "Id-ul-Zuha"]

second_option = [" Indra", "Two", "Sept 8", "India", "Hindi", "Islam", "Nov 15", "Suhagan",
                 "Karnataka", "Varahamihira", "Jalebi", "Chaitra", "Madurai", "Patel", "Moharram"]

third_option = ["Hanuman", "Three", "May 2", " Russia", "Malayalam", "Buddhism", "June 26", "Chiranjeevi",
                "Kerala", "Aryabhatta", "Chikki", "Jyeshtha", "Trivandrum", "Vajpayee",
                "Id-i-Milad"]

fourth_option = ["Ganesha", "Four", "Sept 22", "China", "Telugu", "Hinduism", "Oct 14",
                 "Sushil", "Bihar", "None of these", "Rabdi", "Paush", "Chennai",
                 "Gandhi", "Id-ul-Fitr"]

root = Tk()
root.geometry('1270x652+0+0')  # height,width,distance from x and y axis
root.resizable(0, 0)
root.title('Who wants to be a millianaire')
root.config(bg='black')  # set the blackground color as black

leftFrame = Frame(root, bg='black', padx=90)  # for hori padding
leftFrame.grid(row=0, column=0)

topframe = Frame(leftFrame, bg='black', pady=15)  # for vertical padding
topframe.grid(row=0, column=0)

centerframe = Frame(leftFrame, bg='black', pady=15)
centerframe.grid(row=1, column=0)

bottomFrame = Frame(leftFrame, bg='black')
bottomFrame.grid(row=2, column=0)

rightframe = Frame(root, pady=25, padx=50, bg='black')
rightframe.grid(row=0, column=1)

image50 = PhotoImage(file='50-50.png')
image50X = PhotoImage(file='50-50-X.png')

lifeline50Button = Button(topframe, image=image50, bg='black', bd=0, activebackground='black', width=180, height=80,
                          command=lifeline50)
lifeline50Button.grid(row=0, column=0)

audiencePole = PhotoImage(file='audiencePole.png')
audiencePoleX = PhotoImage(file='audiencePoleX.png')

audiencePoleButton = Button(topframe, image=audiencePole, bg='black', bd=0, activebackground='black', width=180,
                            height=80, command=audiencePoleLifeline)
audiencePoleButton.grid(row=0, column=1)

phoneImage = PhotoImage(file='phoneAFriend.png')
phoneImageX = PhotoImage(file='phoneAFriendX.png')

phoneLifelineButton = Button(topframe, image=phoneImage, bg='black', bd=0, activebackground='black', width=180,
                             height=80, command=phoneLifeline)
phoneLifelineButton.grid(row=0, column=2)

callimage = PhotoImage(files='phone.png')
callButton = Button(root, image=callimage, bd=0, bg='black', activebackground='black', cursor='hand2',
                    command=phoneclick)

centerImage = PhotoImage(file='center.png')

logoLabel = Label(centerframe, image=centerImage, bg='black', width=300, height=200)
logoLabel.grid(row=0, column=0)

amountimage = PhotoImage(file='Picture0.png')
amountimage1 = PhotoImage(file='Picture1.png')
amountimage2 = PhotoImage(file='Picture2.png')
amountimage3 = PhotoImage(file='Picture3.png')
amountimage4 = PhotoImage(file='Picture4.png')
amountimage5 = PhotoImage(file='Picture5.png')
amountimage6 = PhotoImage(file='Picture6.png')
amountimage7 = PhotoImage(file='Picture7.png')
amountimage8 = PhotoImage(file='Picture8.png')
amountimage9 = PhotoImage(file='Picture9.png')
amountimage10 = PhotoImage(file='Picture10.png')
amountimage11 = PhotoImage(file='Picture11.png')
amountimage12 = PhotoImage(file='Picture12.png')
amountimage13 = PhotoImage(file='Picture13.png')
amountimage14 = PhotoImage(file='Picture14.png')
amountimage15 = PhotoImage(file='Picture15.png')

amountImages = [amountimage1, amountimage2, amountimage3, amountimage4, amountimage5, amountimage6, amountimage7,
                amountimage8, amountimage9, amountimage10, amountimage11, amountimage12, amountimage13, amountimage14,
                amountimage15]

amountlabel = Label(rightframe, image=amountimage, bg='black', bd=0)
amountlabel.grid(row=0, column=0)

layoutimage = PhotoImage(file='lay.png')
layoutlabel = Label(bottomFrame, image=layoutimage, bg='black', bd=0)
layoutlabel.grid(row=0, column=0)

questionArea = Text(bottomFrame, font=('arial', 18, 'bold'), width=40, height=2, wrap='word', bg='black', fg='white',
                    bd=0)
questionArea.place(x=70, y=10)

questionArea.insert(END, questions[0])

labelA = Label(bottomFrame, text='A:', bg='black', fg='white', font=('arial', 16, 'bold'))
labelA.place(x=60, y=110)

optionButton1 = Button(bottomFrame, text=first_option[0], font=('arial', 18, 'bold'), bg='black', fg='white', bd=0,
                       activebackground='black', activeforeground='white', cursor='hand2')
optionButton1.place(x=100, y=100)

labelB = Label(bottomFrame, text='B:', bg='black', fg='white', font=('arial', 16, 'bold'))
labelB.place(x=330, y=110)

optionButton2 = Button(bottomFrame, text=second_option[0], font=('arial', 18, 'bold'), bg='black', fg='white', bd=0,
                       activebackground='black', activeforeground='white', cursor='hand2')
optionButton2.place(x=370, y=100)

labelC = Label(bottomFrame, text='C:', bg='black', fg='white', font=('arial', 16, 'bold'))
labelC.place(x=60, y=190)

optionButton3 = Button(bottomFrame, text=third_option[0], font=('arial', 18, 'bold'), bg='black', fg='white', bd=0,
                       activebackground='black', activeforeground='white', cursor='hand2')
optionButton3.place(x=100, y=180)

labelD = Label(bottomFrame, text='D:', bg='black', fg='white', font=('arial', 16, 'bold'))
labelD.place(x=330, y=190)

optionButton4 = Button(bottomFrame, text=fourth_option[0], font=('arial', 18, 'bold'), bg='black', fg='white', bd=0,
                       activebackground='black', activeforeground='white', cursor='hand2')
optionButton4.place(x=370, y=180)

progressbarA = Progressbar(root, orient=VERTICAL, mode='determinate', length=120)
progressbarB = Progressbar(root, orient=VERTICAL, mode='determinate', length=120)
progressbarC = Progressbar(root, orient=VERTICAL, mode='determinate', length=120)
progressbarD = Progressbar(root, orient=VERTICAL, mode='determinate', length=120)

progressbarLabelA = Label(root, text='A', font=('arial', 20, 'bold'), bg='black', fg='white')
progressbarLabelB = Label(root, text='B', font=('arial', 20, 'bold'), bg='black', fg='white')
progressbarLabelC = Label(root, text='C', font=('arial', 20, 'bold'), bg='black', fg='white')
progressbarLabelD = Label(root, text='D', font=('arial', 20, 'bold'), bg='black', fg='white')

optionButton1.bind('<Button-1>', select)
optionButton2.bind('<Button-1>', select)
optionButton3.bind('<Button-1>', select)
optionButton4.bind('<Button-1>', select)

root.mainloop()
