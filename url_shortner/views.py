from django.shortcuts import render,redirect, get_object_or_404
from .models import URL
from django.http import JsonResponse
from django.db import IntegrityError
import hashlib

# Create your views here.
def hash_url(request):
    error_message = None
    if request.method == 'POST':
        original_url = request.POST.get('original_url')
        hashed_url = hashlib.sha256(original_url.encode()).hexdigest()[:10]
        try:
            new_url = URL.objects.create(original_url=original_url, hashed_url=hashed_url)
            return render(request, 'url_shortner/hash_url.html', {'hashed_url': new_url.hashed_url})
        except IntegrityError:
            error_message = "This URL already exists."

    return render(request, 'url_shortner/hash_url.html', {'error_message': error_message})

def redirect_to_original(request, hashed_url):
    url = get_object_or_404(URL, hashed_url=hashed_url)
    url.clicks += 1
    url.save()
    return redirect(url.original_url)