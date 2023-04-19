
from django.contrib.auth import authenticate, login
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *

@api_view(["GET"])
def getStudents(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students,many=True)

    return Response(serializer.data)

@api_view(["GET"])
def getStudentDetail(request,pk):

    student = Student.objects.get(pk=pk)
    serializer = StudentSerializer(student,many=False)

    return Response(serializer.data)

@api_view(["POST"])
def addStudent(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["PUT"])
def updateStudent(request,pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = StudentSerializer(student,request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["DELETE"])
def deleteStudent(request,pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    student.delete()

    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["GET"])
def getMentors(request):
    mentors = Mentor.objects.all()
    serializer = StudentSerializer(mentors,many=True)

    return Response(serializer.data)

@api_view(["GET"])
def getMentorDetail(request,pk):

    mentor = Mentor.objects.get(pk=pk)
    serializer = StudentSerializer(mentor,many=False)

    return Response(serializer.data)

@api_view(["POST"])
def addMentor(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["PUT"])
def updateMentor(request,pk):
    try:
        mentor = Mentor.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = StudentSerializer(mentor,request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["DELETE"])
def deleteMentor(request,pk):
    try:
        mentor = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    mentor.delete()
    
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["GET"])
def getGroupSessions(request):
    groupSession = GroupSession.objects.all()
    serializer = StudentSerializer(groupSession,many=True)

    return Response(serializer.data)

@api_view(["GET"])
def getGroupSessionDetail(request,pk):

    groupSession = GroupSession.objects.get(pk=pk)
    serializer = StudentSerializer(groupSession,many=False)

    return Response(serializer.data)

@api_view(["POST"])
def addGroupSession(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["PUT"])
def updateGroupSession(request,pk):
    try:
        groupSession = GroupSession.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = StudentSerializer(groupSession,request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["DELETE"])
def deleteGroupSession(request,pk):
    try:
        groupSession = GroupSession.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    groupSession.delete()
    
    return Response(status=status.HTTP_204_NO_CONTENT)




@api_view(["GET"])
def getFeedbacks(request):
    feedbacks = Feedback.objects.all()
    serializer = StudentSerializer(feedbacks,many=True)

    return Response(serializer.data)

@api_view(["GET"])
def getFeedbackDetail(request,pk):

    feedback = Feedback.objects.get(pk=pk)
    serializer = StudentSerializer(feedback,many=False)

    return Response(serializer.data)

@api_view(["POST"])
def addFeedback(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["PUT"])
def updateFeedback(request,pk):
    try:
        feedback = Feedback.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = StudentSerializer(feedback,request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["DELETE"])
def deleteFeedback(request,pk):
    try:
        feedback = Feedback.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    feedback.delete()
    
    return Response(status=status.HTTP_204_NO_CONTENT)




@api_view(["GET"])
def getSchedules(request):
    schedules = Schedule.objects.all()
    serializer = StudentSerializer(schedules,many=True)

    return Response(serializer.data)

@api_view(["GET"])
def getScheduleDetail(request,pk):

    schedule = Schedule.objects.get(pk=pk)
    serializer = StudentSerializer(schedule,many=False)

    return Response(serializer.data)

@api_view(["POST"])
def addSchedule(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["PUT"])
def updateSchedule(request,pk):
    try:
        schedule = Schedule.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = StudentSerializer(schedule,request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["DELETE"])
def deleteSchedule(request,pk):
    try:
        schedule = Schedule.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    schedule.delete()
    
    return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(["GET"])
def getInterests(request):
    interests = Interest.objects.all()
    serializer = StudentSerializer(interests,many=True)

    return Response(serializer.data)

@api_view(["GET"])
def getInterestDetail(request,pk):

    interest = Interest.objects.get(pk=pk)
    serializer = StudentSerializer(interest,many=False)

    return Response(serializer.data)

@api_view(["POST"])
def addInterest(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["PUT"])
def updateInterest(request,pk):
    try:
        interest = Interest.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = StudentSerializer(interest,request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["DELETE"])
def deleteInterest(request,pk):
    try:
        interest = Interest.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    interest.delete()
    
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        user.set_password(request.data.get('password'))
        if request.data.get('is_student'):
            user.is_student = True
        elif request.data.get('is_mentor'):
            user.is_mentor = True
        user.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')
    user = authenticate(request, email=email, password=password)
    if user is not None:
        login(request, user)
        return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Invalid email or password'}, status=status.HTTP_401_UNAUTHORIZED)