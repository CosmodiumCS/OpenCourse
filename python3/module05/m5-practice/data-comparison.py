# for this module's practice:
# we will use sets to compare data

# created by : C0SM0

# sets of animals that can live on land and sea [respectively]
can_live_on_land = {"Wolves", "Alligator", "Deer"}
can_live_in_sea = {"Fish", "Dolphin", "Alligator"}

# create terrestial specific sets for the creature types
land_creatures = can_live_on_land - can_live_in_sea
sea_creatures = can_live_in_sea - can_live_on_land
amphibious_creatures = can_live_on_land & can_live_in_sea

# output, creatures that can live on land
print(f"Creatures that live on land:\n{land_creatures}\n")
print(f"Creatures that live in water:\n{sea_creatures}\n")
print(f"Creatures that live in both:\n{amphibious_creatures}\n")

# feel free to keep practicing, here are some more ideas
"""
- compare food at home to food on your grocery list
- prevent duplicate entries when creating an account or submitting quiz/survey answers
"""