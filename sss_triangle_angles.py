import math
import statistics
R = 6371000 #radius of the earth


def angle_calc(rtk, base_deca_tag, rover_deca_tag):
    #              /\
    #             /  \
    #      base  /    \  rover
    #           /      \
    #          /________\
    #               rtk
    rtk_base_angle = sss_triangle_angle_calc(rover_deca_tag, base_deca_tag, rtk)
    rtk_rover_angle = sss_triangle_angle_calc(base_deca_tag, rover_deca_tag, rtk)
    base_rover_angel = sss_triangle_angle_calc(rtk, base_deca_tag, rover_deca_tag)
    return rtk_base_angle, rtk_rover_angle, base_rover_angel

def sss_triangle_angle_calc(a,b,c):
    a_squared = math.pow(a,2)
    b_squared = math.pow(b,2)
    c_squared = math.pow(c,2)
    argument = (b_squared + c_squared - a_squared)/(2*b*c)
    angle = math.degrees(math.acos(argument))
    return angle
def stats(distance_array):
    return statistics.mean(distance_array)

def gps_to_cartesian( latitude, longitude):
    latitude = math.radians(latitude)
    longitude = math.radians(longitude)
    x = R*math.cos(latitude)*math.cos(longitude)
    y = R*math.cos(latitude)*math.sin(longitude)
    z = R*math.sin(latitude)
    return x, y, z

def cartesion_to_gps(x, y, z):
    latitude = math.degrees(math.asin(z/R))
    longitude = math.degrees(math.atan2(y,x))
    return latitude, longitude

def trilateration(rtk, rad1, rad2):
    # rad1 is the distance from the base station to the object of interest
    # rad1 should be place at (0,0) on the cartesion plane
    #rad2 is a similar measurement but it sould be placed on the x axis
    # based on the distance it is from the base station at (rtk,0) on the 
    #cartesion plane
    x =(math.pow(rad1,2) - math.pow(rad2,2) + math.pow(rtk,2))/(2*rtk)
    y_plus = math.sqrt(math.pow(rad1,2) - math.pow(x,2))
    y_minus = -math.sqrt(math.pow(rad1,2) - math.pow(x,2))
    return x, y_plus, y_minus
    

if __name__ == '__main__':
    #a = 7
    #b = 6
    #c = 8
    #print(str(angle_calc(a,b,c)))
   # a = 1, 2, 3, 4, 5, 6
    #print(str(stats(a)))
    lat = 40.7649
    lon = 111.8421
    a = gps_to_cartesian(lat,lon)
    print(str(a))
    
    print(str(cartesion_to_gps(a[0],a[1],a[2])))
    rad1 = 3
    rad2 = 5
    rtk = -4
    print(str(trilateration(rtk,rad1,rad2)))