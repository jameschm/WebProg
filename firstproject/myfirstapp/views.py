from django.shortcuts import render



# Create your views here.
def index(request):
    return render(request, 'myfirstapp/index.html')

def formulaire(request):
    return render(request, 'myfirstapp/formulaire.html')

def main(request):
    return render(request, 'myfirstapp/main.html')

def bonjour(request):
    nom=request.GET["nom"]
    return render(request,'myfirstapp/bonjour.html',{"nom":nom}) 

def traitement(request):
    lform = LivreForm(request.POST)
    if lform.is_valid():
        livre = lform.save()
        return render(request,"/bibliotheque/affiche.html",{"livre" : livre})
    else:
        return render(request,"bibliotheque/ajout.html",{"form": lform})
    
def ajout(request):
    # Your view logic here
    return render(request, 'myfirstapp/ajout.html')

