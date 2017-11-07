from django.shortcuts import render


def landing(request):
    name = "Yaroslav"
    return  render(request,'HomePage.html',locals())