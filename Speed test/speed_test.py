from tkinter import *
import speedtest
window=Tk()
window.title("Internet speed test")
window.geometry("360x600")
window.resizable(False,False) # Disables the Resize button in window
window.configure(bg="#1a212d")

def check():
    test=speedtest.Speedtest()
    Uploading=round(test.upload()/(1024*1024),2)
    #print(Uploading)
    upload.config(text=Uploading)

    downloading=round(test.download()/(1024*1024),2)
    #print(downloading)
    download.config(text=downloading)
    Download.config(text=downloading)
    servernames=[]
    test.get_servers(servernames)
    #print(test.results.ping)
    ping.config(text=test.results.ping)

# Icon For Speed Test
icon=PhotoImage(file="logo.png")
window.iconphoto(False,icon)

# Images
Top=PhotoImage(file="top.png")
Label(window,image=Top,bg="#1a212d").pack()
Main=PhotoImage(file="main.png")
Label(window,image=Main,bg="#1a212d").pack(pady=(40,0))
button=PhotoImage(file="button.png")
Button=Button(window,image=button,bg="#1a212d",bd=0,activebackground="#1a212d",cursor="hand2",command=check)
Button.pack(pady=10)

# Label
Label(window,text="PING",font="arial 10 bold",bg="#384056").place(x=50,y=0)
Label(window,text="DOWNLOAD",font="arial 10 bold",bg="#384056").place(x=140,y=0)
Label(window,text="UPLOAD",font="arial 10 bold",bg="#384056").place(x=260,y=0)

Label(window,text="MS",font="arial 7 bold",bg="#384056",fg="white").place(x=60,y=80)
Label(window,text="MBPS",font="arial 7 bold",bg="#384056",fg="white").place(x=165,y=80)
Label(window,text="MBPS",font="arial 7 bold",bg="#384056",fg="white").place(x=275,y=80)

Label(window,text="DOWNLOAD",font="arial 15 bold",bg="#384056",fg="white").place(x=125,y=280)
Label(window,text="MBPS",font="arial 15 bold",bg="#384056",fg="white").place(x=155,y=380)

ping=Label(window,text="00",font="arial 13 bold",bg="#384056",fg="white")
ping.place(x=70,y=60,anchor="center")
download=Label(window,text="00",font="arial 13 bold",bg="#384056",fg="white")
download.place(x=180,y=60,anchor="center")
upload=Label(window,text="00",font="arial 13 bold",bg="#384056",fg="white")
upload.place(x=290,y=60,anchor="center")
Download=Label(window,text="00",font="arial 40 bold",bg="#384056")
Download.place(x=185,y=350,anchor="center")

window.mainloop()
