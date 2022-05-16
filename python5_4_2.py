def print_reverse(aa):
    bb=len(aa)
    for i in range(bb):
        print(aa[i-bb], end =' ')

print_reverse([1,2,3,4,5])
print_reverse("ABCDEFG")
