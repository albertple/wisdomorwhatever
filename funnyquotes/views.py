from django.shortcuts import render
from funnyquotes.models import *
#from random import randrange

# Create your views here.
def index(request):
	famous_quote = FamousQuote.objects.order_by('?')[:1]
	infamous_quote = InfamousQuote.objects.order_by('?')[:1]

	compiled = [famous_quote[0], infamous_quote[0]]

	return render(request, 'funnyquotes/index.html', {'compiled': compiled})

	#context2 = {'something': something }
	#context = {'famous_quote_list': famous_quote_list}
	# compiled_quote = [famous_quote_list, infamous_quote_list]
	# Doesn't work
	#compiled_quote = famous_quote_list[randrange(len(famous_quote_list))]

	# tried, but returnes DoesNotExist a lot
	#something = FamousQuote.objects.get(pk=randrange(0, len(FamousQuote.objects.all())-1))
	
	# works \\something = FamousQuote.objects.all().order_by('?')[:1]

	#return HttpResponse("This will be the funny quotes page")