#NEWSPAPER

from tkinter import *
from PIL import Image, ImageTk
root=Tk()

#DEFINE THE GEOMETRY, MAXIMUM, MINUIMUM SIZE OF THE GUI WINDOW

root.geometry("600x600")
root.minsize(600, 600)
root.maxsize(600, 600)

#NAME OF THE NEWS COMPANY

texts=Label(text="DAILY NEWS", bg="white", fg="black", font="Cheltenham 19 bold underline")
root.title("NEWS")
texts.pack()

#NEWS CONTENT

label3=Label(text="The Incident occurred in Kanpur's Colonelganj area.\nHimanshu, twenty-two, worked as scrap dealer.\nHe belonged to transformer theft gang.\nHe was previously arrested and jailed.\nTransformer obbery occurred in Kanpur unexpectedly.\nThief contacted live wire, suffered injuries.\nCritically injured man was still alive.\nFour accomplices threw him into Ganga.\nIncident occurred at Gurudev Palace intersection.\nOctober twenty-six, gang attempted transformer theft.\nElectric shock panicked remaining four thieves.\nThey tied limbs and transported him.\nThey drove towards Shuklaganj bridge area.\nThey threw him into river alive.\nMother filed missing report October thirty-one.\nReport was filed at Gwaltoli station.\nPolice arrested Shan Ali Aslam Vishal.\nInterrogation revealed confession about throwing Himanshu.\nPolice verified route using theft-site evidence.\nAuto transport towards Shuklaganj was confirmed.\nSearch teams deployed to recover body.\nAccused presented in court, remanded jail.\n", relief="sunken")
label3.pack(anchor="ne", side="top")

#NEWS HEADING

label2=Label(text="Man Trying To Steal Transformer Electrocuted,\nGang Throws Him Into Ganga", bg="white", fg="black", font="Cheltenham 18 bold underline")
label2.pack(anchor="nw", side="top")

#RELATED IMAGES

phto2=Image.open("theft.png")
resize1=phto2.resize((200, 200), Image.Resampling.LANCZOS)
tk_imge1=ImageTk.PhotoImage(resize1)
label1=Label(root, image=tk_imge1)
label1.image=tk_imge1
label1.pack(side="left", anchor="nw")
root.mainloop()

#NOTES

#Important label options:
# text=adds the text
# bd=background
#fg=foreground
#font=sets the font
#padx=x padding
#pady=y padding
#relief=border styling - SUNKEN, RAISED, GROOVE, RIDGE

#Important pack options:
#1. anchor="nw"
#2. side=top, bottom, left, right
#3. fill
#4. padx
#5. pady