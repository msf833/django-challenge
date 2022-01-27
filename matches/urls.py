from rest_framework import routers
from .views import MatchView

app_name = "Match"


router = routers.DefaultRouter()
router.register("", MatchView , basename="Match")

urlpatterns = router.urls
