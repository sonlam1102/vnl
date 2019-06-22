# VNL - Vietnam National Location
A small program for retrieving and managing Vietnamese locations such as: Province, District and Ward   

# Technical:  
- Language: Python  
- Framework: Django + Django Rest Framework   

# API
- **/location/api/v1/provinces** (GET):  Return list of provinces   
- **/location/api/v1/districts** (POST + payload: ***{ "province_id": "id"}*** ): List districts of province   
- **/location/api/v1/wards** (POST + payload: ***{ "district_id": "id"}*** ): List wards of district       