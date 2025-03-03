def road_trip(stations,capacity,i=0):
    
    """ 
    Recursive function that finds where to stop for gas along a trip
    
    stations: sorted list of station distances
    
    capactiy: max distance you can travel on a full tank
    
    i: current station index
    
    
    """
    
    t=i+1
    
    #keep moving t forward while the next station is still within reach 
    while t<len(stations) and (stations[t]- stations[i]) <=capacity:
        t=t+1
        
    # if t has reached len(stations), we've arrived at the final station
    if t==len(stations):
        print(f"Arrived at station{t-1}(distance{stations[-1]})")
        return 
        
        
        
    #otherswise we must stop and refuel at stations (t-1) 
    
    stop_index=t-1
    print(f"Stopping for gas at station{stop_index}(distance {stations[stop_index]})")
    road_trip(stations, capacity, stop_index)


# Example

if __name__ == "__main__":
    
    stations=[0,100,200,350,400]    #already sorted stations
    #s0=0,s1=100,s2=200,s3=350,s4=400
    
    
    tank_capacity=200
    
    road_trip(stations,tank_capacity)

