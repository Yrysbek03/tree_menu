from django.db import models


class Menu(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return self.name

    def get_children(self):
        return self.menu_set.all()

    def get_parents_ids(self):
        if self.parent:
            return self.parent.get_parents_ids() + [self.parent.id]
        else:
            return []
