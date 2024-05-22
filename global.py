import os

# Name of the file containing the city names
input_file = 'cities.txt'

# List of keywords
keywords = [
    'Restaurants', 'Hotels', 'Tourist Attractions', 'Shopping Centers', 'Parks', 
    'Museums', 'Cafes', 'Bars', 'Night Clubs', 'Gyms', 'Hospitals', 'Pharmacies', 
    'Supermarkets', 'Gas Stations', 'Parking Lots', 'Schools', 'Universities', 
    'Libraries', 'Theaters', 'Cinemas', 'Beaches', 'Swimming Pools', 'Banks', 
    'ATMs', 'Post Offices', 'Police Stations', 'Fire Stations', 'Car Rentals', 
    'Train Stations', 'Bus Stations', 'Airports'
]

# Function to create the files
def create_files(input_file, keywords):
    # Read city names from the file
    with open(input_file, 'r') as file:
        cities = file.read().splitlines()
    
    # Check if the output directory exists, if not, create it
    output_dir = 'output'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Create one file per keyword
    for keyword in keywords:
        kw = keyword.replace(' ', '_').lower()
        filename = f'{kw}.txt'
        filepath = os.path.join(output_dir, filename)
        with open(filepath, 'w') as f:
            for city in cities:
                f.write(f'{keyword} in {city}\n')
    
    print(f'Files created in the directory: {output_dir}')
    
    # Create a file to group all files
    all_file = os.path.join(output_dir, 'all.txt')
    with open(all_file, 'w') as f_all:
        for keyword in keywords:
            kw = keyword.replace(' ', '_').lower()
            filename = f'{kw}.txt'
            filepath = os.path.join(output_dir, filename)
            with open(filepath, 'r') as f:
                f_all.write(f.read())

    print(f'All files grouped into {all_file}')

# Call the function
create_files(input_file, keywords)
