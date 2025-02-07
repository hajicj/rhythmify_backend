from django.conf.urls import url 
from melodies import views 
 
urlpatterns = [ 
    url(r'^api/chants/$', views.chant_list),
    url(r'^api/chants/(?P<pk>[0-9]+)$', views.chant_display),
    url(r'^api/chants/align/$', views.chant_align),
    url(r'^api/chants/upload/$', views.upload_data),
    url(r'^api/chants/data-sources', views.get_data_sources),
    url(r'^api/chants/fontes', views.get_fontes),
    url(r'^api/chants/export/$', views.export_dataset),
    url(r'^api/chants/create-dataset/$', views.create_dataset),
    url(r'^api/chants/add-to-dataset/$', views.add_to_dataset),
    url(r'^api/chants/delete-dataset/$', views.delete_dataset),
    url(r'^api/chants/update-volpiano/$', views.update_volpiano)
]
