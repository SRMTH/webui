from django.db import models

from io import BytesIO
import qrcode


class Motor(models.Model):
    motor_key = models.CharField(max_length=100)
    current_id = models.IntegerField(null=True, blank=True)
    pyplot_support = models.BooleanField(null=True, blank=True)
    sdk_support = models.BooleanField(null=True, blank=True)
    wizard_support = models.BooleanField(null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    qr_code = models.BinaryField(null=True)

    def generate_qr_code(self):
        im = qrcode.make(self.pk)
        o = BytesIO()
        im.save(o, im.format)
        self.qr_code = o.getvalue()

    def save(self, *args, **kwargs):
        self.generate_qr_code()
        super().save(*args, **kwargs)

    def __str__(self):
        return "#{} - {}".format(self.pk, self.motor_key)
