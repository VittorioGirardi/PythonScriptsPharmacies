import csv

class Farmacia:
    def __init__(self):
        self.ListaFarmacie = ["FARMACIA PESCETTO", "FARMACIA BOCCHIOTTI", "FARMACIA S. PIETRO", "FARMACIA SERRA",
                              "FARMACIA GAMALERI", "FARMACIA INTERNAZIONALE", "FARMACIA MARINI", "FARMACIA MULTEDO",
                              "FARMACIA NEGROTTO", "FARMACIA PALMARO", "FARMACIA CALVI", "FARMACIA S. CARLO", "FARMACIA S. PIETRO",
                              "FARMACIA DELLE CATENE", "FARMACIA TIXI", "FARMACIA COMUNALE", "FARMACIA S. GIOVANNI"]
        
        self.ListaOrari = ['DAL LUNEDI AL VENERDI 8:30 - 13:00 | 15:00 - 20:00 | SABATO: 8:30 - 13:00',
                           'DALLE 8:30 ALLE 12:30 | DALLE 15:30 ALLE 20:30 | SABATO: 8:30 - 13:15',
                           'CONTINUATO DALLE 8:00 ALLE 20:00', 'NON TURNA']
        
        self.ListaMesi = ['GENNAIO', "FEBBRAIO", "MARZO", "APRILE", "MAGGIO", "GIUGNO", "LUGLIO", "AGOSTO", "SETTEMBRE", "OTTOBRE", "NOVEMBRE", "DICEMBRE"]

    def print_selected_info(self, selected_farmacia, selected_mese, selected_orario):
        try:
            farmacia_index = self.ListaFarmacie.index(selected_farmacia)
            orario_index = self.ListaOrari.index(selected_orario)
            mese_index = selected_mese - 1 

            print(f"Farmacia:\n {selected_farmacia}")
            print(f"Mese:\n {self.ListaMesi[mese_index]}")
            print(f"Orario:\n {selected_orario}")

        except ValueError:
            print("Scelta invalida.")

    def write_to_csv(self, selected_farmacia, selected_mese, selected_orario):
        with open('orari_farmacia.csv', mode='a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([selected_farmacia, self.ListaMesi[selected_mese - 1], selected_orario])
            print("Gli orari della Farmacia selezionata sono stati inseriti nel file orari_farmacia.csv")

    def prompt_user_for_selections(self):
        restart = 'R'
        quit_key = 'Q'

        while self.ListaFarmacie:
            print_options(self.ListaFarmacie)
            selected_farmacia_index = get_valid_input("\nInserisci il numero corrispondente alla Farmacia: ", range(1, len(self.ListaFarmacie) + 1))
            selected_farmacia = self.ListaFarmacie[selected_farmacia_index - 1]

            print_options(self.ListaMesi)
            selected_mese_index = get_valid_input("\nInserisci il numero corrispondente al mese (1-12): ", range(1, len(self.ListaMesi) + 1))
            selected_mese = selected_mese_index

            print_options(self.ListaOrari)
            selected_orario_index = get_valid_input("\nInserisci il numero corrispondente all'Orario: ", range(1, len(self.ListaOrari) + 1))
            selected_orario = self.ListaOrari[selected_orario_index - 1]
            print(" ")

            self.print_selected_info(selected_farmacia, selected_mese, selected_orario)
            self.write_to_csv(selected_farmacia, selected_mese, selected_orario)

            
            self.ListaFarmacie.remove(selected_farmacia)

            if not self.ListaFarmacie:
                print("Tutte le Farmacie sono state associate. Vuoi ricominciare (R) o uscire (Q)?")
                user_choice = input("Scelta: ").upper()
                if user_choice == restart:
                    
                    self.ListaFarmacie = ["FARMACIA PESCETTO", "FARMACIA BOCCHIOTTI", "FARMACIA S. PIETRO", "FARMACIA SERRA",
                                          "FARMACIA GAMALERI", "FARMACIA INTERNAZIONALE", "FARMACIA MARINI", "FARMACIA MULTEDO",
                                          "FARMACIA NEGROTTO", "FARMACIA PALMARO", "FARMACIA CALVI", "FARMACIA S. CARLO", "FARMACIA S. PIETRO",
                                          "FARMACIA DELLE CATENE", "FARMACIA TIXI", "FARMACIA COMUNALE", "FARMACIA S. GIOVANNI"]
                elif user_choice == quit_key:
                    print("Esecuzione completata!")
                    break
                else:
                    print("Scelta non valida. Uscita.")
                    break

def print_options(options):
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")
                
def get_valid_input(prompt, valid_range):
    while True:
        try:
            user_input = int(input(prompt))
            if user_input in valid_range:
                return user_input
            else:
                print("Input non valido. Riprova.")
        except ValueError:
            print("Input non valido. Riprova.")

farmacia_instance = Farmacia()
farmacia_instance.prompt_user_for_selections()
