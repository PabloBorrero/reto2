

cica = 0
ica = -1
cverde = 0
camarillo = 0
cnaranja = 0
crojo = 0
cmorado = 0
cmarron = 0
sica = 0
alert = ""
while cverde != 1:
    ica = -1
    cica = cica + 1
    c = float(input())
    if c >= 0 and c < 0.054:
        ica = (((50 - 0) / (0.053 - 0)) * (c - 0) + 0)
    elif c >= 0.054 and c < 0.101:
        ica = (((100 - 51) / (0.100 - 0.054)) * (c - 0.054) + 51) 
    elif c >= 0.101 and c < 0.361:
        ica = (((150 - 101) / (0.360 - 0.101)) * (c - 0.101) + 101)
    elif c >= 0.361 and c < 0.650:
        ica = (((200 - 151) / (0.649 - 0.361)) * (c - 0.361) + 151)
    elif c >= 0.650 and c < 1.250: 
        ica = (((300 - 201) / (1.249 - 0.650)) * (c - 0.650) + 201)
    elif c >= 1.250 and c < 1.650:
        ica = (((400 - 301) / (1.649 - 1.250)) * (c - 1.250) + 301)
    elif c >= 1.650 and c < 2.050:
        ica = (((500 - 401) / (2.049 - 1.650)) * (c - 0.650) + 401)
    print(ica)
    if ica != -1:
        sica = sica + ica
        if ica >= 0 and ica <= 50:
            cverde = cverde + 1
        elif ica > 50 and ica <= 100:
            camarillo = camarillo + 1 
        elif ica > 100 and ica <= 150:
            cnaranja = cnaranja + 1
        elif ica > 150 and ica <= 200:
            crojo = crojo + 1
        elif ica > 200 and ica <= 300:
            cmorado = cmorado + 1
        elif ica > 300:
            cmarron = cmarron + 1
            print("Pase")

pica = sica/cica
if pica >= 0 and pica <= 50:
    alert = "verde"
elif pica > 50 and pica <= 100:
    alert = "amarillo"
elif pica > 100 and pica <= 150:
    alert = "naranja"
elif pica > 150 and pica <= 200:
    alert = "rojo"
elif pica > 200 and pica <= 300:
    alert = "morado"
elif pica > 300:
    alert = "marron"
print(cica)
print('{0:.2f} '.format(pica) + alert)
print("verde " + '{0:.2f}'.format(100/cica * cverde) + "%")
print("amarillo " + '{0:.2f}'.format(100/cica * camarillo) + "%")
print("naranja " + '{0:.2f}'.format(100/cica * cnaranja) + "%")
print("rojo " + '{0:.2f}'.format(100/cica * crojo) + "%")
print("morado " + '{0:.2f}'.format(100/cica * cmorado) + "%")
print("marron " + '{0:.2f}'.format(100/cica * cmarron) + "%")