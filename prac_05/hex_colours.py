"""
CP1404/CP5632 Practical
Hex colours in a dictionary
"""

COLOUR_TO_HEX = {"red1": "#ff0000","maroon": "#b03060", "orange1": "#ffa500", "yellow1": "#ffff00",
                 "green1": "#00ff00", "darkgreen": "#006400", "cyan1": "#00ffff", "blue1": "#0000ff",
                 "indigo": "#4b0082", "violet": "#ee82ee"}

colour_name = input("Enter a colour name: ").lower()
while colour_name != "":
    try:
        print(f"{COLOUR_TO_HEX[colour_name]}")
    except KeyError:
        print("Invalid colour name")
    colour_name = input("Enter a colour name: ").lower()
