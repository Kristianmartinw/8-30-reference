# String and length
print('Hello')
print(len('Hello'))

# String Indexing
print('Hello'[0])
print('Hello'[-1])
print('Hello'[0:4])
print('Hello'[:4])  # Returns the same as above
# Starts at beginning and omits the amount of second number
print('Hello'[0:-2])
print('Hello'[:-2])

# String Index Errors
print('Error'[5:1])  # Will return empty string
# print('Error'[5]) # No 5th index so will return IndexError
print('Error'[5:])  # Ranges don't error will return empty string
print('Error'[:5])  # Ranges don't error will return full word

# Find String Index
print('Indexing'.index('x'))
# print('Indexing'.index('y')) # Will result in ValueError since y doesnt exist
print('Indexing'.count('n'))  # Finds reoccurances for letter (case sensitive)

# String concatenation
print('Sun' + 'day')
print('A'+'h'*6)  # Makes the string repeat x amount of times

# Format
pokemon = 'Squirtle'
digimon = 'Gabumon'
print('Who is cooler, {0} or {1}'.format(pokemon, digimon))
print(f'Who is cooler, {digimon} or {pokemon}')

# More methods
print(pokemon.upper())
print(pokemon.lower())
print(pokemon.isupper())
print(pokemon.islower())
print(pokemon.upper().isupper())
print(pokemon.lower().islower())
print(pokemon.startswith('Squirt'))
print(pokemon.endswith('mon'))
print(pokemon.split('l'))
print('-'.join(['poke', 'mon']))
