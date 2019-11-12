class RxDrug:
    def __init__(self, name, rx_ID):
        self.name = name
        self.rx_ID = rx_ID
        self.interactions = ''
        self.description = ''

    def add_interaction(self, other_drugs):
        for i in range(len(other_drugs)):
            if i != len(other_drugs) - 1:
                self.interactions += f'{other_drugs[i]}, '
            else:
                self.interactions += f'{other_drugs[i]}'
        return self.interactions

    def set_description(self, description):
        self.description = description

    # def check_interaction(self, other_drugs):

    def __str__(self):
        return 'Drug: ' + self.name + \
               '\nRX ID: ' + self.rx_ID + \
               '\nDescription: ' + self.description + \
               '\nInteractions: ' + self.interactions + '\n'
