from django.contrib import admin

from riverdata.models import GraniteFallsGauge, JordanRoadGauge, VerlotGauge

# Register your models here.
admin.site.register(GraniteFallsGauge)
admin.site.register(JordanRoadGauge)
admin.site.register(VerlotGauge)
