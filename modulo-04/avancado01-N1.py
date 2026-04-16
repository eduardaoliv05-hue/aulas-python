bases = [1,2,3,4,5,6,7,8,9,10]
print(f"\n{'  ':<2} {'¹':>3} {'²':>3} {'³':>3} {'⁴':>3} {'⁵':>3}{'⁶':>3} {'⁷':>3} {'⁸':>3} {'⁹':>3} {'¹⁰':>3}")
for i, base in enumerate(bases, 1):
        print(f"{i}|{base:>4}{base*2:>4}{base*3:>4}{base*4:>4}{base*5:>4}{base*6:>4}{base*7:>4}{base*8:>4}{base*9:>4}{base*10:>4}")
print("")