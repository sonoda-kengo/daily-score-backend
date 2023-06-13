from django.db import models


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class TaskStatus(models.IntegerChoices):
    NEW = 0, "NEW"
    INPROGRESS = 1, "INPROGRESS"
    DONE = 2, "DONE"
    DELETED = 9, "DELETED"


class DailyTask(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    work_date = models.DateField(db_index=True)
    status = models.CharField(choices=TaskStatus.choices, default=TaskStatus.NEW, db_index=True, max_length=20)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, related_name="category_tasks", null=True, blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
