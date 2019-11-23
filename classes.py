class Raid:

    def __init__(self):
        self.team = {}
        self.roles = [0,0,0]
    
    def add(self,player):

        if isinstance(player,list):
            for p in player:
                self.add(p)
            return
        
        if player.spec in self.team:
            speclist = self.team.get(player.spec)
            speclist.append(player)
            self.team.update({player.spec:speclist})
        else:
            self.team.update({player.spec:[player]})
        if player.role == 'Tank':
            self.roles[0] += 1
        if player.role == 'Healer':
            self.roles[1] += 1
        if player.role == 'DPS':
            self.roles[2] += 1

    def remove(self,player):
        if player.spec in self.team:
            speclist = self.team.get(player.spec)
            if player in speclist:
                speclist.remove(player)
                self.team.update({player.spec:speclist})
            else: raise ValueError('Cannot find: ' + player + '.')
        else: raise ValueError('Cannot find: ' + player + '.')

    def get(self,speclist):
        if speclist in self.team:
            return self.team.get(speclist)
        else: raise ValueError('Raid team does not contain: ' + speclist + '.')

    def getAll(self):
        getAll = []
        for speclist in self.team:
            for player in self.team.get(speclist):
                getAll.append(player)
        return getAll

    def getAllNames(self):
        getAll = []
        for speclist in self.team:
            for player in self.team.get(speclist):
                getAll.append(player.name)
        return getAll

    def getCds(self):
        getCds = {}
        for speclist in self.team:
            for player in self.team.get(speclist):
                for cd in player.cds:
                    if cd in getCds:
                        value = getCds.get(cd)
                        value += 1
                        getCds.update({cd:value})
                    else:
                        getCds.update({cd:1})
        return getCds
    
class Havoc:

    def __init__(self,name,Netherwalk=False,staticTimer=True,dynamicTimer=True,nameTime=False,abbr=True):
        if isinstance(name,str):
            self.name = name
        else: raise TypeError('Name must be String.')
        self.spec = 'Havoc'
        self.role = 'DPS'
        self.cds = {'Darkness':180}
        if Netherwalk==True:
            self.cds.update({'Netherwalk':120})
        self.classes = 'Demon Hunter'
        self.staticTimer = staticTimer
        self.dynamicTimer = dynamicTimer
        self.nameTime = nameTime
        self.abbr = abbr

class Mage:

    def __init__(self,name,Frost=False,staticTimer=True,dynamicTimer=True,nameTime=True,abbr=True):
        if isinstance(name,str):
            self.name = name
        else: raise TypeError('Name must be String.')
        self.spec = 'Fire/Arcane'
        if Frost==True:
            self.spec = 'Frost'
        self.role = 'DPS'
        self.cds = {'Ice Block':240}
        if Frost==True:
            self.cds.update({'Cold Snap':300})
        self.classes = 'Mage'
        self.staticTimer = staticTimer
        self.dynamicTimer = dynamicTimer
        self.nameTime = nameTime
        self.abbr = abbr

class Rogue:
    
    def __init__(self,name,staticTimer=True,dynamicTimer=True,nameTime=True,abbr=True):
        if isinstance(name,str):
            self.name = name
        else: raise TypeError('Name must be String.')
        self.spec = 'Asn/Out/Sub'
        self.role = 'DPS'
        self.cds = {'Cloak of Shadows':120}
        self.classes = 'Rogue'
        self.staticTimer = staticTimer
        self.dynamicTimer = dynamicTimer
        self.nameTime = nameTime
        self.abbr = abbr

class Hunter:
    
    def __init__(self,name,staticTimer=True,dynamicTimer=True,nameTime=True,abbr=True):
        if isinstance(name,str):
            self.name = name
        else: raise TypeError('Name must be String.')
        self.spec = 'BM/MM/Surv'
        self.role = 'DPS'
        self.cds = {'Aspect of the Turtle':180}
        self.classes = 'Hunter'
        self.staticTimer = staticTimer
        self.dynamicTimer = dynamicTimer
        self.nameTime = nameTime
        self.abbr = abbr

class Balance:
    
    def __init__(self,name,staticTimer=True,dynamicTimer=True,nameTime=True,abbr=True):
        if isinstance(name,str):
            self.name = name
        else: raise TypeError('Name must be String.')
        self.spec = 'Balance'
        self.role = 'DPS'
        self.cds = {'Innervate':180}
        self.classes = 'Druid'
        self.staticTimer = staticTimer
        self.dynamicTimer = dynamicTimer
        self.nameTime = nameTime
        self.abbr = abbr
        
class RestoDruid:
    
    def __init__(self,name,TranqTalent=False,Flourish=True,Tree=True,staticTimer=True,dynamicTimer=True,nameTime=True,abbr=True):
        if isinstance(name,str):
            self.name = name
        else: raise TypeError('Name must be String.')
        self.spec = 'RestoDruid'
        self.role = 'Healer'
        self.cds = {'Innervate':180,'Tranquility':180,'Ironbark':60}
        if TranqTalent==True:
            self.cds.update({'Innervate':120})
        if Flourish==True:
            self.cds.update({'Flourish':90})
        self.classes = 'Druid'
        if Tree==True:
            self.cds.update({'Tree of Life':180})
        self.staticTimer = staticTimer
        self.dynamicTimer = dynamicTimer
        self.nameTime = nameTime
        self.abbr = abbr

class Mistweaver:

    def __init__(self,name,staticTimer=True,dynamicTimer=True,nameTime=True,abbr=True):
        if isinstance(name,str):
            self.name = name
        else: raise TypeError('Name must be String.')
        self.spec = 'Mistweaver'
        self.role = 'Healer'
        self.cds = {'Revival':180,'Life Cocoon':120}
        self.classes = 'Monk'
        self.staticTimer = staticTimer
        self.dynamicTimer = dynamicTimer
        self.nameTime = nameTime
        self.abbr = abbr
        
class HolyPally:
    
    def __init__(self,name,Visions=True,HolyAvenger=True,Unbreakable=False,staticTimer=True,dynamicTimer=True,nameTime=True,abbr=True):
        if isinstance(name,str):
            self.name = name
        else: raise TypeError('Name must be String.')
        self.spec = 'HolyPally'
        self.role = 'Healer'
        self.cds = {'Avenging Wrath':120,'Aura Mastery':180,
                    'Blessing of Sacrifice':120,'Divine Shield':300,'Blessing of Protection':300}

        if Visions==True:
            self.cds.update({'Avenging Wrath':100})
        if HolyAvenger==True:
            self.cds.update({'Holy Avenger':90})
        if Unbreakable==True:
            self.cds.update({'Divine Shield':210})
        self.classes = 'Paladin'
        self.staticTimer = staticTimer
        self.dynamicTimer = dynamicTimer
        self.nameTime = nameTime
        self.abbr = abbr

class Pally:
    def __init__(self,name,Tank=False,Unbreakable=False,staticTimer=True,dynamicTimer=True,nameTime=True,abbr=True):
        if isinstance(name,str):
            self.name = name
        else: raise TypeError('Name must be String.')
        self.spec = 'Ret Pally'
        self.role = 'DPS'
        if Tank==True:
            self.spec = 'Prot Pally'
            self.role = 'Tank'
            
        self.cds = {'Divine Shield':300,'Blessing of Protection':300}

        if Tank==True:
            self.cds.update({'Blessing of Sacrifice':120,'Ardent Defender':120})
        if Unbreakable==True:
            self.cds.update({'Divine Shield':210})
            
        self.classes = 'Paladin'
        self.staticTimer = staticTimer
        self.dynamicTimer = dynamicTimer
        self.nameTime = nameTime
        self.abbr = abbr

class Discipline:
    
    def __init__(self,name,Evang=True,Luminous=False,staticTimer=True,dynamicTimer=True,nameTime=True,abbr=True):
        if isinstance(name,str):
            self.name = name
        else: raise TypeError('Name must be String.')
        self.spec = 'Discipline'
        self.role = 'Healer'
        self.cds = {'Rapture':90,'Shadowfiend':180,'Power Word: Barrier':180,
                    'Pain Suppression':180,'Leap of Faith':90}    

        if Luminous==True:
            del self.cds['Power Word: Barrier']
            self.cds.update({'Luminous Barrier':180})
        if Evang==True:
            self.cds.update({'Evangelism':90})
        self.classes = 'Priest'
        self.staticTimer = staticTimer
        self.dynamicTimer = dynamicTimer
        self.nameTime = nameTime
        self.abbr = abbr

class HolyPriest:

    def __init__(self,name,Salv=True,staticTimer=True,dynamicTimer=True,nameTime=True,abbr=True):
        if isinstance(name,str):
            self.name = name
        else: raise TypeError('Name must be String.')
        self.spec = 'HolyPriest'
        self.role = 'Healer'
        self.cds = {'Divine Hymn':180,'Symbol of Hope':300,
                    'Guardian Spirit':180,'Leap of Faith':90}

        if Salv==True:
            self.cds.update({'Holy Word: Salvation':300})
        self.classes = 'Priest'
        self.staticTimer = staticTimer
        self.dynamicTimer = dynamicTimer
        self.nameTime = nameTime
        self.abbr = abbr

class ShadowPriest:
    
    def __init__(self,name,Sanlayn=False,staticTimer=True,dynamicTimer=True,nameTime=True,abbr=True):
        if isinstance(name,str):
            self.name = name
        else: raise TypeError('Name must be String.')
        self.spec = 'ShadowPriest'
        self.role = 'DPS'
        self.cds = {'Vampiric Embrace':120,'Leap of Faith':90}

        if Sanlayn==True:
            self.cds.update({'Vampiric Embrace':75})
        self.classes = 'Priest'
        self.staticTimer = staticTimer
        self.dynamicTimer = dynamicTimer
        self.nameTime = nameTime
        self.abbr = abbr
    

class RestoSham:

    def __init__(self,name,Ascendance=False,WindRush=False,staticTimer=True,dynamicTimer=True,nameTime=True,abbr=True):
        if isinstance(name,str):
            self.name = name
        else: raise TypeError('Name must be String.')
        self.spec = 'RestoSham'
        self.role = 'Healer'
        self.cds = {'Spirit Link Totem':180,'Healing Tide Totem':180}

        if Ascendance==True:
            self.cds.update({'Ascendance':180})
        if WindRush==True:
            self.cds.update({'Wind Rush':120})
        self.classes = 'Shaman'
        self.staticTimer = staticTimer
        self.dynamicTimer = dynamicTimer
        self.nameTime = nameTime
        self.abbr = abbr

class DPSSham:
    def __init__(self,name,WindRush=False,staticTimer=True,dynamicTimer=True,nameTime=True,abbr=True):
        if isinstance(name,str):
            self.name = name
        else: raise TypeError('Name must be String.')
        self.spec = 'DPSSham'
        self.role = 'DPS'
        self.cds = {}

        if WindRush==True:
            self.cds.update({'Wind Rush':120})
        self.classes = 'Shaman'
        self.staticTimer = staticTimer
        self.dynamicTimer = dynamicTimer
        self.nameTime = nameTime
        self.abbr = abbr

class Warrior:

    def __init__(self,name,Tank=False,staticTimer=True,dynamicTimer=True,nameTime=True,abbr=True):
        if isinstance(name,str):
            self.name = name
        else: raise TypeError('Name must be String.')
        if Tank==False:
            self.spec = 'Fury/Arms'
            self.role = 'DPS'
        else:
            self.spec = 'ProtWarr'
            self.role = 'Tank'
        self.cds = {'Rallying Cry':180}
        self.classes = 'Warrior'
        self.staticTimer = staticTimer
        self.dynamicTimer = dynamicTimer
        self.nameTime = nameTime
        self.abbr = abbr
