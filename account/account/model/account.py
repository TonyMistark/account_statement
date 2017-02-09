# coding=utf-8


from django.db import models


# 账单
class Account(models.Model):

    summary = models.CharField("摘要", max_length=200)
    enter = models.IntegerField("入账")
    expense = models.IntegerField("入账")
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)
    create_man = models.CharField("创建人", max_length=200)
    remark = models.CharField("备注", max_length=200)

    def __unicode__(self):
        return self.summary
