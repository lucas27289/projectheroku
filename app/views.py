from django.shortcuts import get_list_or_404, render
from .models import Datos


# Create your views here.
def datos(request):
    datos = get_list_or_404(Datos.objects.all())
    return render(request,'app/datos.html', { 'datos': datos })
    
def index(request):
    return render(request, 'app/index.html')