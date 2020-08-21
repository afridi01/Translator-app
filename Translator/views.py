from django.shortcuts import render
from googletrans import Translator


# Create your views here.
def index(request):
    return render(request, 'index.html')


def analyze(request):
    djangoText = request.GET.get('text', 'default')
    removePuncation = request.GET.get('removePuncation', 'off')
    print(removePuncation)
    print(djangoText)
    # analyzed = djangoText
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    analyzed = ""
    for char in djangoText:
        if char not in punctuations:
            analyzed = analyzed + char

        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    else:
        return HttpResponse('Error')


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
    context = {'translated': tr, 'lang': dt2, 't_lang': lang}

    return render(request, 'transleted.html', context)
