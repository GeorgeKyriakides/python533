# =============================================================================
# HELLO WORLD
# =============================================================================
print('hello world')

print("hello world")

# =============================================================================
# VARIABLE TYPES
# =============================================================================
int_type = 4
float_type = 4.0
string_type = 'four'
bool_type = True

print('Our Variables')
print(int_type)
print(float_type)
print(string_type)
print(bool_type)

# =============================================================================
# TYPE CHECKING
# =============================================================================

print('Our Variables Types')
print(type(int_type))
print(type(float_type))
print(type(string_type))
print(type(bool_type))

print('Checking Variables Types')
print(int_type is int)
print(float_type is float)
print(string_type is str)
print(bool_type is bool)

print('Checking Variables Types Correctly')
print(type(int_type) is int)
print(type(float_type) is float)
print(type(string_type) is str)
print(type(bool_type) is bool)

# =============================================================================
# OPS
# =============================================================================


int_int = int_type+int_type
float_float = float_type+float_type
string_string = string_type+string_type
int_float = int_type+float_type


print('int+int=', int_int)
print('float+float=', float_float)
print('string+string=', string_string)
print('int+float=', int_float)

print('Bools')
print('True And False (True&False)=',True & False)
print('True Or False (True|False)=',True | False)


# =============================================================================
# STRINGS
# =============================================================================

the_string = 'string'
print(the_string)

the_other_string = "string"
print(the_other_string)

the_number_string = '4'
print(the_number_string)
print(the_number_string+the_number_string)

number_from_string = float(4)
print(number_from_string)
print(number_from_string+number_from_string)


# =============================================================================
# TUPLES LISTS
# =============================================================================

a_tuple = (1, 2, 3, 4)
a_list = [1, 2, 3, 4]

a_tuple[0] = 1
a_list[0] = 1

# SLICING
a_tuple[1:]
a_list[1:]

a_tuple[:1]
a_list[:1]

a_tuple[-1]
a_list[-1]

a_tuple[-1:]
a_list[-1:]

a_tuple[:-1]
a_list[:-1]

