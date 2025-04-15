from django.db import models
from django.urls import reverse

# Create your models here.
class Beruf(models.Model):
    short = models.CharField(("Kürzel"), max_length=10)
    description = models.TextField(("Beschreibung"))

    class Meta:
        verbose_name = ("Beruf")
        verbose_name_plural = ("Berufe")

    def __str__(self):
        return f"{self.short}/{self.description}"

    def get_absolute_url(self):
        return reverse("Beruf_detail", kwargs={"pk": self.pk})


class Lehrplan(models.Model):
    profession = models.ManyToManyField(Beruf, verbose_name="Beruf")
    lernfeld = models.CharField(("Lernfeld"), max_length=10)
    description = models.TextField(("Beschreibung"))
    year = models.IntegerField(("Jahr"), default=1)
    duration = models.IntegerField(("Dauer"), default=30)
    kernkompetenz = models.TextField(("Kernkompetenz"))

    class Meta:
        verbose_name = "Lehrplan"
        verbose_name_plural = "Lehrpläne"
        ordering = ["lernfeld"]

    def __str__(self):
        return f"{self.lernfeld} - {self.description}"

    def get_absolute_url(self):
        return reverse("Lehrplan_detail", kwargs={"pk": self.pk})

class LPDetail(models.Model):
    plan = models.ForeignKey(Lehrplan, verbose_name=("Lernfeld"), on_delete=models.CASCADE)
    aim = models.TextField(("kompetenzbasierte Ziele"))
    congrete = models.TextField(("Konkretisierung"), blank=True, null=True)
    situation = models.TextField(("Lernsituation"))
    result = models.CharField(("Handlungsergebnis"), max_length=50)
    competence = models.TextField("überfachliche Kompetenzen")
    notes = models.CharField(("Hinweise"), max_length=50)
    time = models.IntegerField(("Zeit"))

    class Meta:
        verbose_name = "LPDetail"
        verbose_name_plural = "LPDetails"
        ordering = ["plan", "situation", ]

    def __str__(self):
        return f"{self.plan} - {self.situation}"

    def get_absolute_url(self):
        return reverse("LPDetail_detail", kwargs={"pk": self.pk})
