from bed import Bed
from patient import Patient


class HistoryClinical:
    def __init__(self, patient):
        self.patient = patient
        self.general_medicine_counter = 0
        self.specialist_medicine_accountant = 0
        self.cardiology_counter = 0
        self.dental_accountant = 0
        self.pediatrician_accountant = 0
        self.general_medicine_medicine_counter = 0
        self.medicine_counter_specialized_medicine_medicine = 0
        self.cardiology_medication_counter = 0
        self.dental_medicament_counter = 0
        self.pediatrician_medication_counter = 0

    def show_clinical_history(self):
        code = input("Ingresa el código del paciente: ")
        found = False
        p = self.patient.Prim

        while p is not None:
            if p.code == code:
                # Imprimir información del Patient
                print("- Información básica del Paciente -")
                print("- Estado actual:", p.asset)
                print("- Nombre:", p.name)
                print("- Sexo:", p.sex)
                print("Fecha de nacimiento:", p.birthdate)
                print("Historia clínica")
                # Evaluar la temperatura
                if p.temperature >= 41:
                    print("Usted tiene hipertermia")
                elif 39.5 < p.temperature < 41:
                    print("Usted tiene fiebre alta")
                elif 37.5 < p.temperature < 39.5:
                    print("Usted tiene fiebre")
                elif 36 < p.temperature < 37.7:
                    print("Su temperatura es normal")
                else:
                    print("Tiene hipotermia")
                # Imprimir más información médica
                print("Presión Arterial:", p.artery_pressure)
                print("temperatura:", p.temperature)
                print("Saturación de O2:", p.saturation_02)
                print("Frecuencia respiratoria:", p.respiratory_frequency)
                print("Nota de evaluación:", p.evaluation_notes)
                print("Imágenes diagnósticas:", p.diagnostic_images)
                print("Resultado de exámenes de laboratorio:",
                      p.laboratory_test_results)
                print("Medicamentos formulados:", p.formulated_medicines)
                found = True
                break
            p = p.next

        if not found:
            print("No existe el código del Paciente")

    def generate_reports(self):
        total_patients = 300
        chronic_diseases_counter = 0
        bed = Bed()
        p = self.patient.Prim

        while p is not None:
            if (p.artery_pressure >= 140 or p.saturation_02 < 90 or
                    12 < p.respiratory_frequency > 20):
                chronic_diseases_counter += 1
            # Contar Patients por servicio
            if p.service == 1:
                self.general_medicine_counter += 1
            elif p.service == 2:
                self.specialist_medicine_accountant += 1
            elif p.service == 3:
                self.cardiology_counter += 1
            elif p.service == 4:
                self.dental_accountant += 1
            elif p.service == 5:
                self.pediatrician_accountant += 1
            p = p.next
        # Imprimir cantidad de admisiones y Beds disponibles
        print("Cantidad de admisiones:", self.patient.registered_patients)
        print("Hay", bed.show_availability_bed
              (self.patient.registered_patients), "camas disponibles")

        # Calcular y mostrar el porcentaje de ocupación hospitalaria
        print("El porcentaje de ocupación hospitalaria es:",
              (self.patient.registered_patients / total_patients) * 100)

        # Calcular y mostrar el promedio de estancia por medicina general
        print("El promedio de estancia por medicina general:",
              (self.general_medicine_counter / total_patients) * 100)

        # Calcular y mostrar el promedio de estancia por medicina especializada
        print("El promedio de estancia por medicina especializada:",
              (self.specialist_medicine_accountant / total_patients) * 100)

        # Calcular y mostrar el promedio de estancia por cardiología
        print("El promedio de estancia por cardiología:",
              (self.cardiology_counter / total_patients) * 100)

        # Calcular y mostrar el promedio de estancia por odontología
        print("El promedio de estancia por odontología:",
              (self.dental_accountant / total_patients) * 100)

        # Calcular y mostrar el promedio de estancia por pediatra
        print("El promedio de estancia por pediatra:",
              (self.pediatrician_accountant / total_patients) * 100)

        # Mostrar la cantidad de Patients con enfermedades crónicas
        print("Hay", chronic_diseases_counter, "pacientes con enfermedades" +
              " crónicas")

        # Mostrar las altas por cada service
        print("Altas por medicina general:", self.general_medicine_counter)
        print("Altas por medicina especializada:",
              self.specialist_medicine_accountant)
        print("Altas por cardiología:", self.cardiology_counter)
        print("Altas por odontología:", self.dental_accountant)
        print("Altas por pediatra:", self.pediatrician_accountant)

        # Mostrar la prescripción de medicamentos por cada service
        print("Prescripción de medicamentos por medicina general:",
              self.general_medicine_medicine_counter)
        print("Prescripción de medicamentos por medicina especializada:",
              self.medicine_counter_specialized_medicine_medicine)
        print("Prescripción de medicamentos por medicina cardiología:",
              self.cardiology_medication_counter)
        print("Prescripción de medicamentos por medicina odontología:",
              self.dental_medicament_counter)
        print("Prescripción de medicamentos por medicina pediatra:",
              self.pediatrician_medication_counter)

    def high_services(self):
        found = False
        asset = True
        patient = Patient()
        p = self.patient.Prim
        document = input("Ingrese el documento del paciente: ")
        while p is not None:
            while p.asset == "No dado de alta":
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
                        service = int(input("Ingrese el servicio de alta: "))
                        if service == 1:
                            p.asset = "Dado de alta en medicina general"
                            p.service = 1
                            self.patient.registered_patients -= 1
                            asset = False
                        elif service == 2:
                            p.asset = "Dado de alta en medicina especializada"
                            p.service = 2
                            self.patient.registered_patients -= 1
                            asset = False
                        elif service == 3:
                            p.asset = "Dado de alta en cardiología"
                            p.service = 3
                            self.patient.registered_patients -= 1
                            asset = False
                        elif service == 4:
                            p.asset = "Dado de alta en odontología"
                            p.service = 4
                            self.patient.registered_patients -= 1
                            asset = False
                        elif service == 5:
                            p.asset = "Dado de alta en pediatra"
                            p.service = 5
                            self.patient.registered_patients -= 1
                            asset = False
                        else:
                            print("Opción inválida")
                    print("Paciente dado de alta correctamente")
                    found = True
            p = p.next
        if not found:
            print("Paciente no encontrado o ya dado de alta")

    def increment_counter(self, service):
        if service == 1:
            self.general_medicine_medicine_counter += 1
        elif service == 2:
            self.medicine_counter_specialized_medicine_medicine += 1
        elif service == 3:
            self.cardiology_medication_counter += 1
        elif service == 4:
            self.dental_medicament_counter += 1
        elif service == 5:
            self.pediatrician_medication_counter += 1
