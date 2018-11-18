class TV:

    def __init__(self):
        self.brand = brand
        self.channel = 1
        self.volume = 1
        self.onOff = False

    def turnOn(self):
        self.onOff = True

    def turnOff(self):
        self.onOff = False

    def volume(self):
        self.volume = volume
        return self.volume

    def channel(self):
        self.channel = channel
        return self.channel

    def setChannel(self,x):
        self.channel = x

    def setVolume(self,y):
        self.volume = y


class SS(TV):
    serialNumber = 0
    def __init__(self):
        self.serialNumber += 1


class LG(TV):
    serialNumber = 0
    def __init__(self):
        self.serialNumber += 1


a=int(input())
b=int(input())
ss=[]
lg=[]
for i in range (0,a):
    ss.append(SS())

for i in range (0,b):
    lg.append(LG())



while 1:
    t = input()
    r = t.split()

    if r[0] == 'LG':
        if r[2] == 'volume':
            lg[int(r[1])-1].setVolume(r[3])
        if r[2] == 'channel':
            lg[int(r[1])-1].setChannel(r[3])


    if r[0] =='SS':
        if r[2] == 'volume':
            ss[int(r[1])-1].setVolume(r[3])
        if r[2] == 'channel':
            ss[int(r[1])-1].setChannel(r[3])


    if r[0] == 'PP':
        if r[1] == 'LG':
            if r[3] == 'volume':
                print(lg[int(r[2]) - 1].volume)
            if r[3] == 'channel':
                print(lg[int(r[2]) - 1].channel)
        if r[1] == 'SS':
            if r[3] == 'volume':
                print(ss[int(r[2]) - 1].volume)
            if r[3] == 'channel':
                print(ss[int(r[2]) - 1].channel)


    if r[0] == 'END':
        break