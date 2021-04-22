from django.shortcuts import render

# Create your views here.
def gridfunction(request):
    return render(request,'grid.html')
