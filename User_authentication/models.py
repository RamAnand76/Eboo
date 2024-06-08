from django.db import models
from django.contrib.auth import get_user_model
import uuid

# Create your models here.
User = get_user_model()

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    profileimg = models.ImageField(upload_to="profile_images", default="blank-profile-pic.jpeg")
    location = models.CharField(max_length=100, blank=True)
    is_verified = models.BooleanField(default=False)
    is_reader = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_author = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username