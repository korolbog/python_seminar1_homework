# Задача 2. Напишите программу для
# проверки истинности утверждения
# -(X ⋁ Y ⋁ Z) = -X ⋀ -Y ⋀ -Z
# для всех значений предикат.

x = 1
y = 1
z = 1

for x in range(2):
    for y in range(2):
        for z in range(2):
            if -(x or y or z) == -x and -y and -z:
                print(f'-({x} v {y} v {z}) = -{x} ʌ -{y} ʌ -{z} {(-(x or y or z)) == (-x and -y and -z)}')
            else:
                print(f'-({x} v {y} v {z}) = -{x} ʌ -{y} ʌ -{z} {(-(x or y or z)) == (-x and -y and -z)}')