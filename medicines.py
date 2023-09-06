from patient import Patient


class medicines:
    def __init__(self, Patient, historial_clinico):
        """
        Constructor de la clase mediciness.
        """
        self.patient = Patient
        self.historial_clinico = historial_clinico

    def preinscribir_medicines(self):
        """
        Permite preinscribir un medicines para un patient.
        """
        found = False
        asset = True
        patient = Patient()
        p = self.patient.Prim
        document = input("Ingrese el document del paciente: ")
        while p is not None:
            if patient.validate_document(document) == 0:
                print("----------------------------")
                print("-         Menu             -")
                print("- 1. Medicina general      -")
                print("- 2. Medicina especializada-")
                print("- 3. Cardiología           -")
                print("- 4. Odontología           -")
                print("- 5. Pediatra              -")
                print("----------------------------")
                while asset:
                    service = int(input("Ingrese el service de donde se hace" +
                                        "la preinscripción del medicamento: "))
                    if 1 <= service <= 5:
                        medicines = input("Ingrese el medicamento" +
                                          " preinscrito: ")
                        p.formulated_medicines = medicines
                        self.historial_clinico.increment_counter(service)
                        asset = False
                    else:
                        print("Opción inválida")
                print("medicamento preinscrito correctamente")
                found = True
            p = p.next
        if not found:
            print("paciente no encontrado")
