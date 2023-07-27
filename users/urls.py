from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.decorators.cache import cache_page

from study.apps import StudyConfig

app_name = StudyConfig.name

urlpatterns = [
    path('mailing/', MailingListView.as_view(), name='mailing_list'),  # список рассылок
    path('mailing/<int:pk>/', MailingDetailView.as_view(), name='mailing_item'),
    path('mailing/create/', MailingCreateView.as_view(), name='mailing_create'),
    path('mailing/update/<int:pk>/', MailingUpdateView.as_view(), name='mailing_update'),
    path('mailing/delete/<int:pk>/', MailingDeleteView.as_view(), name='mailing_delete'),
]
