from django.urls import path,include # type: ignore
from .views import book_list,book_id

urlpatterns = [
   
    path("postdata/",book_list),
    path("getdata/<int:id>/",book_id),
    path("deletedata/<int:id>/",book_id),
    path("putdata/<int:id>/",book_id), 
    
]
