from django.db import models

__all__ = (
    'InstagramUser',
)


class InstagramUser(models.Model):
    name = models.CharField(max_length=30)
    # symmetrical=False 옵션으로
    follower = models.ManyToManyField(
        'self',
        symmetrical=False,
        blank=True,
    )

    def __str__(self):
        return self.name
