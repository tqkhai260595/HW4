import math

def draw_circle(radius):
    for y in range(2 * radius, -1, -1):
        for x in range(0, 4 * radius + 1):
            dist = math.sqrt((x - 2 * radius) ** 2 + (y - radius) ** 2)
            if dist > radius - 0.5 and dist < radius + 0.5:
                print("*", end="")
            else:
                print(" ", end="")
        print()

def main():
    print("This is a circle (2, 2)")
    draw_circle(6)  # Increase the radius to make a larger circle

if __name__ == "__main__":
    main()

