from django.shortcuts import render
from googletrans import Translator
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'index.html')


def translator(request):
    # this is django remove punciations logics start
    # get the text
    djangoText = request.GET.get('text', 'default')
    # get checkbox value
    removePuncation = request.GET.get('removePuncation', 'off')
    fullcaps = request.GET.get('capitalize', 'off')
    newlineremover = request.GET.get('newlineRemover', 'off')
    extraspaceremover = request.GET.get('extraspaceremover', 'off')
    print(djangoText)
    print(removePuncation)
    text = request.GET.get('text')
    lang = request.GET.get('lang')
    print('text', text, 'lang', lang)
    # connect the translator
    translator = Translator()
    # detect language
    dt = translator.detect(text)
    dt2 = dt.lang
    # translate the text
    if removePuncation == "on":
        punctuations = '''!()-[]{};:'"\<>/?@#$%^&*_~'''
        text = ""
        for char in djangoText:
            if char not in punctuations:
                text = text + char
        translated = translator.translate(text, lang)
        tr = translated.text
        context = {'translated': tr, 'lang': dt2, 't_lang': lang,
                   'purpose': 'Removed Punctuations excepts dot or semiclon'}
        return render(request, 'transleted.html', context)

    elif fullcaps == "on":
        text = ""
        for char in djangoText:
            text = text + char.upper()
        translated = translator.translate(text, lang)
        tr = translated.text
        context = {'translated': tr, 'lang': dt2, 't_lang': lang,
                   'purpose': 'changed to uppercase'}
        return render(request, 'transleted.html', context)

    elif newlineremover == "on":
        text = ""
        for char in djangoText:
            if char != "\n":
                text = text + char
        translated = translator.translate(text, lang)
        tr = translated.text
        context = {'translated': tr, 'lang': dt2, 't_lang': lang,
                   'purpose': 'New line has been removed!'}
        return render(request, 'transleted.html', context)

    elif extraspaceremover == "on":
        text = ""
        for index, char in enumerate(djangoText):
            if djangoText[index] == " " and djangoText[index + 1] == " ":
                pass
            else:
                text = text + char
        translated = translator.translate(text, lang)
        tr = translated.text
        context = {'translated': tr, 'lang': dt2, 't_lang': lang,
                   'purpose': 'Extra space has been removed!'}
        return render(request, 'transleted.html', context)

    else:
        translated = translator.translate(text, lang)
        tr = translated.text
        context = {'translated': tr, 'lang': dt2, 't_lang': lang}
        return render(request, 'transleted.html', context)
