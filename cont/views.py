from django.shortcuts import render
from django.utils import timezone
from .models import SumasYSaldos

# Create your views here.
def base(request):
    return render(request, 'pages/base.html', {})
def front(request):
    return render(request, 'pages/front.html', {})

def balance0(request):
    #balance = SumasYSaldos.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

	result = SumasYSaldos.objects.raw('SELECT * FROM sumas_y_saldos WHERE debe > 0 OR haber > 0')
	#result = SumasYSaldos.objects.all()
	return render(request, 'pages/balance0.html', {'results': result})
