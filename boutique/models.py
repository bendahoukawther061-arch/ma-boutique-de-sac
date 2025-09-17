from django.db import models

# Your Sac model
class Sac(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='sacs/')
    def __str__(self):
        return self.nom

# The new SacImage model
class SacImage(models.Model):
    sac = models.ForeignKey(Sac, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='sacs_images/')
    couleur = models.CharField(max_length=50)

    def __str__(self):
        return f"Image de {self.sac.nom} ({self.couleur})"