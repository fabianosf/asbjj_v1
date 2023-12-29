from django.shortcuts import render
from .forms import ClienteForm

def index(request):
    return render(request, 'index.html')


def contato(request):
    return render(request, 'contato.html')

''' 
# formulario de cadastro
def form_modelform(request):

    if request.method == 'GET':
        form = ClienteForm()
        context = {
            'form': form
        }
        return render(request, 'form_modelform.html', context=context)
    else:
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save()
            form = ClienteForm()
        
        context = {
            'form': form
        }
        return render(request, 'form_modelform.html', context=context)
'''

def formulario(request):

    if request.method == 'GET':
        form = ClienteForm()
        context = {
            'form': form
        }
        return render(request, 'formulario.html', context=context)
    else:
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save()
            form = ClienteForm()
        
        context = {
            'form': form
        }
        return render(request, 'formulario.html', context=context)
            
            
        
    
