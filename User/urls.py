
from django.urls import path,include
from User import views
app_name="User"



urlpatterns = [
    path('District/',views.District, name="District"),
    path('deletedistrict/<int:did>',views.DeleteDistrict,name="DeleteDistrict"),
    path('Updatedis/<int:uid>' , views.Updatedis,name="Updatedis"),


    path('Category/',views.Category, name="Category"),
    path('deletecategory/<int:did>',views.DeleteCategory,name="DeleteCategory"),
    path('Updatecat/<int:uid>' , views.Updatecat,name="Updatecat"),
    

    path('Place/', views.placeInsertSelect,name="placeInsertSelect"),
    path('delPlace/<int:did>', views.delPlace,name="delPlace"),
    path('placeupdate/<int:eid>',views.placeupdate,name="placeupdate"),


]

