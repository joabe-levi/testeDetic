from django.db import models


class BasicModelManager(models.QuerySet):

    def all(self):
        return self.filter(ativo=True)

    def filter(self, *args, **kwargs):
        kwargs.update(dict(ativo=True))
        return super().filter(*args, **kwargs)