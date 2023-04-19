from django.urls import path,include
from .views import *
urlpatterns = [
    path('students',getStudents),
    path('student/<int:pk>',getStudentDetail),
    path("addstudent",addStudent),
    path("updatestudent/<int:pk>",updateStudent),
    path("removestudent/<int:pk>",deleteStudent),

    path('mentors',getMentors),
    path('mentor/<int:pk>',getMentorDetail),
    path("addmentor",addMentor),
    path("updatementor/<int:pk>",updateMentor),
    path("removementor/<int:pk>",deleteMentor),

    path('groupsessions',getGroupSessions),
    path('groupsession/<int:pk>',getGroupSessionDetail),
    path("addgroupsession",addGroupSession),
    path("updategroupsession/<int:pk>",updateGroupSession),
    path("removegroupsession/<int:pk>",deleteGroupSession),

    path('feedbacks',getFeedbacks),
    path('feedback/<int:pk>',getFeedbackDetail),
    path("addfeedback",addFeedback),
    path("updatefeedback/<int:pk>",updateFeedback),
    path("removefeedback/<int:pk>",deleteFeedback),

    path('schedules',getSchedules),
    path('schedule/<int:pk>',getScheduleDetail),
    path("addschedule",addSchedule),
    path("updateschedule/<int:pk>",updateSchedule),
    path("removeschedule/<int:pk>",deleteSchedule),

    path('interests',getInterests),
    path('interest/<int:pk>',getInterestDetail),
    path("addinterest",addInterest),
    path("updateinterest/<int:pk>",updateInterest),
    path("removeinterest/<int:pk>",deleteInterest),

     path('register', register, name='register'),
    path('login', login, name='login'),

    
]

