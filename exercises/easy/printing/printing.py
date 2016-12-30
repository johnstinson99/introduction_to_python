for i in range(0,10):
    print(str(i).rjust(4) + str(i+i).rjust(4) + str(3*i).rjust(4))

# table square using .rjust()
for a in range(1, 13):
    row_list = []
    for b in range (1, 13):
        row_list.append(str(a * b).rjust(4))
    row_string = ''.join(row_list)
    print(row_string)

# table triangle using .rjust()
for a in range(1, 13):
    row_list = []
    for b in range (1, 13):
        if a >= b:
            row_list.append(str(a * b).rjust(4))
    row_string = ''.join(row_list)
    print(row_string)

# attempting to do the same with floats looks messy
for i in range(1, 10):
    print(str(10/i).rjust(20), 20/i, 30/i)

# instead we can use format()
# {<number of argument, starting at zero>:<total number of digits><format, e.g.  .2f (2dps)  }
print()
for i in range(1, 10):
    print('{0:10d} {1:10.2f} {2:10.2f}'.format(i, 20/i, 30/i))

# using arguments in order without being explicit about position
print()
for i in range(1, 10):
    print('{:10d} {:10.2f} {:10.2f}'.format(i, 20/i, 30/i))

# integers
print()
for i in range(1, 10):
    print('{:10d} {:10d} {:10d}'.format(i, i*2, i*3))