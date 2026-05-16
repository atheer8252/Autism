from django.db import models

# Create your models here.

class AutismSupportPlace(models.Model):

    PLACE_TYPES = [
        ('government', 'حكومي'),
        ('private', 'خاص'),
        ('community', 'مجتمعي'),
    ]

    REGIONS = [
        ('riyadh', 'منطقة الرياض'),
        ('eastern', 'المنطقة الشرقية'),
        ('makkah', 'منطقة مكة المكرمة'),
        ('madinah', 'منطقة المدينة المنورة'),
        ('asir', 'منطقة عسير'),
        ('jazan', 'جازان'),
        ('najran', 'نجران'),
        ('qassim', 'القصيم'),
        ('hail', 'حائل'),
        ('tabuk', 'تبوك'),
        ('jouf', 'الجوف'),
        ('northern_borders', 'الحدود الشمالية'),
        ('bahah', 'الباحة'),
    ]


    name = models.CharField(max_length=200)
    description = models.TextField()
    region = models.CharField(max_length=50,choices=REGIONS)
    address = models.TextField()
    phone_number = models.CharField(max_length=10)
    website = models.URLField(blank=True, null=True)
    place_type = models.CharField(max_length=20,choices=PLACE_TYPES)
    x_position = models.IntegerField()
    y_position = models.IntegerField()


    def __str__(self):
        return self.name
