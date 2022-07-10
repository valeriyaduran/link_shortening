from django.http import HttpResponseNotFound, HttpResponseServerError, Http404
from django.urls import reverse_lazy
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, View, ListView, TemplateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib import messages

from links.forms import UserRegisterForm, UserLoginForm, LinkForm
from links.models import Link

from links.shortener_func import shorneter, get_domain


class UserLoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'links/login.html'

    def get_success_url(self):
        return reverse_lazy('home')


class UserLogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('home')


class UserRegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = 'links/register.html'
    success_url = reverse_lazy('login')


class MainView(LoginRequiredMixin, CreateView):
    form_class = LinkForm
    template_name = 'links/index.html'
    login_url = '/login/'

    def post(self, request, *args, **kwargs):
        short_link = None
        if request.method == 'POST':
            linkform = LinkForm(request.POST)
            if linkform.is_valid():
                mylink_form = linkform.save(commit=False)
                mylink_form.user = request.user
                short_link = shorneter(mylink_form.origin_link)
                mylink_form.shortened_link = short_link
                mylink_form.save()
                messages.success(self.request, 'Hooray! Your shortened link is ready! Please, check it below.')
            else:
                short_link = Link.objects.get(origin_link=(linkform.data['origin_link'])).shortened_link
        else:
            linkform = LinkForm()

        return render(request, 'links/index.html',
                      context={'form': linkform,
                               'short_link': short_link})


class MyLinksView(LoginRequiredMixin, ListView):
    model = Link
    template_name = 'links/mylinks.html'
    context_object_name = 'mylinks'

    def get(self, request, *args, **kwargs):
        context = {'mylinks': Link.objects.filter(user=request.user)}
        return render(request, 'links/mylinks.html', context=context)


class ShortLinkRedirectView(TemplateView):

    def get(self, request, *args, **kwargs):
        uri = request.build_absolute_uri()
        try:
            full_url = Link.objects.get(shortened_link=get_domain(uri) + '/' + self.kwargs['url_hash']).origin_link
        except ObjectDoesNotExist:
            raise Http404
        return redirect(full_url)


def custom_handler404(request, exception):
    return HttpResponseNotFound("This page is not found!")


def custom_handler500(request):
    return HttpResponseServerError("Server error!")
