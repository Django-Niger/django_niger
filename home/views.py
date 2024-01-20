from django.shortcuts import render


# Create your views here.
def landing_page(request):
    # Ajoutez ici la logique pour récupérer les données nécessaires, si nécessaire
    return render(request, "landing_page.html")
