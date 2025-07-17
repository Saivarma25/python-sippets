name = "saivarma"
age = 26
height = 5.10

print(f"Name is: {name}", f"Age is: {age}", f"Height is: {height}")
print(type(name), type(age), type(height))

int_var = 10
float_var = 10.0
bool_var = True
str_var = "saivarma"

print(int_var, float_var, bool_var, str_var)
print(type(int_var), type(float_var), type(bool_var), type(str_var))

int_as_int = 10
int_as_str = str(int_as_int)
print(int_as_str, type(int_as_str))

print(isinstance(10, float))
print(isinstance(10.0, int))
print(int_as_int is not int_as_str)

int_str = '25'
int_int = int(int_str)
print(int_int, type(int_int))

len_str = "saivarma"
print(len(len_str))

a, b = "sai", "varma"
c = a + b
print(c, type(c))

d, e, f = c.upper(), c.lower(), c.replace("s", "S")

print(d, e, f)

print(a in c)
print(int_str not in c)

bool_true = True
bool_false = False
print(bool_true + bool_false)
print(bool_true + 10)
print(bool_false + 10)

print(10 > 5, type(10 > 5))

print(bool(0))
print(bool(""))
print(bool("saivarma"))
print(bool(123))
print(123)

print(True == int(1))
print(False == 0)

print(True == True)
print(False == False)

print(10 + 20)
print(20 - 10)
print(20 / 3)
print(20 % 3)
print(20 // 3)
print(2 ** 6)

if 10 > 5 and 9 > 5:
    print("Valid")

if 10 > 5 or 9 != 5:
    print("Valid")

inc_var = 10
inc_var += 10
print(inc_var)
inc_var -= 10
print(inc_var)
inc_var *= inc_var
print(inc_var)
inc_var //= 10
print(inc_var)

print(type(inc_var) == int)
print(isinstance(inc_var, int))
print("10" == inc_var)
print(int("10") == inc_var)