from GENERATOR import *
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
from gtts import gTTS
from googletrans import Translator
from multiprocessing import Pool, Process
from ffmpy import FFmpeg
import time, random, asyncio, timeit, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, urllib, urllib.parse, ast, pytz, wikipedia, pafy, youtube_dl, atexit

cl = RIDEN()
#AcToken = "YOUR TOKEN"
#cl = RIDEN(authTokenRFU=AcToken)
cl.log("YOUR TOKEN : {}".format(str(cl.authToken)))
channel = RIDENChannel(cl,cl.server.CHANNEL_ID['LINE_TIMELINE'])
cl.log("CHANNEL TOKEN : " + str(channel.getChannelResult()))
print ("LOGIN SUCCESS\n")
def Author(Owner):
    try:
        author = "Author {}".format(cl.getContact(Author).displayName)
        print(auhtor)
    except Exception as error:
        print(error)
clProfile = cl.getProfile()
clSettings = cl.getSettings()
RIDEN = RIDENPoll(cl)
INDUK = cl.profile.mid
Rfu = [cl]
RfuBot=[INDUK]
Owner=["u4862fe4b182b2fd194a3108e2f3662e8"]
RfuSekawan = Rfu + RfuBot + Owner

contact = cl.getProfile()
backup = cl.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

Squad = {
    "UnsendPesan":True,
    "SpamInvite":False,
    "Contact":False,
    "GName":"【さัএπัஞ✵ບิथℓℓҨतΩ】",
    "AutoRespon":False,
    "KickRespon":False,
    "KillOn":False,
    "KickOn":False,
    "Upfoto":False,
    "UpfotoBot":False,
    "UpfotoGroup":False,
    "Steal":False,
    "Invite":False,
    "Copy":False,
    "autoAdd":True,
    "PesanAdd":"Terima Kasih Sudah Add Saya",
    "ContactAdd":{},
    "autoBlock":False,
    "autoJoin":True,
    "AutojoinTicket":False,
    "AutoReject":False,
    "AutoRead":False,
    "IDSticker":False,
    "Timeline":False,
    "Welcome":True,
    "BackupBot":True,
    "WcText": "Welcome My Friend",
    "Leave":False,
    "LvText": "See You My Friend",
    "Mic":False,
    "MicDel":False,
    "Adminadd":False,
    "AdminDel":False,
    "Gift":False,
    "readMember":{},
    "readPoint":{},
    "readTime":{},
    "ROM":{},
    "Blacklist":{},
    "Ban":False,
    "Unban":False,
    "FancyFoto":False,
    "Admin": {
        "u4862fe4b182b2fd194a3108e2f3662e8":True #MID ADMIN TARO DISINI
    },
}

Mozilla = {
    "userAgent": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0"
    ],
    "mimic": {
        "copy": False,
        "conpp": False,
        "status": False,
        "target": {}
    }
}

setTime = {}
setTime = Squad['readTime']
mulai = time.time() 
msg_dict = {}

ProfileMe = {
    "displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}
ProfileMe["displayName"] = clProfile.displayName
ProfileMe["statusMessage"] = clProfile.statusMessage
ProfileMe["pictureStatus"] = clProfile.pictureStatus

RfuCctv={
    "Point1":{},
    "Point2":{},
    "Point3":{}
}

Help ="""SELF BOT PYTHON 3 
BY:【さัএπัஞ✵ບิथℓℓҨतΩ】 

me
my name
my bio
my picture
my cover
my video
speed
rename
my bot
my team
stealname [@]
stealbio [@]
stealpict [@]
stealcover [@]
stealvideo [@]
stealmid [@]
profile [@]
spam on [jmlah teks]
cekmid: [mid]
banlock [@]
banlist
contact ban
clear ban
blocklist
friendlist
friendlist mid
runtime
broadcast:
contactbc:
adminadd [@]
admindel [@]
admin:add-on
admin:del-on
changename:
changebio:
remove pesan
restart
bot logout
kick [@]
status
unsend on/off
changepp on/off
timeline on/off
autojoin on/off
autoreject on/off
auto jointicket on/off
gift:on/off
copy on/off
clone [@]
comeback
steal on/off
contact on/off
mic:add-on
mic:del-on
mimic on/off
mimiclist
refresh
___[ GROUP ]___
leaveall grup
kick [on,off->kickall]
invite on/off
kill on/off
rejectall grup
lurking on/off/reset
lurking read
sider on/off
mentionall
welcome on/off
changewelcome:
leave on/off
changeleave:
memberlist
link on/off
my grup
gurl
gcreator
invite gcreator
ginfo
grup id
cfotogrup on/off
spaminvite on/off
announce
___[ MEDIA ]____
topnews
data birth:
urban:
sslink:
maps:
cekcuaca:
jadwalshalat:
idline:
say-id:
say-en:
say-jp:
say-ar:
say-ko:
apakah:
kapan:
wikipedia:
kalender
image:
youtube:
___[ TRANSLATOR ]___
indonesian:
english:
korea:
japan:
thailand:
arab:
malaysia:
jawa:

         THANKS TO 
BY:【さัএπัஞ✵ບิथℓℓҨतΩ】
""""________________________"

#------------------------------------------------ SCRIP DEF ----------------------------------------------------------#

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours,24)
    month, days = divmod(days,30)
    year, month = divmod(month,12)
    century, year = divmod(year,100)
    return '\n%02d Abad\n%02d Tahun\n%02d Bulan\n%02d Hari\n%02d Jam\n%02d Menit\n%02d Detik' % (century, year, month, days, hours, mins, secs)

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def RIDEN_FAST_USER(fast):
    try:
        if fast.type == 0:
            return
        if fast.type == 13:
            if INDUK in fast.param3:
              if Squad['autoJoin'] == True:
                    cl.acceptGroupInvitation(fast.param1)
                    print ("ANDA JOIN DI GRUP")
                    pass

        if fast.type == 13:
            if INDUK in fast.param3:
              if Squad['AutoReject'] == True:
                if fast.param2 not in RfuSekawan and fast.param2 not in Squad["Admin"]:
                    gid = cl.getGroupIdsInvited()
                    for i in gid:
                        cl.rejectGroupInvitation(i)
                        pass

#------------------- ( 1 ) ------------------------- PEMBATAS SCRIP SIDER & WC LV ------------------------------------------------#

        elif fast.type == 55:
            try:
                if RfuCctv['Point1'][fast.param1]==True:
                    if fast.param1 in RfuCctv['Point2']:  
                        Name = cl.getContact(fast.param2).displayName
                        if Name in RfuCctv['Point3'][fast.param1]:
                            pass
                        else:
                            RfuCctv['Point3'][fast.param1] += "\n~" + Name
                            if " " in Name:
                                nick = Name.split(' ')
                                if len(nick) == 2:
                                    cl.mentionWithRFU(fast.param1,fast.param2," Hii\n","" + "\n Nyimak yah kak?" )
                                else:
                                    cl.mentionWithRFU(fast.param1,fast.param2," Nah\n","" + "\n Nongol Sini Chat kak ??" )
                            else:
                                cl.mentionWithRFU(fast.param1,fast.param2," Hey\n","" + "\n What Are You Doing?" )
                    else:
                        pass
                else:
                    pass
            except:
                pass

        if fast.type == 55:
            try:
                if fast.param1 in Squad['readPoint']:
                    if fast.param2 in Squad['readMember'][fast.param1]:
                        pass
                    else:
                        Squad['readMember'][fast.param1] += fast.param2
                    Squad['ROM'][fast.param1][fast.param2] = fast.param2
                else:
                   pass
            except:
                pass   

        if fast.type == 17:
            if Squad["Welcome"] == True:
                if fast.param2 not in Rfu:
                    ginfo = cl.getGroup(fast.param1)
                    cl.mentionWithRFU(fast.param1,fast.param2," Hii","" + "\n " + str(Squad['WcText']))
                    cl.sendMessage(fast.param1, None, contentMetadata={'mid':fast.param2}, contentType=13)
                    print ("MEMBER HAS JOIN THE GROUP")

        if fast.type == 15:
            if Squad["Leave"] == True:
                if fast.param2 not in Rfu:
                    ginfo = cl.getGroup(fast.param1)
                    cl.mentionWithRFU(fast.param1,fast.param2," Hii","" + "\n " + str(Squad['LvText']))
                    cl.sendMessage(fast.param1, None, contentMetadata={'mid':fast.param2}, contentType=13)
                    print ("MEMBER HAS LEFT THE GROUP")

        if fast.type == 46:
            if fast.param2 in RfuBot:
                cl.removeAllMessages()

#------------------- ( 2 ) ------------------------- PEMBATAS SCRIP ------------------------------------------------#

        if fast.type == 26:
            msg = fast.message
            text = msg.text
            rfuText = msg.text
            msg_id = msg.id
            kirim = msg.to           
            user = msg._from
            if msg.toType == 0 or msg.toType == 2:
                if msg.toType == 0:
                    to = kirim
                elif msg.toType == 2:
                    to = kirim
                if msg.contentType == 0:
                    if Squad["AutoRead"] == True:
                        cl.sendChatChecked(kirim, msg_id)
                    if kirim in Squad["readPoint"]:
                        if user not in Squad["ROM"][kirim]:
                            Squad["ROM"][kirim][user] = True
                    if user in Mozilla["mimic"]["target"] and Mozilla["mimic"]["status"] == True and Mozilla["mimic"]["target"][user] == True:
                        text = msg.text
                        if text is not None:
                            cl.sendMessage(kirim,text)
                    if Squad["UnsendPesan"] == True:
                        msg = fast.message
                        if msg.toType == 0:
                            cl.log(" {} - {} ".format(str(user), str(rfuText)))
                        else:
                            cl.log(" {} - {} ".format(str(kirim), str(rfuText)))
                            msg_dict[msg.id] = {"rider": rfuText, "pelaku": user, "createdTime": msg.createdTime, "contentType": msg.contentType, "contentMetadata": msg.contentMetadata}
                    if Squad["Timeline"] == True:
                      if msg.contentType == 16:
                          ret_ = "[ INFORMASI TIMELINE ]\n"
                          if msg.contentMetadata["serviceType"] == "GB":
                              contact = cl.getContact(user).displayName
                              auth = "\nPenulis : {}".format(str(contact.displayName))
                          else:
                              auth = "\nPenulis : {}".format(str(msg.contentMetadata["serviceName"]))
                              ret_ += auth
                          if "stickerId" in msg.contentMetadata:
                              stck = "\n Stiker : https://line.me/R/shop/detail/{}".format(str(msg.contentMetadata["packageId"]))
                              ret_ += stck
                          if "mediaOid" in msg.contentMetadata:
                              object_ = msg.contentMetadata["mediaOid"].replace("svc=myhome|sid=h|","")
                              if msg.contentMetadata["mediaType"] == "V":
                                  if msg.contentMetadata["serviceType"] == "GB":
                                      ourl = "\n\nLink Objek : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                      murl = "\n\nLink Media : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(msg.contentMetadata["mediaOid"]))
                                  else:
                                      ourl = "\n\nLink Objek : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                      murl = "\n\nLink Media : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(object_))
                                  ret_ += murl
                              else:
                                  if msg.contentMetadata["serviceType"] == "GB":
                                      ourl = "\n\nLink Objek : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                  else:
                                      ourl = "\n\nLink Objek : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                              ret_ += ourl
                          if "text" in msg.contentMetadata:
                              dia = cl.getContact(user)
                              zx = ""
                              zxc = ""
                              zx2 = []
                              xpesan = 'Pengirim: '
                              ardian = str(dia.displayName)
                              pesan = ''
                              pesan2 = pesan+"@ARDIAN_GANTENG\n"
                              xlen = str(len(zxc)+len(xpesan))
                              xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                              zx = {'S':xlen, 'E':xlen2, 'M':dia.mid}
                              zx2.append(zx)
                              kata = "\n\nText Type : {}".format(str(msg.contentMetadata["text"]))
                              purl = "\n\nLink Post : {}".format(str(msg.contentMetadata["postEndUrl"]).replace("line://","https://line.me/R/"))
                              ret_ += purl
                              ret_ += kata
                              zxc += pesan2
                              pesan = xpesan + zxc + ret_ + ""
                              cl.sendMessage(kirim, pesan, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                              url = msg.contentMetadata["postEndUrl"]
                              cl.likePost(url[25:58], url[66:], likeType=1001)

        if fast.type == 65:
          if Squad['UnsendPesan'] == True:
              try:
                  you = fast.param1
                  msg.id = fast.param2
                  user = msg._from
                  if msg.id in msg_dict:
                    if msg_dict[msg.id]["pelaku"]:
                        pelaku = cl.getContact(msg_dict[msg.id]["pelaku"])
                        nama = pelaku.displayName
                        dia = "Detect Pesan Terhapus\n"
                        dia += "\n1. Name : " + nama
                        dia += "\n2. Taken : {}".format(str(msg_dict[msg.id]["createdTime"]))
                        dia += "\n3. Pesannya : {}".format(str(msg_dict[msg.id]["rider"]))
                        cl.mentionWithRFU(you,user," Nah","\n\n" +str(dia))
              except:
                  cl.sendMessage(you, "Return")

        if fast.type in [25,26]:
            msg = fast.message
            user = msg._from
            kirim = msg.to
            if msg.contentType == 7:
                if Squad['IDSticker'] == True:
                    stk_id = msg.contentMetadata['STKID']
                    stk_ver = msg.contentMetadata['STKVER']
                    pkg_id = msg.contentMetadata['STKPKGID']
                    filler = "STICKER CHECKS\nSTKID : %s\nSTKPKGID : %s\nSTKVER : %s\n\nTHIS IS LINK\n\nline://shop/detail/%s" % (stk_id,pkg_id,stk_ver,pkg_id)
                    cl.mentionWithRFU(kirim,user,"My Code Sticker\n","" + "\n\n" + str(filler))
                else:
                    pass

        if fast.type == 25:
            msg = fast.message
            user = msg._from
            kirim = msg.to
            if msg.contentType == 1:
              if Squad['Upfoto'] == True:
                if user in Owner:
                    path = cl.downloadObjectMsg(msg.id)
                    cl.updateProfilePicture(path)
                    cl.mentionWithRFU(kirim,user," Update Picture Success ","")
                    Squad['Upfoto'] = False

        if fast.type == 25:
            msg = fast.message
            user = msg._from
            kirim = msg.to
            if msg.contentType == 1:
              if Squad['UpfotoGroup'] == True:
                if user in RfuSekawan or user in Squad["Admin"]:
                    path = cl.downloadObjectMsg(msg.id)
                    cl.updateGroupPicture(kirim, path)
                    cl.mentionWithRFU(kirim,user," Update Picture Grup Success ","")
                    Squad['UpfotoGroup'] = False

        if fast.type == 5:
            if Squad["autoAdd"] == True:
                if (Squad["PesanAdd"] in [""," ","\n",None]):
                    pass
                else:
                    Squad["ContactAdd"][fast.param2] = True
                    usr = cl.getContact(op.param2)
                    cl.sendMessage(fast.param1, "Haii {} " + str(Squad["PesanAdd"]).format(usr.displayName))
                    cl.sendMessage(fast.param1, None, contentMetadata={'mid':INDUK}, contentType=13)

        if fast.type == 5:
            if Squad['autoBlock'] == True:
                try:
                    usr = cl.getContact(op.param2)
                    cl.sendMessage(fast.param1, "Haii {} Sorry Auto Block , Komen di TL dulu ya kalo akun asli baru di unblock".format(usr.displayName))
                    cl.talk.blockContact(0, fast.param1)
                    Squad["Blacklist"][fast.param2] = True
                except Exception as e:
                	print (e)

        if fast.type in [25,26]:
          if Squad['Contact'] == True:
              msg = fast.message
              user = msg._from
              kirim = msg.to
              if msg.contentType == 13:
                if 'displayName' in msg.contentMetadata:
                    contact = cl.getContact(msg.contentMetadata["mid"])
                    try:
                        cover = cl.getProfileCoverURL(user)
                    except:
                        cover = ""
                    cl.sendMessage(kirim,"Nama:\n" + msg.contentMetadata["displayName"] + "\n\nMid:\n" + msg.contentMetadata["mid"] + "\n\nBio:\n" + contact.statusMessage + "\n\nPicture URL:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\nCover URL:\n" + str(cover))
                else:
                    contact = cl.getContact(msg.contentMetadata["mid"])
                    try:
                        cover = cl.getProfileCoverURL(user)
                    except:
                        cover = ""
                    cl.sendText(kirim,"Nama:\n" + contact.displayName + "\n\nMid:\n" + msg.contentMetadata["mid"] + "\n\nBio:\n" + contact.statusMessage + "\n\nPicture URL\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\nCover URL:\n" + str(cover))

        if fast.type == 25:
          if Squad['Invite'] == True:
            msg = fast.message
            user = msg._from
            kirim = msg.to
            if msg.contentType == 13:
                if user in RfuSekawan or user in Squad["Admin"]:
                    _name = msg.contentMetadata["displayName"]
                    invite = msg.contentMetadata["mid"]
                    groups = cl.getGroup(kirim)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            cl.sendText(kirim, _name + " Sudah Berada DiGrup Ini")
                        else:
                            targets.append(invite)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                cl.findAndAddContactsByMid(target)
                                cl.inviteIntoGroup(kirim,[target])
                                cl.sendText(kirim,"Invite " + _name + "\nSUCCESS..")
                                Squad['Invite'] = False
                                break
                            except:             
                                 cl.sendText(kirim, 'Contact error')
                                 Squad['Invite'] = False
                                 break

        if fast.type == 25:
          if Squad['Steal'] == True:
            msg = fast.message
            user = msg._from
            kirim = msg.to
            if msg.contentType == 13:
                if user in RfuSekawan or user in Squad["Admin"]:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = cl.getGroup(kirim)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            print ("[Target] Stealed")
                            break             
                        else:
                            targets.append(copy)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                contact = cl.getContact(target)
                                cl.sendText(kirim,"Nama :\n" + msg.contentMetadata["displayName"] + "\n\nBio :\n" + contact.statusMessage+ "\n\nMid :\n" + msg.contentMetadata["mid"] + "\n\nSteal Succes..")
                                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                cl.sendImageWithURL(kirim,image)
                                cover = cl.getProfileCoverURL(target)
                                cl.sendImageWithURL(kirim, cover)
                                Squad['Steal'] = False
                                break                     
                            except:             
                                 cl.sendText(kirim, 'Contact error')
                                 Squad['Steal'] = False
                                 break

        if fast.type == 25:
          if Squad['KillOn'] == True:
            msg = fast.message
            user = msg._from
            kirim = msg.to
            if msg.contentType == 13:
                if user in RfuSekawan or user in Squad["Admin"]:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = cl.getGroup(kirim)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            print ("[Target] Kick Via Contact")
                            break             
                        else:
                            targets.append(copy)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            if target not in RfuSekawan:
                                try:
                                    cl.kickoutFromGroup(kirim,[target])
                                    Squad['KillOn'] = False
                                    break
                                except:             
                                     cl.sendText(kirim, 'Target Not Found')
                                     Squad['KillOn'] = False
                                     break

        if fast.type == 25:
          if Squad['Gift'] == True:
            msg = fast.message
            user = msg._from
            kirim = msg.to
            if msg.contentType == 13:
                if user in RfuSekawan or user in Squad["Admin"]:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = cl.getGroup(kirim)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            print ("[Target] Send Gift")
                            break             
                        else:
                            targets.append(copy)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                cl.sendMessage(target, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58','PRDTYPE': 'THEME','MSGTPL': '12'}, contentType = 9)
                                Squad['Gift'] = False
                                break
                            except:             
                                 cl.sendText(kirim, 'Target Error')
                                 Squad['Gift'] = False
                                 break

        if fast.type == 25:
          if Squad["Mic"] == True:
            msg = fast.message
            user = msg._from
            kirim = msg.to
            if msg.contentType == 13:
                if user in RfuSekawan or user in Squad["Admin"]:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = cl.getGroup(kirim)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            print ("[Target] Mimic Add")
                            break             
                        else:
                            targets.append(copy)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                Mozilla["mimic"]["target"][target] = True
                                cl.sendText(kirim,"Target ditambahkan!")
                                Squas['Mic'] = False
                                break
                            except:             
                                 cl.sendText(kirim, 'Silahkan untuk on kan kembali & Send Contact Again\nKami akan memuat ulang program')
                                 break

        if fast.type == 25:
          if Squad["MicDel"] == True:
            msg = fast.message
            user = msg._from
            kirim = msg.to
            if msg.contentType == 13:
                if user in RfuSekawan or user in Squad["Admin"]:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = cl.getGroup(kirim)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            print ("[Target] Mimic Add")
                            break             
                        else:
                            targets.append(copy)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                del Mozilla["mimic"]["target"][target]
                                cl.sendText(kirim,"Target is Dellete!")
                                Squad['MicDel'] = False
                                break
                            except:             
                                 cl.sendText(kirim, 'Silahkan untuk on kan kembali & Send Contact Again\nKami akan memuat ulang program')
                                 break

        if fast.type == 25:
          if Squad['Copy'] == True:
            msg = fast.message
            user = msg._from
            kirim = msg.to
            if msg.contentType == 13:
                if user in RfuSekawan or user in Squad["Admin"]:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = cl.getGroup(kirim)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            print ("[Target] Stealed")
                            break             
                        else:
                            targets.append(copy)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                cl.cloneContactProfile(target)
                                cl.sendText(kirim, "Copy Contact Success")
                                Squad['Copy'] = False
                                break
                            except:             
                                 cl.sendText(kirim, "Contact Error")
                                 Squad['Copy'] = False
                                 break
                                 
                                 
#======= AUTO TAG & CHAT BATAS SCRIP ========
        if fast.type == 26:
            msg = fast.message
            user = msg._from
            kirim = msg.to
            if msg.contentType == 0 and user not in INDUK and msg.toType == 2:
                if "MENTION" in msg.contentMetadata.keys() != None:
                    if Squad['AutoRespon'] == True:
                        contact = cl.getContact(user)
                        cName = contact.displayName
                        balas = [cName + "\n" + str(Squad['MentionText'])]
                        ret_ = "" + random.choice(balas)
                        name = re.findall(r'@(\w+)', msg.text)
                        mention = ast.literal_eval(msg.contentMetadata["MENTION"])
                        mentionees = mention['MENTIONEES']
                        for mention in mentionees:
                              if mention['M'] in INDUK:
                                  cl.mentionWithRFU(kirim,user,"","" +str(ret_))
                                  break

        if fast.type == 26:
            msg = fast.message
            user = msg._from
            kirim = msg.to
            if msg.contentType == 0 and user not in RfuSekawan or user not in Squad["Admin"]:
                if "MENTION" in msg.contentMetadata.keys() != None:
                    if Squad['KickRespon'] == True:
                        contact = cl.getContact(user)
                        cName = contact.displayName
                        balas = [cName + "Dont Tag Me","Sorry Dont Tag Me"]
                        ret_ = "" + random.choice(balas)
                        name = re.findall(r'@(\w+)', msg.text)
                        mention = ast.literal_eval(msg.contentMetadata["MENTION"])
                        mentionees = mention['MENTIONEES']
                        for mention in mentionees:
                              if mention['M'] in INDUK:
                                  cl.mentionWithRFU(kirim,user,"","" +str(ret_))
                                  cl.kickoutFromGroup(kirim,[user])
                                  break

        if fast.type == 25:
          if Squad['SpamInvite'] == True:
            msg = fast.message
            user = msg._from
            kirim = msg.to
            if msg.contentType == 13:
                if user in RfuSekawan or user in Squad["Admin"]:
                    korban = msg.contentMetadata["displayName"]
                    invite = msg.contentMetadata["mid"]
                    groups = cl.getGroup(kirim)
                    pending = groups.invitee
                    targets = []
                    for x in groups.members:
                        if korban in x.displayName:
                            cl.sendText(kirim, korban + " Sudah Berada DiGrup Ini")
                        else:
                            targets.append(invite)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                cl.findAndAddContactsByMid(target)
                                cl.createGroup("RIDEN SPAM GROUP",[target]) # KALAU MAU BUAT BANYAK SILAHKAN TAMBAHIN SESUKA KALIAN :>
                                cl.createGroup("RIDEN SPAM GROUP",[target]) # HANYA SPAM VIA CONTACT
                                cl.createGroup("RIDEN SPAM GROUP",[target])
                                cl.sendText(kirim,"Spam Invite ke " + korban + "\nSUCCESS..")
                                Squad['SpamInvite'] = False
                            except:             
                                 cl.sendText(kirim, 'Contact error')
                                 Squad['SpamInvite'] = False
                                 break

#------------------- ( 3 ) ------------------------- PEMBATAS SCRIP ------------------------------------------------#

        if fast.type == 25 or fast.type == 26:
            msg = fast.message
            text = msg.text
            rfuText = msg.text
            msg_id = msg.id
            kirim = msg.to           
            user = msg._from
            if msg.toType == 0 or msg.toType == 2:
                if msg.toType == 0:
                    to = kirim
                elif msg.toType == 2:
                    to = kirim
                if msg.contentType == 0:
                    if Squad['AutoRead'] == True:
                        cl.sendMessage(0, msg_id)
                    elif rfuText is None:
                        return
                    else:               
                        if rfuText.lower() == '0':
                            cl.sendMessage(0, user)
                        elif rfuText in ["Me","me"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                cl.sendMessage(kirim, None, contentMetadata={'mid': user}, contentType=13)
                                cl.mentionWithRFU(kirim,user," Hay","")

                        elif rfuText in ["Help","help"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                 cl.sendMessage(kirim, str(Help))

                        elif rfuText in ["Speed","speed"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                no = time.time()
                                cl.sendText("ue86841a3982b7da6e8094f3c218d79b6", ' ')
                                elapsed_time = time.time() - no
                                cl.sendText(kirim, "%s" % (elapsed_time))

                        elif rfuText in ["Rename","rename"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                team1 = cl.getContact(INDUK).displayName
                                cl.mentionWithRFU(kirim,INDUK," Ready On ","" + str(" ("+team1+")"))

                        elif rfuText in ["My team","my team"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                rfu = ""
                                sekawan = ""
                                wa = 0
                                wi = 0
                                for m_id in Owner:
                                    wa = wa + 1
                                    end = '\n'
                                    rfu += str(wa) + ". " +cl.getContact(m_id).displayName + "\n"
                                for m_id in Squad["Admin"]:
                                    wi = wi + 1
                                    end = '\n'
                                    sekawan += str(wi) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendText(kirim,"【さัএπัஞ✵ບิथℓℓҨतΩ】\n\nOwner:\n"+rfu+"\nAdmin:\n"+sekawan+"\n( %s ) 【さัএπัஞ✵ບิथℓℓҨतΩ】" %(str(len(Owner)+len(Squad["Admin"]))))                                

                        elif rfuText.lower().startswith("leaveall grup"):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                gid = cl.getGroupIdsJoined()
                                for i in gid:
                                    cl.leaveGroup(i)
                                    print ("Kicker Leave All group")

                        elif rfuText in ["Kick on","kick on"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad["KickOn"] = True
                                cl.sendText(kirim,"Status:\n{''cancel'':0,''kick'':1}")
                        elif rfuText in ["Kick off","kick off"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad["KickOn"] = False
                                cl.sendText(kirim,"Status:\n{''cancel'':0,''kick'':0}")

                        elif rfuText.lower().startswith("kickall"):
                            if user in RfuSekawan or user in Squad["Admin"]:
                              if msg.toType == 2:
                                if Squad["KickOn"]:
                                    _name = msg.text.replace("kickall","")
                                    gs = cl.getGroup(kirim)
                                    targets = []
                                    for g in gs.members:
                                        if _name in g.displayName:
                                            targets.append(g.mid)
                                    if targets == []:
                                        cl.sendText(kirim,"Target Not found.")
                                    else:
                                        for target in targets:
                                          if target not in RfuSekawan and target not in Squad["Admin"]:
                                            try:
                                                klist=[cl]
                                                kicker=random.choice(klist)
                                                kicker.kickoutFromGroup(kirim,[target])
                                            except Exception as error:
                                                cl.sendText(kirim, str(error))

                        elif rfuText.lower().startswith("spam "):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                txt = rfuText.split(" ")
                                jmlh = int(txt[2])
                                teks = rfuText.replace("Spam "+str(txt[1])+" "+str(jmlh)+" ","")
                                tulisan = jmlh * (teks+"\n")
                                if txt[1] == "on":
                                    if jmlh <= 500:
                                       for x in range(jmlh):
                                           cl.sendText(kirim, teks)
                                    else:
                                       cl.sendText(kirim, "Maksimal 500 SpamTeks!")
                                elif txt[1] == "off":
                                    if jmlh <= 500:
                                        cl.sendText(kirim, tulisan)
                                    else:
                                        cl.sendText(kirim, "Maksimal 500 SpamTeks!")

                        elif rfuText.lower().startswith("cekmid: "):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                ardian = rfuText.replace("Cekmid: ","")
                                cl.sendMessage(kirim, None, contentMetadata={'mid': ardian}, contentType=13)
                                contact = cl.getContact(ardian)
                                ganteng = cl.getProfileCoverURL(ardian)
                                path = str(ganteng)
                                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                try:
                                    cl.sendText(kirim,"Nama :\n" + contact.displayName + "\n\nBio :\n" + contact.statusMessage)
                                    cl.sendText(kirim,"Profile Picture " + contact.displayName)
                                    cl.sendImageWithURL(kirim,image)
                                    cl.sendText(kirim,"Cover Picture " + contact.displayName)
                                    cl.sendImageWithURL(kirim,path)
                                except:
                                    pass

                        elif ("Banlock " in rfuText):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"][0]["M"]
                                targets = []
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                for target in targets:
                                    try:
                                        Squad["Blacklist"][target] = True
                                        cl.sendText(kirim,"Succes Banned ")
                                    except:
                                        pass

                        elif rfuText in ["Banlist","banlist"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                if Squad["Blacklist"] == {}:
                                    cl.sendText(kirim,"Nothing in Blacklist")
                                else:
                                    mc = "Daftar Blacklist "
                                    num=1
                                    ragets = cl.getContacts(Squad["Blacklist"])
                                    for mi_d in ragets:
                                        mc+="\n%i. %s" % (num, mi_d.displayName)
                                        num=(num+1)
                                    mc+="\n\n Total %i Blacklist " % len(ragets)
                                    cl.sendText(kirim, mc)

                        elif rfuText.lower().startswith("contact ban"):
                            if user in RfuSekawan or user in Squad["Admin"]:
                              if Squad["Blacklist"] == {}:
                                  cl.sendText(kirim,"Tidak Ada Blacklist")
                              else:
                                  cl.sendText(kirim,"Contact Blacklist")
                                  h = ""
                                  for i in Squad["Blacklist"]:
                                      h = cl.getContact(i)
                                      cl.sendMessage(kirim, None, contentMetadata={'mid': i}, contentType=13)

                        elif rfuText.lower().startswith("clear ban"):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad["Blacklist"] = {}
                                cl.sendText(kirim,"Succes clear Blacklist is nothing??")
                                print ("Clear Ban")

                        elif rfuText.lower().startswith("link on"):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                if msg.toType == 2:
                                    group = cl.getGroup(kirim)
                                    group.preventedJoinByTicket = False
                                    cl.updateGroup(group)

                        elif rfuText.lower().startswith("link off"):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                if msg.toType == 2:
                                    group = cl.getGroup(kirim)
                                    group.preventedJoinByTicket = True
                                    cl.updateGroup(group)

                        elif rfuText.lower().startswith("gurl"):
                          if user in RfuSekawan or user in Squad["Admin"]:
                            if msg.toType == 2:
                                grup = cl.getGroup(kirim)
                                if grup.preventedJoinByTicket == False:
                                    set = cl.reissueGroupTicket(kirim)
                                    cl.sendMessage(kirim, "Group Ticket : \nhttps://line.me/R/ti/g/{}".format(str(set)))
                                else:
                                    cl.sendMessage(kirim, "Ketik Link on Dulu kaka")

                        elif rfuText.lower().startswith("gcreator"):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                try:
                                    group = cl.getGroup(kirim)
                                    GS = group.creator.mid
                                    cl.sendMessage(kirim, None, contentMetadata={'mid': GS}, contentType=13)
                                    cl.mentionWithRFU(kirim,GS,"Group Creator","")
                                    contact = cl.getContact(GS.mid)
                                except:
                                    W = group.members[0].mid
                                    cl.sendMessage(kirim, None, contentMetadata={'mid': W}, contentType=13)
                                    cl.mentionWithRFU(kirim,W,"Group Creator","")

                        elif rfuText.lower().startswith("invite gcreator"):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                try:
                                    group = cl.getGroup(kirim)
                                    GS = group.creator.mid
                                    cl.sendMessage(kirim, None, contentMetadata={'mid': GS}, contentType=13)
                                    cl.mentionWithRFU(kirim,GS,"Group Creator","")
                                    cl.findAndAddContactsByMid(GS)
                                    cl.inviteIntoGroup(kirim,[GS])
                                    cl.mentionWithRFU(kirim,user,"Invite Done","")
                                    contact = cl.getContact(GS.mid)
                                except:
                                    W = group.members[0].mid
                                    cl.sendMessage(kirim, None, contentMetadata={'mid': W}, contentType=13)
                                    cl.mentionWithRFU(kirim,W,"Group Creator","")
                                    cl.findAndAddContactsByMid(W)
                                    cl.inviteIntoGroup(kirim,[W])
                                    cl.mentionWithRFU(kirim,user,"Invite Done","")

                        elif rfuText.lower().startswith("ginfo"):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                group = cl.getGroup(kirim)
                                try:
                                    gCreator = group.creator.displayName
                                except:
                                    gCreator = "Tidak ditemukan"
                                if group.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(group.invitee))
                                if group.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(line.reissueGroupTicket(group.id)))
                                cuki = "INFO GRUP"
                                cuki += "\nNama Group : {}".format(str(group.name))
                                cuki += "\nID Group :\n? {}".format(group.id)
                                cuki += "\nPembuat : {}".format(str(gCreator))
                                cuki += "\nJumlah Member : {}".format(str(len(group.members)))
                                cuki += "\nJumlah Pending : {}".format(gPending)
                                cuki += "\nGroup Qr : {}".format(gQr)
                                cuki += "\nGroup Ticket : {}".format(gTicket)
                                cl.sendMessage(kirim, str(cuki))

                        elif rfuText.lower().startswith("memberlist"):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                kontak = cl.getGroup(kirim)
                                group = kontak.members
                                num=1
                                msgs="LIST MEMBER\n"
                                for ids in group:
                                    msgs+="\n%i. %s" % (num, ids.displayName)
                                    num=(num+1)
                                msgs+="\n\nTOTAL MEMBER ( %i )" % len(group)
                                cl.sendText(kirim, msgs)

                        elif rfuText.lower().startswith("blocklist"):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                blockedlist = cl.getBlockedContactIds()
                                kontak = cl.getContacts(blockedlist)
                                num=1
                                msgs="My Blocked\n"
                                for ids in kontak:
                                    msgs+="\n%i. %s" % (num, ids.displayName)
                                    num=(num+1)
                                msgs+="\n\nTotal Blocked : %i" % len(kontak)
                                cl.sendText(kirim, msgs)

                        elif rfuText.lower().startswith("friendlist mid"):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                gruplist = cl.getAllContactIds()
                                kontak = cl.getContacts(gruplist)
                                num=1
                                msgs="List Mid Friend\n"
                                for ids in kontak:
                                    msgs+="\n%i. %s" % (num, ids.mid)
                                    num=(num+1)
                                msgs+="\n\nTotal Mid Friend : %i" % len(kontak)
                                cl.sendText(kirim, msgs)

                        elif rfuText.lower().startswith("group id"):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                saya = rfuText.replace('Grup id','')
                                gid = cl.getGroup(kirim)
                                cl.sendText(kirim, "ID Grup : \n" + gid.id + "\nName Grup : \n" + str(gid.name))

                        elif rfuText.lower().startswith("lurking on"):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                if kirim in Squad['readPoint']:
                                        try:
                                            del Squad['readPoint'][kirim]
                                            del Squad['readMember'][kirim]
                                            del Squad['readTime'][kirim]
                                        except:
                                            pass
                                        Squad['readPoint'][kirim] = msg.id
                                        Squad['readMember'][kirim] = ""
                                        Squad['readTime'][kirim] = datetime.now().strftime('%H:%M:%S')
                                        Squad['ROM'][kirim] = {}
                                        with open('sider.json', 'w') as fp:
                                            json.dump(Squad, fp, sort_keys=True, indent=4)
                                            cl.sendMessage(kirim,"Lurking already on")
                                else:
                                    try:
                                        del read['readPoint'][kirim]
                                        del read['readMember'][kirim]
                                        del read['readTime'][kirim]
                                    except:
                                        pass
                                    Squad['readPoint'][kirim] = msg.id
                                    Squad['readMember'][kirim] = ""
                                    Squad['readTime'][kirim] = datetime.now().strftime('%H:%M:%S')
                                    Squad['ROM'][kirim] = {}
                                    with open('sider.json', 'w') as fp:
                                        json.dump(Squad, fp, sort_keys=True, indent=4)
                                        cl.sendMessage(kirim, "Set reading point:\n" + readTime)
                                        
                        elif rfuText.lower().startswith("lurking off"):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                if kirim not in Squad['readPoint']:
                                    cl.sendMessage(kirim,"Lurking already off..")
                                else:
                                    try:
                                            del Squad['readPoint'][kirim]
                                            del Squad['readMember'][kirim]
                                            del Squad['readTime'][kirim]
                                    except:
                                          pass
                                    cl.sendMessage(kirim, "Delete reading point:\n" + readTime)
                
                        elif rfuText.lower().startswith("lurking reset"):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                if kirim in Squad["readPoint"]:
                                    try:
                                        Squad["readPoint"][kirim] = True
                                        Squad["readMember"][kirim] = {}
                                        Squad["readTime"][kirim] = readTime
                                        Squad["ROM"][kirim] = {}
                                    except:
                                        pass
                                    cl.sendMessage(kirim, "Reset reading point:\n" + readTime)
                                else:
                                    cl.sendMessage(kirim, "Lurking on dulu kaka..")
                                    
                        elif rfuText.lower().startswith("lurking read"):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                if kirim in Squad['readPoint']:
                                    if Squad["ROM"][kirim].items() == []:
                                        cl.sendMessage(kirim,"[ Reader ]:\nNone")
                                    else:
                                        chiya = []
                                        for rom in Squad["ROM"][kirim].items():
                                            chiya.append(rom[1])
                                        cmem = cl.getContacts(chiya) 
                                        zx = ""
                                        zxc = ""
                                        zx2 = []
                                        xpesan = 'Pembaca Pesan:\n'
                                    for x in range(len(cmem)):
                                        xname = str(cmem[x].displayName)
                                        pesan = ''
                                        pesan2 = pesan+"@ARDIAN_GANTENG\n"
                                        xlen = str(len(zxc)+len(xpesan))
                                        xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                        zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                                        zx2.append(zx)
                                        zxc += pesan2
                                    text = xpesan+ zxc + "\nLurking time: \n" + readTime
                                    try:
                                        cl.sendMessage(kirim, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                    except Exception as error:
                                        print (error)
                                    pass
                                else:
                                    cl.sendMessage(kirim,"Lurking on dulu kaka ??")

                        elif rfuText.lower().startswith("sider on"):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                try:
                                    del RfuCctv['Point2'][kirim]
                                    del RfuCctv['Point3'][kirim]
                                    del RfuCctv['Point1'][kirim]
                                except:
                                    pass
                                RfuCctv['Point2'][kirim] = msg.id
                                RfuCctv['Point3'][kirim] = ""
                                RfuCctv['Point1'][kirim]=True
                                cl.sendText(kirim,"Sider Set to On..")

                        elif rfuText.lower().startswith("sider off"):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                if kirim in RfuCctv['Point2']:
                                    RfuCctv['Point1'][kirim]=False
                                    cl.sendText(kirim, RfuCctv['Point3'][kirim])
                                else:
                                    cl.sendText(kirim, "Off not Going")

                        elif rfuText.lower().startswith("mentionall"):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                gname = cl.getGroup(kirim)
                                local = [contact.mid for contact in gname.members]
                                try:
                                    lur = len(local)//20
                                    for fu in range(lur+1):
                                        hdc = u''
                                        sell=0
                                        com=[]
                                        for rid in gname.members[fu*20 : (fu+1)*20]:
                                            com.append({"S":str(sell), "E" :str(sell+6), "M":rid.mid})
                                            sell += 7
                                            hdc += u'@A_RFU\n'
                                            atas = '\n Halo {} '.format(str(gname.name))
                                            atas += '\n Halo {} Sekawan'.format(str(len(local)))
                                        cl.sendMessage(kirim, text=hdc + str(atas), contentMetadata={u'MENTION': json.dumps({'MENTIONEES':com})}, contentType=0)
                                except Exception as error:
                                    cl.sendMessage(kirim, str(error))

                        elif rfuText.lower().startswith("welcome on"):
                          if user in RfuSekawan or user in Squad["Admin"]:
                            if user in RfuSekawan:
                                Squad['Welcome'] = True
                                cl.sendText(kirim,"Cek Welcome Already ON")
                        elif rfuText.lower().startswith("welcome off"):
                          if user in RfuSekawan or user in Squad["Admin"]:
                            if user in RfuSekawan:
                                Squad['Welcome'] = False
                                cl.sendText(kirim,"Cek Welcome Already Off")

                        elif rfuText.lower().startswith("changewelcome "):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                teks = rfuText.split(": ")
                                data = rfuText.replace(teks[0] + ": ","")
                                try:
                                    Squad["WcText"] = data
                                    cl.sendText(kirim,"Name Welcome Change to:\n" +str("(" +data+ ")"))
                                except:
                                    cl.sendText(kirim,"Name Error")

                        elif rfuText.lower().startswith("leave on"):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad['Leave'] = True
                                cl.sendText(kirim,"Cek Leave Already ON")
                        elif rfuText.lower().startswith("leave off"):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad['Leave'] = False
                                cl.sendText(kirim,"Cek Leave Already Off")

                        elif rfuText.lower().startswith("changeleave "):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                teks = rfuText.split(": ")
                                data = rfuText.replace(teks[0] + ": ","")
                                try:
                                    Squad["LvText"] = data
                                    cl.sendText(kirim,"Name Leave Change to:\n" +str("(" +data+ ")"))
                                except:
                                    cl.sendText(kirim,"Name Error")

                        elif rfuText.lower().startswith("runtime"):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                eltime = time.time() - mulai                                
                                opn = " "+waktu(eltime)
                                cl.sendText(kirim,"Connect to RFU SEKAWAN\nBot Active\n" + opn)                

                        elif rfuText.lower().startswith("broadcast: "):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                bc = msg.text.replace("Broadcast: ","")
                                gid = cl.getGroupIdsJoined()
                                for i in gid:
                                    cl.mentionWithRFU(i,user," BROADCAST BY:","\n" + str(" ("+bc+")"))

                        elif rfuText.lower().startswith("contactbc: "):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                bc = msg.text.replace("Contactbc: ","")
                                gid = cl.getAllContactIds()
                                for i in gid:
                                    cl.mentionWithRFU(i,user," BROADCAST BY:","\n" + str(" ("+bc+")"))

                        elif rfuText.lower().startswith("adminadd "):
                            if user in RfuSekawan:
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"][0]["M"]
                                targets = []
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                for target in targets:
                                    if target in Squad["Admin"]:
                                        cl.sendText(kirim, "Sudah Terdaftar di Admin")
                                    else:
                                        try:
                                            Squad["Admin"][target] = True
                                            cl.sendText(kirim, "Terdaftar Menjadi Admin ")
                                        except Exception as e:
                                            cl.sendText(kirim, str(error))

                        elif rfuText.lower().startswith("admindell "):
                            if user in Owner:
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"][0]["M"]
                                targets = []
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                for target in targets:
                                    if target not in Squad["Admin"]:
                                        cl.sendText(kirim, "Belum Terdaftar di Admin")
                                    else:
                                        try:
                                            del Squad["Admin"][target]
                                            cl.sendText(kirim, "Succes Dihapus menjadi admin")
                                        except Exception as e:
                                            cl.sendText(kirim, str(error))

                        elif rfuText.lower().startswith("changename: "):
                            if user in RfuSekawan:
                                name = rfuText.split(": ")
                                change = rfuText.replace(name[0] + ": ","")
                                cll = cl.getProfile()
                                cll.displayName = change
                                cl.updateProfile(cll)
                                owner = "uc721ad1f11fb7e128453ba5a27424998"
                                cl.mentionWithRFU(kirim,owner," Update Name Success","\n Change to " + str(change))

                        elif rfuText.lower().startswith("changebio: "):
                            if user in RfuSekawan:
                                proses = rfuText.split(": ")
                                teks = rfuText.replace(proses[0] + ": ","")
                                no1 = cl.getProfile()
                                no1.statusMessage = teks
                                cl.updateProfile(no1)
                                cl.sendText(kirim,"My Bio Change To : " + teks)

                        elif rfuText.lower().startswith("remove message"):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                try:
                                    cl.removeAllMessages(fast.param2)
                                    ginfo = cl.getGroup(kirim)
                                    cl.mentionWithRFU(kirim,user," Remove Message Success ","\n In Grup" + str(" ("+ginfo.name+")"))
                                except:
                                    pass

                        elif rfuText.lower().startswith("restart"):
                            if user in RfuSekawan:
                                cl.sendText(kirim, 'Restarting Server Prosses..')
                                print ("Restarting Server")
                                restart_program()

                        elif rfuText.lower().startswith("bot logout"):
                            if user in RfuSekawan:
                                cl.mentionWithRFU(kirim,user," Akses Off","")
                                print ("Selfbot Off")
                                exit(1)

                        elif rfuText.lower().startswith("kick "):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"][0]["M"]
                                targets = []
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                for target in targets:
                                    if target in Rfu:
                                        pass
                                    else:
                                        try:
                                            klist=[cl]
                                            kicker=random.choice(klist)
                                            kicker.kickoutFromGroup(kirim,[target])
                                            Squad["Blacklist"][target] = True
                                        except Exception as e:
                                            cl.sendText(kirim, str(error))

                        elif rfuText.lower().startswith("my grup"):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                groups = cl.groups
                                ret_ = "GRUP JOIN"
                                no = 0 + 1
                                for gid in groups:
                                    group = cl.getGroup(gid)
                                    ret_ += "\n\n{}. {} ".format(str(no), str(group.name))
                                    no += 1
                                ret_ += "\n\nTOTAL {} GRUP JOIN".format(str(len(groups)))
                                cl.sendText(kirim, str(ret_))

                        elif rfuText.lower().startswith("rejectall grup"):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                ginvited = cl.getGroupIdsInvited()
                                if ginvited != [] and ginvited != None:
                                    for gid in ginvited:
                                        cl.rejectGroupInvitation(gid)
                                    cl.sendMessage(kirim, "Succes Cancell {} Invite Grup".format(str(len(ginvited))))
                                else:
                                    cl.sendMessage(kirim, "Nothing Invited")

                        elif rfuText.lower().startswith("status"):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                try:
                                    hasil = "Status Bot\n"
                                    if Squad["autoAdd"] == True: hasil += "\nAuto Add ( on )"
                                    else: hasil += "\nAuto Add ( off )"
                                    if Squad["autoJoin"] == True: hasil += "\nAuto Join ( on )"
                                    else: hasil += "\nAuto Join ( off )"
                                    if Squad["AutoReject"] == True: hasil += "\nAuto Reject Room ( on )"
                                    else: hasil += "\nAuto Reject Room ( off )"
                                    if Squad["AutojoinTicket"] == True: hasil += "\nAuto Join Ticket ( on )"
                                    else: hasil += "\nAuto Join Ticket ( off )"
                                    if Squad["autoRead"] == True: hasil += "\nAuto Read ( on )"
                                    else: hasil += "\nAuto Read ( off )"
                                    if Squad["AutoRespon"] == True: hasil += "\nDetect Mention ( on )"
                                    else: hasil += "\nDetect Mention ( off )"
                                    if Squad["KickRespon"] == True: hasil += "\nDetect Mention ( on )"
                                    else: hasil += "\nDetect Kick Mention ( off )"
                                    if Squad["Contact"] == True: hasil += "\nCheck Contact ( on )"
                                    else: hasil += "\nCheck Contact ( off )"
                                    if Squad["Timeline"] == True: hasil += "\nCheck Post Timeline ( on )"
                                    else: hasil += "\nCheck Post ( off )"
                                    if Squad["IDSticker"] == True: hasil += "\nCheck Sticker ( on )"
                                    else: hasil += "\nCheck Sticker ( off )"
                                    if Squad["UnsendPesan"] == True: hasil += "\nUnsend Message ( on )"
                                    else: hasil += "\nUnsend Message ( off )"
                                    if Squad["KickOn"] == True: hasil += "\nKick All Member ( on )"
                                    else: hasil += "\nKick All Member ( off )"
                                    if Squad["SpamInvite"] == True: hasil += "\nSpam invite via contact ( on )"
                                    else: hasil += "\nSpam invite Via Contact ( off )"
                                    hasil += "\n\nStatus Bot"
                                    cl.sendMessage(kirim, str(hasil))
                                except Exception as error:
                                    cl.sendMessage(kirim, str(error))

                        elif rfuText.lower().startswith("unsend on"):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad['UnsendPesan'] = True
                                cl.sendText(kirim,"Cek UnsendMessage Set to on..")
                        elif rfuText.lower().startswith("unsend off"):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad['UnsendPesan'] = False
                                cl.sendText(kirim,"Cek UnsendMessage Set to off..")

                        elif rfuText.lower().startswith("changepp on"):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad['Upfoto'] = True
                                cl.sendText(kirim,"Send Pict For UpPict")
                        elif rfuText.lower().startswith("changepp off"):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad['Upfoto'] = False
                                cl.sendText(kirim,"Send Pict Already Off")

                        elif rfuText.lower().startswith("cfotogrup on"):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad['UpfotoGrup'] = True
                                cl.sendText(kirim,"Send Pict For Change Foto Grup")
                        elif rfuText.lower().startswith("cfotogrup off"):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad['UpfotoGrup'] = False
                                cl.sendText(kirim,"Send Pict Already Off")

                        elif rfuText.lower().startswith("timeline on"):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad['Timeline'] = True
                                cl.sendText(kirim,"Cek Post Set to on..")
                        elif rfuText.lower().startswith("timeline off"):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad['Timeline'] = False
                                cl.sendText(kirim,"Cek Post Set to off..")

                        elif rfuText.lower().startswith("autojoin on"):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad['autoJoin'] = True
                                cl.sendText(kirim,"Join Set To On..")
                        elif rfuText.lower().startswith("autojoin off"):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad['autoJoin'] = False
                                cl.sendText(kirim,"Join Set To Off..")

                        elif rfuText.lower().startswith("autoreject on"):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad['AutoReject'] = True
                                cl.sendText(msg.to,"Reject Set To On..")
                        elif rfuText.lower().startswith("autoreject off"):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad['AutoReject'] = False
                                cl.sendText(msg.to,"Reject Set To Off..")

                        elif rfuText.lower().startswith("admin:add-on"):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad["Adminadd"] = True
                                cl.sendText(kirim,"Send Contact to added Admin..")
                        elif rfuText.lower().startswith("admin:add-off"):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad["Adminadd"] = False
                                cl.sendText(kirim,"Send Contact to added Admin in Off..")

                        elif rfuText.lower().startswith("admin:del-on"):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad["AdminDel"] = True
                                cl.sendText(kirim,"Send Contact to Dellete Admin..")
                        elif rfuText.lower().startswith("admin:del-off"):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad["AdminDel"] = False
                                cl.sendText(kirim,"Send Contact to Dellete Admin in Off..")

                        elif rfuText.lower().startswith("gift on"):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad["Gift"] = True
                                cl.sendText(kirim,"Send Contact to send Gift..")
                        elif rfuText.lower().startswith("gift off"):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad["Gift"] = False
                                cl.sendText(kirim,"Send Contact to Gift in Off..")

                        elif rfuText.lower().startswith("spaminvite on"):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad["SpamInvite"] = True
                                cl.sendText(kirim,"Send Contact to spam grup..")
                        elif rfuText.lower().startswith("spaminvite off"):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad["Gift"] = False
                                cl.sendText(kirim,"Send Contact to send grup Off..")

                        elif rfuText.lower().startswith("auto jointicket on"):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad["AutojoinTicket"] = True
                                cl.sendText(kirim,"Join Ticket Set To On")
                        elif rfuText.lower().startswith("auto jointicket off"):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad["AutojoinTicket"] = False
                                cl.sendText(kirim,"Join Ticket Set To Off")
                        elif '/ti/g/' in rfuText.lower():
                            if user in RfuSekawan or user in Squad["Admin"]:
                                link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                links = link_re.findall(msg.text)
                                n_links=[]
                                for l in links:
                                    if l not in n_links:
                                        n_links.append(l)
                                for ticket_id in n_links:
                                    if Squad["AutojoinTicket"] == True:
                                        group=cl.findGroupByTicket(ticket_id)
                                        cl.acceptGroupInvitationByTicket(group.id,ticket_id)
                                        cl.sendText(kirim,"Success Masuk %s" % str(group.name))

                        elif rfuText.lower().startswith("copy on"):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad['Copy'] = True
                                cl.sendText(kirim,"Send Contact For Copy User")
                        elif rfuText.lower().startswith("copy off"):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad['Copy'] = False
                                cl.sendText(kirim,"Send Contact Already Off")

                        elif rfuText.lower().startswith("clone "):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = cl.getContact(ls)
                                        cl.cloneContactProfile(ls)
                                        cl.sendMessage(kirim, "Berhasil mengclone profile {}".format(contact.displayName))

                        elif rfuText.lower().startswith("comeback"):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                try:
                                    clProfile.displayName = str(ProfileMe["displayName"])
                                    clProfile.statusMessage = str(ProfileMe["statusMessage"])
                                    clProfile.pictureStatus = str(ProfileMe["pictureStatus"])
                                    cl.updateProfileAttribute(8, clProfile.pictureStatus)
                                    cl.updateProfile(clProfile)
                                    cl.sendMessage(kirim, "Already back to my account")
                                except:
                                    cl.sendMessage(kirim, "Error Come Back")

                        elif rfuText.lower().startswith("steal on"):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad['Steal'] = True
                                cl.sendText(kirim,"Send Contact For Cek Contact")
                        elif rfuText.lower().startswith("steal off"):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad['Steal'] = False
                                cl.sendText(kirim,"Send Contact Already Off")

                        elif rfuText.lower().startswith("contact on"):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad['Contact'] = True
                                cl.sendText(kirim,"Contact Set to on")
                        elif rfuText.lower().startswith("contact off"):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad['Contact'] = False
                                cl.sendText(kirim,"Contact Already Off")

                        elif rfuText.lower().startswith("invite on"):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad['Invite'] = True
                                cl.sendText(kirim,"Send Contact For Invite Target")
                        elif rfuText.lower().startswith("invite off"):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad['Invite'] = False
                                cl.sendText(kirim,"Send Contact Set Off")

                        elif rfuText.lower().startswith("kill on"):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad["KillOn"] = True
                                cl.sendMessage(kirim, "SendContact For Kick Taget")
                        elif rfuText.lower().startswith("kill off"):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad["KillOn"] = False
                                cl.sendMessage(kirim, "SendContact For Kick Taget in Off")

                        elif rfuText.lower().startswith("mic:add-on"):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Target["Mic"] = True
                                cl.sendText(kirim,"Send Contact To Clone Message User")
                        elif rfuText.lower().startswith("mic:del-on"):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Target["MicDel"] = True
                                cl.sendText(kirim,"Send Contact Dellete Clone Message User")
                        elif rfuText.lower().startswith("mimic "):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                sep = rfuText.split(" ")
                                mic = rfuText.replace(sep[0] + " ","")
                                if mic == "on":
                                    if Mozilla["mimic"]["status"] == False:
                                        Mozilla["mimic"]["status"] = True
                                        cl.sendText(kirim,"Mimic Set to on")
                                elif mic == "off":
                                    if Mozilla["mimic"]["status"] == True:
                                        Mozilla["mimic"]["status"] = False
                                        cl.sendText(kirim,"Mimic Message off")

                        elif rfuText.lower().startswith("mimiclist"):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                if Mozilla["mimic"]["target"] == {}:
                                    cl.sendText(kirim,"Tidak Ada Target")
                                else:
                                    mc = "Mimic List"
                                    for mi_d in Mozilla["mimic"]["target"]:
                                        mc += "\n? "+cl.getContact(mi_d).displayName
                                    cl.sendText(kirim,mc + "\nFinish")

                        elif rfuText.lower().startswith("refresh"):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                try:
                                    Squad['Mic'] = False
                                    Squad['MicDel'] = False
                                    Squad['Gift'] = False
                                    Squad['Steal'] = False
                                    Squad['Invite'] = False
                                    Squad['Contact'] = False
                                    Squad['Copy'] = False
                                    Squad['autoJoin'] = False
                                    Squad['autoAdd'] = False
                                    Squad['AutojoinTicket'] = False
                                    Squad['UnsendPesan'] = False
                                    Squad['AutoReject'] = False
                                    Squad['Timeline'] = False
                                    Squad['Upfoto'] = False
                                    Squad['UpfotoGrup'] = False
                                    Squad['Adminadd'] = False
                                    Squad['AdminDel'] = False
                                    Squad['Welcome'] = False
                                    Squad['Leave'] = False
                                    Squad['Ban'] = False
                                    Squad['Unban'] = False
                                    Squad['KillOn'] = False
                                    Squad['KickOn'] = False
                                    Squad['SpamInvite'] = False
                                    cl.sendText(kirim,"Refresh Success")
                                except Exception as e:
                                    cl.sendText(kirim, str(error))

                        elif rfuText.lower().startswith("my name"):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                contact = cl.getContact(user)
                                cl.sendMessage(kirim, "MyName : {}".format(contact.displayName))
                        elif rfuText.lower().startswith("my bio"):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                contact = cl.getContact(user)
                                cl.sendMessage(kirim, "My Status : \n{}".format(contact.statusMessage))
                        elif rfuText.lower().startswith("my picture"):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                contact = cl.getContact(user)
                                cl.sendImageWithURL(kirim,"http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus))
                        elif rfuText.lower().startswith("my video"):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                contact = cl.getContact(user)
                                cl.sendVideoWithURL(kirim,"http://dl.profile.line-cdn.net/{}/vp".format(contact.pictureStatus))
                        elif rfuText.lower().startswith("my cover"):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                channel = cl.getProfileCoverURL(user)          
                                path = str(channel)
                                cl.sendImageWithURL(kirim, path)

                        elif rfuText.lower().startswith("stealname "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = cl.getContact(ls)
                                    cl.sendMessage(to, "[ Display Name ]\n{}".format(str(contact.displayName)))
                        elif rfuText.lower().startswith("stealbio "):
                          if user in RfuSekawan or user in Squad["Admin"]:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = cl.getContact(ls)
                                    cl.sendMessage(kirim, "[ Status Message ]\n{}".format(str(contact.statusMessage)))
                        elif rfuText.lower().startswith("stealpict "):
                          if user in RfuSekawan or user in Squad["Admin"]:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = cl.getContact(ls)
                                    path = "http://dl.profile.line.naver.jp/{}".format(contact.pictureStatus)
                                    cl.sendImageWithURL(kirim, str(path))
                        elif rfuText.lower().startswith("stealvideo "):
                          if user in RfuSekawan or user in Squad["Admin"]:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = cl.getContact(ls)
                                    path = "http://dl.profile.line.naver.jp/{}/vp".format(contact.pictureStatus)
                                    cl.sendVideoWithURL(kirim, str(path))
                        elif rfuText.lower().startswith("stealcover "):
                          if user in RfuSekawan or user in Squad["Admin"]:
                            if cl != None:
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        channel = cl.getProfileCoverURL(ls)
                                        path = str(channel)
                                        cl.sendImageWithURL(kirim, str(path))
                        elif rfuText.lower().startswith("stealmid "):
                          if user in RfuSekawan or user in Squad["Admin"]:
                              try:
                                  key = eval(msg.contentMetadata["MENTION"])
                                  u = key["MENTIONEES"][0]["M"]
                                  cmid = cl.getContact(u).mid
                                  cl.sendText(kirim, str(cmid))
                              except Exception as e:
                                  cl.sendText(kirim, str(e))
                        elif rfuText.lower().startswith("profile "):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                try:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    u = key["MENTIONEES"][0]["M"]
                                    cname = cl.getContact(u).displayName
                                    cmid = cl.getContact(u).mid
                                    cstatus = cl.getContact(u).statusMessage
                                    cpic = cl.getContact(u).picturePath
                                    a = cl.getProfileCoverURL(mid=u)
                                    cl.sendText(kirim, 'Nama : '+cname+'\nMid : '+cmid+'\nBio : '+cstatus+'\nURL Picture : http://dl.profile.line.naver.jp'+cpic)
                                    cl.sendMessage(kirim, None, contentMetadata={'mid': cmid}, contentType=13)
                                    cl.sendImageWithURL(kirim, a)
                                    if "videoProfile='{" in str(cl.getContact(u)):
                                        cl.sendVideoWithURL(kirim, 'http://dl.profile.line.naver.jp'+cpic+'/vp.small')
                                    else:
                                        cl.sendImageWithURL(kirim, 'http://dl.profile.line.naver.jp'+cpic)
                                except Exception as e:
                                    cl.sendText(kirim, str(e))

                        elif rfuText.lower().startswith("randomgrup: "):
                            if user in RfuSekawan or user in Squad["Admin"]:
                              if msg.toType == 2:
                                  strnum = rfuText.replace("randomgrup: ","")
                                  source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                                  try:
                                      num = int(strnum)
                                      group = cl.getGroup(kirim)
                                      for var in range(0,num):
                                          name = "".join([random.choice(source_str) for x in range(10)])
                                          time.sleep(0.01)
                                          group.name = name
                                          cl.updateGroup(group)
                                  except Exception as e:
                                      cl.sendText(kirim, str(e))

                        elif rfuText.lower().startswith("annoence"):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                try:
                                    gett = cl.getChatRoomAnnouncements(kirim)
                                    for a in gett:
                                        aa = cl.getContact(a.creatorMid).displayName
                                        bb = a.contents
                                        cc = bb.link
                                        textt = bb.text
                                        cl.sendText(kirim, 'Pemberitahuan Grup\n\nLink: ' + str(cc) + '\nPenulis: ' + str(aa) + '\nTeksnya: ' + str(textt))
                                        break
                                except Exception as e:
                                    cl.sendText(kirim, "Pemberitahuan Grup Tidak Ditemukan")

#------------------------------------------ SOCIAL MEDIA ----------------------------------------------------#

                        elif rfuText.lower().startswith("topnews"):
                              if user in RfuSekawan or user in Squad["Admin"]:
                                  rfu=requests.get("https://newsapi.org/v2/top-headlines?country=id&apiKey=1214d6480f6848e18e01ba6985e2008d")
                                  data=rfu.text
                                  data=json.loads(data)
                                  hasil = "Top News\n\n"
                                  hasil += "(1) " + str(data["articles"][0]["title"])                                                        
                                  hasil += "\n     Sumber : " + str(data["articles"][0]["source"]["name"])
                                  hasil += "\n     Penulis : " + str(data["articles"][0]["author"])
                                  hasil += "\n     Link : " + str(data["articles"][0]["url"])
                                  hasil += "\n\n(2) " + str(data["articles"][1]["title"])                                                        
                                  hasil += "\n     Sumber : " + str(data["articles"][1]["source"]["name"])
                                  hasil += "\n     Penulis : " + str(data["articles"][1]["author"])   
                                  hasil += "\n     Link : " + str(data["articles"][1]["url"])
                                  hasil += "\n\n(3) " + str(data["articles"][2]["title"])                                                        
                                  hasil += "\n     Sumber : " + str(data["articles"][2]["source"]["name"])
                                  hasil += "\n     Penulis : " + str(data["articles"][2]["author"])
                                  hasil += "\n     Link : " + str(data["articles"][2]["url"])
                                  hasil += "\n\n(4) " + str(data["articles"][3]["title"])                                                        
                                  hasil += "\n     Sumber : " + str(data["articles"][3]["source"]["name"])
                                  hasil += "\n     Penulis : " + str(data["articles"][3]["author"])
                                  hasil += "\n     Link : " + str(data["articles"][3]["url"])
                                  hasil += "\n\n(5) " + str(data["articles"][4]["title"])                                                        
                                  hasil += "\n     Sumber : " + str(data["articles"][4]["source"]["name"])
                                  hasil += "\n     Penulis : " + str(data["articles"][4]["author"])
                                  hasil += "\n     Link : " + str(data["articles"][4]["url"])
                                  hasil += "\n\n(6) " + str(data["articles"][5]["title"])                                                        
                                  hasil += "\n     Sumber : " + str(data["articles"][5]["source"]["name"])
                                  hasil += "\n     Penulis : " + str(data["articles"][5]["author"])
                                  hasil += "\n     Link : " + str(data["articles"][5]["url"])
                                  path = data["articles"][3]["urlToImage"]
                                  cl.sendText(kirim, str(hasil))
                                  cl.sendImageWithURL(kirim, str(path))

                        elif rfuText.lower().startswith("data birth: "):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                tanggal = rfuText.replace("data birth: ","")
                                r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                                data=r.text
                                data=json.loads(data)
                                lahir = data["data"]["lahir"]
                                usia = data["data"]["usia"]
                                ultah = data["data"]["ultah"]
                                zodiak = data["data"]["zodiak"]
                                cl.sendText(kirim," I N F O R M A S I \n"+"Date Of Birth : "+lahir+"\nAge : "+usia+"\nUltah : "+ultah+"\nZodiak : "+zodiak+"\n  I N F O R M A S I ")

                        elif rfuText.lower().startswith("urban: "):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                sep = rfuText.split(" ")
                                judul = rfuText.replace(sep[0] + " ","")
                                url = "http://api.urbandictionary.com/v0/define?term="+str(judul)
                                with requests.session() as s:
                                    s.headers["User-Agent"] = random.choice(Mozilla["userAgent"])
                                    r = s.get(url)
                                    data = r.text
                                    data = json.loads(data)
                                    cu = "Urban Result\n\n"
                                    cu += "\nText: "+ data["tags"][0]
                                    cu += ","+ data["tags"][1]
                                    cu += ","+ data["tags"][2]
                                    cu += ","+ data["tags"][3]
                                    cu += ","+ data["tags"][4]
                                    cu += ","+ data["tags"][5]
                                    cu += ","+ data["tags"][6]
                                    cu += ","+ data["tags"][7]
                                    cu += "\n[1]\nAuthor: "+str(data["list"][0]["author"])+"\n"
                                    cu += "\nWord: "+str(data["list"][0]["word"])+"\n"
                                    cu += "\nLink: "+str(data["list"][0]["permalink"])+"\n"
                                    cu += "\nDefinition: "+str(data["list"][0]["definition"])+"\n"
                                    cu += "\nExample: "+str(data["list"][0]["example"])+"\n"
                                    cl.sendText(kirim, str(cu))

                        elif rfuText.lower().startswith("sslink: "):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                 website = msg.text.replace("sslink: ","")
                                 response = requests.get("http://rahandiapi.herokuapp.com/sswebAPI?key=betakey&link="+website+"")
                                 data = response.json()
                                 pictweb = data['result']
                                 cl.sendImageWithURL(kirim, pictweb)

                        elif rfuText.lower().startswith("maps: "):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                location = rfuText.lower().replace("maps: ","")
                                with requests.session() as web:
                                    web.headers["user-agent"] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
                                    rfu = web.get("http://api.corrykalam.net/apiloc.php?lokasi={}".format(urllib.parse.quote(location)))
                                    data = rfu.text
                                    data = json.loads(data)
                                    if data[0] != "" and data[1] != "" and data[2] != "":
                                        link = "https://www.google.co.id/maps/@{},{},15z".format(str(data[1]), str(data[2]))
                                        ret_ = "Check Location\n"
                                        ret_ += "\n Lokasi : " + data[0]
                                        ret_ += "\n Google Maps : " + link
                                        ret_ += "\n\nSearch Location Success"
                                    else:
                                        ret_ = "Searching Location Error or Location Tidak Ditemukan"
                                    cl.sendText(kirim,str(ret_))

                        elif rfuText.lower().startswith("cekcuaca: "):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                weather = rfuText.lower().replace("cekcuaca: ","")
                                with requests.session() as web:
                                    web.headers["user-agent"] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
                                    rfu = web.get("http://api.corrykalam.net/apicuaca.php?kota={}".format(urllib.parse.quote(weather)))
                                    data = rfu.text
                                    data = json.loads(data)
                                    if "result" not in data:
                                        ret_ = "Cheking Weather\n"
                                        ret_ += "\nSuhu : " + data[1].replace("Suhu : ","")
                                        ret_ += "\nLokasi : " + data[0].replace("Temperatur di kota ","")
                                        ret_ += "\nKelembaban : " + data[2].replace("Kelembaban : ","")
                                        ret_ += "\nTekanan Udara : " + data[3].replace("Tekanan udara : ","")
                                        ret_ += "\nKecepatan Angin : " + data[4].replace("Kecepatan angin : ","")
                                        ret_ += "\n\nSearching Weather Success"
                                    else:
                                        ret_ = "Checking Weather Error or Not Found Location"
                                    cl.sendText(kirim, str(ret_))

                        elif rfuText.lower().startswith("jadwalshalat: "):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                shalat = rfuText.lower().replace("jadwalshalat: ","")
                                with requests.session() as web:
                                    web.headers["user-agent"] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
                                    rfu = web.get("http://api.corrykalam.net/apisholat.php?lokasi={}".format(urllib.parse.quote(shalat)))
                                    data = rfu.text
                                    data = json.loads(data)
                                    if data[1] != "Subuh : " and data[2] != "Dzuhur : " and data[3] != "Ashar : " and data[4] != "Maghrib : " and data[5] != "Isha : ":
                                        ret_ = "Jadwal Shalat\n"
                                        ret_ += "\nLocation : " + data[0]
                                        ret_ += "\n " + data[1]
                                        ret_ += "\n " + data[2]
                                        ret_ += "\n " + data[3]
                                        ret_ += "\n " + data[4]
                                        ret_ += "\n " + data[5]
                                        ret_ += "\n\nJadwal Shalat Wilayah"
                                    else:
                                        ret_ = "Jadwa Shalat Wilayah Error or Not Found Location" 
                                    cl.sendText(kirim, str(ret_))

                        elif rfuText.lower().startswith("idline: "):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                 msgg = rfuText.replace('idline: ','')
                                 conn = cl.findContactsByUserid(msgg)
                                 if True:
                                    cl.sendText(kirim,"Link User : https://line.me/ti/p/~" + msgg)
                                    cl.sendMessage(kirim, None, contentMetadata={'mid': conn.mid}, contentType=13)
                                    contact = cl.getContact(conn.mid)
                                    cl.sendImageWithURL(kirim,"http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                                    cover = cl.getProfileCoverURL(conn.mid)
                                    cl.sendImageWithURL(kirim, cover)
                                    cl.mentionWithRFU(kirim,conn.mid,"Tag User\n","")

                        elif rfuText.lower().startswith("say-id: "):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                try:
                                    isi = rfuText.lower().replace('say-id: ','')
                                    tts = gTTS(text=isi, lang='id', slow=False)
                                    tts.save('temp.mp3')
                                    cl.sendAudio(kirim, 'temp.mp3')
                                except Exception as e:
                                    cl.sendText(kirim, str(e))

                        elif rfuText.lower().startswith("say-en: "):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                try:
                                    isi = rfuText.lower().replace('say-en: ','')
                                    tts = gTTS(text=isi, lang='en', slow=False)
                                    tts.save('temp.mp3')
                                    cl.sendAudio(kirim, 'temp.mp3')
                                except Exception as e:
                                    cl.sendText(kirim, str(e))

                        elif rfuText.lower().startswith("say-jp: "):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                try:
                                    isi = rfuText.lower().replace('say-jp: ','')
                                    tts = gTTS(text=isi, lang='ja', slow=False)
                                    tts.save('temp.mp3')
                                    cl.sendAudio(kirim, 'temp.mp3')
                                except Exception as e:
                                    cl.sendText(kirim, str(e))

                        elif rfuText.lower().startswith("say-ar: "):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                try:
                                    isi = rfuText.lower().replace('say-ar: ','')
                                    tts = gTTS(text=isi, lang='ar', slow=False)
                                    tts.save('temp.mp3')
                                    cl.sendAudio(kirim, 'temp.mp3')
                                except Exception as e:
                                    cl.sendText(kirim, str(e))

                        elif rfuText.lower().startswith("say-ko: "):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                try:
                                    isi = rfuText.lower().replace('say-ko: ','')
                                    tts = gTTS(text=isi, lang='ko', slow=False)
                                    tts.save('temp.mp3')
                                    cl.sendAudio(kirim, 'temp.mp3')
                                except Exception as e:
                                    cl.sendText(kirim, str(e))

                        elif rfuText.lower().startswith("apakah: "):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                try:
                                    txt = ['iya','tidak','bisa jadi','mungkin saja','tidak mungkin','au ah gelap']
                                    isi = random.choice(txt)
                                    tts = gTTS(text=isi, lang='id', slow=False)
                                    tts.save('temp2.mp3')
                                    cl.sendAudio(kirim, 'temp2.mp3')
                                except Exception as e:
                                    cl.sendText(kirim, str(e))

                        elif rfuText.lower().startswith("kapan: "):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                try:
                                    txt = ['kapan kapan','besok','satu abad lagi','Hari ini','Tahun depan','Minggu depan','Bulan depan','Sebentar lagi']
                                    isi = random.choice(txt)
                                    tts = gTTS(text=isi, lang='id', slow=False)
                                    tts.save('temp2.mp3')
                                    cl.sendAudio(kirim, 'temp2.mp3')
                                except Exception as e:
                                    cl.sendText(kirim, str(e))

                        elif rfuText.lower().startswith("wikipedia: "):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                try:
                                    wiki = rfuText.lower().replace("wikipedia: ","")
                                    wikipedia.set_lang("id")
                                    pesan="Title ("
                                    pesan+=wikipedia.page(wiki).title
                                    pesan+=")\n\n"
                                    pesan+=wikipedia.summary(wiki, sentences=1)
                                    pesan+="\n"
                                    pesan+=wikipedia.page(wiki).url
                                    cl.sendText(kirim, pesan)
                                except:
                                    try:
                                        pesan="Over Text Limit! Please Click link\n"
                                        pesan+=wikipedia.page(wiki).url
                                        cl.sendText(kirim, pesan)
                                    except Exception as e:
                                        cl.sendText(kirim, str(e))

                        elif rfuText.lower().startswith("kalender"):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                tz = pytz.timezone("Asia/Makassar")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                cl.sendMessage(kirim, readTime)

                        elif rfuText.lower().startswith("gambar: "):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                try:
                                    query = rfuText.replace("gambar: ", "")
                                    query = query.replace(" ", "+")
                                    gambar = cl.download_image(query)
                                    cl.sendImageWithURL(kirim, gambar)
                                except Exception as e:
                                    cl.sendText(kirim, str(e))                                    

                        elif rfuText.lower().startswith("youtube: "):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                try:
                                    query = rfuText.replace("youtube: ", "")
                                    query = query.replace(" ", "+")
                                    x = cl.youtube(query)
                                    cl.sendText(kirim, x)
                                except Exception as e:
                                    cl.sendText(kirim, str(e))

#--------------------------------- TRANSLATOR -------------------------------------------------#

                        elif rfuText.lower().startswith("indonesian: "):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                sep = rfuText.split(" ")
                                isi = rfuText.replace(sep[0] + " ","")
                                translator = Translator()
                                hasil = translator.translate(isi, dest='id')
                                text = hasil.text
                                cl.sendMessage(kirim, "Translator Indonesian\n\n" + str(text))

                        elif rfuText.lower().startswith("english: "):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                sep = rfuText.split(" ")
                                isi = rfuText.replace(sep[0] + " ","")
                                translator = Translator()
                                hasil = translator.translate(isi, dest='en')
                                text = hasil.text
                                cl.sendMessage(kirim, "Translator English\n\n" + str(text))

                        elif rfuText.lower().startswith("korea: "):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                    sep = rfuText.split(" ")
                                    isi = rfuText.replace(sep[0] + " ","")
                                    translator = Translator()
                                    hasil = translator.translate(isi, dest='ko')
                                    text = hasil.text
                                    cl.sendMessage(kirim, "Translator Korea\n\n" + str(text))

                        elif rfuText.lower().startswith("japan: "):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                sep = rfuText.split(" ")
                                isi = rfuText.replace(sep[0] + " ","")
                                translator = Translator()
                                hasil = translator.translate(isi, dest='ja')
                                text = hasil.text
                                cl.sendMessage(kirim, "Translator Japan\n\n" + str(text))

                        elif rfuText.lower().startswith("thailand: "):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                sep = rfuText.split(" ")
                                isi = rfuText.replace(sep[0] + " ","")
                                translator = Translator()
                                hasil = translator.translate(isi, dest='th')
                                text = hasil.text
                                cl.sendMessage(kirim, "Translator Thailand\n\n" + str(text))

                        elif rfuText.lower().startswith("arab: "):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                sep = rfuText.split(" ")
                                isi = rfuText.replace(sep[0] + " ","")
                                translator = Translator()
                                hasil = translator.translate(isi, dest='ar')
                                text = hasil.text
                                cl.sendMessage(kirim, "Translator Saudi Arabia\n\n" + str(text))

                        elif rfuText.lower().startswith("malaysia: "):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                sep = rfuText.split(" ")
                                isi = rfuText.replace(sep[0] + " ","")
                                translator = Translator()
                                hasil = translator.translate(isi, dest='ms')
                                text = hasil.text
                                cl.sendMessage(kirim, "Translator Malaysia\n\n" + str(text))

                        elif rfuText.lower().startswith("jawa: "):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                sep = rfuText.split(" ")
                                isi = rfuText.replace(sep[0] + " ","")
                                translator = Translator()
                                hasil = translator.translate(isi, dest='jw')
                                text = hasil.text
                                cl.sendMessage(kirim, "Translator Jawa\n\n" + str(text))

    except Exception as error:
        print (error)

#-------------------------------------------- FINNISHING SCRIP ------------------------------------------------#

while True:
    try:
        Operation = RIDEN.singleTrace(count=50)
        if Operation is not None:
            for fast in Operation:
                RIDEN.setRevision(fast.revision)
                thread1 = threading.Thread(target=RIDEN_FAST_USER, args=(fast,))#self.OpInterrupt[fast.type], args=(fast,)
                thread1.start()
                thread1.join()
    except Exception as error:
        print (error)
