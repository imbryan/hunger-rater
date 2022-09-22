from django.shortcuts import render


def hungerrater(request):
    return render(request, 'hungerrater.html', context={})
