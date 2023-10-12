def cacti_number(plot):
    # Initialize a variable to keep track of the count
    count = 0

    # Iterate through the rows and columns of the plot
    for i in range(len(plot)):
        for j in range(len(plot[i])):
            # Check if the current plot is empty (0)
            if plot[i][j] == 0:
                # Check if there are no adjacent cacti (horizontally or vertically)
                if (
                    (i == 0 or plot[i - 1][j] == 0) and  # Check above
                    (i == len(plot) - 1 or plot[i + 1][j] == 0) and  # Check below
                    (j == 0 or plot[i][j - 1] == 0) and  # Check left
                    (j == len(plot[i]) - 1 or plot[i][j + 1] == 0)  # Check right
                ):
                    # Increment the count if conditions are met
                    count += 1

    return count

if __name__ == "__main__":
    # Code to execute when the script is run directly
    pass


