from tkinter import *
from tkinter import messagebox
import requests 
from CF_WeatherApp import WeatherApp

def get_weather():
    start = WeatherApp.startWeather()
    return start
type='general'
class NewsApp:
    def __init__(self,app):
        self.app=app
        self.app.title("NewsApp")
        self.app.geometry("1470x600")
        # Variables 
        self.NewsCatButton=[] 
        self.newCat=['general','entertainment','business','sports','health','science','technology']

        # GUI 
        dark_blue='#081D54'
        light_blue='#0066CC'
        font_color='white'
        self.title=Label(self.app,text='NewsApp',font=('rockwell bold',30),bg=dark_blue,fg=font_color,relief=GROOVE,pady=25,bd=12).pack(fill=X)
        F1=Label(self.app,text='Category',bg=dark_blue,fg='white',font=('roboto slab',20,'bold'),relief=GROOVE,bd=10)
        F1.place(x=0,y=80,width=300,relheight=0.88)

        for i in range(len(self.newCat)):
            b=Button(F1,text=self.newCat[i].upper(),font=('roboto slab',14,'bold'),bd=7,width=20,height=2,bg=light_blue,fg=font_color)
            b.grid(row=i,column=0,padx=10,pady=5)
            b.bind('<Button-1>',self.NewArea)
            self.NewsCatButton.append(b) 
        
        F2=Frame(self.app,relief=GROOVE,bd=7)
        F2.place(x=320,y=80,relwidth=0.78,relheight=0.88) 
        newsTitle=Label(F2,text="New Area",bg=light_blue,fg=font_color,bd=7,relief=GROOVE,font=('roboto slab',20,'bold')).pack(fill=X)
        scroll_y=Scrollbar(F2,orient=VERTICAL)
        self.textarea=Text(F2,yscrollcommand=scroll_y.set,font=('Lora bold',15),bg=dark_blue,fg=font_color)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.insert(END,"\n\t\n\t\n\t\n\t\n\t\n\t\n\t\n\t\n\t\n\t\t\t         PLEASE SELECT ANY CATEGORY TO SHOW HEADLINES \n\t\t\t   PLEASE BE PATIENT IT DEPENDS ON YOUR INTERNET CONNECTION")
        self.textarea.pack(fill='x') 

        self.b2 = Button(F2,text='Check-Weather'.upper(),font=('rockwell bold',14),bg='#0400C3',fg='white',width=20,bd=7,command=get_weather)
        self.b2.place(x=0,y=625,relwidth=1,relheight=0.1)


    
    def NewArea(self,event):
        type=event.widget.cget('text').lower()
        
        type=event.widget.cget('text').lower()
        apiKey='eafc1487da934a1b994a06d775b0b06e' 
        newsUrl=f'https://newsapi.org/v2/top-headlines?country=in&category={type}&apiKey={apiKey}'
        self.textarea.delete("1.0",END)
        self.textarea.insert(END,"\n Read the Latest news provided by our NewApp\n\n")
        self.textarea.insert(END,"-------------------------------------------------------------------\n\n")
        try:
            articles=(requests.get(newsUrl).json())['articles']
            if(articles!=0):
                for i in range(len(articles)):
                    self.textarea.insert(END,f"{articles[i]['title']}\n")
                    self.textarea.insert(END,f"{articles[i]['description']}\n")
                    self.textarea.insert(END,f"{articles[i]['content']}\n")
                    self.textarea.insert(END,f"read more...{articles[i]['url']}\n")
                    self.textarea.insert(END,f"\n--------------------------------------------------------------\n")
                    self.textarea.insert(END,f"--------------------------------------------------------------------\n\n")
            
            else:
                self.textarea.insert(END,"Sorry, no news available")
        
        except Exception as e:
            messagebox.showerror("ERROR","Sorry, cannot connect to internet using NewsApp")



app=Tk()
NewsApp(app) 
app.state("zoomed") #always open app in full screen
pic=PhotoImage(file='newsIcon.png')
app.iconphoto(False,pic) 
app.mainloop()