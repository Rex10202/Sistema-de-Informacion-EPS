class Bed:
    def __init__(self):
        """
        Constructor de la clase Cama que inicializa el número total de camas
        disponibles.
        """
        self.total_beds = 300

    def calculate_bed_availability(self, registered_patients):
        """
        Calcula la disponibilidad de camas restando el número de pacientes
        registrados al total de camas.
        """
        return self.total_beds - registered_patients

    def show_availability_bed(self, registered_patients):
        """
        Muestra la disponibilidad de camas.
        """
        if registered_patients is not None:
            return self.total_beds - registered_patients
        else:
            return self.total_beds
