message = 'It was a bright cold day in April, and the clock were sriking thirteen.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] += 1

print(count)
