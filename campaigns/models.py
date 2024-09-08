from django.db import models
from safedelete.models import SafeDeleteModel
import random
import string
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Campaign(SafeDeleteModel):
    class CampaignStatus(models.TextChoices):
        ONGOING = "ONGOING", _("Ongoing")
        COMPLETED = "COMPLETED", _("Completed")

    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(
        max_length=255,
        choices=CampaignStatus.choices,
        default=CampaignStatus.ONGOING,
    )
    story = models.TextField()
    invite_link = models.CharField(
        max_length=10,
        default=''.join(random.choices(string.ascii_letters + string.digits, k=10))
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} ({self.id})'


class Note(models.Model):
    campaign = models.ForeignKey(Campaign, on_delete=models.DO_NOTHING, related_name='notes')
    content = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.content[:10]}... ({self.id})'
    
class Player(SafeDeleteModel):
    name = models.CharField(max_length=255)
    campaign = models.ForeignKey(Campaign, on_delete=models.DO_NOTHING)
    player_class = models.CharField(max_length=255)
    level = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} ({self.id})'