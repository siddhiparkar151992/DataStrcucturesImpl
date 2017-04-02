def water_collected(heights):
    water_collected = 0
    left_height = []
    right_height = []

    temp_max = heights[0]
    for height in heights:
        if (height > temp_max):
            temp_max = height
        left_height.append(temp_max)
        
    print(left_height)
    
    temp_max = heights[-1]
    
    for height in reversed(heights):
        if (height > temp_max):
            temp_max = height
        right_height.insert(0, temp_max)
        
    print(right_height)
    
    for i, height in enumerate(heights):
        water_collected += (min(left_height[i], right_height[i]) - height * b)
    return water_collected

if __name__ == "__main__":
    arr = [3, 3, 4, 4, 4, 2, 3, 1, 3, 2, 1, 4, 7, 3, 1, 6, 4, 1]
    r = 3
    b = 6
    print(water_collected(arr))
    
