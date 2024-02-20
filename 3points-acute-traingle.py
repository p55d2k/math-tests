import random
import math
import time

def is_acute_triangle(p1, p2, p3):
    # get 3 random points on the unit circle
    a = math.dist(p2, p3)
    b = math.dist(p1, p3)
    c = math.dist(p1, p2)

    # calculate the angles of the triangle using the law of cosines
    angles = []
    for sides in [(a, b, c), (b, c, a), (c, a, b)]:
        angle = math.acos((sides[0]**2 + sides[1]**2 - sides[2]**2) / (2 * sides[0] * sides[1]))
        angles.append(angle)
    
    # check if all angles are less than 90 degrees
    return all(angle < math.pi/2 for angle in angles)

def main():
    num_points = 3
    num_acute_triangles = 0
    
    sample_size = int(input("Enter the number of tests: "))
    circle_size = 2 * math.pi

    for i in range(sample_size):
        # generate random points on the unit circle
        points = []
        for _ in range(num_points):
            angle = random.uniform(0, circle_size)
            x = math.cos(angle)
            y = math.sin(angle)
            points.append((x, y))
        
        # check if the triangle formed by the points is acute
        acute = is_acute_triangle(*points)
        if acute:
            num_acute_triangles += 1
        
        # print the points to 2dp each and whether the triangle is acute
        # print(f"Points: {points}, Acute: {acute}")
        print(f"Trial {i+1} | Points: {[(round(x, 2), round(y, 2)) for x, y in points]} | Acute: {acute}")
    
    probability = num_acute_triangles / sample_size
    
    # print results
    time.sleep(2)
    
    print("\033c")
    print(f"Sample size: {sample_size}")
    print(f"Number of acute triangles: {num_acute_triangles}")
    print(f"Fraction of those forming an acute triangle: {probability:.4f}")
    
    time.sleep(5)

main()