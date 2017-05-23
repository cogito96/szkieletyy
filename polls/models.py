from django.db import models

class Zespol(models.Model):
    class Meta:
        verbose_name_plural = "Zespoly"
    nazwa_klubu = models.CharField(max_length=50)
    trener = models.CharField(max_length=50)
    prezes = models.CharField(max_length=50)
    strona_internetowa = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nazwa_klubu

    def licz_punkty(self):
      mecze=Mecz.objects.all()
      punkty = 0
      bramki_stracone = 0
      bramki_strzelone = 0
      for m in mecze:
        if self==m.zespol_gospodarz:
            if m.bramki_gospodarz>m.bramki_gosc:
               punkty+=3
               bramki_stracone += m.bramki_gosc
               bramki_strzelone += m.bramki_gospodarz
            if m.bramki_gospodarz==m.zespol_gosc:
               punkty+=1
               bramki_stracone += m.bramki_gosc
               bramki_strzelone += m.bramki_gospodarz
        if self==m.zespol_gosc:
            if m.bramki_gospodarz<m.bramki_gosc:
               punkty+=3
               bramki_strzelone += m.bramki_gosc
               bramki_stracone += m.bramki_gospodarz
            if m.bramki_gospodarz==m.zespol_gosc:
               punkty+=1
               bramki_strzelone += m.bramki_gosc
               bramki_stracone += m.bramki_gospodarz
      return [punkty, bramki_strzelone, bramki_stracone]


class Zawodnik(models.Model):
    class Meta:
        verbose_name_plural = "Zawodnicy"
    zespol = models.ForeignKey(Zespol,on_delete=models.CASCADE)
    imie = models.CharField(max_length=50)
    nazwisko = models.CharField(max_length=50)
    pozycja = models.CharField(max_length=50)
    data_urodzenia = models.DateField('data urodzenia')

    def __unicode__(self):
        return self.imie +" "+ self.nazwisko

    def liczz (self):
        zdarzenie = Zdarzenie.objects.all()
        ile_fauli=0
        ile_zoltych_kartek=0
        ile_czerwonych_kartek=0
        strzaly=0
        gole=0
        for z in zdarzenie:
            if self == z.zawodnik:
                if z.typ_zdarzenia.nazwa =="Bramka":
                    gole+=1
                if z.typ_zdarzenia.nazwa =="Faul":
                    ile_fauli+=1
                if z.typ_zdarzenia.nazwa =="Zolta kartka":
                    ile_zoltych_kartek+=1
                if z.typ_zdarzenia.nazwa == "Czerwona kartka":
                    ile_czerwonych_kartek+=1
                if z.typ_zdarzenia.nazwa =="Strzal na bramke":
                    strzaly+=1
        return [gole,self.zespol,self.imie,self.nazwisko,gole,strzaly,ile_fauli,ile_zoltych_kartek,ile_czerwonych_kartek]

class Mecz(models.Model):
    class Meta:
        verbose_name_plural = "Mecze"
    zespol_gospodarz = models.ForeignKey(Zespol, on_delete=models.CASCADE, related_name="rola_gospodarza")
    zespol_gosc = models.ForeignKey(Zespol, on_delete=models.CASCADE, related_name="rola_goscia")
    data = models.DateField('data rozegrania')
    bramki_gospodarz = models.IntegerField(default=0)
    bramki_gosc = models.IntegerField(default=0)
    kolejka = models.IntegerField(default=0)

    def __unicode__(self):
        return "Kolejka " + str(self.kolejka) +": "+ str(self.zespol_gospodarz) +" "+ str(self.bramki_gospodarz)+" "+ str(self.zespol_gosc) +" "+ str(self.bramki_gosc)


    def licz (self):
        lista_statystyk_dom=[]
        lista_statystyk_wyjazd=[]
        zdarzenia = Zdarzenie.objects.all()
        zawodnicy= Zawodnik.objects.all()
        jestem_dom= False
        jestem_wyjazd=False
        for zawodnik in zawodnicy:
            ile_fauli=0
            ile_zoltych_kartek=0
            strzaly=0
            gole=0
            ile_czerwonych_kartek=0
            jestem_dom=False
            jestem_wyjazd=False
            if self.zespol_gospodarz == zawodnik.zespol:
                jestem_dom=True
            if self.zespol_gosc == zawodnik.zespol:
                jestem_wyjazd=True
            for zdarzenie in zdarzenia:
                if self == zdarzenie.mecz:
                    if zdarzenie.zawodnik == zawodnik :
                        if zdarzenie.typ_zdarzenia.nazwa =="Bramka":
                            gole+=1
                        if zdarzenie.typ_zdarzenia.nazwa =="Faul":
                            ile_fauli+=1
                        if zdarzenie.typ_zdarzenia.nazwa =="Zolta kartka":
                            ile_zoltych_kartek+=1
                        if zdarzenie.typ_zdarzenia.nazwa == "Czerwona kartka":
                            ile_czerwonych_kartek+=1
                        if zdarzenie.typ_zdarzenia.nazwa =="Strzal na bramke":
                            strzaly+=1
            if  jestem_dom == True:
                lista_dom=[zawodnik.imie,zawodnik.nazwisko,gole,strzaly,ile_fauli,ile_zoltych_kartek,ile_czerwonych_kartek]
                lista_statystyk_dom.append(lista_dom)
            if  jestem_wyjazd == True:
                lista_wyjazd=[zawodnik.imie,zawodnik.nazwisko,gole,strzaly,ile_fauli,ile_zoltych_kartek,ile_czerwonych_kartek]
                lista_statystyk_wyjazd.append(lista_wyjazd)
        return [{'gospodarz':lista_statystyk_dom},{'gosc':lista_statystyk_wyjazd}]

    def statystyki (self):
        zdarzenia = Zdarzenie.objects.all()
        ile_faul_dom=0
        ile_zoltych_kartek_dom=0
        strzaly_dom=0
        gole_dom=0
        ile_czerwonych_kartek_dom=0
        ile_faul_wyjazd=0
        ile_zoltych_wyjazd=0
        strzaly_wyjazd=0
        gole_wyjazd=0
        ile_czerwonych_kartek_wyjazd=0
        for z in zdarzenia:
            if z.mecz == self:
                if self.zespol_gospodarz ==z.zawodnik.zespol:
                    if z.typ_zdarzenia.nazwa =="Bramka":
                        gole_dom+=1
                    if z.typ_zdarzenia.nazwa =="Faul":
                        ile_faul_dom+=1
                    if z.typ_zdarzenia.nazwa =="Zolta kartka":
                        ile_zoltych_kartek_dom+=1
                    if z.typ_zdarzenia.nazwa == "Czerwona kartka":
                        ile_czerwonych_kartek_dom+=1
                    if z.typ_zdarzenia.nazwa =="Strzal na bramke":
                        strzaly_dom+=1
                if self.zespol_gosc == z.zawodnik.zespol:
                    if z.typ_zdarzenia.nazwa =="Bramka":
                        gole_wyjazd+=1
                    if z.typ_zdarzenia.nazwa =="Faul":
                        ile_faul_wyjazd+=1
                    if z.typ_zdarzenia.nazwa =="Zolta kartka":
                        ile_zoltych_kartek_wyjazd+=1
                    if z.typ_zdarzenia.nazwa == "Czerwona kartka":
                        ile_czerwonych_kartek_wyjazd+=1
                    if z.typ_zdarzenia.nazwa =="Strzal na bramke":
                        strzaly_wyjazd+=1
        gole=[gole_dom,gole_wyjazd]
        strzaly=[strzaly_dom,strzaly_wyjazd]
        ile_fauli=[ile_faul_dom,ile_faul_wyjazd]
        ile_zoltych_kartek=[ile_zoltych_kartek_dom,ile_zoltych_wyjazd]
        ile_czerwonych_kartek=[ile_czerwonych_kartek_dom,ile_czerwonych_kartek_wyjazd]
        return[gole,strzaly,ile_fauli,ile_zoltych_kartek,ile_czerwonych_kartek]


class TypZdarzenia(models.Model):
    class Meta:
        verbose_name_plural = "Akcja"
    nazwa = models.CharField(max_length=50)

    def __unicode__(self):
        return self.nazwa

class Zdarzenie(models.Model):
    mecz = models.ForeignKey(Mecz, on_delete=models.CASCADE)
    zawodnik = models.ForeignKey(Zawodnik, on_delete=models.CASCADE)
    minuta = models.IntegerField(default=0)
    typ_zdarzenia = models.ForeignKey(TypZdarzenia, on_delete=models.CASCADE)


    class Meta:
        verbose_name_plural = "Zdarzenie"


    def __unicode__(self):
        return str(self.zawodnik)+" "+str(self.typ_zdarzenia)






