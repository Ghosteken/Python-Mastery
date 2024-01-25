import math

def calculate_triangle_area(base, height):
    area = 0.5 * base * height
    return area

def calculate_sphere_volume(radius):
    volume = (4/3) * math.pi * radius**3
    return volume

def main():
    # Input for the triangle
    base_triangle = float(input("Enter the base of the triangle: "))
    height_triangle = float(input("Enter the height of the triangle: "))

    # Calculate and display the area of the triangle
    area_triangle = calculate_triangle_area(base_triangle, height_triangle)
    print(f"The area of the triangle is: {area_triangle:.2f} square units")

    # Input for the sphere
    radius_sphere = float(input("\nEnter the radius of the sphere: "))

    # Calculate and display the volume of the sphere
    volume_sphere = calculate_sphere_volume(radius_sphere)
    print(f"The volume of the sphere is: {volume_sphere:.2f} cubic units")

if __name__ == "__main__":
    main()
