# Date: 12 Jun 2023
# Author: Joao Romao & Carlos Romao

# Today we're going to cover conditions:
# 1 - Operators
# 2 - Logical Operator
# 3 - conditional structural
# 4 - ternary expressions
# 5 - conditional functions and methods

# 1
var_1 = 3
var_2 = None
# ==
print(f'== : {var_1 == var_2}')
# !=
print(f'!= : {var_1 != var_2}')
# <
# print(f' < : {var_1 < var_2}')
# # >
# print(f' > : {var_1 > var_2}')
# # <=
# print(f'<= : {var_1 <= var_2}')  # menor ou igual
# # >=
# print(f'>= : {var_1 >= var_2}')  # maior ou igual

if var_1 == var_2:
    print(0)
elif 5 != 0:
    print(1)
else:
    print('Nothing...')

# 2 - Logical Operator

# and
if var_1 and var_2:
    print('AND')
else:
    print('Not valid...')
# or
if var_1 or var_2:
    print('OR')
else:
    print('Not valid...')
# not
if not var_1:
    print('NOT VAR')
else:
    print('ELSE NOT...')

# in
