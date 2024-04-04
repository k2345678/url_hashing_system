from django.shortcuts import render, redirect, get_object_or_404
from .models import URL
from .forms import URLForm
from django.db import IntegrityError
import hashlib

from django.shortcuts import render, redirect, get_object_or_404
from .models import URL
from .forms import URLForm
from django.db import IntegrityError
import hashlib

from django.shortcuts import render, redirect, get_object_or_404
from .models import URL
from .forms import URLForm
from django.db import IntegrityError
import hashlib

def hash_url(request):
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            original_url = form.cleaned_data['original_url']
            hashed_url = hashlib.sha256(original_url.encode()).hexdigest()[:10]
            try:
                new_url = URL.objects.create(original_url=original_url, hashed_url=hashed_url)
                return render(request, 'url_shortner/hash_url.html', {'hashed_url': new_url.hashed_url})
            except IntegrityError:
                error_message = "This URL already exists."
                request.session['error_message'] = error_message 
                return redirect('hash_url')  
        else:
            error_message = "Please provide a valid URL."
            request.session['error_message'] = error_message 
            return redirect('hash_url') 
    form = URLForm()

    error_message = request.session.pop('error_message', None) 

    return render(request, 'url_shortner/hash_url.html', {'form': form, 'error_message': error_message})


def redirect_to_original(request, hashed_url):
    url = get_object_or_404(URL, hashed_url=hashed_url)
    url.clicks += 1
    url.save()
    return redirect(url.original_url)
