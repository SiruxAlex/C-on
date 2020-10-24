from django.shortcuts import render
from django.views.generic import TemplateView

# Creators-on
class CCmain(TemplateView):
    template_name = "creator-center-main.html"

class CMAcomplete(TemplateView):
    template_name = "creator-market-ad-complete.html"
    
class CMAproposal(TemplateView):
    template_name = "creator-market-ad-proposal.html"
    
class CMdetail1(TemplateView):
    template_name = "creator-market-detail-1.html"
    
class CMdetail(TemplateView):
    template_name = "creator-market-detail.html"
    
class CMmain1(TemplateView):
    template_name = "creator-market-main-1.html"
    
class CMmain(TemplateView):
    template_name = "creator-market-main.html"
    
class CMmypage(TemplateView):
    template_name = "creator-market-mypage.html"
    
class CR1(TemplateView):
    template_name = "creator-register-1.html"

    
class CR2(TemplateView):
    template_name = "creator-register-2.html"

    
class CR3(TemplateView):
    template_name = "creator-register-3.html"