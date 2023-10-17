"""Displays the Wimbledon Champions and how many times they have won.
Estimate: 25 minutes
Actual:   40 minutes
"""

FILENAME = "wimbledon.csv"


def main():
    """Gets the frequency of champions and countries winning and displays in terminal."""
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        champions_to_times_won = get_frequency(in_file, "Champion")
        countries_to_times_won = get_frequency(in_file, "Country")
        display_champions(champions_to_times_won)
        display_countries(countries_to_times_won)


def get_frequency(file, column_name):
    """Gets the frequency of an item in a CSV file."""
    key_to_frequency = dict()
    first_line = file.readline()
    first_line = first_line.split(",")
    index = first_line.index(column_name)
    for line in file:
        champion = line.split(",")[index]
        if champion in key_to_frequency:
            key_to_frequency[champion] += 1
        else:
            key_to_frequency[champion] = 1
    file.seek(0, 0)
    return key_to_frequency


def display_champions(champions_to_times_won):
    """Displays the number of times a champion has won Wimbledon."""
    print("Wimbledon Champions: ")
    for champion in champions_to_times_won:
        print(f"{champion} {champions_to_times_won[champion]}")
    
    
def display_countries(countries_to_times_won):
    """Displays countries that have won Wimbledon."""
    print(f"These {len(countries_to_times_won)} countries have won Wimbledon: ")
    countries_that_have_won = list()
    for country in sorted(countries_to_times_won.keys()):
        countries_that_have_won.append(country)
    print(' '.join(countries_that_have_won))
    
    
main()
