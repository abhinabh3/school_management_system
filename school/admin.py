from django.contrib import admin
from .models import Student,Teacher,Class,Attendance,Examination,Grade,Book,BorrowRecord,Parent, User,Course

# Register your models here.

admin.site.register(User)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Class)
admin.site.register(Course)
admin.site.register(Attendance)
admin.site.register(Examination)
admin.site.register(Grade)
admin.site.register(Book)
admin.site.register(BorrowRecord)
admin.site.register(Parent)

