# percobaan fungsi 8 membuat fungsi dengan or atau and
def is_a_triangle (a, b, c) :
    return a + b > c and b + c > a and c + a > b

print(is_a_triangle(1, 1, 1))
print(is_a_triangle(1, 1, 3)) 