from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # 기본적으로 제공하는 필드 : username, password
    name = models.CharField(blank = False)
    id_front = models.IntegerField()
    id_back = models.IntegerField()
    birth_date = models.DateField()
    level = models.CharField()


class Class(models.Model):
    image = models.ImageField(upload_to=None, blank=True)
    title = models.CharField()
    category = models.TextField()
    start_time = models.DateTimeField()
    place = models.TextField()
    isFree = models.TextChoices('무료', '유료')
    tuition = models.IntegerField()
    apply_start_time = models.DateTimeField()
    apply_end_time = models.DateTimeField()
    content = models.TextField() 

    class Meta:
        ordering = ['apply_end_time'] #신청 마감일이 촉박한 순 정렬
    
    def __str__(self):
        return self.title


class Review(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE, blank=True)
    class_id = models.ForeignKey(Class, on_delete = models.CASCADE, blank=True)
    score = models.IntegerField()
    content = models.TextField()
    time = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-time'] #최신순 정렬

    def __str__(self):
        return f"작성자:{self.user_id} - 클래스:{self.class_id}"


class Apply(models.Model):
    user_id = models.ForeignKey(User,on_delete = models.CASCADE, blank=True)
    class_id = models.ForeignKey(Class, on_delete = models.CASCADE, blank=True)  
    time = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ['-time'] #최신순 정렬

    def __str__(self):
        return f"지원자:{self.user_id} - 클래스:{self.class_id}"