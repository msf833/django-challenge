from rest_framework import routers
from .views import StadiumView

app_name = "stadium"


router = routers.DefaultRouter()
router.register("", StadiumView , basename="Stadium")

urlpatterns = router.urls
