# Steam-Profile-Fetcher

###### Dreckig und schnell, aber funktioniert ¯\_(ツ)_/¯

Funktion:

Dursucht die von Steam zur Verfügung gestellte XML File des gegeben Profils.
Gesucht wird nach einem Profil mit der CustomID oder der Steam64 ID welche jeweils in der Profil URL gefunden werden kann.
Die XML Datei wird nach den üblichen tags dursucht und herausgefiltert / geparsed.

XML Files nach folgendem Schema:
[Steamworks Community Data](https://partner.steamgames.com/documentation/community_data)


###### Beispiel - CustomID:
```
1) cid
2) dubskyplays
```

###### Beispiel - Steam64:
```
1) id64
2) 76561198104614635
```
