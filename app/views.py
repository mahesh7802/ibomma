from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request,'main.html')
def home(request):
    return render(request,'home.html')
def enter(request):
    return render(request,'enter.html')