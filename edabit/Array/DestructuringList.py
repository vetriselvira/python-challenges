arr = ["cars", "planes", ["trains", ["motorcycles"]]]

# trans1 = arr[0]
# trans2 = arr[1]
# trans3 = arr[2][0]
# trans4 = arr[2][1][0]
trans1,trans2,[trans3,[trans4 ]] = arr

print(trans1) # outputs "cars"
print(trans2) # outputs "planes"
print(trans3) # outputs "trains"
print(trans4) # outputs "motorcycles"