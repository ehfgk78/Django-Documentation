from django.db import models

# models 패키지를 만들고 abstract_base_class.py에 아래 내용을 추가
# multi_table.py에 새 내용을 추가
# admin이 잘 작동하도록
# __init__.py를 작성
# 각 모듈에 __all__을 작성

__all__ = (
    'School',
    'CommonInfo',
    'Student',
    'Teacher'
)


class School(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class CommonInfo(models.Model):
    school = models.ForeignKey(
        School,
        blank=True,
        null=True,
        related_name='%(app_label)s_%(class)s_set',
    )
    name = models.CharField(max_length=100, default='')
    age = models.PositiveIntegerField(default=0)

    class Meta:
        abstract = True


class Student(CommonInfo):
    home_group = models.CharField(max_length=5)


class Teacher(CommonInfo):
    subject = models.CharField(max_length=30)
