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

def read(request, id):
    # Your logic to retrieve and display the data with the given ID
    return render(request, 'myfirstapp/read.html')

def affiche(request, id):
    livre = models.Livre.objects.get(pk=id) 
    return render(request,"bibliotheque/affiche.html",{"livre": livre})

def update(request, id):
    # Your view logic here
    return render(request, 'myfirstapp/update.html')

def traitementupdate(request, id):
    lform = LivreForm(request.POST)
    if lform.is_valid():
        livre = lform.save(commit=False) 
        livre.id = id; 
        livre.save() 
        return HttpResponseRedirect("/bibliotheque/") 
    else:
        return render(request, "bibliotheque/update.html", {"form": lform, "id": id})




