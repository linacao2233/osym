from django.shortcuts import render
from django.http import HttpResponse

# from .models import Sentence,Chapter

# Create your views here.

# def index(request):
# 	template = 'main/index.html'

# 	#sentences = Sentence.objects.all().order_by('chapter')
# 	chapters = Chapter.objects.filter(article=
# 		'second').order_by('order')

# 	context= {
# 	#'sentences': sentences,
# 	'chapters': chapters,
# 	}

# 	return render(request, template, context)

# def savesentence(request):
# 	"""
# 	save the translated part
# 	"""
# 	# sentence = Sentence.objects.get(pk=pk)
# 	if request.POST:
# 		pk = request.POST.get('pk')
# 		sentence = Sentence.objects.get(pk=pk)
# 		sentence.English = request.POST.get('English')
# 		sentence.save()
# 	else:
# 		return HttpResponse('no post data')

# 	return HttpResponse('saved')
	

# def chinesepage(request):
# 	template = 'main/chinesepage.html'
# 	chapters = Chapter.objects.filter(article=
# 		'second').order_by('order')

# 	# chapters = Chapter.objects.all().order_by('order')

# 	context= {
# 	'chapters': chapters,
# 	}

# 	return render(request, template, context)
