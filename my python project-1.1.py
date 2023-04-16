import pandas as pd
from PIL import Image   #python imaging library for images  
from PIL import ImageDraw
from PIL import ImageFont
img=Image.open("C:\\Users\\priya\\Desktop\\New folder\\Presentation 1 (7)_page-0001.jpg")  #path of my image
l1 = ImageDraw.Draw(img)
myFont = ImageFont.truetype("C:\\Windows.old\\Users\\HP\\AppData\\Local\\Temp\\$PowerISO$\\boot\\fonts\\times new roman bold italic.ttf",72)  #path of my font
l1.text((370, 150), "PRIYANSH INDORIA", font=myFont, fill =(255, 0, 0))
myfont = ImageFont.truetype("C:\\Windows.old\\Users\\HP\\AppData\\Local\\Temp\\$PowerISO$\\boot\\fonts\\times new roman bold italic.ttf",48)  # python interpreter with image editing capabilities 
l1.text((220,300), "CONTACT :", font=myfont, fill=(7, 213, 245))
myfont = ImageFont.truetype("C:\\Windows.old\\Users\\HP\\AppData\\Local\\Temp\\$PowerISO$\\boot\\fonts\\times new roman bold italic.ttf",44)
l1.text((220,400), "9694111429", font=myfont, fill=(162, 168, 50))
l1.text((220,450), "priyansh81099@gmail.com", font=myfont, fill=(162, 168, 50))
l1.text((220,550), "Hello Everyone!\n\n" "Welcome to the my MINI PROJECT\n\n" "An Enthusiastic and Self Motivated Learner\nlooking to work on new technologies in an\norganisation where i can gain more knowledge\nand can enhance my skills to provide a great\noutput to the company. ", font=myfont, fill=(245, 133, 7))
l1.text((220,1000),"EXPERTISE :\n\n", font=myfont, fill=(235, 189, 52))
l1.text((220,1100),"Python Language\n""C++ Language(BASIC)\nMySQL\nMicrosoft Power BI ""\n Microsoft Excel", font=myfont, fill=(143, 235, 52))
df={"Qualification      ": ['B.tech(HONOURS)','Senior  Secondary','Higher  Secondary'],
    "  University and":['RTU-','CBSE-','CBSE-'],
    "Year": ['2022','2018','2015'],
    "    Grades": [' 8.57','   64.80',' 8.00']   # DataFrame created by pandas 
}
c=pd.DataFrame(df,index=["•","•","•"])
l1.text((220,1380),c.to_string(), font=myfont, fill=(245, 15, 61))
l1.text((220,1650),"PROJECTS:", font=myfont, fill=(52, 235, 235))
l1.text((220,1740),'•  Created "MY RESUME  using python programming \n    language"\n•  Created an "Indian Restaurant Menu using python\n   OOPS concept "\n ', font=myfont, fill=(52, 235, 235))
myfont = ImageFont.truetype("C:\\Windows.old\\Users\\HP\\AppData\\Local\\Temp\\$PowerISO$\\boot\\fonts\\times new roman bold italic.ttf",40)
l1.text((1260,900),"HOBBIES:", font=myfont, fill=(245, 15, 61))
l1.text((1260,1000),"• Travelling\n\n•  Listening to Music\n\n•  Watching Horror \n\n   Movies", font=myfont, fill=(245, 15, 61))
img.show()
img.save("C:\\Users\\priya\\Desktop\\pro.final pic.png")

