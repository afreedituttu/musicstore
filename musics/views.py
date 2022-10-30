from django import shortcuts
from musics.models import Albums
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .forms import userform
from django.views.generic import View

# Create your views here.

def delete(request, pk):
    Albums.objects.filter(pk=pk).delete()
    return redirect('/')

class index(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'all_album'

    def get_queryset(self):
        return Albums.objects.all()


class detail(generic.DeleteView):
    template_name = 'detail.html'
    model = Albums.objects.all()
    context_object_name = 'alb'

    def get_queryset(self):
        return Albums.objects.all()
    
class add(CreateView):
    model = Albums
    fields = ['title','artist','logo']
    template_name = 'albums_form.html'
    
class update(UpdateView):
    model = Albums
    fields = ['title','artist','logo']
    template_name = 'albums_form.html'


#class delete(DeleteView):
 #   model = Albums
  #  success_url = reverse_lazy('music:index')
  #  template_name = 'deleted.html'


class register(View):
    form_class = userform
    template_name = 'form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name,{'form':form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            username_r = form.cleaned_data['username']
            password_r = form.cleaned_data['password']
            user.set_password(password_r)
            email = form.cleaned_data['email']
            user.save()

            user = authenticate(username=username_r,password=password_r)

            if user is not None:
                if user.is_active:
                    login(request,user)
                    return render('music:index')

        return render(request,self.template_name,{'form':form})

def addsong(request, pk):
    if request.method=='POST':
        SongName = request.POST['songname']
        path = request.POST['file']
        Duration = request.POST['duration']
        album = Albums.objects.get(pk=pk)
        album.song_set.create(name=SongName,path=path,duration=Duration)
        album.save()
        redirect_url = '/music/'+str(pk)
        return redirect(redirect_url)
    else:
        return render(request,'addsong_form.html')

def songdelete(request, id, name):
    album = Albums.objects.get(pk=id)
    album.song_set.get(name=name).delete()
    redirect_url = '/music/'+id
    return redirect(redirect_url)
