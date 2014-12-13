# -*- coding: utf-8 -*-
from django.views.generic.edit import FormView
from django.views.generic import View
from django.contrib.auth.forms import AuthenticationForm
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login


class Login(FormView):
    template_name = 'account/login.html'
    form_class = AuthenticationForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(Login, self).get_context_data(**kwargs)
        context['form'] = self.get_form(self.get_form_class())
        return context

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(self.request, user)
                return super(Login, self).form_valid(form)
            else:
                return super(Login, self).form_invalid(form)
        else:
            return super(Login, self).form_invalid(form)

    # def form_invalid(self, form):
    #     pass
