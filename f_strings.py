# Formate Strings

person = "Sanjay"
coins = 3

# Old way of formatting was by using %s

message = "\n%s has %s coins left." %(person, coins)

print("Old - " + message)

# New way of formatting

message = "\n{} has {} coins left.".format(person, coins)
print("New - " + message)

message = "\n{1} has {0} coins left.".format(coins, person)
print("New with index - " + message)

message = "\n{person} has {coins} coins left.".format(coins = coins, person = person)
print("New with named param - " + message)

player = {
    'person': 'Sanjay',
    'coins': 3
}

message = "\n{person} has {coins} coins left.".format(**player)
print("New with dictionary - " + message)

# Latest way of fromatting - using f-Strings

message = f"\n {person} has {coins} coins left."
print("New with f-strings - " + message)

message = f"\n {person} has {2*4} coins left."  # Perform an operation
print("New with f-strings - " + message)

message = f"\n {person.upper()} has {2*4} coins left."  # Call a function
print("New with f-strings - " + message)

message = f"\n {player['person']} has {20*14} coins left."  # Perform an operation
print("New with f-strings - " + message)

## Passing formatting options

num = 10
print(f"\n2.25 times {num} is {2.25 * num:.2f}")

for num in range(1,11):
    print(f"2.25 times {num} is {2.25 * num:.2f}")


for num in range(1,11):
    print(f"{num} divided by 2.52 is {num / 2.52:.2%}")