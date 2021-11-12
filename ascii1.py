# a = 'c8e9aca0c6f2e5f3e8c4efe7a1a0d4e8e5a0e6ece1e7a0e9f3baa0e8eafae3f9e4eafae2eae4e3eaebfaebe3f5e7e9f3e4e3e8eaf9eaf3e2e4e6f2'
# a = 'd4e8e1f4a0f7e1f3a0e6e1f3f4a1a0d4e8e5a0e6ece1e7a0e9f3baa0c4c4c3d4c6fbb9e1e6b3e3b9e4b3b7b7e2b6b1e4b2b6b9e2b1b1b3b3b7e6b3b3b0e3b9b3b5e6fd'
# for i in range(0, len(a), 2):
    # print(chr(int(a[i:i+2], 16)-128), end='')
a = '666c61677b68656c6c6f5f776f726c647d'
for i in range(0, len(a), 2):
    print(chr(int(a[i:i+2], 16)), end='')

# b = a.split(',')

b = '011001010010011001100101'
table = ''.maketrans('01', '10')
b.translate(table)