from django.conf.urls import include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView


# urlpatterns = [
#     # Examples:
#     # url(r'^$', 'Web_platform_rev03.views.home', name='home'),
#     # url(r'^blog/', include('blog.urls')),
#
#     url(r'^admin/', include(admin.site.urls)),
# ]


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^displayInfo/', include('displayInfo.urls')),
    url(r'^$', RedirectView.as_view(url='/displayInfo/', permanent=True)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    url(r'^accounts/', include('django.contrib.auth.urls')),
]
