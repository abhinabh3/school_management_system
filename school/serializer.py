from rest_framework.serializers import ModelSerializer
from .models import Student,Teacher,Class,Attendance,Examination,Grade,Book,BorrowRecord,Parent, User,Course
from rest_framework import serializers





class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["email","username","password","role"]

class StudentSerializer(ModelSerializer):
    username = serializers.CharField(source='user.username',read_only=True)
    class Meta:
        model = Student
        fields =  ["id","user","contact_info","academic_records","username","name"]
    
    
class TeacherSerializer(ModelSerializer):
    username = serializers.CharField(source='user.username',read_only=True)
    class Meta:
        model = Teacher
        fields =  ["id","user","availability","username","name"]



class ClassSerializer(ModelSerializer):
    teacher_name = serializers.CharField(source='teacher.name', read_only=True)
    student_names = serializers.SerializerMethodField()

    class Meta:
        model = Class
        fields = ["id", "name", "schedule", "teacher", "students", "teacher_name", "student_names"]

    def get_student_names(self, obj):
        
        return [student.name for student in obj.students.all()]

class CourseSerializer(ModelSerializer):
    teacher_name = serializers.CharField(source='teacher.name', read_only=True)
    student_names = serializers.SerializerMethodField()
    classes_name = serializers.CharField(source='classes.name', read_only=True)

    class Meta:
        model = Course
        fields = ["id", "name","description", "schedule", "teacher", "students","teacher", "teacher_name", "student_names","classes","classes_name"]

    def get_student_names(self, obj):
        
        return [student.name for student in obj.students.all()]


class AttendanceSerializer(ModelSerializer):
    student_name = serializers.CharField(source='student.name', read_only=True)
    class Meta:
        model = Attendance
        fields = ["id","student","date","student_name","status","classes"]

class ExaminationSerializer(ModelSerializer):
    
    class_name = serializers.CharField(source='classes.name', read_only=True)
    course_name = serializers.CharField(source='course.name', read_only=True)
    
    class Meta:
        model = Examination
        fields = ["id","course","date","class_name","classes","course_name"]
    
  

class GradeSerializer(ModelSerializer):
    
    student_name = serializers.CharField(source='student.name', read_only=True)
    course_name = serializers.CharField(source='exam.course.name', read_only=True)
    

    
    class Meta:
        model = Grade
        fields = ["id","student","exam","grade","student_name","course_name"]
    

class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

class BorrowRecordSerializer(ModelSerializer):
    username = serializers.CharField(source='user.username',read_only=True)
    book_name = serializers.CharField(source='book.title',read_only=True)
    book_author = serializers.CharField(source='book.author',read_only=True)
    class Meta:
        model = BorrowRecord
        fields = ["id","book","user","borrow_date","return_date","username","book_name","book_author"]

class ParentSerializer(ModelSerializer):
   
    username = serializers.CharField(source='user.username',read_only=True)
    class Meta:
        model = Parent
        fields =  ["id","user","username"]

