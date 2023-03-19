from django.shortcuts import render

# Create your views here.
def noori(request):
    return render(request,'noori.html')

def baba(request):
    return render(request,'baba.html')