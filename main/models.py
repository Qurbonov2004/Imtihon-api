from django.db import models



class Xodimlar(models.Model):
    f_name=models.CharField(max_length=255)
    l_name=models.CharField(max_length=255)
    

    class Meta:
        verbose_name='Xodimlar'

    



class Davomat(models.Model):
    employee=models.ForeignKey(Xodimlar, on_delete=models.CASCADE)
    data=models.DateField()

    
    @property
    def day(request):
        
    


