
if __name__ == "__main__":

# Create an empty dictionary called pokedex.
    pokedex = {

    }
# Add the following key, value pairs to the dictionary:

#   'Venosaur': ['Grass', 'Poisen']
#   'Charizard': ['Fire', 'Flying']
#   'Blastoise': ['Water']
    pokedex['Venasaur'] = ['Grass', 'Poison']
    pokedex['Charizard'] = ['Fire', 'Flying']
    pokedex['Blastoise'] = ['Water']
    print(pokedex)
 
# Remove 'Blastoise' from the dictionary.
    del pokedex['Blastoise']
    print(pokedex)