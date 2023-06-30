from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
import os
from django.core.files.storage import FileSystemStorage, default_storage
from .models import EnkripsiFiles, DekripsiFiles
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib import messages
import timeit

# Create your views here.

def index(request):
    context = {
        'name' : 'xorchiper',
        'header' : 'XOR Chiper BPJS kesehatan',
        'sub' : 'Dengan Gotong Royong, Semua Tertolong'
    }
    return render(request, 'index.html', context)

@login_required(login_url=settings.LOGIN_URL)
def home(request):
    context = {
        'name' : 'xorchiper',
    }

    return render(request, 'home.html', context)


@login_required(login_url=settings.LOGIN_URL)
def enkripsi(request):

    if request.method == "POST":
        namaFile = request.POST.get('namafile')
        myfile = request.FILES['fil']
        kunci = request.POST.get('kunci')
        i = 0
        max = 6 - 1

        if len(kunci) <= max:
            messages.error(request, "kunci harus lebih dari 5 karakter")
            return redirect('enkripsi')
        else:
            user = request.user
            
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            
            start = timeit.default_timer()
            file_upload_dir = os.path.join(settings.MEDIA_ROOT)
            f = default_storage.open(os.path.join(file_upload_dir, filename), 'rb')
            data = f.read()
            f.close()
            data = bytearray(data)

            for index, nilai in enumerate(data):
                data[index] = nilai ^ ord(kunci[i])
                if i >= max:
                    i = 0
                else:
                    i += 1

            f = default_storage.open(os.path.join(file_upload_dir, filename), 'wb')
            f.write(data)
            f.close()

            stop = timeit.default_timer() 
            lama_eksekusi = stop - start 

            size = myfile.size
            form = EnkripsiFiles(document=namaFile, fi=filename, encrypted_by=user, size=size, time=lama_eksekusi)
            form.save()

            messages.success(request, "file berhasil di enkripsi")
            return redirect('enkripsiHistory')

    files = EnkripsiFiles.objects.all()
    konteks = {
        'files' : files,
    }

    return render(request, 'enkripsi.html', konteks)



def login(request):
    
    return render(request, 'registration/login.html')

@csrf_exempt
def signup(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pas = request.POST.get('password')
        if User.objects.filter(username = uname).first():
            messages.error(request, "This username is already taken")
            return redirect('signup')
        else:
            my_user = User.objects.create_user(uname,email,pas)
            my_user.save()
            messages.success(request, "User berhasil dibuat!")
            return redirect('login')

    else:
        pass


    return render(request, 'registration/signup.html')

@login_required(login_url=settings.LOGIN_URL)
def enkripsiHistory(request):
    files = EnkripsiFiles.objects.all()
    konteks = {
        'files' : files,
        'name' : 'xorchiper',
    }
    return render(request, 'enkripsiHistory.html', konteks)

@login_required(login_url=settings.LOGIN_URL)
def dekripsiHistory(request):
    files = DekripsiFiles.objects.all()
    konteks = {
        'files' : files,
        'name' : 'xorchiper',
    }
    return render(request, 'dekripsiHistory.html', konteks)

def delete(request, id_file):
    file = EnkripsiFiles.objects.get(id=id_file)
    file.delete()

    return redirect('enkripsiHistory')

def deletee(request, id_file):
    file = DekripsiFiles.objects.get(id=id_file)
    file.delete()

    return redirect('dekripsiHistory')


@login_required(login_url=settings.LOGIN_URL)
def dekripsi(request):
    if request.method == "POST":
        namaFile = request.POST.get('namafile')
        myfile = request.FILES['fil']
        kunci = request.POST.get('kunci')
        i = 0
        max = 6 - 1

        if len(kunci) <= max:
            messages.error(request, "kunci harus lebih dari 5 karakter")
            return redirect('dekripsi')
        else:
            user = request.user
            
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            
            start = timeit.default_timer()
            file_upload_dir = os.path.join(settings.MEDIA_ROOT)
            print(file_upload_dir)
            f = default_storage.open(os.path.join(file_upload_dir, filename), 'rb')
            data = f.read()
            f.close()
            data = bytearray(data)

            for index, nilai in enumerate(data):
                data[index] = nilai ^ ord(kunci[i])
                if i >= max:
                    i = 0
                else:
                    i += 1

            f = default_storage.open(os.path.join(file_upload_dir, filename), 'wb')
            f.write(data)
            f.close()

            stop = timeit.default_timer() 
            lama_eksekusi = stop - start 
         

            size = myfile.size
            form = DekripsiFiles(document=namaFile, fi=filename, encrypted_by=user, size=size, time=lama_eksekusi)
            form.save()

            messages.success(request, "file berhasil di dekripsi")
            return redirect('dekripsiHistory')
        
    files = DekripsiFiles.objects.all()
    konteks = {
        'files' : files,
    }

    return render(request, 'dekripsi.html', konteks)
