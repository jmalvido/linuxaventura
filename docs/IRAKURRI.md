# LinuxAventura — hasierako gida

## Martxan jarri Ubuntuko makina birtualean

Jarri linuxaventura karpeta zure HOME direktorioan eta exekutatu:

```bash
cd ~/linuxaventura
bash jugar.sh
```

Python 3.8 edo berriagoa eta Bash behar dira. Jokoak ez du sudo behar.
Lehen aldian aukeratu 2 (Euskera). Ondoren, aukeratu jardueraren zenbakia.
Jarduerak independenteak dira eta edozein ordenatan egin daitezke.

## Komandoak

Jokoaren komandoak berdinak dira bi hizkuntzetan, eta LETRA LARRIZ idatzi behar dira:

- COMPROBAR: uneko helburua egiaztatu; batzuetan aurkitutako datu bat eskatzen du.
- PISTA: laguntza mailakatua; berriro eskatuz gero, laguntza zehatzagoa.
- AYUDA: nola jokatu eta uneko helburua erakutsi.
- REINICIAR: jarduera honetako lana ezabatu eta berreraiki; berrespena eskatzen du.
- MENU: menura itzuli, lana mantenduta.
- ACTUALIZAR: argitaratutako jarduerak deskargatu, biltegia konfiguratu ondoren.
- SALIR: jokotik irten.

Menuan IDIOMA erabil daiteke hizkuntza aldatzeko. Dagoeneko sortutako
eszenatokiko fitxategien edukia ez da aldatzen: horrela ez da lana gainidazten.
Beste hizkuntzan sortzeko, aldatu hizkuntza eta berrabiarazi jarduera REINICIAR erabiliz.

Linuxeko komandoak benetakoak dira: pwd, ls, cat, cd, mkdir, cp, mv eta touch.
Fitxategien izenak berdinak dira bi hizkuntzetan. Linuxek letra larriak eta xeheak
bereizten ditu. Komandoen irteera sistemaren hizkuntzaren araberakoa da.

Aurrerapena automatikoki gordetzen da urrats bat gainditzean. Fitxategiak diskoan
daude; editore batean lanean ari bazara, gorde zure aldaketak. Jarduera osatuta ere,
praktikatzen jarrai dezakezu. MENU erabiliz beste jarduera bat aukeratu dezakezu.

## Jarduerak

1. Ongi etorri Linuxera: lehen urratsak (pwd, ls, cat).
2. Ongi etorri Linuxera: arakatu karpetak (cd, bideak, ls -a).
3. Ongi etorri Linuxera: antolatu fitxategiak (mkdir, cp, mv, touch).
4. Aurkitu birusa: ikasitakoa erabiltzeko misioa. «Birusa» testu kaltegabea da.

Eguneratzeek ez dute ikaslearen lana ezabatzen. Hasitako jarduerek beren bertsioa
mantentzen dute REINICIAR egin arte. Konexiorik gabe ere joka daiteke.
Jokoak ez du makina isolatzen: lan egin eszenatokiaren barruan eta erabili zure VM.
GitHub biltegia konfiguratzeko eta jarduerak gehitzeko, ikusi README.md eta
CREAR_ACTIVIDADES.md. Uneko bertsioa Linuxerako da, ez Windows natiborako.


## Unitateko hedapena (0.3)

Orain 10 joko eta definizioen jarduera gehigarri bat daude:

5. Galdutako agenda: data eta egutegia.
6. Nor dago agintean?: erabiltzaileak eta sistema.
7. Terminalaren liburutegia: man, info, whereis, Tab eta prompt-a.
8. Txandarako lasterbideak: aliasak sortu, probatu eta kendu.
9. Operadorearen erreleboa: historia, pasahitzen komandoa eta saiotik irten.
10. IZAR operazioa: unitateko azken misioa, 12 urratsekin.
11. Gehigarria: 27 definizio, komandoarekin erantzuteko.

Tresnak instalatzeko: `sudo apt install python3 wget ncal man-db info`.
Idatzi agindu bakoitza lerro bereizi batean. Aliasak eta historia jardueraka gordetzen dira;
REINICIAR aukerak jarduera horretakoak garbitzen ditu. Pasahitz errealak ez dira aldatzen.
Azken misioan > erabiltzen ikasiko duzu, irteera fitxategi batean gordetzeko.
Bertsio hau instalatzeko erabili eguneratzeko scripta; ACTUALIZAR aukerak ez du motorra eguneratzen.
