from django.shortcuts import render, get_object_or_404
from .models import Sac

def liste_sacs(request):
    sacs = Sac.objects.all()
    return render(request, 'boutique/liste_sacs.html', {'sacs': sacs})

def detail_sac(request, sac_id):  # <-- Ajoutez cette fonction
    sac = get_object_or_404(Sac, pk=sac_id)
    return render(request, 'boutique/detail_sac.html', {'sac': sac})