# Importación de módulos
from medicines import medicines
from patient import Patient
from historialClinico import HistoryClinical
import os

# Función para limpiar la pantalla según el sistema operativo


def clean_screen():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "nt":
        os.system("cls")
# Creación de instancias


patient = Patient()
clinical_history = HistoryClinical(patient)
medicines = medicines(patient, clinical_history)
asset = True

# Función para mostrar el menú


def menu():
    print("------------------------------")
    print("-         Menu               -")
    print("- 1. Registrar paciente      -")
    print("- 2. Ver historial medico    -")
    print("- 3. Generar reportes        -")
    print("- 4. Dar de alta             -")
    print("- 5. Preinscribir medicinas")
    print("- 6. Salir                   -")
    print("------------------------------")


menu()  # Mostrar el menú inicial
while asset:
    option = int(input("Digite la opción deseada: "))
    if option == 1:
        patient.register_patient()
        clean_screen()
        menu()
    elif option == 2:
        clinical_history.show_clinical_history()
        menu()
    elif option == 3:
        clinical_history.generate_reports()
        menu()
    elif option == 4:
        clinical_history.high_services()
        menu()
    elif option == 5:
        medicines.preinscribir_medicines()
        menu()
    elif option == 6:
        print("Gracias por usar el programa")
        asset = False
    else:
        print("Opción inválida")
