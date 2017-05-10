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

class Zawodnik(models.Model):
    class Meta:
        verbose_name_plural = "Zawodnicy"
    zespol = models.ForeignKey(Zespol,on_delete=models.CASCADE)
    imie = models.CharField(max_length=50)
    nazwisko = models.CharField(max_length=50)
    pozycja = models.CharField(max_length=50)
    data_urodzenia = models.DateField('data published')

    def __unicode__(self):
        return self.imie +" "+ self.nazwisko

class Mecz(models.Model):
    class Meta:
        verbose_name_plural = "Mecze"
    zespol_gospodarz = models.ForeignKey(Zespol, on_delete=models.CASCADE, related_name="rola_gospodarza")
    zespol_gosc = models.ForeignKey(Zespol, on_delete=models.CASCADE, related_name="rola_goscia")
    data = models.DateField('data published')
    bramki_gospodarz = models.IntegerField(default=0)
    bramki_gosc = models.IntegerField(default=0)
    kolejka = models.IntegerField(default=0)

    def __unicode__(self):
        return "Kolejka " + str(self.kolejka) +": "+ str(self.zespol_gospodarz) +" "+ str(self.bramki_gospodarz)+" "+ str(self.zespol_gosc) +" "+ str(self.bramki_gosc)

class TypZdarzenia(models.Model):
    class Meta:
        verbose_name_plural = "Akcja"
    nazwa = models.CharField(max_length=50)

class Zdarzenie(models.Model):
    mecz = models.ForeignKey(Mecz, on_delete=models.CASCADE)
    zawodnik = models.ForeignKey(Zawodnik, on_delete=models.CASCADE)
    minuta = models.IntegerField(default=0)
    typ_zdarzenia = models.ForeignKey(TypZdarzenia, on_delete=models.CASCADE)






