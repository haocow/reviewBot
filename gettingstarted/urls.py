from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

import hello.views
import reviewBot.views.webhook
import reviewBot.views.transactions

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", hello.views.index, name="index"),
    path("hello/", hello.views.hello, name="hello"),
    path("db/", hello.views.db, name="db"),
    path("admin/", admin.site.urls),

    path("webhook/", reviewBot.views.webhook.webhook, name="webhook"),
    path("transactions/", reviewBot.views.transactions.transactions, name="transactions")
]
