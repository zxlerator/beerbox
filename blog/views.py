# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views import generic

class IndexView(generic.TemplateView):
    template_name = "blog/index.html"

class AboutView(generic.TemplateView):
    template_name = "blog/about.html"

class FaqView(generic.TemplateView):
    template_name = "blog/faq.html"

class TermsView(generic.TemplateView):
    template_name = "blog/terms.html"

class PrivacyView(generic.TemplateView):
    template_name = "blog/privacy.html"
