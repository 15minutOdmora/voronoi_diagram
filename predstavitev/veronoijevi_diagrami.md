

# Uvod

# Zgodovina

# Jump Flood algoritem

# Delaunay triangulacija

### Delaunay definicija

Denimo, da imamo v 2D prostoru točke A, B, C, D. Ustvarimo dva trikotnika ABD in BCD, ki si delita stranico BD.
Dva trikotnika skupaj tvorita štirikotnik, katerega razpolovi njuna skupna stranica BD. Pravimo, da velja
Delaunay triangulacija, če kota, ki si nasprotujeta in nista "presekana" z stranico BD skupaj sestavljata kot, ki je 
manjši od 180 stopinj.

### Zanimive lastnosi

Na wiki viru.

## Triangulacija algoritem

### Deli in vladaj (Divide and conquer)

Algoritem deluje na principu deljenja problema na manjše pod probleme katere rekurzivno združimo skupaj, da dobimo 
končni rezultat. 

Opomba: Izračunan rezultat velja le za konveksno ogrinjačo na množici točk.

Algoritem po korakih:

Denimo, da imamo množico 10 točk, prikazano na sliki 1

![Slika 1](slike/delaunay_trig_primer_postopka/slika1.gif)

#### 1 - Urejanje točk

Točke nato uredimo po velikosti:

- Najprej po x-koordinatah
- V primeru, da imata dve točki enako x-koordinato uredimo še po y-koordinati

#### 2 - Rekurzivno polovično deljenje (Divide)

Postopoma delimo na dele ali celice, ki vsebujejo skupke največ 3 točk. 

Torej med dvema točkama, ki sta na sredini ustvarimo mejo. Nato na vsaki strani postopoek ponovimo. Ponavljamo dokler 
nam ne ostanejo celice, ki vsebujejo največ 3 točke in najmanj 2 točki.

Točke v vsaki celici povežemo skupaj, tako nastanejo trikotniki oziroma daljice med točkami.

![Slika 2](slike/delaunay_trig_primer_postopka/slika2.gif)

#### 3 - Rekurzivno Lepljenje (Merge - Conquer)

Sledi lepljenje. Celice bomo postopoma spajali skupaj, tako, da bomo ohranjali Delaunay-ovo triangulacijo. Torej bomo
ustvarjali nove povezave, katire bodo tvorile trikotnike, ki zadostiju Delaunajevemu pogoju.
Rekurzivno lepimo po istem zaporedju kot smo točke razdelili na celice.

##### 3.1 - Spajanje

Spajamo torej dve celici (ali podmnožici točk), ki sta si sosednji, imamo levo celico in desno celico pri tem za lažje
razumevanje v prihodnosti definiramo izraze za poimenovanje povezav:

- **LL** = Vse povezave iz leve celice (obe točki povezave se nahajajo v levi celici)
- **RR** = Vse povezave iz desne celice (obe točki povezave se nahajajo v desni celici)
- **LR** = Nove povezave med levo in desno celico (ena točka v levi celici druga pa v desni)

Za ohranjanje Delaunajeve triangulacije bo v določenih primerih potrebno nekatere LL in RR povezavi odstraniti (izbrisati),
nikoli pa nebomo ustvarjali novih LL ali RR povezav.

Če spojimo torej celici iz zgornje primera:

![Slika 3](slike/delaunay_trig_primer_postopka/slika3.gif)

V zgornjem primeru je bilo spajanje precej enostavno saj smo samo ustvarili nove trikotnike med dvema celicama. 

Zato si bomo na podrobnejše pogledali spajanje zgoraj nastalih celic, saj bo le to prikazalo natančen potek algoritma.

Spodnji pod-algoritem iteriramo.

**Ustvarimo bazno LR povezavo**

Bazna LR povezava je najbolj spodnja povezava med levo in desno celico, ki ne seka nobene LL ali RR povezave.

![Slika 4](slike/delaunay_trig_primer_postopka/slika4.gif)

Od tod se premikamo navzgor, da določimo naslednjo LR povezavo nad bazno povezavo. Pri tem opazimo, da bo na novo nastala
povezava sigurno vsebovala eno od dveh točk ki določajo bazno LR povezavo, druga točka pa bo vsebovana na drugi strani.

Izbiro zožamo tako, da izberemo dve kandidatni točki, eno iz leve strani, drugo iz desne strani. Začnimo z desno stranjo:
Kandidate izbiramo zaporedoma po velikosti kota, ki ga povezava med kandidatom in desno točko LR baze tvori. 

![Slika 5](slike/delaunay_trig_primer_postopka/slika5.gif)

Za vsakega potencialnega kandidata nato preverimo če zadostuje pogojem:

**I)** Kot med bazno LR povezavo in povezavo desne točke do kandidata mora biti manj kot 180 stopinj

**II)** Očrtana krožnica trikotnika ki jo tvorita obe točki bazne LR povezave in kandidata nesme vsebovati naslednjega
kandidata

![Slika 6](slike/delaunay_trig_primer_postopka/slika6.gif)

Prvi kandidat zadostuje prvemu pogoju ne pa drugemu.

Ločimo na primere, ko kandidat zadostuje:

- I. in II. veljata = Kandidat postane naš končni kandidat (izbranec)
- I. ne velja = Ne izberemo nobenega kandidata za desno stran
- I. velja II. ne velja = Izbrišemo povezavo RR, ki jo tvori desna točka bazne LR povezave in kandidatna točka

Pogoje nato izvedemo na naslednjih korakih dokler:

1) Dobimo izbranca (končnega kandidata)
2) Ugotovimo, da noben kadidat iz desne strani ne bo izbran

![Slika 7](slike/delaunay_trig_primer_postopka/slika7.gif)

Po izbrisu slabe povezave najdemo našega izbranca.

Isto storimo za levo stran kjer je postopek simetričen:

![Slika 8](slike/delaunay_trig_primer_postopka/slika8.gif)

Ob končanem postopku določanja kandidatov na obeh straneh nam ostanejo 3 možnosti:

I) Iz obeh strani nismo dobili nobenega "izbranca" = Zaključimo, spajanje je končano

II) Dobimo "izbranca" le iz ene strani = Izbranca oz. točko povežemo z točko bazne LR povezave, ki se nahaja na drugi strani

III) Dobimo oba "izbranca" = Primerna LR povezava je izbrana glede na spodnji test:

Če desni izbranec ni vsebovan v notranjosti očrtanega kroga, ki ga določa trikotnik bazne LR povezave in levega izbranca:
    
Levi izbranec določa novo povezavo med njim in desno točko bazne LR povezave. 

Nasprotno velja za levega izbranca (če levi ni vsebovan, desni določa novo povezavo)

Po zagotovljenem obstoju Delaunajeve triangulacije bo vsaj eden zadostoval zgornjemu pogoju.

Po unikatnosti Del. triangulacije bo natanko eden zadostoval pogoju (razen v primeru, ko so 4 točke ko-planarne).

![Slika 9](slike/delaunay_trig_primer_postopka/slika9.gif)

Enkrat, ko je nova povezava dodana je celoten proces ponovljen tako, da nova povezava postane bazna LR povezava.

Če ponovimo postopek, do konca:

![Slika 10](slike/delaunay_trig_primer_postopka/slika10.gif)

Tako dobimo našo končno Delaunajovo triangulacijo:

![Končna triangulacija](slike/delaunay_trig_primer_postopka/final_delaunay.gif)

# Kako povezati točke

# Primer v drugih metrikah

# Primeri uporabe
