from django.shortcuts import get_object_or_404
from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated

from .serializers import PaperSerializer
from papers.models import Paper
from conferences.models import Conference
from . import pagination

class PaperListView(generics.ListAPIView):
    serializer_class = PaperSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = pagination.PaperCursorPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'keyword', 'conference__title']
    ordering_fields = ['title', 'last_modified']

    def get_queryset(self):
        user = self.request.user
        return Paper.objects.filter(user=user)
    
    def get_view_name(self):
        return "List of Papers (User)"

class PaperDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PaperSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Paper.objects.filter(user=user)
    
    def get_view_name(self):
        return "Detail View of Paper (User)"

class PaperCreateView(generics.CreateAPIView):
    serializer_class = PaperSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        conf_acronym = self.kwargs.get('conf')
        conference = get_object_or_404(Conference, acronym=conf_acronym)
        serializer.save(user=self.request.user, conference=conference)
    
    def get_view_name(self):
        return "Submit Paper to Conference"