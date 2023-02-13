from django.shortcuts import render

# Create your views here.
def inicioDef(request):
    return render(request,"index.html",{})

