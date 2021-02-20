import pywhatkit as wt

try:
    wt.sendwhatmsg("+593xxxxxxxxx", "Hello word, I am python!", 20,49) #los numeros es la hora de envio (hora, minuto)
    print("Successfully Sent!")
except:
    print("An Unexpected Error")
    