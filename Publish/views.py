from django.shortcuts import render, redirect
from .models import Ebook
from .forms import EbookForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def publish_ebook(request):
    if request.method == 'POST':
        form = EbookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EbookForm()
    return render(request, 'publish_ebook.html', {'form': form})