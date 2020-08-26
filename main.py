import  json
#pillow for jpeg files and gif images
from difflib import get_close_matches
from tkinter import *
import pyttsx3 as pp
from tkinter import messagebox


engine=pp.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

rate=engine.getProperty('rate')
engine.setProperty('rate',150)

#########################functon############
def iexit():
    res =messagebox.askyesno('confirm',' you want to EXIT')
    if res:
        root.destroy()
    else:
        pass
def clear():
    textarea.delete(1.0, END)
    enterwordentry.delete(0, END)
meaning=' '
def search():
    textarea.delete(1.0,END)
    data=json.load(open('data.json'))

    word=enterwordentry.get()
    word=word.lower()
    if word in data:
        meaning=data[word]
    elif len(get_close_matches(word,data.keys()))>0:
        close_match=get_close_matches(word,data.keys())[0]
        res=messagebox.askyesno('confirm','did you mean {}'.format(close_match))
        if res:
            meaning=data[close_match]
        else:
            messagebox.showinfo('information','the word doesn\'t exist')
            meaning=''
    else:
        messagebox.showerror('error','the word doesn\'t exist plz double check')
    if meaning!='':
        if isinstance(meaning,list):
            for item in meaning:
                textarea.insert(END,u'\u2022' + item + '\n\n')
            else:
                meaning=meaning[0:30]
                textarea.insert(END,u'\u2022 {} \n\n'.format(meaning))

def wordaudio():
    engine.say(enterwordentry.get())
    engine.runAndWait()
def meaningaudio():
    engine.say(textarea.get(1.0,END))
    engine.runAndWait()
#########################gui part
root=Tk()
root.geometry('1000x626+100+10')
root.title('talking dictionary created by BVG')

bgImage=PhotoImage(file='bg.png')
bglabel=Label(root,image=bgImage)
bglabel.place(x=0,y=0)

enterwordlabel=Label(root,text='ENTER WORD',font=('elephant',29,'bold'),fg='green',bg='whitesmoke') #castellar  convert text into upper case
enterwordlabel.place(x=530,y=20)

enterwordentry=Entry(root,font=('arial',23,'bold'),bd=8,relief=GROOVE,justify=CENTER)
enterwordentry.place(x=530,y=80)

searchImage=PhotoImage(file='search.png')
searchButton=Button(root,image=searchImage,bd=0,bg='whitesmoke',activebackground='whitesmoke',cursor='hand2',command=search)
searchButton.place(x=620,y=150)

micImage=PhotoImage(file='mic.png')
micButton=Button(root,image=micImage,bd=0,bg='whitesmoke',activebackground='whitesmoke',cursor='hand2',command=wordaudio)
micButton.place(x=710,y=150)


meaningLabel=Label(root,text='MEANING',font=('elephant',29,'bold'),fg='red3',bg='whitesmoke')
meaningLabel.place(x=580,y=240)

textarea=Text(root, font=('arial', 15, 'bold'),relief=RIDGE, height=8, width=34, wrap='word',bg='white')
textarea.place(x=520,y=300)

audioImage=PhotoImage(file='microphone.png')
audioButton=Button(root,image=audioImage,bd=0,bg='whitesmoke',activebackground='whitesmoke',cursor='hand2',command=meaningaudio)
audioButton.place(x=530,y=555)

clearImage=PhotoImage(file='clear.png')
clearButton=Button(root,image=clearImage,bd=0,bg='whitesmoke',activebackground='whitesmoke',cursor='hand2',command=clear)
clearButton.place(x=650,y=555)

exitImage=PhotoImage(file='exit.png')
exitButton=Button(root,image=exitImage,bd=0,bg='whitesmoke',activebackground='whitesmoke',cursor='hand2',command=iexit)
exitButton.place(x=800,y=555)
root.resizable(0,0)
root.mainloop()