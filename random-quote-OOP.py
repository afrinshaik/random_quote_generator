#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import tkinter as tk
import urllib, json

class Quote:
       
    def __init__(self,url):
        self.url = url
    #Function to get quote from json
    def get_quote(self):
        #Open url using urllib and decode it
        data = urllib.request.urlopen(self.url).read().decode('utf-8')
        #Replace special characters ' with \'
        data = data.replace(r"\'", "'")
        #Load data from json
        json_data = json.loads(data)
        if json_data['quoteAuthor'] == "":
            json_data['quoteAuthor'] = "Unknown"
        self.quote = json_data['quoteText'] + "\n\n\t\t-" + json_data['quoteAuthor']
        return self.quote
    #Function to insert new quote when clicked on new quote button
    def quote_new(self):
        #Assign new quote to quote variable
        self.quote = self.get_quote()
        #Delete previous quote
        text.delete('1.0',tk.END)
        #Insert new quote
        text.insert(tk.END, self.quote)

#Create an instance of class Quote
random_quote = Quote('http://api.forismatic.com/api/1.0/?method=getQuote&key=457653&format=json&lang=en&json=?')

#Create a window
window = tk.Tk()
#Add title to window
window.title("Random Quote Generator")
#Add width and height to window
window.geometry("400x300")
#Label
label1 = tk.Label(window, text="Today's Quote")
label1.grid(row = 0,column=0)
#Text
text = tk.Text(window, width=50, height=10)
text.grid(row=1,column=0)
#Delete previous quote if exists
text.delete('1.0',tk.END)
#Insert quote
text.insert(tk.END, random_quote.get_quote())
#Button New Quote
new_quote = tk.Button(window, text="New Quote",command=random_quote.quote_new)
new_quote.grid(row = 2, column=0)
#Button Close
close = tk.Button(window,text="Close", command=window.destroy)
close.grid(row=3,column=0)
#mainloop
window.mainloop()

               
               