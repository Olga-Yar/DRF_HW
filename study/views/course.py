# для курса через ViewSets
from rest_framework.viewsets import ModelViewSet

from study.models import Course
from study.seriallizers.course import CourseSerializer


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
