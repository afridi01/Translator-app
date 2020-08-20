from django.shortcuts import render
from googletrans import Translator


# Create your views here.
def index(request):
    return render(request, 'index.html')


def translator(request):
    text = request.GET.get('text')
    lang = request.GET.get('lang')
    print('text', text, 'lang', lang)

    # connect the translator
    translator = Translator()
    # detect language
    dt = translator.detect(text)
    dt2 = dt.lang
    # translate the text
    translated = translator.translate(text, lang)
    tr = translated.text
    context = {'translated': tr, 'lang': dt2, 't_lang':lang }

    return render(request, 'transleted.html', context)
