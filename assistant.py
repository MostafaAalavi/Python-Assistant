#by mostafa alavi
import speech_recognition as sr

from datetime import datetime

END_PHRASE = "finish"


print('if you want to exit pelece say "finish"')
print('I lisening to you')

#function of geting audio
def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            return r.recognize_google(audio, language = 'en-US')
        except :
            return 'pelece try agin'


while True : #geting audio
    text = get_audio()
   
    if text.find('hey python') ==0:
        print('I can do something for you')




#comand of time
    if text.find("time") ==0:
        now = datetime.now()
        dd = str(now.day) #Get Day
        mm = str(now.month) #Get Month
        yyyy = str(now.year) #Get year
        hour = str(now.hour) #Get hour
        mi = str(now.minute) #Get minute
        ss = str(now.second) #Get Second
        print(dd + "/" + mm + "/" + yyyy + "   " + hour + ":" + mi + ":" + ss)


        
#for exit
    if text.find(END_PHRASE) ==0:
        print("bye bye !")
        break
