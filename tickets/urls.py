from rest_framework import routers
from .views import TicketView

app_name = "Ticket"


router = routers.DefaultRouter()
router.register("", TicketView , basename="Ticket")

urlpatterns = router.urls
