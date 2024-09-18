import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout



kivy.require('2.0.0')

glwssa = [" "    ,"x","w","s","b","t","y","u","i","o","z","a","e","d","k","g","h","j","f","l","p","q","c","v","r","n","m"]
codegl = ["blyat","!","@","#","$","%","^","&","*","(",")","_","-","=","+","[","{","]","}","~","|",":",";",">","<","?","/"]

class Blyat(BoxLayout):

    #glwssa = ["x","w","s","b","t","y","u","i","o","z","a","e","d","k","g","h","j","f","l","p","q","c","v","r","n","m"]
    #codegl = ["!","@","#","$","%","^","&","*","(",")","_","-","=","+","[","{","]","}","~","|",":",";",">","<","?","/"]

    

    def __init__(self):
        super(Blyat,self).__init__()
    

    def code(self):
        Msg = self.ids.mnm.text
        newMsg = ""
        
        for i in Msg:
            count=0
            for j in glwssa:
                if (i.lower() == j.lower()):
                    newMsg = newMsg + str(codegl[count])
                    break
                count+=1

        self.ids.mnm.text = newMsg


    def decode(self):
        Msg = self.ids.mnm.text
        newMsg = ""
        flag=1
        for i in Msg:
            count=0
            for j in codegl:
                
                if (i.lower() == j.lower()):
                    if(flag==1):
                        newMsg = newMsg + str(glwssa[count].upper())
                    else:
                        newMsg = newMsg + str(glwssa[count])
                    
                    flag=0
                    break
                if (count==26 and flag==0):
                    newMsg = newMsg + " "
                    flag=1
                    break
                count+=1

        self.ids.mnm.text = newMsg
        

class Crypso(App):
        
    def build(self):
        return Blyat()


x = Crypso()
x.run()
