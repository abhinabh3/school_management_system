from django.db import models
from django.contrib.auth.models import AbstractUser

# User role choices
class UserRole(models.TextChoices):
    ADMIN = 'Admin', 'Admin'
    TEACHER = 'Teacher', 'Teacher'
    STUDENT = 'Student', 'Student'
    PARENT = 'Parent', 'Parent'

# Custom User model
class User(AbstractUser):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)
    username = models.CharField(max_length=200, default="username")
    role = models.CharField(
        max_length=10,
        choices=UserRole.choices,
        default=UserRole.STUDENT,
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return f"{self.username} ({self.role})"

# Student model
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, limit_choices_to={'role': UserRole.STUDENT})
    name = models.CharField(max_length=100, default="unknown")
    contact_info = models.CharField(max_length=100)
    academic_records = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.user.username

# Teacher model
class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, limit_choices_to={'role': UserRole.TEACHER})
    name = models.CharField(max_length=100, default="unknown")
    availability = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.user.username

# Class model
class Class(models.Model):
    name = models.CharField(max_length=100)
    schedule = models.TextField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student, related_name="classes")

    def __str__(self):
        return f"{self.name} - Teacher: {self.teacher.user.username}"

# Course model
class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    schedule = models.TextField()
    students = models.ManyToManyField(Student, related_name="courses")
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    classes = models.ForeignKey(Class,on_delete=models.CASCADE,default=1)

    def __str__(self):
        return self.name

# Attendance model
class Attendance(models.Model):
    STATUS_CHOICES = [
        ('present', 'Present'),
        ('absent', 'Absent')
    ]
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    classes = models.ForeignKey(Class, on_delete=models.CASCADE,default=1)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.student.user.username} - {self.status} on {self.date}"

# Examination model
class Examination(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE,default=1)
    date = models.DateField()
    classes = models.ForeignKey(Class, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.course.name} Exam on {self.date}"

# Grade model
class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    exam = models.ForeignKey(Examination, on_delete=models.CASCADE)
    grade = models.CharField(max_length=3)

    def __str__(self):
        return f"{self.student.user.username} - {self.exam.course.name}: {self.grade}"

# Book model for library system
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    is_checked_out = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} by {self.author}"

# Borrow record model
class BorrowRecord(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    borrow_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} borrowed {self.book.title} on {self.borrow_date}"

# Parent model
class Parent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, limit_choices_to={'role': UserRole.PARENT})

    def __str__(self):
        return self.user.username
