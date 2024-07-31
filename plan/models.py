from django.db import models

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

