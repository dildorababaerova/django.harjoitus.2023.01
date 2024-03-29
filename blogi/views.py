from django.shortcuts import redirect, render
from .models import Postaus
from django.urls import reverse


def postaukset(request):
    #postaukset = ["eka", "toka"]
    postaukset = Postaus.objects.all()

    context = {"postaukset": postaukset}
    return render(
        request,
         "blogi/postauslista.html",
         context,
         )


def nayta_postaus(request, id):
    postaus = Postaus.objects.get(id=id)
    context = {"postaus": postaus}
    return render(request, "blogi/postaus.html", context)


def uusi_postaus(request):
    if request.method == "GET":
        # 1.Lomake näytetään ensimmäisenä kertaa
        return render(request, "blogi/uusi_postaus.html")
    
    elif request.method == "POST":
        #2. Käyttäjä täytti ja lahetti lomakkeen

        # Luetaan lomakkeen tiedot POST-datasta
        otsikko = request.POST["otsikko"]
        teksti = request.POST['teksti']

        #Luodaan uusi postaus-objekti tietokantaan
        postaus = Postaus.objects.create(
            otsikko=otsikko,
            teksti=teksti,

        )
        #Muodostetaan URL-osoite luotuun Postaus_objektiin
        url = reverse('nayta_postaus', args=(postaus.id,))

        #Palautetaan uudelleenohjaus uuden Postaus- objektin URL:iin
        return redirect(url)
    
    

