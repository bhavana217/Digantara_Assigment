from django.db import models

class AlgorithmLog(models.Model):
    algorithm_name = models.CharField(max_length=100)
    input_data = models.JSONField()
    output_data = models.JSONField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.algorithm_name} at {self.timestamp}"