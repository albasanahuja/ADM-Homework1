# PROBLEM 1

# INTRODUCTION
#Say "Hello, World!" With Python
if __name__ == '__main__':
    print("Hello, World!")

import math
import os
import random
import re
import sys

#Python If-Else
if __name__ == '__main__':
    n = int(input().strip())
if n % 2 != 0:
    print("Weird")
elif 2 <= n <= 5:
    print("Not Weird")
elif 6<= n <= 20:
    print("Weird")
else:
    print("Not Weird")

#Arithmetic Operators
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a+b)
    print(a-b)
    print(a*b)

#Python: Division
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a//b)
    print(a/b)

#Loops
if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i**2)
      
#Write a function
def is_leap(year):
    leap = False
        
    # Write your logic here
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False   
    return leap

year = int(input())
print(is_leap(year))

#Print Function
if __name__ == '__main__':
    n = int(input())
    for i in range(1, n + 1):
        print(i, end='')

#BASIC DATA TYPES
#List Comprehensions
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    print([[i, j, k]
        for i in range(x + 1)
        for j in range(y + 1)
        for k in range(z + 1)
        if i + j + k != n])

#Find the Runner-Up Score!
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    scores = sorted(set(arr))
    print(scores[-2])   

#Nested Lists
if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    scores = sorted(set(student[1] for student in students))
    second_lowest = scores[1]

    names = sorted(student[0] for student in students if student[1] == second_lowest)

    for name in names:
        print(name)
      
#Finding the percentage
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    marks = student_marks[query_name]
    average = sum(marks) / len(marks)
    print(f"{average:.2f}")

#STRINGS
#sWAP cASE
def swap_case(s):
    return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
  
#String Split and Join
def split_and_join(line):
    # write your code here
    a = line.split(" ")
    return "-".join(a)
    
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
  
#What's Your Name?
def print_full_name(first, last):
    print(f"Hello {first} {last}! You just delved into python.")

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
  
#Mutations
def mutate_string(string, position, character):
    return string[:position] + character + string[position + 1:]

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

#Find a string
def count_substring(string, sub_string):
    count = 0
    for i in range(len(string) - len(sub_string) + 1):
        if string[i:i + len(sub_string)] == sub_string:
            count += 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
  
#String Validators
if __name__ == '__main__':
    s = input()

    print(any(c.isalnum() for c in s))
    print(any(c.isalpha() for c in s))
    print(any(c.isdigit() for c in s))
    print(any(c.islower() for c in s))
    print(any(c.isupper() for c in s))

#Text Alignment
thickness = int(input())
c = 'H'

# Top Cone
for i in range(thickness):
    print((c * i).rjust(thickness - 1) + c + (c * i).ljust(thickness - 1))

# Top Pillars
for i in range(thickness + 1):
    print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))

# Middle Belt
for i in range((thickness + 1) // 2):
    print((c * thickness * 5).center(thickness * 6))

# Bottom Pillars
for i in range(thickness + 1):
    print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))

# Bottom Cone
for i in range(thickness):
    print(((c * (thickness - i - 1)).rjust(thickness) + c +
           (c * (thickness - i - 1)).ljust(thickness)).rjust(thickness * 6))
  
#Text Wrap
import textwrap

def wrap(string, max_width):
    return textwrap.fill(string, max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

#Designer Door Mat
if __name__ == '__main__':
    n, m = map(int, input().split())

    for i in range(1, n, 2):
        pattern = '.|.' * i
        print(pattern.center(m, '-'))

    print('WELCOME'.center(m, '-'))

    for i in range(n - 2, 0, -2):
        pattern = '.|.' * i
        print(pattern.center(m, '-'))

#String Formatting
def print_formatted(number):
    # your code goes here
    width = len(bin(number)[2:])

    for i in range(1, number + 1):
        decimal = str(i)
        octal = oct(i)[2:]
        hexadecimal = hex(i)[2:].upper()
        binary = bin(i)[2:]

        print(decimal.rjust(width), octal.rjust(width),
              hexadecimal.rjust(width), binary.rjust(width))
              
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
  
#Alphabet Rangoli
def print_rangoli(size):
    # your code goes here
    import string
    alphabet = string.ascii_lowercase
    lines = []

    for i in range(size):
        letters = alphabet[size - 1:size - i - 1:-1] + alphabet[size - i - 1:size]
        row = '-'.join(letters)
        lines.append(row.center(4 * size - 3, '-'))

    print('\n'.join(lines + lines[-2::-1]))
    
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

#Capitalize!
import math
import os
import random
import re
import sys

def solve(s):
    return ' '.join(word.capitalize() for word in s.split(' '))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()

#The Minion Game
def minion_game(string):
    vowels = 'AEIOU'
    kevin = 0
    stuart = 0

    for i in range(len(string)):
        if string[i] in vowels:
            kevin += len(string) - i
        else:
            stuart += len(string) - i

    if kevin > stuart:
        print("Kevin", kevin)
    elif stuart > kevin:
        print("Stuart", stuart)
    else:
        print("Draw")
        
if __name__ == '__main__':
    s = input()
    minion_game(s)

#Merge the Tools!
def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        substring = string[i:i + k]
        result = ""

        for char in substring:
            if char not in result:
                result += char

        print(result)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

#SETS
#Introduction to Sets
def average(array):
    # your code goes here
    distinct_heights = set(array)
    return round(sum(distinct_heights) / len(distinct_heights), 3)
    
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
  
#Symmetric Difference
if __name__ == '__main__':
    m = int(input())
    a = set(map(int, input().split()))

    n = int(input())
    b = set(map(int, input().split()))

    result = sorted(a.symmetric_difference(b))

    for num in result:
        print(num)
      
#No Idea!
if __name__ == '__main__':
    n, m = map(int, input().split())
    array = list(map(int, input().split()))
    set_a = set(map(int, input().split()))
    set_b = set(map(int, input().split()))

    happiness = 0

    for num in array:
        if num in set_a:
            happiness += 1
        elif num in set_b:
            happiness -= 1

    print(happiness)
  
#Set .add()
if __name__ == '__main__':
    n = int(input())
    countries = set()

    for _ in range(n):
        country = input().strip()
        countries.add(country)

    print(len(countries))
  
#Set .discard(), .remove() & .pop()
n = int(input())
s = set(map(int, input().split()))
N = int(input())

for _ in range(N):
    args = input().split()
    if args[0] == "pop":
        s.pop()
    else:
        getattr(s, args[0])(int(args[1]))

print(sum(s))

#Set .union() Operation
n_eng = int(input())
eng_subs = set(input().split())
n_fren = int(input())
fren_subs = set(input().split())

print(len(eng_subs.union(fren_subs)))

#Set .intersection() Operation
n_eng = int(input())
eng_subs = set(input().split())
n_fren = int(input())
fren_subs = set(input().split())

print(len(eng_subs.intersection(fren_subs)))

#Set .difference() Operation
n_eng = int(input())
eng_subs = set(input().split())
n_fren = int(input())
fren_subs = set(input().split())

print(len(eng_subs.difference(fren_subs)))

#Set .symmetric_difference() Operation
n_eng = int(input())
eng_subs = set(input().split())
n_fren = int(input())
fren_subs = set(input().split())

print(len(eng_subs.symmetric_difference(fren_subs)))

#Set Mutations
n_a = int(input())
set_a = set(map(int, input().split()))
n_ops = int(input())

for _ in range(n_ops):
    op_name, _ = input().split()
    other_set = set(map(int, input().split()))
    getattr(set_a, op_name)(other_set)

print(sum(set_a))

#The Captain's Room
if __name__ == '__main__':
    k = int(input())
    rooms = list(map(int, input().split()))

    unique_rooms = set(rooms)
    captain_room = (sum(unique_rooms) * k - sum(rooms)) // (k - 1)

    print(captain_room)

#Check Subset
t = int(input())

for _ in range(t):
    n_a = input()
    set_a = set(input().split())
    n_b = input()
    set_b = set(input().split())
    
    print(set_a.issubset(set_b))

#Check Strict Superset
set_a = set(input().split())
n = int(input())

print(all(set_a > set(input().split()) for _ in range(n)))

#COLLECTIONS
#collections.Counter()
from collections import Counter

num_shoes = int(input())
shoe_inventory = Counter(input().split())
num_customers = int(input())

total_earned = 0

for _ in range(num_customers):
    size, price = input().split()
    if shoe_inventory[size] > 0:
        total_earned += int(price)
        shoe_inventory[size] -= 1

print(total_earned)

#DefaultDict Tutorial
from collections import defaultdict

n, m = map(int, input().split())
d = defaultdict(list)

for i in range(1, n + 1):
    d[input()].append(str(i))

for _ in range(m):
    word = input()
    if word in d:
        print(" ".join(d[word]))
    else:
        print("-1")

#Collections.namedtuple()
from collections import namedtuple

n, Student = int(input()), namedtuple('Student', input().split())
marks = [int(Student(*input().split()).MARKS) for _ in range(n)]
print(f"{sum(marks) / n:.2f}")

#Collections.OrderedDict()
from collections import OrderedDict

n = int(input())
ordered_dict = OrderedDict()

for _ in range(n):
    parts = input().split()
    price = int(parts[-1])
    item_name = " ".join(parts[:-1])
    ordered_dict[item_name] = ordered_dict.get(item_name, 0) + price

for item, net_price in ordered_dict.items():
    print(item, net_price)

#Word Order
from collections import OrderedDict

n = int(input())
word_counts = OrderedDict()

for _ in range(n):
    word = input()
    word_counts[word] = word_counts.get(word, 0) + 1

print(len(word_counts))
print(" ".join(map(str, word_counts.values())))

#Collections.deque()
from collections import deque

n = int(input())
d = deque()

for _ in range(n):
    cmd = input().split()
    if len(cmd) == 1:
        getattr(d, cmd[0])()
    else:
        getattr(d, cmd[0])(cmd[1])

print(*d)

#Piling Up!
t = int(input())

for _ in range(t):
    n = int(input())
    blocks = list(map(int, input().split()))
    
    l, r = 0, n - 1
    last_picked = float('inf')
    possible = True
    
    while l <= r:
        if blocks[l] > blocks[r]:
            current = blocks[l]
            l += 1
        else:
            current = blocks[r]
            r -= 1
            
        if current > last_picked:
            possible = False
            break
            
        last_picked = current
        
    print("Yes" if possible else "No")

#Company Logo
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    s = input()
    
    counts = {}
    for char in s:
        counts[char] = counts.get(char, 0) + 1
        
    sorted_chars = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    
    for i in range(3):
        print(f"{sorted_chars[i][0]} {sorted_chars[i][1]}")

#DATE AND TIME
#Calendar Module
import calendar

month, day, year = map(int, input().split())
day_index = calendar.weekday(year, month, day)
print(calendar.day_name[day_index].upper())

#Time Delta
import math
import os
import random
import re
import sys
from datetime import datetime

def time_delta(t1, t2):
    fmt = "%a %d %b %Y %H:%M:%S %z"
    time1 = datetime.strptime(t1, fmt)
    time2 = datetime.strptime(t2, fmt)
    return str(int(abs((time1 - time2).total_seconds())))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()
        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()

#ERRORS AND EXCEPTIONS
#Exceptions
t = int(input())

for _ in range(t):
    a, b = input().split()
    try:
        print(int(a) // int(b))
    except ZeroDivisionError:
        print("Error Code: integer division or modulo by zero")
    except ValueError as e:
        print("Error Code:", e)

#Incorrect Regex
import re
import sys

lines = sys.stdin.read().splitlines()
if lines:
    t = int(lines[0])
    for i in range(1, t + 1):
        if i < len(lines):
            try:
                re.compile(lines[i])
                print("True")
            except re.error:
                print("False")

#BUILT-INS
#Zipped!
n, x = map(int, input().split())
subjects = [list(map(float, input().split())) for _ in range(x)]

for marks in zip(*subjects):
    print(sum(marks) / x)

#Input()
x, k = map(int, input().split())
P = input()
print(eval(P) == k)

#Python Evaluation
eval(input())

#Athlete Sort
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input().strip())

    arr.sort(key=lambda x: x[k])
    
    for row in arr:
        print(*row)

#Any or All
n = int(input())
arr = input().split()
print(all(int(i) > 0 for i in arr) and any(i == i[::-1] for i in arr))

#ginortS
print("".join(sorted(input(), key=lambda c: (c.isdigit(), c.isdigit() and int(c) % 2 == 0, c.isupper(), c))))

#PYTHON FUNCTIONALS
#Map and Lambda Function
cube = lambda x: x**3# complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    if n == 0:
        return []
    if n == 1:
        return [0]
    fibs = [0, 1]
    for _ in range(2, n):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs
    
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))

#Validating Email Addresses With a Filter
import re
def fun(s):
    # return True if s is a valid email, else return False
    return bool(re.match(r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$', s))
def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)

#REGEX AND PARSINGS
#Detect Floating Point Number
import re

t = int(input())
for _ in range(t):
    print(bool(re.match(r'^[+-]?[0-9]*\.[0-9]+$', input())))

#Re.split()
regex_pattern = r"[,.]"	# Do not delete 'r'.

import re
print("\n".join(re.split(regex_pattern, input())))

#RGroup(), Groups() & Groupdict()
import re

s = input()
match = re.search(r'([a-zA-Z0-9])\1', s)
print(match.group(1) if match else -1)

#Re.findall() & Re.finditer()

s = input()
matches = re.findall(r'(?<=[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM])([aeiouAEIOU]{2,})(?=[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM])', s)

if matches:
    print('\n'.join(matches))
else:
    print(-1)

#Re.start() & Re.end()
import re

s = input()
k = input()

pattern = re.compile(k)
m = pattern.search(s)

if not m:
    print("(-1, -1)")
else:
    while m:
        print(f"({m.start()}, {m.end() - 1})")
        m = pattern.search(s, m.start() + 1)

#Regex Substitution
import re

n = int(input())
for _ in range(n):
    print(re.sub(r'(?<= )(&&|\|\|)(?= )', lambda m: 'and' if m.group() == '&&' else 'or', input()))

#Validating Roman Numerals
regex_pattern = r"^M{0,3}(C[MD]|D?C{0,3})(X[LC]|L?X{0,3})(I[VX]|V?I{0,3})$"	# Do not delete 'r'.

import re
print(str(bool(re.match(regex_pattern, input()))))

#Validating phone numbers
import re

n = int(input())
for _ in range(n):
    if re.match(r'^[789]\d{9}$', input()):
        print("YES")
    else:
        print("NO")

#Validating and Parsing Email Addresses
import re
import email.utils

n = int(input())
for _ in range(n):
    name, addr = email.utils.parseaddr(input())
    if re.match(r'^[a-zA-Z][a-zA-Z0-9\-._]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$', addr):
        print(email.utils.formataddr((name, addr)))

#Hex Color Code
import re

n = int(input())
for _ in range(n):
    matches = re.findall(r'(?<!^)#(?:[\da-fA-F]{3}){1,2}(?!\w)', input())
    for match in matches:
        print(match)

#HTML Parser - Part 1
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(f"Start : {tag}")
        for name, value in attrs:
            print(f"-> {name} > {value}")
            
    def handle_endtag(self, tag):
        print(f"End   : {tag}")
        
    def handle_startendtag(self, tag, attrs):
        print(f"Empty : {tag}")
        for name, value in attrs:
            print(f"-> {name} > {value}")

n = int(input())
html_code = "\n".join(input() for _ in range(n))
parser = MyHTMLParser()
parser.feed(html_code)

#HTML Parser - Part 2
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if '\n' in data:
            print(">>> Multi-line Comment")
        else:
            print(">>> Single-line Comment")
        print(data)

    def handle_data(self, data):
        if data != '\n':
            print(">>> Data")
            print(data)

n = int(input())
html_code = "\n".join(input() for _ in range(n))
parser = MyHTMLParser()
parser.feed(html_code)

#Detect HTML Tags, Attributes and Attribute Values
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for name, value in attrs:
            print(f"-> {name} > {value}")
            
    def handle_startendtag(self, tag, attrs):
        print(tag)
        for name, value in attrs:
            print(f"-> {name} > {value}")

n = int(input())
html_code = "\n".join(input() for _ in range(n))
parser = MyHTMLParser()
parser.feed(html_code)

#Validating UID
t = int(input())
for _ in range(t):
    uid = input()
    if (len(uid) == 10 and 
        uid.isalnum() and 
        len(set(uid)) == 10 and 
        sum(1 for c in uid if c.isupper()) >= 2 and 
        sum(1 for c in uid if c.isdigit()) >= 3):
        print("Valid")
    else:
        print("Invalid")

#Validating Credit Card Numbers
import re

n = int(input())
for _ in range(n):
    card = input()
    if re.match(r'^[456](\d{15}|\d{3}-\d{4}-\d{4}-\d{4})$', card) and not re.search(r'(\d)\1{3}', card.replace('-', '')):
        print("Valid")
    else:
        print("Invalid")

#Validating Postal Codes
regex_integer_in_range = r"^[1-9][0-9]{5}$"	# Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"(?=(\d)\d\1)"	# Do not delete 'r'.

import re
P = input()
print (bool(re.match(regex_integer_in_range, P)) and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)

#Matrix Script
import math
import os
import random
import re
import sys

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

decoded_string = "".join(matrix[i][j] for j in range(m) for i in range(n))
print(re.sub(r'(?<=[a-zA-Z0-9])[^a-zA-Z0-9]+(?=[a-zA-Z0-9])', ' ', decoded_string))

#XML
#XML 1 - Find the Score
import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    # your code goes here
    return len(node.attrib) + sum(get_attr_number(child) for child in node)

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))

#XML2 - Find the Maximum Depth
import xml.etree.ElementTree as etree

maxdepth = 0
def depth(elem, level):
    global maxdepth
    # your code goes here
    level += 1
    if level > maxdepth:
        maxdepth = level
    for child in elem:
        depth(child, level)

if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)

#CLOSURES AND DECORATOS
#Standardize Mobile Number Using Decorators
def wrapper(f):
    def fun(l):
        # complete the function
        f([f"+91 {n[-10:-5]} {n[-5:]}" for n in l])
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 
  
#Decorators 2 - Name Directory
import operator

def person_lister(f):
    def inner(people):
        # complete the function
        return [f(person) for person in sorted(people, key=lambda x: int(x[2]))]
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')

#NUMPY
#Arrays
import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    return numpy.array(arr[::-1], float)

arr = input().strip().split(' ')
result = arrays(arr)
print(result)

#Shape and Reshape
import numpy

print(numpy.array(input().split(), int).reshape(3, 3))

#Transpose and Flatten
import numpy

n, m = map(int, input().split())
matrix = numpy.array([input().split() for _ in range(n)], int)

print(numpy.transpose(matrix))
print(matrix.flatten())

#Concatenate
import numpy

n, m, p = map(int, input().split())
arr1 = numpy.array([input().split() for _ in range(n)], int)
arr2 = numpy.array([input().split() for _ in range(m)], int)

print(numpy.concatenate((arr1, arr2)))

#Zeros and Ones
import numpy

shape = tuple(map(int, input().split()))

print(numpy.zeros(shape, dtype=int))
print(numpy.ones(shape, dtype=int))

#Eye and Identity
import numpy
numpy.set_printoptions(legacy='1.13')

n, m = map(int, input().split())
print(numpy.eye(n, m))

#Array Mathematics
import numpy

n, m = map(int, input().split())
a = numpy.array([input().split() for _ in range(n)], int)
b = numpy.array([input().split() for _ in range(n)], int)

print(a + b)
print(a - b)
print(a * b)
print(a // b)
print(a % b)
print(a ** b)

#Floor, Ceil and Rint
import numpy
numpy.set_printoptions(legacy='1.13')

arr = numpy.array(input().split(), float)
print(numpy.floor(arr))
print(numpy.ceil(arr))
print(numpy.rint(arr))

#Sum and Prod
import numpy

n, m = map(int, input().split())
arr = numpy.array([input().split() for _ in range(n)], int)
print(numpy.prod(numpy.sum(arr, axis=0)))

#Min and Max
import numpy

n, m = map(int, input().split())
arr = numpy.array([input().split() for _ in range(n)], int)
print(numpy.max(numpy.min(arr, axis=1)))

#Mean, Var, and Std
import numpy

n, m = map(int, input().split())
arr = numpy.array([input().split() for _ in range(n)], int)

print(numpy.mean(arr, axis=1))
print(numpy.var(arr, axis=0))
print(round(numpy.std(arr), 11))

#Dot and Cross
import numpy

n = int(input())
a = numpy.array([input().split() for _ in range(n)], int)
b = numpy.array([input().split() for _ in range(n)], int)

print(numpy.dot(a, b))

#Inner and Outer
import numpy

a = numpy.array(input().split(), int)
b = numpy.array(input().split(), int)

print(numpy.inner(a, b))
print(numpy.outer(a, b))

#Polynomials
import numpy

p = numpy.array(input().split(), float)
x = float(input())
print(numpy.polyval(p, x))

#Linear Algebra
import numpy

n = int(input())
a = numpy.array([input().split() for _ in range(n)], float)
print(round(numpy.linalg.det(a), 2))

#WARMUP
#Birthday Cake Candles
import math
import os
import random
import re
import sys

def birthdayCakeCandles(candles):
    # Write your code here
    return candles.count(max(candles))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()


#IMPLEMENTATION
#Number Line Jumps
import math
import os
import random
import re
import sys

def kangaroo(x1, v1, x2, v2):
    # Write your code here
    if v1 > v2 and (x2 - x1) % (v1 - v2) == 0:
        return "YES"
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()

#Viral Advertising
import math
import os
import random
import re
import sys

def viralAdvertising(n):
    # Write your code here
    shared = 5
    cumulative = 0
    for _ in range(n):
        liked = shared // 2
        cumulative += liked
        shared = liked * 3
    return cumulative

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()

#RECURSION
#Recursive Digit Sum
import math
import os
import random
import re
import sys

def superDigit(n, k):
    # Write your code here
    total = sum(int(char) for char in str(n)) * k
    while total > 9:
        total = sum(int(char) for char in str(total))
    return total

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()

#SORTING
#Insertion Sort - Part 1
import math
import os
import random
import re
import sys

def insertionSort1(n, arr):
    # Write your code here
    target = arr[-1]
    i = n - 2
    
    while i >= 0 and arr[i] > target:
        arr[i + 1] = arr[i]
        print(*arr)
        i -= 1
        
    arr[i + 1] = target
    print(*arr)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)

#Insertion Sort - Part 2
import math
import os
import random
import re
import sys

def insertionSort2(n, arr):
    # Write your code here
    for i in range(1, n):
        target = arr[i]
        j = i - 1
        
        while j >= 0 and arr[j] > target:
            arr[j + 1] = arr[j]
            j -= 1
            
        arr[j + 1] = target
        print(*arr)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)


# PROBLEM 2

# Birthday Cake Candles
def birthdayCakeCandles(candles):
    return candles.count(max(candles))

# Number Line Jumps (Kangaroo)
def kangaroo(x1, v1, x2, v2):
    if v1 > v2 and (x2 - x1) % (v1 - v2) == 0:
        return "YES"
    return "NO"

# Viral Advertising
def viralAdvertising(n):
    shared = 5
    cumulative = 0
    for _ in range(n):
        liked = shared // 2
        cumulative += liked
        shared = liked * 3
    return cumulative

# Recursive Digit Sum (Super Digit)
def superDigit(n, k):
    total = sum(int(char) for char in str(n)) * k
    while total > 9:
        total = sum(int(char) for char in str(total))
    return total

# Insertion Sort - Part 1
def insertionSort1(n, arr):
    target = arr[-1]
    i = n - 2
    while i >= 0 and arr[i] > target:
        arr[i + 1] = arr[i]
        print(*arr)
        i -= 1
    arr[i + 1] = target
    print(*arr)

# Insertion Sort - Part 2
def insertionSort2(n, arr):
    for i in range(1, n):
        target = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > target:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = target
        print(*arr)
