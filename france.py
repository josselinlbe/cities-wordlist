import os
import json

json_file_path = './countries/france.json'

with open(json_file_path, 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)
    cities = {entry['place_name'] for entry in data if entry['country_code'] == 'FR'}

paris_arrondissements = [f'Paris {i}e' for i in range(1, 20)]
lyon_arrondissements = [f'Lyon {i}e' for i in range(1, 9)]
marseille_arrondissements = [f'Marseille {i}e' for i in range(1, 16)]

cities.update(paris_arrondissements)
cities.update(lyon_arrondissements)
cities.update(marseille_arrondissements)

place_types = [
    'coiffeur', 'restaurant', 'atm', 'hôtel', 'bar', 'café', 'supermarché', 'pharmacie', 'banque', 'boulangerie',
    'librairie', 'cinéma', 'musée', 'parc', 'gym', 'salle de sport', 'parking', 'magasin de vêtements',
    'fleuriste', 'hôpital', 'dentiste', 'médecin', 'garage', 'station-service', 'bijouterie', 'bibliothèque',
    'discothèque', 'laverie', 'centre commercial', 'opticien', 'boucherie', 'charcuterie', 'pâtisserie', 
    'poissonnerie', 'fromagerie', 'marché', 'tabac', 'cordonnier', 'pressing', 'épicerie', 'kiosque à journaux',
    'brasserie', 'sushi', 'pizzeria', 'snack-bar', 'bar à vin', 'bar à cocktails', 'salon de thé', 'spa', 
    'institut de beauté', 'club de sport', 'patinoire', 'bassin de natation', 'centre de remise en forme', 
    'centre de loisirs', 'terrain de golf', 'terrain de tennis', 'skatepark', 'parc d attractions', 
    'zoo', 'aquarium', 'parc naturel', 'site historique', 'monument', 'galerie d art', 'salle de concert', 
    'théâtre', 'opéra', 'boîte de nuit', 'centre culturel', 'espace événementiel', 'palais des congrès', 
    'bureau de poste', 'mairie', 'préfecture', 'commissariat', 'caserne de pompiers', 'tribunal', 
    'école', 'collège', 'lycée', 'université', 'centre de formation', 'bibliothèque universitaire', 
    'musée des sciences', 'planétarium', 'observatoire', 'base nautique', 'port de plaisance', 'gare', 
    'aéroport', 'station de métro', 'station de tramway', 'arrêt de bus', 'gare routière', 'parking à vélos',
    'parc relais', 'aire de covoiturage', 'carrefour', 'rond-point', 'pont', 'tunnel', 'autoroute', 
    'voie rapide', 'boulevard', 'rue piétonne', 'rue commerçante', 'quartier', 'lotissement', 'résidence', 
    'immeuble', 'gratte-ciel', 'parc d affaires', 'zone industrielle', 'port industriel', 'site touristique', 
    'plage', 'montagne', 'forêt', 'rivière', 'lac', 'réserve naturelle'
]

output_directory = 'countries'
output_file = os.path.join(output_directory, 'france.txt')

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

with open(output_file, 'w', encoding='utf-8') as file:
    for city in cities:
        for place_type in place_types:
            file.write(f'{place_type} {city}\n')

print(f'Wordlist saved to {output_file}')