from django.db import models


class Province(models.Model):
    id = models.CharField(max_length=10, null=False, blank=False, primary_key=True)
    name = models.CharField(max_length=255, null=False, blank=False)
    type = models.CharField(max_length=255, null=False, blank=False)

    class Meta:
        db_table = 'province'

    def __str__(self):
        return self.name


class District(models.Model):
    id = models.CharField(max_length=10, null=False, blank=False, primary_key=True)
    name = models.CharField(max_length=255, null=False, blank=False)
    type = models.CharField(max_length=255, null=False, blank=False)
    province = models.ForeignKey(Province, on_delete=models.CASCADE, related_name='districts')

    class Meta:
        db_table = 'district'

    def __str__(self):
        return self.name


class Ward(models.Model):
    id = models.CharField(max_length=10, null=False, blank=False, primary_key=True)
    name = models.CharField(max_length=255, null=False, blank=False)
    type = models.CharField(max_length=255, null=False, blank=False)
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='wards')

    class Meta:
        db_table = 'ward'

    def __str__(self):
        return self.name
