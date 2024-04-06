from django.urls import path
from olp_app.views import CourseList, CourseDetails, CreateCourse, CourseEnrollment


urlpatterns = [
    path("courses/", CourseList.as_view(), name="courses"),
    path("courses/create/", CreateCourse.as_view(), name="create_course"),
    path("courses/<int:id>/", CourseDetails.as_view(), name="course_details"),
    path("enrollments/", CourseEnrollment.as_view(), name="enrollments"),
]
