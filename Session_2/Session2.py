# =============================================================================
# INPUT
# =============================================================================

user_input = input('Give me an input: ')

# =============================================================================
# FLOW CONTROL
# =============================================================================

# =============================================================================
# IF
# =============================================================================
if user_input is 'one':
    print(1)
elif user_input is 'two':
    print(2)
else:
    print(3)

# =============================================================================
# WHILE
# =============================================================================
count = 0
while True:
    print(count)
    count += 1
    if count > 10:
        break

count = 0
while count <= 10:
    print(count)
    count += 1

# =============================================================================
# FOR
# =============================================================================

for count in range(11):
    print(count)

# =============================================================================
# FUNCTIONS
# =============================================================================


def my_print(message):
    length = 10
    new_str = ('#'*length)+' '+message+' '+('#'*length)
    print(new_str)

my_print('Hello World')

# SCOPE!!!!!!!!!!!!!!!!
print(length)


def my_print2(message, length=15):
    max_length = 40

    new_str = ('#'*length)+' '+message+' '+('#'*length)

    if len(new_str) > max_length:
        start = int((len(new_str)-max_length)/2)
        new_str = new_str[start:start+max_length]

    print(new_str)


my_print2('Hello World')
my_print2('Hello Bigger World')
my_print2('Hello World and Bigger World', length=30)
# =============================================================================
#  FUNCTION-FUNCTION CALL
# =============================================================================
def truncate_string(string, max_length):
    if len(string) > max_length:
        start = int((len(string)-max_length)/2)
        new_str = string[start:start+max_length]
        return new_str
    return string

def my_print3(message, length=15, symbol='#'):
    max_length = 50

    new_str = (symbol*length)+' '+message+' '+(symbol*length)
    new_str = truncate_string(new_str, max_length)


    print(new_str)

my_print3('Hello World', symbol='*')
my_print3('Hello Bigger World', length=30)
my_print3('Hello World and Bigger World', length=30, symbol='*')

# =============================================================================
# MUKTIPLE RETURN VALUES
# =============================================================================

def get_min_max_mean(list):
    min_ = min(list)
    max_ = max(list)
    avg_ = sum(list)/len(list)

    return min_, max_, avg_

my_list = [45, 4.2, 15, 32]
get_min_max_mean(my_list)

# =============================================================================
# IMPORTS AND __NAME__ == '__MAIN__'
# =============================================================================
from print_4 import my_print4


# =============================================================================
# FILE READING
# =============================================================================
with open('text_file.txt') as file:
    content = file.read()
    print(content)



with open('text_file.txt') as file:
    lines = file.readlines()
    for line in lines:
        print(line)

# =============================================================================
# FILE WRITING
# =============================================================================
buffer = ''

with open('text_file.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        line = line.replace('e','3')
        line = line.replace('a','4')
        line = line.replace('t','7')
        buffer += line

with open('text_file_altered.txt', 'w') as file:
    file.writelines(buffer)
