def road_trip_iterative(stations, capacity):
    n = len(stations) - 1  #destination index
    i = 0                       #starting station index
    while i < n:            
        t = i + 1       #find furthest station from current station
        while t <= n and stations[t] - stations[i] <= capacity:
            t += 1
        t = t - 1       #go back to the last reachable station as t increments to one plus reachable 

        if t == n:          #dest reachable
            break
        else:
                i = t    #refuel at station t and repeat process
    
    return i

if __name__ == "__main__":
    
    stations=[0,100,200,350,400]    #already sorted stations
    #s0=0,s1=100,s2=200,s3=350,s4=400
    
    
    tank_capacity=200
    
    road_trip(stations,tank_capacity)

