from django.shortcuts import render
from ..myfirstapp.forms import LivreForm
from . import models
def ajout(request):
    if request.method == "POST": 
        form = LivreForm(request)
        if form.is_valid(): 
            livre = form.save() 
        
            return render(request,"/bibliotheque/affiche.html",{"livre" : livre}) 

        else:
            return render(request,"bibliotheque/ajout.html",{"form": form})
    else :
        form = LivreForm() 
        return render(request,"bibliotheque/ajout.html",{"form" : form})

def traitement(request):
    lform = LivreForm(request.POST)
    if lform.is_valid():
        livre = lform.save()
        return render(request,"/bibliotheque/affiche.html",{"livre" : livre})
    else:
        return render(request,"bibliotheque/ajout.html",{"form": lform})