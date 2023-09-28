nums = [1, 2, 3]

# Mala manera de realizar el desempaquetado
# primero = nums[0]
# segundo = nums[1]
# tercero = nums[2]

nums2 = list(range(1, 11))
primero, segundo, *otros, pen_u, ultimo = nums2
print(nums2)
print(primero, segundo, otros, pen_u, ultimo)
