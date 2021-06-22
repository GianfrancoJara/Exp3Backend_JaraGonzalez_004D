from django.urls import path
from .views import contacto, contratacion, galeria, home, quienessomos, vercontrataciones, form_del_solicitud, form_mod_solicitud

urlpatterns = [
    path('', home,name="home"),
    path('galeria/', galeria, name='galeria'),
    path('quienessomos/', quienessomos, name='quienessomos'),
    path('contacto/', contacto, name='contacto'),
    path('contratacion/', contratacion, name='contratacion'),
    path('vercontrataciones/', vercontrataciones, name='vercontrataciones'),
    path('form_mod_solicitud/<id>', form_mod_solicitud, name="form_mod_solicitud"),
    path('form_del_solicitud/<id>', form_del_solicitud, name="form_del_solicitud") 
]