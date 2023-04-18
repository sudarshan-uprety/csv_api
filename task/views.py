from django.shortcuts import render,HttpResponse

# Create your views here.
from django.shortcuts import render
from .forms import MyModelForm
import csv
from .models import MyModel

def data_upload(request):
    if request.method == 'POST':
        form = MyModelForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_files']
            decoded_file = csv_file.read().decode('utf-8').splitlines()
            reader = csv.DictReader(decoded_file)
            for row in reader:
                MyModel.objects.create(
                    name=row['name'],
                    email=row['email'],
                    age=row['age']
                )
            return HttpResponse('Send')
    else:
        form = MyModelForm()
    return render(request, 'upload.html', {'form': form})


def display_items(request):
    items = MyModel.objects.all()
    return render(request, 'display.html', {'items': items})