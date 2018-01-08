from django.conf.urls import url
from coleta import views
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', views.index, name='index'),

    # 404
    url(r'', TemplateView.as_view(template_name='404.html'), name='404'),
]
