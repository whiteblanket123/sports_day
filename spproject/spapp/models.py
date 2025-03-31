from django.db import models

class Event(models.Model):
    classs = models.CharField(max_length=10)
    relay = models.IntegerField()
    performance = models.IntegerField()
    ssrieum  = models.IntegerField()
    basketball  = models.IntegerField()
    soccer  = models.IntegerField()
    dodge_ball  = models.IntegerField()
    jump_rope  = models.IntegerField()

    class Meta:
        db_table = 'event'  # 데이터베이스 테이블 이름 지정
        verbose_name = 'Event'  # 모델의 단수 이름
        verbose_name_plural = 'Events'  # 모델의 복수 이름