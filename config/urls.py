from django.contrib import admin
from django.urls import path
from strawberry.django.views import GraphQLView
from tasks.presentation.schema import schema

urlpatterns = [
    path('admin/', admin.site.urls),
    path('graphql/', GraphQLView.as_view(schema=schema)),  # Endpoint GraphQL
]
