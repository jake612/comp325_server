import pandas as pd
import numpy as np
from collections import defaultdict
import geopandas
import geopy
import folium
import csv
import math
from geopy.geocoders import Nominatim
import geopy.distance

# Some abreviations dont work
def distance(coords_1, coords_2):
    return(geopy.distance.distance(coords_1, coords_2).miles)

# coords_1 = (52.2296756, 21.0122287)
# coords_2 = (52.406374, 16.9251681)

# Generate location coordinates for the map
def coordinates(l):
    locator = Nominatim(user_agent='myGeocoder')
    loc = locator.geocode(l)
    return(loc.latitude, loc.longitude)


# [ low is better, 1 or 0, Higher is better, 1 or 0]
# [distance from 0, 1 or 0, Distance from range, 1 or 0 ]
# [(val/max_distance) * 25, val * 25, (val/range) * 25, val * 25]
def weighting(c,p_dist,p_qual,p_ins,p_cst,p_spec,p_type,p_fth): # c raw/un-normalized scores for every therapist
    global customer_range
    total_parts = (1/p_dist)+(1/p_qual)+(1/p_ins)+(1/p_cst)+(1/p_spec)+(1/p_type)+(1/p_fth)
    #w = 100/len(c[0])
    
    score = defaultdict(list)
    
    # For all therapists
    for i in range(len(c)):
        val = c[i]
        # Distance
        if(val[0]==-1):
            distance = 0
        else:
            maximum = max(c.keys(), key=(lambda k: c[k][0]))
            # Basically, compared to the farthest therapist, how far is each therapist?
            # 1-calculation because we want to reward closer measurements not farther
            distance = (1-(val[0]/c[maximum][0])) * (p_dist*total_parts)#* w
            
        # Insurance
        # value is either 1 or 0, yes or no
        insurance = val[1]* (p_ins/total_parts) #*w
        
        # Budget Overlaps
        # How large is the overlap of therapist cost and customer range?
        budget = (val[2]/customer_range) * (p_cst/total_parts)#* w
        
        # Qualifications
        # value is either 1 or 0, yes or no
        qualifications = val[3] * (p_qual/total_parts)#* w
        
        # specialities
        # value is either 1 or 0, yes or no
        specialities = val[4] * (p_spec/total_parts)#* w
        
        # faith
        # value is either 1 or 0, yes or no
        faith = val[5] * (p_fth/total_parts)#* w
        
        # approach
        # value is either 1 or 0, yes or no
        approach = val[6] * (p_type/total_parts)#* w
        
        # score for therapist
        score[i]= [distance + insurance + budget + qualifications + specialities + faith + approach]
        
    #return list sorted from highest score to lowest score
    return sorted(score.items(), key=lambda k: k[1], reverse=True)

def results(df, ranking, num_results):
    return_string = ""
    if(num_results>len(ranking) or num_results<1):
        num_results = len(ranking)
    for i in range(num_results):
        num = ranking[i][0]
        return_string = return_string + str(df['name'][num]) + ':\n' + str(df['street'][num]) + ', ' + str(df['locality'][num]) + '\n' + str(df['insurance'][num]) + '\n' + 'cost: ' + str(df['low_cost'][num]) + '-' + str(df['high_cost'][num]) + '\n' + str(df['titles'][num]) + '\n' + str(df['specialities'][num]) + '\n' + str(df['treatment-approach'][num]) + '\n\n'
    return return_string

def IMDAMAP(num_suggestions, ranking, df):
    if (num_suggestions > len(ranking) or num_suggestions < 1):
        num_suggestions = len(ranking)

    map1 = folium.Map(
        location=[35.913200, -79.055847],
        tiles='cartodbpositron',
        zoom_start=12,
    )

    def format_map_info(df, i):
        div = '<div id="poppingup" style = "min-width: 300px;">'
        content = '<p>' + df['name'][i] + '</p><p>' + df['street'][index] + ', ' + df['locality'][index] + ', ' + \
                  df['region'][index]
        return div + content + '</p></div>'

    for i in range(num_suggestions):

        index = ranking[i][0]
        try:
            lat = df['lat'][i]
            long = df['long'][i]
            if math.isnan(lat) or math.isnan(long):
                lat, long = coordinates(df['street'][index] + ', ' + df['locality'][index] + ', ' + df['region'][index])
            df.apply(lambda row: folium.Marker(location=[lat, long], popup=format_map_info(df, index)).add_to(map1),
                     axis=1)
        except:
            print('Location Incomplete')
    #             if(not pd.isnull(df['Street'][index])):
    #                 loc += df['Street'][index]
    #             if(not pd.isnull(df['Locality'][index])):
    #                 loc = loc + ', ' + df['Locality'][index]
    #             if(not pd.isnull(df['Region'][index])):
    #                 loc += df['Region'][index]

    map_name = 'map.html'
    map1.save(map_name)
    return map_name


def get_rank_info_and_map(dict_fields):
    df = pd.read_csv('info.csv')

    therapists = df.shape[0] # The number of therapists in the data frame
    criteria = defaultdict(list) # Will list scores for each therapists accross all measured categories
    customer_range = 0
    criteria_key = ['distance','insurance','budget','qualifications','specialities','faith','treatment-approach']
# Inputs:
    # Address
    # Insurance
    # MinBudget
    # MaxBudget
    # Qualifications
    # address, insurance, minCost, maxCost, qualifications
    def best_match(address, insurance, minCost, maxCost, qualifications, specialities, faith, approach, p_dist, p_qual,p_ins,p_cst,p_spec,p_type,p_fth):
        locator = Nominatim(user_agent='myGeocoder')
        home_loc = locator.geocode(address)
        home_coords = (home_loc.latitude,home_loc.longitude)
        for i in range(therapists):        
            # Distance
            try:
                dest_coords = (df['lat'][i], df['lon'][i])
                criteria[i].append(distance(home_coords, dest_coords))
            except: # Some abreviations arent working, this is a temporary measure
                #Logical infinity
                criteria[i].append(-1)
           
               
           # Insurance
            try:
                if(insurance in df['insurance'][i]):
                   #Accepted Insurance
                    criteria[i].append(1)
                else:
                   #Not Accepted Insurance
                   criteria[i].append(0)
            except:
               # Accomodate NaNs
                criteria[i].append(0)
               
           
           # Budget
            global customer_range
            customer_range = maxCost-minCost
            try:
                customer = range(minCost,maxCost)
               # print(customer)
               # YES IM CONVERTING TO INTS AND YES ITS TECHNICALLY CHEATING
                therapist = range(int(df['low_cost'][i]),int(df['high_cost'][i]))
               
               #OVERLAP () = customer range, [] = therapist range
                c = set(customer)
                if(maxCost in therapist and minCost in therapist): # [ ( ) ] customer range encompassed
                    overlap = c
                elif(minCost in therapist): # [ ( ] ) therapist contains minCost
                    overlap = c
                elif( df['high_cost'] < maxCost and df['low_cost'] > minCost): # ( [ ] )
                    overlap = c
                else: # Might be too expensive
                    overlap = c.intersection(therapist)            
                criteria[i].append(len(overlap))
               
            except:
               #NaNs
               #Improper ranges
               criteria[i].append(0)
    
               
           # Qualifications
            if(set(qualifications).issubset(set(df['titles'][i]))):
                criteria[i].append(1)
            else:
                criteria[i].append(0)
               
           
           
           # Specialities
            delim = ';'
            try:
                ther_specialities = set(df['specialities'][i].split(delim))
           
            except:
                ther_specialities = set([])
           
            if(set(specialities).issubset(ther_specialities)):
                criteria[i].append(1)
            else:
                criteria[i].append(0)
           
           
           # Faith
            try:
                ther_faith = set(df['faith'][i].split(delim))
            except:
                ther_faith = set([])
            if(len(set(faith)) == 0 or set(faith).issubset(ther_faith)):
                criteria[i].append(1)
            else:
                criteria[i].append(0)
           
           
           # Treatment approach
            try:
                ther_ap = set(df['treatment-approach'][i].split(delim))
            except:
                ther_ap = set([])
            if(set(approach).issubset(ther_ap)):
                criteria[i].append(1)
            else:
                criteria[i].append(0)
              
           #
           # print(criteria[i])
            # Take raw criteria and return the ranking of each therapist
        return(weighting(criteria,p_dist,p_qual,p_ins,p_cst,p_spec,p_type,p_fth))
   
   
    customer_location = dict_fields['address']
    insurance = dict_fields['insurance']
    minimum_cost = int(dict_fields['min_cost'])
    maximum_cost = int(dict_fields['max_cost'])
    qualifications = dict_fields['qualifications']
    specialities = dict_fields['specialities']
    approach = dict_fields['approach']
    p_dist = int(dict_fields['p_dist'])
    p_qual = int(dict_fields['p_qual'])
    p_ins = int(dict_fields['p_ins'])
    p_cst = int(dict_fields['p_cst'])
    p_spec = int(dict_fields['p_spec'])
    p_type = int(dict_fields['p_type'])
    p_fth = 1
    faith = ''
    ranking = best_match(customer_location,insurance,minimum_cost,maximum_cost,qualifications,specialities,faith,approach, p_dist, p_qual, p_ins, p_cst, p_spec, p_type, p_fth)
    results_string = results(df, ranking, 10)
    map_name = IMDAMAP(10, ranking, df)
    return results_string, map_name

if __name__ == '__main__':
    get_rank_info_and_map()
