#!/usr/sbin/python
# GNU Affero General Public License v3.0 or later (see COPYING or https://www.gnu.org/licenses/agpl.txt)

import random


def main():
    """Main function."""
    # Dictionary of all class and spec combinations
    classes_and_specs = {
        "Death Knight": ["Blood", "Frost", "Unholy"],
        "Demon Hunter": ["Havoc", "Vengenance"],
        "Druid": ["Balance", "Feral", "Guardian", "Restoration"],
        "Evoker": ["Devastation", "Augmentation", "Preservation"],
        "Hunter": ["Beast Mastery", "Marksmanship", "Survival"],
        "Mage": ["Arcane", "Fire", "Frost"],
        "Monk": ["Windwalker", "Brewmaster", "Mistweaver"],
        "Paladin": ["Holy", "Protection", "Retribution"],
        "Priest": ["Discipline", "Holy", "Shadow"],
        "Rogue": ["Assassination", "Outlaw", "Subtlety"],
        "Shaman": ["Elemental", "Enhancement", "Restoration"],
        "Warlock": ["Affliction", "Demonology", "Destruction"],
        "Warrior": ["Arms", "Fury", "Protection"]
    }

    # Initialize answer
    answer = "n"

    # Loop until user reponse
    while answer != "y":
        class_selection = random.choice(list(classes_and_specs.keys()))
        spec_selection = random.choice(classes_and_specs[class_selection])
        print("Class: " + class_selection)
        print("Spec: " + spec_selection)
        answer = input("Are you satisfied with that result? [y/n]: ")
        print("")


main()
