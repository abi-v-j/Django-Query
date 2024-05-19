from API.db_main_utils import *
def fetch_districts():
    query = "SELECT * FROM User_tbl_district"
    return fetch_all(query)

def fetch_district_by_id(did):
    query = "SELECT * FROM User_tbl_district WHERE id = %s"
    return fetch_one(query, [did])

def insert_district(district_name):
    query = "INSERT INTO User_tbl_district (district_name) VALUES (%s)"
    return insert(query, [district_name])

def update_district(did, district_name):
    query = "UPDATE User_tbl_district SET district_name = %s WHERE id = %s"
    return update(query, [district_name, did])

def delete_district(did):
    query = "DELETE FROM User_tbl_district WHERE id = %s"
    return delete(query, [did])

# Specific utility functions for category
def fetch_categories():
    query = "SELECT * FROM User_tbl_category"
    return fetch_all(query)

def fetch_category_by_id(cid):
    query = "SELECT * FROM User_tbl_category WHERE id = %s"
    return fetch_one(query, [cid])

def insert_category(category_name):
    query = "INSERT INTO User_tbl_category (category_name) VALUES (%s)"
    return insert(query, [category_name])

def update_category(cid, category_name):
    query = "UPDATE User_tbl_category SET category_name = %s WHERE id = %s"
    return update(query, [category_name, cid])

def delete_category(cid):
    query = "DELETE FROM User_tbl_category WHERE id = %s"
    return delete(query, [cid])

# Specific utility functions for place
def fetch_places():
    query = "SELECT  p.id as id, p.place_name,  d.id as district_id,  d.district_name  FROM User_tbl_place p inner join User_tbl_district d on p.district_id = d.id"
    return fetch_all(query)

def fetch_place_by_id(pid):
    query = "SELECT * FROM User_tbl_place WHERE id = %s"
    return fetch_one(query, [pid])

def insert_place(place_name, district_id):
    query = "INSERT INTO User_tbl_place (place_name, district_id) VALUES (%s, %s)"
    return insert(query, [place_name, district_id])

def update_place(pid, place_name, district_id):
    query = "UPDATE User_tbl_place SET place_name = %s, district_id = %s WHERE id = %s"
    return update(query, [place_name, district_id, pid])

def delete_place(pid):
    query = "DELETE FROM User_tbl_place WHERE id = %s"
    return delete(query, [pid])