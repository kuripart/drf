from rest_framework import routers
from demo import api_views


router = routers.DefaultRouter()
router.register(r'basic', api_views.BasicViewset)