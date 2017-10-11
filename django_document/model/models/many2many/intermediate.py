from django.db import models

__all__ = (
    'Idol',
    'Group',
    'Membership',
)


# class IdolManager(models.Manager):
#     pass

class Idol(models.Model):
    name = models.CharField(max_length=30)

    # 오브젝츠 = IdolManager()
    # objects = models.Manager()

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=50)
    debut_date = models.DateField()
    members = models.ManyToManyField(
        Idol,
        through='Membership',
        through_fields=('group', 'idol'),
    )

    def __str__(self):
        return self.name


class Membership(models.Model):
    idol = models.ForeignKey(
        Idol,
        on_delete=models.CASCADE,
        related_name='membership_set'
    )
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    #     # Idol,
    #     # null=True,
    #     # on_delete=models.CASCADE,
    #     # related_name='recommend_membership_set',
    # )
    recommenders = models.ManyToManyField(
        Idol,
        blank=True,
        related_name='recommend_membership_set',
    )
    joined_date = models.DateField()
    is_active = models.BooleanField()

    def __str__(self):
        return f'{self.group.name}' \
               f'{self.idol.name}' \
               f'({self.is_active.name})'
