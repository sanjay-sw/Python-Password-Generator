import random

lower_alphabets = tuple(map(chr, range(ord('a'), ord('z')+1)))
upper_alphabets = tuple(map(chr, range(ord('A'), ord('Z')+1)))
numbers = tuple(map(str, range(0, 10)))
chars = ('!', '@', '#', '$', '%', '&')

Order = (lower_alphabets,
            upper_alphabets,
            numbers,
            chars,
            )

def password_generate(total, sequences):
    r = number_generator(total, len(sequences))

    password = []
    for (population, k) in zip(sequences, r):
        n = 0
        while n < k:
            position = random.randint(0, len(population)-1)
            password += population[position]
            n += 1
    random.shuffle(password)
    
    while repeating(password):
        random.shuffle(password)
        
    return ''.join(password)

def number_generator(total, sequence_number):

    current_total = 0
    r = []
    for n in range(sequence_number-1, 0, -1):
        current = random.randint(1, total - current_total - n)
        current_total += current
        r.append(current)
    r.append(total - sum(r))
    random.shuffle(r)

    return r

def repeating(password):
    """ Check if there is any 2 characters repeating consecutively """
    n = 1
    while n < len(password):
        if password[n] == password[n-1]:
            return True
        n += 1
    return False


print (password_generate(random.randint(6, 30), Order))
