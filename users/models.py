from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

User = get_user_model()


# class Achievement(models.Model):
#     name = models.CharField(max_length=255)
#     description = models.TextField()
#
#     def __str__(self):
#         return f"Achievement<{self.pk}> - {self.name}"
#
#     class Meta:
#         verbose_name = 'Достижение'
#         verbose_name_plural = 'Достижения'
#


class Profile(models.Model):
    """
    User Profile model

    Attributes:
        user: A OneToOneField to User.
        achievements: A TextField achievements of a User.
        favorite_subjects: A TextField favorite_subjects of a User.
        about: A TextField about of a User.
    """

    # fixme email is not unique
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    achievements = models.TextField(blank=True, null=True)
    favorite_subjects = models.TextField(blank=True, null=True)
    about = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Дополнительное поле"
        verbose_name_plural = "Дополнительные поля"


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created or not hasattr(instance, "profile"):
        Profile.objects.create(user=instance)
    instance.profile.save()
