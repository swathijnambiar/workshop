from django.contrib.auth.decorators import login_required
from registration.urls import *
from registration.models import *
from workshop.views import *
from django.contrib.auth import views as auth_views


admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'workshop.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', Home.as_view(), name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^register/', include('registration.urls')),
    url(r'^user/login/$',
        anonymous_required(auth_views.login),
        {'template_name': 'register/login.html'},
        name='login'),
    url(r'^user/logout/$',
        auth_views.logout,
        {'template_name': 'register/logout.html'},
        name='logout')


]


