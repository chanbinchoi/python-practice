import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

print(random.choice(friends))

random_int = random.randint(0, len(friends)-1)
print(friends[random_int])