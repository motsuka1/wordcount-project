from django.http import HttpResponse
from django.shortcuts import render #to get ascess to html files
import operator

def homepage(request): #when someone looks for this home page, it will send this request. Which url they are looking
    return render(request, "home.html") #access to home.html #{} can run python script ex) {"hithere": "This is me"}

# def eggs(request):
#     return HttpResponse("<h1>Eggs are great</h1>")

def count(request):
    fulltext = request.GET["fulltext"] #refers to textare in home.html

    wordlist = fulltext.split()

    worddictionary = {}

    for word in wordlist:
        if word in worddictionary:
            #increase
            worddictionary[word] += 1 #adding word and number in the worddictionary

        else:
            #add to the worddictionary
            worddictionary[word] = 1

        sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, "count.html", {"fulltext": fulltext, "count": len(wordlist), "sortedwords": sortedwords}) #first fulltext refers to the one in count.html and second one is one line above

def about(request):
    return render(request, "about.html")
