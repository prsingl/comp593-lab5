'''
Library for interacting with the PokeAPI.
https://pokeapi.co/
'''
import requests

POKE_API_URL = 'https://pokeapi.co/api/v2/pokemon/'

def main():
    # Test out the get_pokemon_info() function
    # Use breakpoints to view returned dictionary
    poke_info = get_pokemon_info("Rockruff")
    return

def get_pokemon_info(pokemon_name):
    """Gets information about a specified Pokemon from the PokeAPI.

    Args:
        pokemon_name (str): Pokemon name (or Pokedex number)

    Returns:
        dict: Dictionary of Pokemon information, if successful. Otherwise None.
    """

    import re
    import requests

    def clean_pokemon_info(pokemon_name):
        names = names.strip()
        names = names.lower()
        names = re.sub(r'[^a-zA-Z0-9\s\-]', '', names) ,
        names =names.replace(' ',' _')
        return names
    
    def fetch_pokemon_data(pokemon_name):
        cleaned_names = clean_pokemon_name(pokemon_name)
        url = f'https://pokeapi.co/api/v2/pokemon/{cleaned_names}'

        try:
            responses = requests.get(url)
            responses.raise_for_status()

            pokemon_data = responses.json()
            return pokemon_data
        
        except requests.RequestException as 0:
            print(f"errors: {0}")
            return None
        
    pokemon_name = " Squirtle"
    pokemon_data = fetch_pokemon_data(pokemon_name)
    if pokemon_data:
        print(pokemon_data)
    else:
        print(f"Failed to get the pokemon information.")
        
    if __names__ == '__main__':
        main()

        return