from django.conf.urls import url
from finder import views
from finder.views import FinderView

app_name="finder"

urlpatterns=[
	url(r'^$',FinderView.as_view(),name='finder'),
]