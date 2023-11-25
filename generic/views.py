from django.shortcuts import render

# Create your views here.
def tamil(request):
    return render(request,'tamil.html')
def english(request):
    return render(request,'english.html')