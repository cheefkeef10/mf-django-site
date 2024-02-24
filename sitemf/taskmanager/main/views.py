from django.shortcuts import render,redirect
from .models import News, Files, nalogovaya
from django.views.generic import ListView,DetailView
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
import os
from django.conf import settings
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator

from django.db import connection
from django.contrib.auth import authenticate



class Index(ListView):
    model = News
    queryset = News.objects.all().order_by('datetime')
    template_name = 'main/index.html'
    paginate_by = 3




class DetailArticleView(DetailView):
    model = News
    template_name = 'main/blog_post.html'

def files(request):
    files = Files.objects.all()
    return render(request, "files/files.html",{'text': 'Файлы', 'files':files})


# def signin(request):
#     if request.user.is_authenticated:
#         return render(request, 'main/index.html')
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('/profile/')  # profile
#         else:
#             msg = 'Error Login'
#             form = AuthenticationForm(request.POST)
#             return render(request, 'registration/login.html', {'form': form, 'msg': msg})
#     else:
#         form = AuthenticationForm()
#         return render(request, 'registration/login.html', {'form': form})
#
# def logout_user(request):
#      logout(request)
#      return redirect('/')

@login_required()
def profile(request):
    if request.user.username == 'bauntRN':
        all_data = nalogovaya.objects.filter(oktmo_id__startswith='81606').values('ID','datetime','oktmo_id','KBK','KPP','oktmo_id','NAIMPLAT')
        paginator = Paginator(all_data, 50)
        page_number = request.GET.get('page')
        all_data = paginator.get_page(page_number)
        return render(request, 'registration/profile.html', {'all_data': all_data})


    if request.user.username == 'barguzinRN':
        all_data = nalogovaya.objects.filter(oktmo_id__startswith='81603').values('ID','datetime','oktmo_id','KBK','KPP','oktmo_id','NAIMPLAT')
        paginator = Paginator(all_data, 50)
        page_number = request.GET.get('page')
        all_data = paginator.get_page(page_number)
        return render(request, 'registration/profile.html', {'all_data': all_data})

    if request.user.username == 'bichurRN':
        all_data = nalogovaya.objects.filter(oktmo_id__startswith='81609').values('ID','datetime','oktmo_id','KBK','KPP','oktmo_id','NAIMPLAT')
        paginator = Paginator(all_data, 50)
        page_number = request.GET.get('page')
        all_data = paginator.get_page(page_number)
        return render(request, 'registration/profile.html', {'all_data': all_data})

 # def profile(request):
#     all_data = nalogovaya.objects.all()
#     paginator = Paginator(all_data,50)
#     page_number = request.GET.get('page')
#     all_data = paginator.get_page(page_number)
#     context = {
#         'all_data': all_data
#     }
#     return render(request, 'registration/profile.html', context)






def delete_item(request,myid):
    item = nalogovaya.objects.get(ID = myid)
    item.delete()
    messages.info(request,"Успешно удалено")
    return redirect(profile)








def download(request, path):
    # get the download path
    download_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(download_path):
        with open(download_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/specifications")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(download_path)
            return response
    raise Http404


class BlogSearchView(ListView):
    model = News
    template_name = 'main/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return News.objects.filter(headline__icontains=query).order_by('datetime')