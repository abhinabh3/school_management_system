from django.shortcuts import render
from .models import Student,Teacher,Class,Attendance,Examination,Grade,Book,BorrowRecord,Parent,UserRole,User,Course
from rest_framework.viewsets import ModelViewSet
from .serializer import StudentSerializer,TeacherSerializer,ClassSerializer,AttendanceSerializer,ExaminationSerializer,GradeSerializer,BookSerializer,BorrowRecordSerializer,ParentSerializer,UserSerializer,CourseSerializer
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework import permissions

# Create your views here.


class IsAdmin(permissions.BasePermission):
    """
    Permission to allow only admins.
    """
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        return request.user.role == UserRole.ADMIN


class IsTeacher(permissions.BasePermission):
    """
    Permission to allow only teachers.
    """
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        return request.user.role == UserRole.TEACHER


class IsStudent(permissions.BasePermission):

    """
    Permission to allow only students.
    """
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        if request.user.role == UserRole.STUDENT:
            return request.method in permissions.SAFE_METHODS
        
        return False



class IsParent(permissions.BasePermission):
    """
    Permission to allow only parents.
    """
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        return request.user.role == UserRole.PARENT




@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_users(request):
    users = User.objects.all()  
    user_data = [{"id": user.id, "email": user.email, "username": user.username, "role": user.role} for user in users]
    return Response(user_data)

@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    email = request.data.get("email")
    password = request.data.get("password")
    user = authenticate(username = email, password = password)
    if user == None:
        return Response("Invalid Credential")
    else:
        token,_ = Token.objects.get_or_create(user = user)
        return Response(token.key) 

@api_view(["POST"])
@permission_classes([AllowAny])
def register(request):
        password = request.data.get("password")
        role = request.data.get("role", UserRole.STUDENT)  

        if not password:
            return Response({"error": "Password is required"}, status=400)

        request.data["password"] = make_password(password)
        
        
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()  
            return Response({
                "message": "User created successfully",
                "user_id": user.id  
            }, status=201)
        else:
            return Response(serializer.errors, status=400)

 



@api_view(['POST']) 
@permission_classes([IsAuthenticated])  
def logout(request):
    try:
        token = Token.objects.get(user=request.user)
        token.delete() 
        return Response("Successfully logged out.")
    except:
        return Response("Logout Unsuccessful")
    


@permission_classes([IsAdmin | IsTeacher])
class StudentViewset(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filterset_fields = ["user"]
    search_fields = ["contact_info","user__username","name"]

@permission_classes([IsAdmin | IsTeacher])
class TeacherViewset(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    filterset_fields = ["user"]
    search_fields = ["user__username","name"]

@permission_classes([IsAdmin | IsStudent | IsTeacher])
class ClassViewset(ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    filterset_fields = ["teacher","students"]
    search_fields = ["name","teacher__name"]

@permission_classes([IsAdmin | IsStudent | IsTeacher])
class CourseViewset(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filterset_fields = ["teacher","classes"]
    search_fields = ["name","teacher__name"]

@permission_classes([IsTeacher | IsAdmin | IsStudent])
class AttendanceViewset(ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    filterset_fields = ["student"]
    search_fields = ["date","student__name"]

@permission_classes([IsTeacher | IsAdmin | IsStudent])
class ExaminationViewset(ModelViewSet):
    queryset = Examination.objects.all()
    serializer_class = ExaminationSerializer
    filterset_fields = ["classes","course"]
    search_fields = ["course__name","date","classes__name"]

@permission_classes([IsTeacher | IsAdmin])
class GradeViewset(ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    filterset_fields = ["student","exam"]
    search_fields = ["grade","student__name"]

@permission_classes([IsAdmin | AllowAny])
class BookViewset(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    search_fields = ["title","author"]

@permission_classes([IsStudent | IsTeacher | IsAdmin | IsParent])
class BorrowRecordViewset(ModelViewSet):
    queryset = BorrowRecord.objects.all()
    serializer_class = BorrowRecordSerializer
    filterset_fields = ["book","user"]
    search_fields = ["user__username","book__title","book__author"]

@permission_classes([IsAdmin])
class ParentViewset(ModelViewSet):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer
    filterset_fields = ["user"]
    search_fields = ["user__username"]


