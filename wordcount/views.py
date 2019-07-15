from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
	return render(request, 'home.html', {'name': 'Hi Adnan'})
	
def count(request):
	data = request.GET['FTextArea']
	print(data)
	wordlist = data.split()
	C = len(wordlist)
	
	worddictionary = {}
	for word in wordlist:
		if word in worddictionary:
			worddictionary[word] += 1
		else:
			worddictionary[word] = 1
			
	
	return render(request, 'count.html' , {'text': data , 'words': C , 'worddictionary' : worddictionary})

def contact(request):
	return HttpResponse('<h1> This is contact page. </h1> <br> Welcome to Contact Page.')