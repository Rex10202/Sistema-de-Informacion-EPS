from nodo import Nodo
from bed import Bed


class Patient:
    def __init__(self):
        self.Prim = None
        self.last = None
        self.registered_patients = 0

    def register_patient(self):
        bed = Bed()
        registered_patients = 0
        asset = True
        option = True
        reply = "s"
        while reply == "s" or reply == "S":
            if bed.calculate_bed_availability(registered_patients) == 0:
                print("No hay camas disponibles")
                break
            while asset:
                document = input("Digite el documento del paciente: ")
                # Validación del documento
                if (self.validate_document(document) == 0 and
                        bed.calculate_bed_availability(registered_patients)
                        != 0):
                    name = input("Digite el nombre del patient: ")
                    sex = input("Digite el sexo del paciente (M o F): ")
                    # Validación del sex
                    while sex not in ["m", "M", "f", "F"]:
                        print("Valor incorrecto")
                        sex = input("Digite el sexo del paciente (M o F): ")
                    # Captura de fecha de nacimiento
                    while True:
                        day = int(input("Digite el día: "))
                        if 1 <= day <= 31:
                            break
                        else:
                            print("Día debe estar entre 1 y 31.")
                    while True:
                        mouth = int(input("Digite el mes: "))
                        if 1 <= mouth <= 12:
                            break
                        else:
                            print("El mes debe estar entre 1 y 12.")
                    while True:
                        years = int(input("Digite el año: "))
                        if 1900 <= years <= 2023:
                            break
                        else:
                            print("El año debe estar entre 1900 y 2023.")
                    birthdate = str(day) + "/" + str(mouth) + "/" + str(years)
                    print("Datos del paciente")
                    artery_pressure = int(input("Digite la presión arterial " +
                                                "del paciente: "))
                    temperature = int(input("Digite la temperatura del " +
                                            "paciente: "))
                    saturation_02 = int(input("Dogite la saturación de O2 " +
                                              "del paciente: "))
                    respiratory_frequency = int(input("Digite la frecuencia" +
                                                      " cardiaca del " +
                                                      "paciente:"))
                    note_evaluation = input("Digite la nota de evaluación: ")
                    diagnotic_images = input("Digite las radiografías que se" +
                                             " le hicieron (N/A): ")
                    laboratory_test_result = input("Digite los resultados " +
                                                   "de los exámenes del" +
                                                   " paciente (N/A): ")
                    formulated_medicines = input("Digite los medicamentos" +
                                                 " del paciente (N/A): ")
                    # Ingreplyar información del patient
                    self.enter_information(document, name, sex, birthdate,
                                           artery_pressure, temperature,
                                           saturation_02,
                                           respiratory_frequency,
                                           note_evaluation, diagnotic_images,
                                           laboratory_test_result,
                                           formulated_medicines)
                    self.registered_patients += 1
                    asset = False
                else:
                    print("Este documento ya se encuentra registrado")
                    break
            while option:
                reply = input("¿Quiere ingresar otro paciente? S/N: ")
                if reply == "S" or reply == "s":
                    asset = True
                    option = False
                elif reply == "N" or reply == "n":
                    option = False
                else:
                    print("Ingreso una opción inválida")

    def enter_information(self, co, na, sex, birth, pre_art, temp, sat_o2,
                          fre_reply, not_eva, img_dayg, replyul_exam,
                          medic_form):
        new = Nodo()
        new.code = co
        new.name = na
        new.sex = sex
        new.birthdate = birth
        new.artery_pressure = pre_art
        new.temperature = temp
        new.saturation_02 = sat_o2
        new.respiratory_frequency = fre_reply
        new.evaluation_notes = not_eva
        new.diagnostic_images = img_dayg
        new.laboratory_test_results = replyul_exam
        new.formulated_medicines = medic_form
        new.next = None

        if self.Prim is None:
            self.Prim = self.last = new
        else:
            if self.Prim.code > co:
                new.next = self.Prim
                self.Prim.previous = new
                self.Prim = new
            else:
                if self.last.code < co:
                    self.last.next = new
                    new.previous = self.last
                    self.last = new
                else:
                    p = self.Prim
                    while p.code < co:
                        p = p.next
                    new.next = p
                    new.previous = p.previous
                    if p.previous is not None:
                        p.previous.next = new
                    p.previous = new

    def validate_document(self, co):
        p = self.Prim
        while p is not None and p.code != co:
            p = p.next
        if p is None:
            return 0
        return 1
