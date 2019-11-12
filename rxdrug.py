"""
    will lehman
    cs5001-02
    fall 2019
    11/21/2019
    hw6
    rxdrug.py

    class RxDrug
    class Prescription
"""


class RxDrug:
    '''
        class: rx drug
           in: name (string), rx_ID (integer), and interactions (string)
      methods: set description
               add interaction
               check interaction
               interactions to str
               __str__ (to string)
    '''
    def __init__(self, name, rx_ID, interactions):
        self.name = name
        self.rx_ID = rx_ID
        self.interactions = interactions
        self.description = ''
        self.interact_string = ''

    def set_description(self, description):
        '''
            function: set description
                  in: description
                 out: nothing
                does: setter. sets description based on input.
        '''
        self.description = description

    def add_interaction(self, other_drugs):
        '''
            function: add interaction
                  in: other drugs (list of string)
                 out: nothing
                does: adds a drug to the list of interactions if its not in the
                      list.
        '''
        for other_drug in other_drugs:
            if other_drug not in self.interactions:
                self.interactions.append(other_drug)

    def check_interaction(self, other_drugs):
        '''
            function: check interaction
                  in: other drugs (list of string)
                 out: other interactions (list converted to string at return)
                does: checks to see if param interaction list includes drugs
                      on the objects (drug's) list of interactions, if so,
                      returns the interaction.
        '''
        other_interactions = []
        for other_drug in other_drugs:
            if other_drug in self.interactions:
                other_interactions += [other_drug]
        return ', '.join(other_interactions)

    def interactions_to_str(self):
        '''
            function: interactions to str
                  in: nothing
                 out: list of interactions converted to string
                does: returns object's list of interactions converted to string
        '''
        for i in range(len(self.interactions)):
            if i != len(self.interactions) - 1:
                self.interact_string += f'{self.interactions[i]}, '
            else:
                self.interact_string += f'{self.interactions[i]}'
        return self.interact_string

    def __str__(self):
        '''
            function: __str__ (to string)
                  in: nothing
                 out: important information about the object in string form
                does: returns object's information converted to string
        '''
        return 'Drug: ' + self.name + \
               '\nRX ID: ' + self.rx_ID + \
               '\nDescription: ' + self.description + \
               '\nInteractions: ' + self.interactions_to_str() + '\n'


class Prescription:
    '''
        class: prescription
           in: name (string), description (string), and drugs (list of strings)
      methods: drugs to str
               __str__ (to string)
    '''
    def __init__(self, name, description, drugs):
        self.name = name
        self.description = description
        self.drugs = drugs
        self.drug_string = ''

    def drugs_to_str(self):
        '''
            function: drugs_to_str
                  in: nothing
                 out: list of drugs converted to string
                does: returns object's list of drugs converted to string
        '''
        for i in range(len(self.drugs)):
            if i != len(self.drugs) - 1:
                self.drug_string += f'{self.drugs[i]}, '
            else:
                self.drug_string += f'{self.drugs[i]}'
        return self.drug_string

    def __str__(self):
        '''
            function: __str__ (to string)
                  in: nothing
                 out: important information about the object in string form
                does: returns object's information converted to string
        '''
        return 'Name: ' + self.name + \
               '\nDescription: ' + self.description + \
               '\nDrugs: ' + self.drugs_to_str() + '\n'

