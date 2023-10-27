nums = (1, 2, 3) + (4, 5, 6)
print(nums)

nums2 = tuple([3, 5, 5])
print(nums2)

menosNumeros = nums[:2]
print(menosNumeros)

primero, segundo, *otros = nums
print(primero, segundo, otros)
for n in nums:
    print(n)