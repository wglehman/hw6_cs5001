from rxdrug import RxDrug


def unpack_interactions():
    try:
        file_interactions = open('rxcui_drugs.txt', 'r')

        interaction_list = []

        for line in file_interactions:
            interaction_list += [line.split('|')]

            for i in range(len(interaction_list)):
                interact_string = interaction_list[i][3]
                interact_string = interact_string.rstrip('\n')
                interact_string = interact_string.split(',')

                rx_drug = RxDrug(interaction_list[i][0],
                                 interaction_list[i][1])
                rx_drug.add_interaction(interact_string)
                rx_drug.set_description(interaction_list[i][2])
                # interaction_dict[interaction_list[i][0]] = \
                #     {'RX_ID': interaction_list[i][1],
                #      'DESCRIPTION': interaction_list[i][2],
                #      'INTERACTIONS': interact_string}
                print(rx_drug)

        file_interactions.close()
        # return interaction_dict

    except FileNotFoundError:
        print('file not found, check the directory')
        return

    except OSError:
        print('error reading file')
        return


def main():
    unpack_interactions()

    # for drug, info in interactions.items():
    #     rxDrug = RxDrug(drug, info['RX_ID'])
    #     rxDrug.add_interaction(info['INTERACTIONS'])
    #     rxDrug.set_description(info['DESCRIPTION'])
    #     print(rxDrug)


main()
