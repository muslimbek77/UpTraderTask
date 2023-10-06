
from importlib.util import find_spec

from django.contrib import admin
from django.urls import path, include, reverse_lazy
from django.conf import settings
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url=reverse_lazy('home'))),
]

for app in settings.MENUEXAMPLE_APPS:
    mod = app + '.urls'
    if find_spec(mod):
        urlpatterns.append(path(app + '/', include(mod)))

