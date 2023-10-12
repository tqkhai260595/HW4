def my_steps(n):
  if n <= 1: 
    return 1

  ways = [0] * (n + 1)
  ways[1] = 1
  ways[2] = 2

  for i in range(3, n + 1):
    ways[i] = ways[i - 1] + ways[i - 2]

  return ways[n]

def print_ways(n):

  print(f"Input: {n}")
  
  total_ways = my_steps(n)

  print(f"Output: {total_ways}")

  print("Reason: Here are the ways to climb the ladder:")
  
  if n == 2:
    print("1. 1 step + 1 step")
    print("2. 2 steps")

  elif n == 3:
    print("1. 1 step + 1 step + 1 step")
    print("2. 2 steps + 1 step") 
    print("3. 1 step + 2 steps")
  
  else:
    _print_ways(n, n-2, "", 2, 2)
    _print_ways(n, n-1, "", 3, 3)

if __name__ == "__main__":

  n = int(input("Enter number of steps: "))

  if 1 <= n <= 25:
    print_ways(n)
  else:
    print("Enter number between 1-25")
