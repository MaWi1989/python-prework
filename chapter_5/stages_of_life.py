age = 8
if age < 2:
    stage = 'a baby'
elif age < 4:
    stage = 'a toddler'
elif age < 13:
    stage = 'a kid'
elif age < 20:
    stage = 'a teenager'
elif age < 65:
    stage = 'an adult'
elif age >= 65:
    stage = 'an elder'
print("You are " + stage + ".")
