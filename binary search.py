def search(listb, n):
    listb.sort()  # Ensure the list is sorted before searching
    l = 0
    u = len(listb) - 1

    while l <= u:
        mid = (l + u) // 2

        if listb[mid] == n:
            return mid  # Return the index if found
        elif listb[mid] < n:
            l = mid + 1  # Update l to mid + 1 to search in the right half
        else:
            u = mid - 1  # Update u to mid - 1 to search in the left half
    
    return -1  # Return -1 if not found

# Example usage
listb = [21, 5, 6, 987, 25, 23, 5]
n = 21

pos = search(listb, n)
if pos != -1:
    print(f"Found at index {pos}")
else:
    print("Not found")
