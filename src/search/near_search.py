'''
Created on Jun 2, 2015

@author: qiulei
'''

import urllib.request
import json
from search.poi_distribution import poi_type_map


def poi_distribution_newyork():
    
    poi_map = poi_type_map("../../gplace_type_map.txt")

    url_1 = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location='
    url_2 = '&radius=650&key=AIzaSyBxODBMe80kjYwRjNUTY6FymkJ7eHFhWs8'
    
    
    all_poi_types = ["Nightlife Spot","Professional&Other Places","Shops&Services", "Travel&Transport","Arts&Entertainment","Food","Outdoors&Recreation","College&University"]
    
    sw_lat = 40.700478;
    sw_lon = -74.023807;
    ne_lat = 40.768283;
    ne_lon = -73.95409;
        
    lat_offset = (ne_lat - sw_lat)/5;
        
    lon_offset_h = (-73.980150 + 74.023807)/3;
    lon_offset_v = (-73.997745 + 74.023807)/5;
    
    init_lat = sw_lat + lat_offset/2
    init_lon = sw_lon + lon_offset_h/2 + lon_offset_v/2
    
    
    poi_in_neighborhood = [ [0 for i in range(len(all_poi_types))] for i in range(15) ]
    
    for i in range(5):
        for j in range(3):
            lat = init_lat + i*lat_offset
            lon = init_lon + j*lon_offset_h + i*lon_offset_v
            location = str(lat)+','+str(lon)
            site = url_1+location+url_2
            x = urllib.request.urlopen(site)
            json_obj = json.loads(x.read().decode('utf-8'))
            type_val = {}
            for jo in json_obj['results']:
                for ty in jo['types']:
                    if(ty in poi_map):
                        t = poi_map[ty]
                    else:
                        continue
         
                    if(t in type_val):
                        type_val[t] = type_val[t]+1
                    else:
                        type_val[t] = 1
            
            for k in range(len(all_poi_types)):
                if(all_poi_types[k] in type_val):
                    poi_in_neighborhood[3*i+j][k] = type_val[all_poi_types[k]]
                else:
                    poi_in_neighborhood[3*i+j][k] = 0
    
    return poi_in_neighborhood
                
    
    

poi_in_neighborhood = poi_distribution_newyork()
for neigh in poi_in_neighborhood:
    print(neigh)