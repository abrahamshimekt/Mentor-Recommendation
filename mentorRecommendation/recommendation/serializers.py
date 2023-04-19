from rest_framework import serializers
from .models import *
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


class MentorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentor
        fields = "__all__"


class GroupSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupSession
        fields = "__all__"



class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields ="__all__"

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = "__all__"
class SchedulSerializer(serializers.ModelSerializer):
    class Meta:
        model=Schedule
        fields = "__all__"
class InterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interest
        fields = "__all__"


