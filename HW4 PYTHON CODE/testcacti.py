# testcacti.py

from cacti import cacti_number

def main():
    plot1 = [
        [1, 0, 1, 0, 1],
        [0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0]
    ]
    
    plot2 = [
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0],
        [1, 0, 1, 0, 0, 1]
    ]
    
    print(cacti_number(plot1))
    print(cacti_number(plot2))

if __name__ == "__main__":
    main()

