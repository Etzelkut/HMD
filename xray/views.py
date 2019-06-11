from django.shortcuts import render
from .forms import UploadFileForm
from .model import open_image
from .model2 import open_image2
from accounts.models import CustomUser
def upload_file(request):
    if request.method == 'POST':
        print("POST method")
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            result = open_image(request.FILES['file'].read())
            user = CustomUser.objects.get(username=request.user.username)
            if result:
                user.xray = 'yes'
            else:
                user.xray = 'no' 
            user.save()
            return render(request, '../templates/xray.html', {'result' : result })
    else:
        form = UploadFileForm()
    return render(request, '../templates/xray.html', {'form': form})

def upload_pneumonia(request):
    if request.method == 'POST':
        print("POST method")
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            result = open_image2(request.FILES['file'].read())
          #  user = CustomUser.objects.get(username=request.user.username)
            return render(request, '../templates/xray_cancer.html', {'result' : result })
    else:
        form = UploadFileForm()
    return render(request, '../templates/xray_cancer.html', {'form': form})

