import xml.etree.ElementTree as ET
import urllib.request
import os

clear = lambda: os.system('cls')

#Suchabfrage
def suchen():
        targetid = idabfrage()
        tree = ET.parse(urllib.request.urlopen('http://steamcommunity.com/id/' + targetid +'/?xml=1'))  
        root = tree.getroot()

        clear()

        steam64 = root[0].text
        steamid = root[1].text
        status = root[2].text
        privacy = root[4].text
        tban = root[10].text
        vban = root[9].text
        since = root[13].text
        groups = root[10].text

        print("_________________________________")
        print("[> Steam Profil Informationen <]")
        print("_________________________________")
        print("Nutzer: " + steamid)
        print("Status: " + status)
        print("Beitritt: " + since)
        print("")
        print("64ID: " + steam64)
        print("Privacy: " + privacy)
        print("")
        print("Trade Banned: " + tban)
        print("VAC Banned: " + vban)
        print("_________________________________")
        print("Gruppen")
        print("_________________________________")

        x=0
        for group in root.findall('groups/group/groupID64'):
                x+=1
                print("Gruppe " + str(x)+ " >> " + group.text)

        print("\nGruppen insgesamt: " + str(x))       
        return

#ID Abfrage
def idabfrage():
        id_art = input("CID oder ID64: ")
        if id_art == "CID" or "cid":
                target = input("SteamCID: ")
                return target
        elif id_art == "id64" or "ID64":
                target = input("Steam64: ")
                return target
        else:
                print("Error")
                exit()
                return