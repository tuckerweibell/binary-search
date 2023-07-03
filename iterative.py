
# Iterative Binary Search Function
# Args are (Array, target)
def search(array,t):

# Set left and right prior to iteration
    l, r = 0, len(array) - 1
# Iteration while in bounds
    while l <= r:
        # Get middle index of new left right bounds
        m = int(l + (r-l)/2)
        # If middle val is target return middle index
        if array[m] == t:
            return m
        # If target is less than middle index set right bound to middle - 1
        elif t < array[m]:
            r = m-1
        # If target is greater that middle index set left bound to middle + 1
        else:
            l = m+1
    # Return not found if target not in array
    return "Not Found"


# Only run below code if run as a script
if __name__ == "__main__":
    array = [1,2,3,4,5,6,7,8,9,10]
    t = 9
    print(f"Index is: {search(array,t)}")