from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=255)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    def delete(self, *args, **kwargs):
        if self.project_set.exists():  # verifica projetos relacionados
            raise ProtectedError("Não é possível excluir cliente com projetos relacionados.", self)
        return super().delete(*args, **kwargs)
