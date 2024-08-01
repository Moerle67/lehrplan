from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profession(models.Model):
    designation = models.CharField(("Bezeichnug"), max_length=250)
    abbreviation = models.CharField(("Abkürzung"), max_length=10)
    time = models.IntegerField(("Dauer (Monate)"), default=24)
    comment = models.TextField(("Kommentar"), blank=True, null=True)

    class Meta:
        verbose_name = ("Beruf")
        verbose_name_plural = ("Berufe")

    def __str__(self):
        return f"{self.abbreviation} - {self.designation}"

    #def get_absolute_url(self):
    #    return reverse("Beruf_detail", kwargs={"pk": self.pk})

class Lernfeld(models.Model):
    nummer = models.CharField(("Nummer"), max_length=10)
    designation = models.CharField(("Bezeichnung"), max_length=250)
    content = models.TextField(("Beschreibung"))
    profession = models.ForeignKey(Profession, verbose_name=("Beruf"), on_delete=models.RESTRICT)
    time1 = models.IntegerField(("UE 1. Lehrjahr"), default=0)
    time2 = models.IntegerField(("UE 2. Lehrjahr"), default=0)
    time3 = models.IntegerField(("UE 3. Lehrjahr"), default=0)
    

    class Meta:
        verbose_name = ("Lernfeld")
        verbose_name_plural = ("Lernfelder")

    def __str__(self):
        return f"LF: {self.nummer} - {self.designation} ({self.profession.abbreviation})"

    #def get_absolute_url(self):
    #    return reverse("Lernfeld_detail", kwargs={"pk": self.pk})

class Thema(models.Model):
    name = models.CharField(("Thema"), max_length=50)
    description = models.TextField(("Beschreibung"))
    

    def __str__(self):
        return self.name

#    def get_absolute_url(self):
#        return reverse("Thema_detail", kwargs={"pk": self.pk})

class Lerneinheit(models.Model):
    name = models.CharField(("Bezeichnung"), max_length=50)
    field = models.ForeignKey(Thema, verbose_name=("Thema"), on_delete=models.CASCADE)
    description = models.TextField(("Beschreibung"))
    author = models.ForeignKey(User, verbose_name=("Autor"), on_delete=models.SET_NULL, null=True, related_name="author")
    lernfeld = models.ManyToManyField(Lernfeld, verbose_name=("Lernfelder"))
    time = models.IntegerField(("Unterichtseinheiten"), default=5)
    possible = models.ManyToManyField(User, verbose_name=("mögliche Ausbilder"), related_name="possib")
    class Meta:
        verbose_name = ("Lerneinheit")
        verbose_name_plural = ("Lerneinheiten")

    def __str__(self):
        return f"{self.name}/{self.author} ({self.time}h)"

    #def get_absolute_url(self):
    #    return reverse("Lerneinheit_detail", kwargs={"pk": self.pk})

