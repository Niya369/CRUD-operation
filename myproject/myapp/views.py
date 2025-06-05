
# Create your views here.
from django.shortcuts import render
from .forms import NameForm

def get_name(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            return render(request, 'myapp/thanks.html', {'name': name})
    else:
        form = NameForm()
    return render(request, 'myapp/name.html', {'form': form})
