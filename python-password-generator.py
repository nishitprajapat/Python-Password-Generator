upper_case = "ABCDEFGHIJKLMNOPQRSUVWXYZ"
lower_case = "abcdefghijklmnopqrstuvwxyz"
symbol = "<>/\\~!@#$%^&*()_- "
number = "1234567890"

all = upper_case + symbol + number + lower_case

length = 20
amount = 10

for i in range(amount):
    password = "".join(random.sample(all,length))
    print(password)
