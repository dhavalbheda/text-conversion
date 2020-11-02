from django.http import HttpResponse
from django.shortcuts import render
from utils import removePuncuation

def index(request):
    text = request.POST.get('oldText','') 
    return render(request,'index.html',{'text':text})

def analyze(request):
    text = request.POST.get('text','default') 
    removePunc = request.POST.get('punctuation','off') 
    case = request.POST.get('case','default')
    space = request.POST.get('extraSpace','off')
    newline = request.POST.get('newline','off')
    
    newText = removePuncuation({
                'text': text,
                'case': case,
                'removePunc': removePunc,
                'space': space,
                'newline': newline})
    params = {
        'oldText': text,
        'newText': newText,
        'count': len(newText)
    }
    return render(request, 'analyze.html',params)
