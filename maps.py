# -*- coding: utf-8 -*-
"""Print the following (using "print").
1. A list of all cities in the USA in
alphabetic order.
2. All cities in Asia, in alphabetic
order, next to the name of the country.
In your output, label each answer with a number
so it looks like this:
1
American City
American City
2
Asian City - Country
Asian City - Country"""

locations = {'North America': {'USA': ['Mountain View', 'Atlanta']},\
             'Asia': {'India': ['Bangalore'], 'China': ['Shanghai']},\
             'Africa': {'Egypt': ['Cairo']}\
             }

print '1'
print sorted(locations['North America']['USA'])[0]
print sorted(locations['North America']['USA'])[1]

print '2'
cities = []
for country, city in locations['Asia'].iteritems():
    cities.append([city[0], country])
print sorted(cities)[0][0], ' - ', sorted(cities)[0][1]
print sorted(cities)[1][0], ' - ', sorted(cities)[1][1]


"""Write a HashTable class that stores strings
in a hash table, where keys are calculated
using the first two letters of the string."""

class HashTable(object):
    def __init__(self):
        self.table = [None]*10000

    def store(self, string):
        """Input a string that's stored in 
        the table."""
        hash_value = self.calculate_hash_value(string)
        if hash_value != -1:
            if self.table[hash_value] != None:
                self.table[hash_value].append(string)
            else: 
                self.table[hash_value] = [string]

    def lookup(self, string):
        """Return the hash value if the
        string is already in the table.
        Return -1 otherwise."""
        hash_value= self.calculate_hash_value(string)
        if hash_value != -1:
            if self.table[hash_value] != None:
                if string in self.table[hash_value]:
                    return hash_value
        return -1

    def calculate_hash_value(self, string):
        """Helper function to calulate a
        hash value from a string."""
        if len(string) > 2:
            return ord(string[0]) * 100 + ord(string[1])
        return -1

# Setup
hash_table = HashTable()

# Test calculate_hash_value
# Should be 8568
print hash_table.calculate_hash_value('UDACITY')

# Test lookup edge case
# Should be -1
print hash_table.lookup('UDACITY')

# Test store
hash_table.store('UDACITY')
# Should be 8568
print hash_table.lookup('UDACITY')

# Test store edge case
hash_table.store('UDACIOUS')
# Should be 8568
print hash_table.lookup('UDACIOUS')
