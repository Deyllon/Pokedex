from django.db import models

class Pokemon(models.Model):
    foto_pokemon = models.ImageField(upload_to='fotos/%d%m%Y', blank=False)
    nome = models.CharField(max_length=100, blank=False, null=False)
    slug = models.SlugField()
    numero_pokedex = models.CharField(max_length=100, blank=False, null=False)
    habilidade1 = models.CharField(max_length=100, blank=False, null=False)
    habilidade2 = models.CharField(max_length=100, blank=True, null=True)
    altura = models.FloatField(blank=False, null=False)
    status_hp = models.CharField(max_length=100, blank=False, null=False)
    status_ataque = models.CharField(max_length=100, blank=False, null=False)
    status_defesa = models.CharField(max_length=100, blank=False, null=False)
    status_ataque_especial = models.CharField(max_length=100, blank=False, null=False)
    status_defesa_especial = models.CharField(max_length=100, blank=False, null=False)
    status_velocidade = models.CharField(max_length=100, blank=False, null=False)
    tipo1 = models.CharField(max_length=100, blank=False, null=False)
    tipo2 = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return self.nome