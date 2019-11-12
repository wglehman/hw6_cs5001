"""
    will lehman
    cs5001-02
    fall 2019
    11/21/2019
    hw6
    rxdrug_driver.py
"""


from rxdrug import RxDrug, Prescription


def unpack_interactions():
    '''
        function: unpack interations
              in: nothing
             out: a dictionary with keys set to the name of drugs from the
                  object RxDrug and the value the corresponding RxDrug object.
            does: unpacks and parses file, creating object based on fields in
                  file.
    '''
    # try/catch for file opening and path checking
    try:
        # open file in read mode
        file_interactions = open('rxcui_drugs.txt', 'r')

        # dictionary of drug objects
        dict_of_drugs = {}
        # interaction list used temporarily while creating objects
        interaction_list = []

        # unpacks the file line by line
        for line in file_interactions:
            # looks for vertical bars as separators and saves content to list
            interaction_list += [line.split('|')]

            # unpacks drug listings, cleans up the interaction portion,
            # because it's at the end it has \n and also needs to be a list
            # of strings because of its content
            for i in range(len(interaction_list)):
                interact_string = interaction_list[i][3]
                interact_string = interact_string.rstrip('\n')
                interact_string = interact_string.split(',')

                # creates objects of RxDrug based on parsed content, sending
                # name, id, and interactions initially
                rx_drug = RxDrug(interaction_list[i][0],
                                 interaction_list[i][1],
                                 interact_string)

                # sets description string for single object
                rx_drug.set_description(interaction_list[i][2])

                # dict of drugs stored by name
                dict_of_drugs[rx_drug.name] = rx_drug

        # closes out file
        file_interactions.close()

    except FileNotFoundError:
        print('file not found, check the directory')
        return

    except OSError:
        print('error reading file')
        return

    # returns dict to main()
    return dict_of_drugs


def unpack_heroes():
    '''
        function: unpack heroes
              in: nothing
             out: a dictionary with keys set to the name of heroes from the
                  object Prescription and the value the corresponding
                  Prescription object.
            does: unpacks and parses file, creating object based on fields in
                  file.
    '''
    # try/catch for file opening and path checking
    try:
        # opens in read mode
        file_prescriptions = open('prescriptions.txt', 'r')

        # initializes dictionary for storing objects and temporary list
        dict_of_heroes = {}
        hero_list = []

        # iterates over lines to create prescription objects, parses based on
        # vertical bar
        for line in file_prescriptions:
            hero_list += [line.split('|')]

            # cleans up drug list into a list of strings
            for i in range(len(hero_list)):
                hero_string = hero_list[i][2]
                hero_string = hero_string.rstrip('\n')
                hero_string = hero_string.split(',')

                # creates prescription object for each hero
                hero_script = Prescription(hero_list[i][0],
                                           hero_list[i][1],
                                           hero_string)

                # saves object to dictionary with key set to their name
                dict_of_heroes[hero_script.name] = hero_script

        # closes out file
        file_prescriptions.close()

    except FileNotFoundError:
        print('file not found, check the directory')
        return

    except OSError:
        print('error reading file')
        return

    # returns dictionary of objects to main()
    return dict_of_heroes


def check_interactions(dict_of_drugs, dict_of_heroes):
    '''
        function: check interactions
              in: dictionary of drugs (dictionary of RxDrug objects) and
                  dictionary of heroes (dictionary of Prescription objects)
             out: nothing
            does: unpacks heroes values, prints out information about the
                  heroes drugs and their interactions. Makes calls to methods
                  in RxDrug and Prescription objects.
    '''
    # unpacking values (objects) from dict_of_heroes
    for hero in dict_of_heroes.values():
        # finds interactions by calling check_interactions in RxDrug with the
        # heroes first drug as the name and the other_drugs as all the drugs
        # they're taking. Though *very* unlikely, I figured checking the drug
        # against itself might be a good idea.
        interactions = \
            dict_of_drugs[hero.drugs[0]].check_interaction(hero.drugs)

        # prints initial information, calling on object and method drugs_to_str
        # to format the data correctly. end='' so next print will appear right.
        print('checking scripts for', hero.name,
              'who suffers from', hero.description,
              '\ncurrent drug(s):', hero.drugs_to_str(), end='')

        # if else depending on what check_interaction() returned.
        if interactions != '':
            print('\nWARNING! drug drug interaction between', hero.drugs[0],
                  'and', interactions, '\n')
        else:
            print('\nno serious drug interactions\n')


def main():
    # calls two functions to create dicts of objects, then passes them to the
    # checker/printer function for final processing.
    dict_of_drugs = unpack_interactions()
    dict_of_heroes = unpack_heroes()
    check_interactions(dict_of_drugs, dict_of_heroes)


main()
