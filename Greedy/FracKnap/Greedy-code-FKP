def greedy_fkp(X,capacity):
    
    total_mass=0
    total_value=0
    selected_items=[]
    
    
    for value,mass in X:
        
        if total_mass+mass <= capacity:  #if we can take the whole item 
            selected_items.append((value,mass,1))
            total_mass += mass
            total_value += value         
        else:                                                   #if we cant take the whole item 
            fraction= (capacity-total_mass) / mass
            selected_items.append((value,mass,fraction))        
            total_value+= value * fraction 
            total_mass = capacity
            
            break
        
    return total_value, selected_items


if __name__=="__main__":
    objects = [(60, 10), (100, 20), (120, 30)]  # (value, mass)
    capacity = 50

    # Step 1: Sort objects by decreasing value-to-mass ratio (O(n log n))
    sorted_objects = sorted(objects, key=lambda x: x[0] / x[1], reverse=True)

    # Call the greedy function with the sorted list
    max_value, items_taken = greedy_fkp(sorted_objects, capacity)

    print(f"Maximum value obtained: {max_value}")
    print("Items taken (value, mass, fraction):")
    for item in items_taken:
        print(item)