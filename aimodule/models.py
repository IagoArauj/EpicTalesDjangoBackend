from django.db import models

# Create your models here.

class AIModel(models.Model):
    user_input = models.TextField()
    response = models.TextField()
    temperature = models.FloatField()
    model_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Chat with {self.model_name} ({self.created_at})"
