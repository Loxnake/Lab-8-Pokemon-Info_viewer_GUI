import requests

def retrieveMon(pokeName):
    """
    gets a dictionary of information from the pokeAPI for one pokemon

    :param name: Pokemon's name or pokedex number
    """
    if pokeName is None:
        return
    pokeName = pokeName.lower().strip()
    if pokeName == '':
        return
    response = requests.get('https://pokeapi.co/api/v2/pokemon/' + str(pokeName))

    print('Getting Pokemon Information...', end = '')
    
    if response.status_code == 200:
     print('Success!')
     return response.json()
    else:
     print('Fialed, Response code:',response.status_code)
     return