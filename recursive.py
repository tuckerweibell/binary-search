

# Recursive Binary Search Function
# Takes args (Array, left element index, right element index, target)
def search(array, l, r, t):

# Calculate middle of range
    m = int(l+(r-l)/2)
# If out of range bounds return Not Found.
    if l > r:
        return ("Not Found")
# If target is equal to middle value return middle index
    if t == array[m]:
        return m
# If target is less that middle value return search on bottom half
    elif t < array[m]:
        return search(array, l, m-1, t)
# If target is larger that middle value return search on top half
    else:
        return search(array, m+1, r, t)

# Only execute this if run as a script.
if __name__ == "__main__":
    array = [1,2,3,4,5,6,7,8,9,10]
    t = 9
    print(f"Index is: {search(array, 0, len(array)-1, t)}")
