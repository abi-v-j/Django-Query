from django.shortcuts import render, redirect
from API.db_utils import *

def District(request):
    data = fetch_districts()
    if request.method == "POST":
        district_name = request.POST.get("txt_district")
        insert_district(district_name)
        return redirect('User:District')
    return render(request, "User/District.html", {"District": data})

def DeleteDistrict(request, did):
    delete_district(did)
    return redirect("User:District")

def Updatedis(request, uid):
    dis = fetch_district_by_id(uid)
    if request.method == "POST":
        district_name = request.POST.get("txt_district")
        update_district(uid, district_name)
        return redirect("User:District")
    return render(request, "User/District.html", {"disdata": dis})

# Category Views
def Category(request):
    data = fetch_categories()
    if request.method == "POST":
        category_name = request.POST.get("txt_category")
        insert_category(category_name)
        return redirect('User:Category')
    return render(request, "User/Category.html", {"Category": data})

def DeleteCategory(request, did):
    delete_category(did)
    return redirect("User:Category")

def Updatecat(request, uid):
    cat = fetch_category_by_id(uid)
    if request.method == "POST":
        category_name = request.POST.get("txt_category")
        update_category(uid, category_name)
        return redirect("User:Category")
    return render(request, "User/Category.html", {"catdata": cat})

# Place Views
def placeInsertSelect(request):
    districts = fetch_districts()
    data = fetch_places()
    if request.method == "POST":
        place_name = request.POST.get('txtname')
        district_id = request.POST.get('sel_district')
        insert_place(place_name, district_id)
        return redirect("User:placeInsertSelect")
    return render(request, "User/Place.html", {'data': data, "districtdata": districts})

def delPlace(request, did):
    delete_place(did)
    return redirect("User:placeInsertSelect")

def placeupdate(request, eid):
    districts = fetch_districts()
    editdata = fetch_place_by_id(eid)
    if request.method == "POST":
        place_name = request.POST.get("txtname")
        district_id = request.POST.get('sel_district')
        update_place(eid, place_name, district_id)
        return redirect("User:placeInsertSelect")
    return render(request, "User/Place.html", {"editdata": editdata, "districtdata": districts})