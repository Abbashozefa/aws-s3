from django.shortcuts import render
from django.http import HttpResponse
from .forms import UploadFileForm

# Create your views here.
def page(request):
    return HttpResponse('hi')
def page2(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST)
        
    else:
        form = UploadFileForm()
    return render(request, 'index.html', {'form': form})
    
