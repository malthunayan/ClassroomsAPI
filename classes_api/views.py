from django.shortcuts import render
from rest_framework.generics import (ListAPIView,
	RetrieveAPIView, RetrieveUpdateAPIView,
	CreateAPIView, DestroyAPIView
	)

from classes.models import Classroom
from .serializers import (ClassroomListSerializer,
	ClassroomDetailSerializer, ClassroomUpdateSerializer,
	)


class ClassroomList(ListAPIView):
	queryset = Classroom.objects.all()
	serializer_class = ClassroomListSerializer

class ClassroomDetail(RetrieveAPIView):
	queryset = Classroom.objects.all()
	serializer_class = ClassroomDetailSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'classroom_id'

class ClassroomUpdate(RetrieveUpdateAPIView):
	queryset = Classroom.objects.all()
	serializer_class = ClassroomUpdateSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'classroom_id'

class ClassroomDelete(DestroyAPIView):
	queryset = Classroom.objects.all()
	lookup_field = 'id'
	lookup_url_kwarg = 'classroom_id'

class ClassroomCreate(CreateAPIView):
	serializer_class = ClassroomUpdateSerializer

	def perform_create(self, serializer):
		serializer.save(teacher=self.request.user)