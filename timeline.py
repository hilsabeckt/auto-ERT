import classes
from sortedcontainers import SortedDict

raid = classes.Raid()
Kaynruxpins = classes.Havoc('Kaynruxpins')
Brutallboss = classes.Warrior('Brutallboss',Tank=True)
Moperx = classes.HolyPally('Moperx')
Zenzr = classes.HolyPally('Zenzr')
Fortplease = classes.Discipline('Fortplease',nameTime=False)
Lynthiaqt = classes.HolyPriest('Lynthiaqt')
#Lynthiaqt = classes.Discipline('Lynthiaqt')
#Raho = classes.RestoDruid('Raho')
Shamnut = classes.DPSSham('Shamnut',WindRush=True)

#staticTime,dynamicTime,nameTime,abbr
force_list = [('Brutallboss',True,True,True,True),('Shamnut',True,True,True,True),('Zertimonk',True,True,True,True)]
raid.add([Kaynruxpins,Brutallboss,Moperx,Zenzr,Lynthiaqt,Fortplease,Shamnut])

spellid = {'Darkness':'196718','Innervate':'29166','Tranquility':'740','Flourish':'197721','Revival':'115310',
           'Avenging Wrath':'31884','Aura Mastery':'31821','Holy Avenger':'105809','Rapture':'47536',
           'Shadowfiend':'34433', 'Power Word: Barrier':'62618','Luminous Barrier':'271466','Evangelism':'246287',
           'Divine Hymn':'64843', 'Symbol of Hope':'64901','Holy Word: Salvation':'265202',
           'Spirit Link Totem':'98008','Healing Tide Totem':'108280','Ascendance':'114050','Rallying Cry':'97462',
           'Ironbark':'102342','Life Cocoon':'116849','Blessing of Sacrifice':'6940','Pain Suppression':'33206',
           'Guardian Spirit':'47788','Tree of Life':'33891','Aspect of the Turtle':'186265','Ice Block':'45438',
           'Cold Snap':'235219','Divine Shield':'642','Blessing of Protection':'1022','Ardent Defender':'31850',
           'Cloak of Shadows':'31224','Netherwalk':'196555','Leap of Faith':'73325','Wind Rush':'192077','Vampiric Embrace':'15286'}

colorid = {'Death Knight':'C41F3B','Demon Hunter':'A330C9','Druid':'FF7D0A','Hunter':'A9D271','Mage':'40C7EB',
           'Monk':'00FF96','Paladin':'F58CBA','Priest':'FFFFFF','Rogue':'FFF569','Shaman':'0070DE',
           'Warlock':'8787ED','Warrior':'C79C6E'}

abbr = {'Darkness':'Darkness','Innervate':'Inner','Tranquility':'Tranq','Flourish':'Flour','Revival':'Rvl',
           'Avenging Wrath':'Wings','Aura Mastery':'AM','Holy Avenger':'HA','Rapture':'Rapt',
           'Shadowfiend':'Fiend', 'Power Word: Barrier':'Barrier','Luminous Barrier':'Barrier','Evangelism':'Evang',
           'Divine Hymn':'Hymn', 'Symbol of Hope':'Symbol','Holy Word: Salvation':'Salv',
           'Spirit Link Totem':'SLT','Healing Tide Totem':'HTT','Ascendance':'Ascend','Rallying Cry':'Rally',
           'Ironbark':'Bark','Life Cocoon':'Cocoon','Blessing of Sacrifice':'Sac','Pain Suppression':'PS',
           'Guardian Spirit':'GS','Tree of Life':'Tree','Aspect of the Turtle':'Turtle','Ice Block':'Block',
           'Cold Snap':'Snap','Divine Shield':'Bubble','Blessing of Protection':'BoP','Ardent Defender':'Ardent',
           'Cloak of Shadows':'Cloak','Netherwalk':'Walk','Leap of Faith':'Grip','Wind Rush':'WRT','Vampiric Embrace':'VE'}

class Ertnote:

    def __init__(self):
        self.note = SortedDict()
        self.name = SortedDict()
        
    def check_avail(self,time,ability,player):
        if ability not in player.cds.keys():
            raise ValueError(player.name + ' does not have ' + ability + '.')
        for prev_time in self.note.irange(minimum=time-player.cds[ability],maximum=time, inclusive = (False,False)):
            for prev_ability, prev_player in self.note.get(prev_time):
                if ability == prev_ability and player == prev_player:
                    raise ValueError(player.name + "'s " + ability + ' was used at: '  + str(prev_time) +
                                     '. It still has a a remaining cooldown of: ' + str(player.cds[ability] - time) + '.')
                    return False
        return True

    def update(self,time,ability,player):
        if Ertnote.check_avail(self,time,ability,player) == True:
            if time in self.note.keys():
                cdlist = self.note.get(time)
                cdlist.append((ability,player))
                self.note.update({time:cdlist})
            else:
                self.note.update({time:[(ability,player)]})

    def name_time(self,time,name):
        self.name.update({time:name})

    def get_name_time(self,time):
        if time in self.name:
            return self.name.get(time)
        else: raise KeyError('Ertnote does not contain name for: ' + str(time) + '.')

    def get(self,time):
        if time in self.note:
            return self.note.get(time)
        else: raise KeyError('Ertnote does not contain: ' + str(time) + '.')

    def getAll(self):
        getAll = []
        for time in self.note:
            getAll.append(self.note.get(time))
        return getAll

    def convert_ERT(self,filename,*force_names):
        if not isinstance(note,Ertnote):
            raise TypeError('Input must be of type Ertnote.')
        file = open(filename,'w')
        text = ''
        for time in self.note:
            ms = str(int(time/60)) + ':' + format(time%60,'02d')
            pdict = {}
            
            for playerlist in force_names:
                for player in playerlist:
                    text += '{p:' + player[0] + '}'
                    if player[1] == True:
                        text += ms+'   '
                    if player[2] == True:
                        text += '{time:' + ms + '}   '
                    if player[3] == True:
                        text += self.get_name_time(time) + '   '
                    for action in self.note.get(time):
                        text += '|cff'+colorid[action[1].classes]
                        text += '{spell:'+spellid[action[0]]+'} '
                        if player[4] == True:
                            text += abbr.get(action[0])
                        else:
                            text += action[0]
                        cddict = raid.getCds()
                        if raid.getCds().get(action[0])>1:
                            text += ' (' + action[1].name + ')'
                        text += '|r   '
                        if action[1] in pdict:
                            actionlist = pdict.get(action[1])
                            if action[0] not in actionlist:
                                actionlist.append(action[0])
                                pdict.update({action[1]:actionlist})
                        elif action[1].name not in list(zip(*force_list))[0]:
                            pdict.update({action[1]:[action[0]]})
                    text = text[:-3] + '{/p}'
            
            for player in pdict:
                text += '{p:' + player.name + '}'
                if player.staticTimer == True:
                    text += ms+'   '
                if player.dynamicTimer == True:
                    text += '{time:' + ms + '}   '
                if player.nameTime == True:
                    text += self.get_name_time(time) + '   '
                text += '|cff'+colorid[player.classes]
                for action in pdict.get(player):
                    text +='{spell:'+spellid[action]+'} '
                    if player.abbr == True:
                        text += abbr.get(action) + '   '
                    else:
                        text += action + '   '
                text = text[:-3] + '|r{/p}'
            text += '\n'
        file.write(text)
        file.close()

    def convert_ERT_backup(self,filename):
        if not isinstance(note,Ertnote):
            raise TypeError('Input must be of type Ertnote.')
        file = open(filename,'w')
        text = ''
        for time in self.note:
            ms = str(int(time/60)) + ':' + format(time%60,'02d')
            pdict = {}
            text += ms+'   '
            text += '{time:' + ms + '}   '
            for action in self.note.get(time):
                text += '|cff'+colorid[action[1].classes]
                text += '{spell:'+spellid[action[0]]+'} ' + abbr.get(action[0])
                cddict = raid.getCds()
                if raid.getCds().get(action[0])>1:
                    text += ' (' + action[1].name + ')'
                    text += '|r   '
                    if action[1] in pdict:
                        actionlist = pdict.get(action[1])
                        if action[0] not in actionlist:
                            actionlist.append(action[0])
                            pdict.update({action[1]:actionlist})
                    elif action[1].name not in list(zip(*force_list))[0]:
                        pdict.update({action[1]:[action[0]]})
                else: text += '|r   '
            text += '\n'
        file.write(text)
        file.close()

        
note = Ertnote()
note.name_time(0,'DPS')
note.update(0,'Avenging Wrath',Moperx)
note.update(0,'Avenging Wrath',Zenzr)

note.name_time(20,'Prep Dmg')
note.update(20,'Rapture', Fortplease)
note.update(20,'Shadowfiend', Fortplease)

note.name_time(45,'Rank/Sparks')
note.update(45,'Holy Word: Salvation', Lynthiaqt)

note.name_time(120,'Deferred Sentence')
note.update(120,'Avenging Wrath',Moperx)
note.update(120,'Avenging Wrath',Zenzr)

note.name_time(125,'First Spark')
note.update(125,'Power Word: Barrier',Fortplease)
note.update(125,'Divine Hymn',Lynthiaqt)

note.name_time(130,'Deferred Sentence')
note.update(130,'Rapture', Fortplease)

note.name_time(140,'Second Spark')
note.update(140,'Aura Mastery', Moperx)
note.update(140,'Darkness',Kaynruxpins)

note.name_time(155,'Third Spark/Charge')
note.update(155,'Aura Mastery', Zenzr)
note.update(155,'Rallying Cry', Brutallboss)

note.name_time(225,'Sparks')
note.update(225,'Avenging Wrath',Moperx)
note.update(225,'Avenging Wrath',Zenzr)

note.name_time(275,'Deferred Sentence')
note.update(275,'Rapture', Fortplease)
note.update(275,'Shadowfiend', Fortplease)

note.name_time(330,'1st Spark')
note.update(330,'Avenging Wrath',Moperx)
note.update(330,'Avenging Wrath',Zenzr)
note.update(330,'Divine Hymn',Lynthiaqt)
note.update(330,'Power Word: Barrier',Fortplease)
note.update(330,'Darkness',Kaynruxpins)

note.name_time(340,'2nd Spark')
note.update(340,'Aura Mastery', Moperx)
note.update(340,'Rallying Cry', Brutallboss)

note.name_time(350,'3rd Spark')
note.update(350,'Aura Mastery', Zenzr)

note.name_time(390,'Sparks')
note.update(390,'Rapture', Fortplease)

note.name_time(425,'Deferred Sentence')
note.update(425,'Holy Word: Salvation', Lynthiaqt)

'''
note.name_time(15,'Prep Dmg')
note.update(15,'Avenging Wrath',Moperx)
note.update(15,'Avenging Wrath',Zenzr)

note.name_time(40,'Rank/Sparks')
note.update(40,'Rapture', Fortplease)
note.update(40,'Shadowfiend', Fortplease)

note.name_time(120,'Deferred Sentence')
note.update(120,'Avenging Wrath',Moperx)
note.update(120,'Avenging Wrath',Zenzr)

note.name_time(125,'First Spark')
note.update(125,'Power Word: Barrier',Fortplease)
note.update(125,'Divine Hymn', Lynthiaqt)

note.name_time(140,'Second Spark')
note.update(140,'Aura Mastery', Moperx)
note.update(140,'Darkness',Kaynruxpins)

note.name_time(155,'Third Spark/Charge')
note.update(155,'Aura Mastery', Zenzr)
note.update(155,'Rallying Cry', Brutallboss)

note.name_time(225,'Sparks')
note.update(225,'Avenging Wrath',Moperx)
note.update(225,'Avenging Wrath',Zenzr)

note.name_time(275,'Deferred Sentence')
note.update(275,'Rapture', Fortplease)
note.update(275,'Shadowfiend', Fortplease)
note.update(275,'Holy Word: Salvation', Lynthiaqt)

note.name_time(330,'1st Spark')
note.update(330,'Avenging Wrath',Moperx)
note.update(330,'Avenging Wrath',Zenzr)
note.update(330,'Power Word: Barrier',Fortplease)
note.update(330,'Darkness',Kaynruxpins)

note.name_time(340,'2nd Spark')
note.update(340,'Aura Mastery', Moperx)
note.update(340,'Rallying Cry', Brutallboss)

note.name_time(350,'3rd Spark')
note.update(350,'Aura Mastery', Zenzr)

note.name_time(390,'Sparks')
note.update(390,'Rapture', Fortplease)

note.name_time(425,'Deferred Sentence')
note.update(425,'Divine Hymn', Lynthiaqt)
'''
'''
note.name_time(15,'Prep Dmg')
note.update(15,'Avenging Wrath',Moperx)
note.update(15,'Avenging Wrath',Zenzr)

note.name_time(40,'Rank/Sparks')
note.update(40,'Rapture', Lynthiaqt)
note.update(40,'Shadowfiend', Lynthiaqt)

note.name_time(45,'Rank/Sparks')
note.update(45,'Tree of Life', Raho)

note.name_time(120,'Deferred Sentence')
note.update(120,'Avenging Wrath',Moperx)
note.update(120,'Avenging Wrath',Zenzr)

note.name_time(125,'First Spark')
note.update(125,'Power Word: Barrier',Lynthiaqt)
note.update(125,'Tranquility', Raho)

note.name_time(130,'Transition')
note.update(130,'Wind Rush',Shamnut)

note.name_time(140,'Second Spark')
note.update(140,'Aura Mastery', Moperx)
note.update(140,'Darkness',Kaynruxpins)

note.name_time(155,'Third Spark/Charge')
note.update(155,'Aura Mastery', Zenzr)
note.update(155,'Rallying Cry', Brutallboss)

note.name_time(225,'Sparks')
note.update(225,'Avenging Wrath',Moperx)
note.update(225,'Avenging Wrath',Zenzr)

note.name_time(275,'Deferred Sentence')
note.update(275,'Rapture', Lynthiaqt)
note.update(275,'Shadowfiend',Lynthiaqt)
note.update(275,'Tree of Life', Raho)

note.name_time(330,'1st Spark')
note.update(330,'Avenging Wrath',Moperx)
note.update(330,'Avenging Wrath',Zenzr)
note.update(330,'Power Word: Barrier',Lynthiaqt)
note.update(330,'Darkness',Kaynruxpins)

note.name_time(340,'2nd Spark')
note.update(340,'Aura Mastery', Moperx)
note.update(340,'Rallying Cry', Brutallboss)

note.name_time(350,'3rd Spark')
note.update(350,'Aura Mastery', Zenzr)

note.name_time(390,'Sparks')
note.update(390,'Rapture', Lynthiaqt)

note.name_time(425,'Deferred Sentence')
note.update(425,'Tranquility', Raho)
'''

note.convert_ERT('note.txt',force_list)
note.convert_ERT_backup('backupnote.txt')

