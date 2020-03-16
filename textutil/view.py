from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    utext = request.POST.get('textin', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    tupper = request.POST.get('upper', 'off')
    tlower = request.POST.get('lower', 'off')
    removenewl = request.POST.get('removenewl', 'off')
    removeextras = request.POST.get('removeextras', 'off')

    if removepunc == "on":
        atext = ""
        punc = '''!()-{}[];:'"\,<>./?|~`@#$%^&*_'''
        for char in utext:
            if char not in punc:
                atext = atext + char
        utext = atext
        para = {'purpose': 'Remove Puctuations', 'analyzed': atext}

    if tupper == "on":
        atext = ""
        for char in utext:
            atext = atext + char.upper()
        utext = atext
        para = {'purpose': 'Upper Case', 'analyzed': atext}

    if tlower == "on":
        atext = ""
        for char in utext:
            atext = atext + char.lower()
        utext = atext
        para = {'purpose': 'Lower Case', 'analyzed': atext}

    if removenewl == "on":
        atext = ""
        for char in utext:
            if char != "\n" and char != "\r":
                atext = atext + char
        utext = atext
        para = {'purpose': 'Remove New Lines', 'analyzed': atext}

    if removeextras == "on":
        atext = ""
        for ind, char in enumerate(utext):
            if not (utext[ind] == " " and utext[ind + 1] == " "):
                atext = atext + char
        utext = atext
        para = {'purpose': 'Remove Extra Spaces', 'analyzed': atext}

    if removepunc != "on" and removeextras != "on" and removenewl != "on" and tlower != "on" and tupper != "on":
        return HttpResponse("Error")

    return render(request, 'analyze.html', para)


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')
