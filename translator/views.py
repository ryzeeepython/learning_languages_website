from django.shortcuts import render
from django.http import HttpResponse
from translator.forms import Form
from . import translate

def index(request):
    Translator = translate.Translate()
    context = {}
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            translation = Translator.translate(str(form.cleaned_data['text']), str(form.cleaned_data['language']))
            context = {'success': 1, 'translation': translation}    
    else:
        form = Form()
    context['form']  = form

    return render(request, 'translator/index.html', context = context)

 