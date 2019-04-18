from tkinter import *
from tkinter import ttk
import requests as req
from bs4 import BeautifulSoup
from collections import OrderedDict
import datetime
import socket
from urllib.request import urlopen, URLError, HTTPError
from tkinter import messagebox
import urllib.request
from PIL import ImageTk, Image
import webbrowser


class mainwindow(Frame):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.mainpage()

    def mainpage(self):
        self.frame1 = Frame(self.master, bg='maroon')
        self.frame1.grid(row=0, column=0, sticky=N + S + W + E)
        now=datetime.datetime.now()
        date_time = Label(self.frame1,text='UPDATED: '+now.strftime("%Y-%m-%d %H:%M:%S"),fg='white',bg='maroon', font='arial 10 bold')
        date_time.grid(row=0,column=0,sticky=W)
        refresh = Button(self.frame1, text="Refresh",command=self.mainpage)
        refresh.grid(row=0,column=1,sticky=E)
        self.urlmain = "https://timesofindia.indiatimes.com/"
        self.r = req.get(self.urlmain)
        self.soup = BeautifulSoup(self.r.content, 'html.parser')
        self.TNS()
        self.LN()
        self.CITY()
        self.SPORTS()
        self.LIVEMARK()

    def forloopfuncmainpage(self,text2):
        for i in range(len(text2)-1):
            self.text.insert('end', str(i + 1) + '.' + text2[i].get_text() + "\n")
            key = str(i + 1) + '.' + text2[i].get_text() + "\n"
            ulink = 'https://timesofindia.indiatimes.com%s' % text2[i].get('href')
            self.link.update({key: ulink})
            self.text.bind("<Double-Button-1>",self.OnDouble)

    def TNS(self):
        self.topNewsStories = Label(self.frame1, text="TOP NEWS STORIES", fg='white', bg='black',font='arial 12 bold')
        self.topNewsStories.grid(row=1, column=0, sticky=W+E)
        self.text = Listbox(self.frame1, width=40, height=8, selectmode=SINGLE,bg='white',fg='maroon')
        self.text.grid(row=2, column=0, sticky=W + E + N + S)
        text = self.soup.find('div', {'class': 'top-story'})
        text1 = text.find('ul',{'data-vr-zone':'top_stories', 'class':'list8'})
        text2 = text1.find_all('a')
        self.forloopfuncmainpage(text2)

    def LN(self):
        self.latestNews = Label(self.frame1, text="LATEST NEWS", fg='white', bg='black', font='arial 12 bold')
        self.latestNews.grid(row=1, column=1, sticky=W+E)
        self.text = Listbox(self.frame1, width=40, height=10, selectmode=SINGLE,bg='white',fg='maroon')
        self.text.grid(row=2, column=1, sticky=W + E + N + S)
        text = self.soup.find('div', {'id': 'lateststories'})
        text1 = text.find('ul', {'data-vr-zone': 'latest', 'class': 'list9'})
        text2 = text1.find_all('a')
        self.forloopfuncmainpage(text2)

    def CITY(self):
        self.citylabel = Label(self.frame1, text="CITY", fg='white', bg='black', font='arial 12 bold')
        self.citylabel.grid(row=4, column=0, sticky=W+E,columnspan=2)
        self.text = Listbox(self.frame1, width=40, height=5, selectmode=SINGLE, bg='white',fg='maroon')
        self.text.grid(row=5, column=0, columnspan=2,sticky=W + E + N + S)
        text = self.soup.find('div', {'class': 'toicity toi-widgets'})
        text1 = text.find('ul', {'data-vr-zone': 'city', 'class': 'list2'})
        text2 = text1.find_all('a')
        self.forloopfuncmainpage(text2)

    def SPORTS(self):
        self.acrosslabel = Label(self.frame1, text="SPORTS", fg='white', bg='black', font='arial 12 bold')
        self.acrosslabel.grid(row=7,column=0,sticky=W+E,columnspan=2)
        self.text = Listbox(self.frame1, width=40, height=7, selectmode=SINGLE, bg='white',fg='maroon')
        self.text.grid(row=8, column=0, columnspan=2,sticky=W + E + N + S)
        text = self.soup.find('div', {'class': 'widget fullwidth clearfix rpos citrus'})
        text1 = text.find('ul', {'class': 'list2'})
        text2 = text1.find_all('a')
        self.forloopfuncmainpage(text2)

    def LIVEMARK(self):
        framelive = Frame(self.frame1,bg='black')
        framelive.grid(row=9,column=0,sticky=W,columnspan=2)
        Label(framelive, text="LIVE MARKET", fg='white', bg='black', font='arial 12 bold').grid(row=0,column=0,sticky=W+E,columnspan=8)
        Label(framelive, text='SENSEX', fg='white', bg='black', font='arial 10 bold').grid(row=1, column=0,sticky=N + W + E + S,columnspan=2,padx=20)
        Label(framelive, text='NIFTY', fg='white', bg='black', font='arial 10 bold').grid(row=1, column=2,sticky=N + W + E + S,columnspan=2,padx=35)
        Label(framelive, text='GOLD', fg='white', bg='black', font='arial 10 bold').grid(row=1, column=4,sticky=N + W + E + S,columnspan=2,padx=45)
        Label(framelive, text='USD', fg='white', bg='black', font='arial 10 bold').grid(row=1, column=6,sticky=N + W + E + S,columnspan=2,padx=55)
        url = 'https://economictimes.indiatimes.com/markets'
        r = req.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')
        text1 = soup.find('div', {'class': 'data-container flt width_auto'})
        text2 = text1.find_all('div', {'class': 'div-data sAdv'})
        j = 0
        for i in range(len(text2)):
            text3 = text2[i].find('b')
            text4 = text2[i].find_all('a')
            if text4[2].get_text()[0] == '-':
                msg = '\\/'
            else:
                msg = '/\\'
            Label(framelive, text=text3.get_text() + msg + text4[2].get_text(), fg='white', bg='black',
                  font='arial 9 bold').grid(row=2, column=j, sticky=W+E+S+N, columnspan=2)
            j = j + 2

    def initUI(self):
        self.master.title("TOI")
        menubar = Menu(self.master)
        self.master.config(menu=menubar)

        #CITY MENU STARTS'''
        self.city = {'METRO CITIES': ['Mumbai', 'Delhi', 'Bangalore', 'Hyderabad', 'Kolkata', 'Chennai'],
                     'OTHER CITIES': ['Agartala', 'Agra', 'Ajmer', 'Amaravati', 'Ahmedabad', 'Allahabad', 'Amritsar',
                                      'Aurangabad', 'Bareilly', 'Bhopal',
                                      'Bhubaneswar', 'Chandigarh', 'Coimbatore', 'Cuttack', 'Dehradun', 'Erode',
                                      'Faridabad', 'Ghaziabad', 'Goa', 'Gurgaon',
                                      'Guwahati', 'HUBBALLI', 'Imphal', 'Indore', 'Itanagar', 'Jaipur', 'Jammu',
                                      'Jamshedpur', 'Jodhpur', 'Kanpur', 'Kochi',
                                      'Kohima', 'Kolhapur', 'Kozhikode', 'Lucknow', 'Ludhiana', 'Madurai', 'Mangalore',
                                      'Meerut', 'Mysore', 'Nagpur', 'Nashik',
                                      'Navi Mumbai', 'Noida', 'Patna', 'Puducherry', 'Pune', 'Raipur', 'Rajkot',
                                      'Ranchi', 'Srinagar', 'Salem', 'Shillong',
                                      'Shimla', 'Surat', 'Thane', 'Trichy', 'Thiruvananthapuram', 'Udaipur', 'Vadodara',
                                      'Varanasi', 'Vijayawada', 'Visakhapatnam']}
        self.link = OrderedDict()
        citymenu = Menu(menubar)
        menubar.add_cascade(label='City',menu=citymenu)
        metrocitymenu = Menu(citymenu)
        othercitymenu = Menu(citymenu)
        citymenu.add_cascade(label='METRO CITIES',menu=metrocitymenu)
        citymenu.add_cascade(label='OTHER CITIES', menu=othercitymenu)

        for i in range(len(self.city['METRO CITIES'])):
            metrocitymenu.add_command(label=self.city['METRO CITIES'][i],command= lambda cityn = self.city['METRO CITIES'][i] : self.content(cityn))
        for j in range(len(self.city['OTHER CITIES'])):
            othercitymenu.add_command(label=self.city['OTHER CITIES'][j], command= lambda cityn = self.city['OTHER CITIES'][j] : self.content(cityn))
        #'''CITY MENU ENDS

        #INDIA MENU STARTS'''
        indiamenu = Menu(menubar)
        menubar.add_cascade(label='India',menu=indiamenu)
        self.india = ['India','Maharashtra','Delhi','Karnataka','Tamil Nadu','Telangana','Uttar Pradesh','West Bengal','Gujarat','Madhya Pradesh',
                      'Bihar','Chandigarh','Rajasthan','Arunachal Pradesh','Andhra Pradesh','Assam','Chhattisgarh','Goa','Haryana',
                      'Himachal Pradesh','Jammu and Kashmir','Jharkhand','Kerala','Manipur','Meghalaya','Mizoram','Nagaland','Odisha',
                      'Punjab','Sikkim','Tripura','Uttarakhand','Andaman and Nicobar Islands','Dadra and Nagar Haveli','Daman and Diu',
                      'Lakshadweep','Pondicherry']
        for i in range(len(self.india)):
            indiamenu.add_command(label=self.india[i],command= lambda staten=self.india[i] : self.content(staten))
        #'''INDIA MENU ENDS

        #WORLD MENU STARTS'''
        worldmenu = Menu(menubar)
        menubar.add_cascade(label='World', menu=worldmenu)
        self.world = ['US','Pakistan','South Asia','UK','Europe','China','Middle East','Rest of World','Mad Mad World']

        self.menuname = ['usmenu','pakistanmenu','samenu','ukmenu','europemenu','chinamenu','memenu','rowmenu','mmwmenu']

        for i in range(len(self.world)):
            worldmenu.add_command(label=self.world[i], command= lambda worldn=self.world[i] : self.content(worldn))
        #'''WORLD MENU ENDS

        #BUSINESS MENU STARTS'''
        businessmenu = Menu(menubar)
        menubar.add_cascade(label='Business', menu=businessmenu)
        self.business = ["India Business","International Business"]
        for i in range(len(self.business)):
            businessmenu.add_command(label=self.business[i], command = lambda businame=self.business[i] : self.content(businame))
        #'''BUSINESS MENU ENDS

        menubar.add_command(label='Sports',command = lambda sport='Sports' : self.content(sport))
        menubar.add_command(label='Previously Saved',command = lambda save = 'Saved' : self.content(save))

    def contentfunc(self):               #FRAME FOR CONTENT FUNCTIONS
        conFrame = Frame(self.master,bg='white')
        conFrame.grid(row=0,column=0,sticky=W)
        self.text = Listbox( conFrame, width=100, height=34, selectmode=SINGLE)
        self.text.grid(row=0, column=0, sticky=W + E + N + S)
        s = ttk.Scrollbar( conFrame, orient=VERTICAL, command=self.text.yview)
        s.grid(column=1, row=0, sticky=(N, S))
        self.backButton = Button(conFrame, text="Back to main page",bg='maroon',fg='white', command=self.mainpage)
        self.backButton.grid(row=2, column=0, sticky=E + W)

    def contentdclick(self):            #FRAME FOR DOUBLE CLICK FUNCTIONS
        dclickFrame = Frame(self.master,bg='white')
        dclickFrame.grid(row=0,column=0,sticky=W)
        self.text = Text(dclickFrame, width=75, height=32)
        self.text.grid(row=0, column=0, sticky=W + E + N + S)
        s = ttk.Scrollbar(dclickFrame, orient=VERTICAL, command=self.text.yview)
        s.grid(column=1, row=0, sticky=(N, S))
        self.saveButton = Button(dclickFrame, text="Save", bg='maroon', fg='white', command=self.savepageinfo)
        self.saveButton.grid(row=1, column=0, sticky=E + W)
        backButton = Button(dclickFrame, text="Back to main page",bg='maroon',fg='white', command=self.mainpage)
        backButton.grid(row=2, column=0, sticky=E + W)

    def towritetofile(self,heading,body):
        self.heading=heading
        self.body=body

    def savepageinfo(self):
        now = datetime.datetime.now()
        filename=now.strftime("%Y-%m-%d")+".txt"
        fileopen = open(filename, 'a')
        filesave = open("savedfiles.txt",'a')
        filesave.write(filename+"\n")
        filesave.close()
        fileopen.writelines(self.heading)
        fileopen.writelines(self.body+"\n")
        fileopen.close()

    def OnDouble(self, event):
        self.contentdclick()
        widget = event.widget
        selection = widget.curselection()
        value = widget.get(selection[0])
        urlnew = self.link[value]
        try:
            r = req.get(urlnew)
            print(urlnew)
            soup = BeautifulSoup(r.content, 'html.parser')
            print(type(soup.find('div', {'class': 'Normal'})))
        except req.exceptions.ConnectionError:
            self.text.insert('end', "An error occurred! Please try again later.")

        try:
            soup.find('div', {'class': 'Normal'}).get_text()
        except AttributeError:
            heading = soup.find('h1').get_text() + "\n--------------------------------------------------------'''\n"
            body = self.link[value]+ "\nHead to the above link and watch the video!" + "\n'''--------------------------------------------------------\n"
            self.towritetofile(heading, body)
            self.text.insert('end', heading)
            self.text.insert('end', body)
            urllink=self.link[value]
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(urllink)
        else:
            heading=soup.find('h1').get_text() + "\n--------------------------------------------------------'''\n"
            i = 1
            nametemp=''
            for img in soup.findAll('img'):
                if 'https://static.toiimg.com/photo/' in img.get('src'):
                    trash = img.get('src')
                elif '/thumb/msid-' in img.get('src'):
                    image = "https://timesofindia.indiatimes.com" + img.get('src')
                    print(image)

                    if img.get('alt') is None:
                        trash = str(i)
                    elif len(img.get('alt'))!=0 and len(img.get('alt'))<50:
                        nametemp = img.get('alt')
                    elif len(img.get('alt'))==0 or len(img.get('alt'))>50:
                        nametemp="00"+str(i)
                    print("type:"+str(type(nametemp + ".jpeg")))
                    imagefile = open(nametemp + ".jpeg", 'wb')
                    imagefile.write(urllib.request.urlopen(image).read())
                    imagefile.close()
                i = i + 1
            filename = nametemp + ".jpeg"
            try:
                img = ImageTk.PhotoImage(Image.open(filename))
            except FileNotFoundError:
                body = soup.find('div', {'class': 'Normal'}).get_text() + "\n'''--------------------------------------------------------\n"
                self.towritetofile(heading, body)
                self.text.insert('end', heading)
                self.text.insert('end', body)
            else:
                ref = Label(image=img)
                ref.image = img
                body=soup.find('div', {'class': 'Normal'}).get_text()+ "\n'''--------------------------------------------------------\n"
                self.towritetofile(heading,body)
                self.text.insert('end', heading)
                self.text.image_create(END, image=ref.image)
                self.text.insert('end',"\n")
                self.text.insert('end', body)
        self.text.config(state=DISABLED)

    def forLoopContent(self,text2):
        for i in range(len(text2)):
            self.text.insert('end', str(i + 1) + '.' + text2[i].get_text() + "\n")
            key = str(i + 1) + '.' + text2[i].get_text() + "\n"
            ulink = 'https://timesofindia.indiatimes.com%s' % text2[i].get('href')
            print('https://timesofindia.indiatimes.com%s' % text2[i].get('href') + "\n")
            self.link.update({key: ulink})
            print(text2[i].get_text() + "\n")
            self.text.bind("<Double-Button-1>", self.OnDouble)

    def forLoopSports(self,text2):
        k=1
        for i in range(1,len(text2),2):
            self.text.insert('end', str(k) + '.' + text2[i].get_text() + "\n")
            key = str(k) + '.' + text2[i].get_text() + "\n"
            k=k+1
            ulink = 'https://timesofindia.indiatimes.com%s' % text2[i].get('href')
            print('https://timesofindia.indiatimes.com%s' % text2[i].get('href') + "\n")
            self.link.update({key: ulink})
            print(text2[i].get_text() + "\n")
            self.text.bind("<Double-Button-1>", self.OnDouble)

    def sportsFrame(self):
        framesport = Frame(self.master,bg='white')
        framesport.grid(row=0,column=0,sticky=N+S+E+W)
        sportsnews=Label(framesport,text='SPORTS NEWS',fg='maroon',bg='white',font='arial 10 bold')
        sportsnews.grid(row=0,column=0,sticky=W)
        self.text = Listbox(framesport, width=100, height=5, selectmode=SINGLE, bg='light grey')
        self.text.grid(row=1, column=0, sticky=W + E + N + S)
        s = ttk.Scrollbar(framesport, orient=VERTICAL, command=self.text.yview)
        s.grid(column=1, row=1, sticky=(N, S))
        url = 'https://timesofindia.indiatimes.com/sports'
        r = req.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')
        text = soup.find('div', {'class': 'sports-home-videos'})
        text1 = text.find('ul', {'class': 'cvs_wdt clearfix'})
        text2 = text1.find_all('a')
        self.forLoopSports(text2)
        sportname = ['CRICKET','FOOTBALL']
        rowno=2
        t = soup.find('div', {'id': 'c_sport_wdt_1'})
        text = t.find_all('div', {'class': 'news-section clearfix'})
        for i in range(1, len(text)):
            Label(framesport, text = sportname[i-1], fg = 'maroon', bg = 'white', font = 'arial 10 bold').grid(row=rowno, column=0, sticky=W)
            self.text = Listbox(framesport, width=100, height=5, selectmode=SINGLE, bg='light grey')
            self.text.grid(row=rowno+1, column=0, sticky=W + E + N + S)
            s = ttk.Scrollbar(framesport, orient=VERTICAL, command=self.text.yview)
            s.grid(column=1, row=rowno+1, sticky=(N, S))
            rowno=rowno+2
            text1 = text[i].find('ul', {'class': 'cvs_wdt clearfix'})
            text2 = text1.find_all('a')
            self.forLoopSports(text2)
        framesport1 = Frame(framesport, bg='white')
        framesport1.grid(row=6, column=0,columnspan=2, sticky=N + S + E + W)
        sportname1=['TENNIS','HOCKEY','WWE','NFL']
        t = soup.find('div', {'id': 'c_sport_wdt_1'})
        text = t.find('div', {'class': 'section_wdgt clearfix'})
        text1 = text.find_all('div', {'class': 'section'})
        rowno=0
        rowno1=0
        for i in range(len(text1)):
            if i%2==0:
                Label(framesport1, text=sportname1[i - 1], fg='maroon', bg='white', font='arial 10 bold').grid(row=rowno, column=0, sticky=W)
                self.text = Listbox(framesport1, width=50, height=3, selectmode=SINGLE, bg='light grey')
                self.text.grid(row=rowno + 1, column=0, sticky=W + E + N + S)
                rowno = rowno + 2
                text2 = text1[i].find('ul', {'class': 'cvs_wdt clearfix'})
                text3 = text2.find_all('a')
                self.forLoopSports(text3)
            else:
                Label(framesport1, text=sportname1[i - 1], fg='maroon', bg='white', font='arial 10 bold').grid(row=rowno1, column=1, sticky=W)
                self.text = Listbox(framesport1, width=50, height=3, selectmode=SINGLE, bg='light grey')
                self.text.grid(row=rowno1 + 1, column=1, sticky=W + E + N + S)
                rowno1 = rowno1 + 2
                text2 = text1[i].find('ul', {'class': 'cvs_wdt clearfix'})
                text3 = text2.find_all('a')
                self.forLoopSports(text3)
        backButton = Button(framesport, text="Back to main page", bg='maroon', fg='white', command=self.mainpage)
        backButton.grid(row=7, column=0, sticky=E + W)

    def OnDoubleOpenSaved(self, event):
        self.contentdclick()
        widget = event.widget
        selection = widget.curselection()
        value = widget.get(selection[0])
        fileprint = open(value[0:14], 'r')
        for i in fileprint:
            self.text.insert('end', i)

    def openSavedNews(self):
        file = open('savedfiles.txt', 'r')
        l = [file.readline()]
        self.text.insert('end', l[0])
        for i in file:
            if i in l:
                pass
            else:
                l.append(i)
                self.text.insert('end', i)
        self.text.bind("<Double-Button-1>", self.OnDoubleOpenSaved)

    def content(self, name):
        self.name = name
        self.contentfunc()
        if self.name in self.city['METRO CITIES'] or self.name in self.city['OTHER CITIES']:
            url = 'https://timesofindia.indiatimes.com/city/' + self.name
            r = req.get(url)
            soup = BeautifulSoup(r.content, 'html.parser')
            text = soup.find('div', {'id': 'c_articlelist_stories_2'})
            text1 = text.find('ul')
            text2 = text1.find_all('a')
            self.forLoopContent(text2)
        elif self.name == 'India':
            url = 'https://timesofindia.indiatimes.com/india'
            r = req.get(url)
            soup = BeautifulSoup(r.content, 'html.parser')
            text = soup.find('div', {'id': 'c_02010501'})
            text1 = text.find('ul', {'class': 'list5 clearfix'})
            text2 = text1.find_all('a')
            self.forLoopContent(text2)
        elif self.name in self.india and self.name !="India":
            url = 'https://timesofindia.indiatimes.com/india/' + self.name
            r = req.get(url)
            soup = BeautifulSoup(r.content, 'html.parser')
            text = soup.find('div', {'id': 'c_articlelist_stories_2'})
            text1 = text.find('ul',{'class':'list5 clearfix'})
            text2 = text1.find_all('a')
            self.forLoopContent(text2)
        elif self.name in self.world :
            print(self.name)
            url = 'https://timesofindia.indiatimes.com/world/' + self.name
            print(url)
            r = req.get(url)
            soup = BeautifulSoup(r.content, 'html.parser')
            text = soup.find('div', {'id': 'c_articlelist_stories_2'})
            text1 = text.find('ul', {'class': 'list5 clearfix'})
            text2 = text1.find_all('a')
            self.forLoopContent(text2)
        elif self.name in self.business:
            url = 'https://timesofindia.indiatimes.com/business/' + self.name
            print(url)
            r = req.get(url)
            soup = BeautifulSoup(r.content, 'html.parser')
            text = soup.find('div', {'id': 'c_articlelist_stories_2'})
            text1 = text.find('ul', {'class': 'list5 clearfix'})
            text2 = text1.find_all('a')
            self.forLoopContent(text2)
        elif self.name =='Sports':
            self.sportsFrame()
        elif self.name=='Saved':
            self.openSavedNews()


def mainloopwindow():
    root = Toplevel()
    root.title("TOI")
    root.withdraw()
    root.geometry("625x570")
    root.resizable(0, 0)
    root.configure(background='maroon')
    mainwin = mainwindow()


def mainwin():
    root = Tk()
    root.title("TOI")
    root.geometry("625x570")
    root.resizable(0, 0)
    root.configure(background='white')
    print("printing image!")
    canvas = Canvas(root, width=625, height=570, bg='maroon')
    canvas.grid(row=0, column=0, sticky=N + S + E + W)
    gif1 = PhotoImage(file='display2.gif')
    canvas.create_image(0, 0, image=gif1, anchor=NW)
    contbutton = Button(root, text="Click to Continue", command=mainloopwindow, anchor='w', width=30,
                        activebackground="#33B5E5")
    contbutton_window = canvas.create_window(10, 10, anchor='nw', window=contbutton)
    root.mainloop()


def OnDouble(event):
    root = Tk()
    root.title("TOI")
    root.geometry("625x570")
    root.resizable(0, 0)
    root.configure(background='white')
    dclickFrame = Frame(root, bg='white')
    dclickFrame.grid(row=0, column=0, sticky=W)
    text = Text(dclickFrame, width=75, height=32)
    text.grid(row=0, column=0, sticky=W + E + N + S)
    s = ttk.Scrollbar(dclickFrame, orient=VERTICAL, command=text.yview)
    s.grid(column=1, row=0, sticky=(N, S))
    widget = event.widget
    selection = widget.curselection()
    value = widget.get(selection[0])
    fileprint=open(value[0:14],'r')
    for i in fileprint:
        text.insert('end',i)


def backmain():
    if messagebox.askyesno('Exit','Exit?')==TRUE:
        exit()
    else:
        pass



def opensavednews(root):
    root.destroy()
    root = Tk()
    root.title("TOI")
    root.geometry("625x570")
    root.resizable(0, 0)
    root.configure(background='maroon')
    canvas = Canvas(root, width=625, height=570, bg='maroon')
    canvas.grid(row=0, column=0, sticky=N + S + E + W)
    Label(canvas,text='LAST SAVED NEWS',fg='maroon',bg='white',font='arial').grid(row=0,column=0,sticky=E+W)
    text = Listbox(canvas, width=100, height=10, selectmode=SINGLE, bg='light grey')
    text.grid(row=1, column=0, sticky=W + E + N + S)
    backbutton = Button(canvas, text="Back", command=backmain)
    backbutton.grid(row=2, column=0, sticky=S + W)
    file = open('savedfiles.txt','r')
    l=[file.readline()]
    text.insert('end', l[0])
    for i in file:
        if i in l:
            pass
        else:
            l.append(i)
            text.insert('end',i)
    text.bind("<Double-Button-1>", OnDouble)
    root.mainloop()


def offlineframe(root):
    if messagebox.askyesno('Saved News','You are offline. Would you like to surf through your old saved news items?') == TRUE:
        opensavednews(root)
    elif messagebox.askretrycancel('Offline',"You are offline.Please check your internet connection and try again.") == TRUE:
        root.destroy()
        checkconnection()
    else:
        exit()


def offline():
    root = Tk()
    root.title("TOI")
    root.geometry("625x570")
    root.resizable(0, 0)
    root.configure(background='white')
    canvas = Canvas(root, width=625, height=570, bg='maroon')
    canvas.grid(row=0, column=0, sticky=N + S + E + W)
    gif1 = PhotoImage(file='display2.gif')
    canvas.create_image(0, 0, image=gif1, anchor=NW)
    offlineframe(root)
    root.mainloop()


def checkconnection():
    socket.setdefaulttimeout(23)
    url = 'http://google.com/'
    try:
        response = urlopen(url)
    except HTTPError as e:
        print("The server couldn't fulfill the request. Reason:", str(e.code))
        offline()
    except URLError as e:
        print('We failed to reach a server. Reason:', str(e.reason))
        offline()
    else:
        html = response.read()
        print('got response!')
        mainwin()


def main():
    checkconnection()


if __name__ =='__main__':
    main()