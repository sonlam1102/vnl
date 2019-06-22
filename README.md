# VNL - Vietnam National Location
A small program for retrieving and managing Vietnamese locations such as: Province, District and Ward using RestAPI

# Technical:  
- Language: Python  
- Framework: Django + Django Rest Framework   

# Step to run    
1. Create mysql database with name **vnl** (can modified by your name, remember to config in ***vnl/settings.py*** file)      
2. Run **pip install -r requirements.txt** to install necessary packages    
3. Run **python manage.py migrate** to apply database models and location master data     
4. Start django server by running **python manage.py runserver**

# API
- **/location/api/v1/provinces** (GET):  Return list of provinces   
- **/location/api/v1/districts** (POST + payload: ***{ "province_id": "id"}*** ): List districts of province   
- **/location/api/v1/wards** (POST + payload: ***{ "district_id": "id"}*** ): List wards of district    