class Nodo:
    def __init__(self):
        # Atributos para almacenar información del paciente
        self.code = ""  # Código
        self.name = ""  # Nombre
        self.sex = ""  # Sexo
        self.birthdate = ""  # Fecha de nacimiento
        self.artery_pressure = 0  # Presión arterial
        self.temperature = 0  # Temperatura corporal
        self.saturation_02 = 0  # Saturación de oxígeno
        self.respiratory_frequency = 0  # Frecuencia respiratoria
        self.evaluation_notes = ""  # Notas de evolución
        self.diagnostic_images = ""  # Imágenes diagnósticas
        self.laboratory_test_results = ""  # Resultados de exámenes
        self.formulated_medicines = ""  # Formula de medicamentos
        self.asset = "No dado de alta"  # Estado asset
        self.service = 0  # service médico asignado al paciente (código)
        # Enlaces a nodos previous y next en una lista doblemente enlazada
        self.next = None  # Referencia al next nodo
        self.previous = None  # Referencia al nodo previous
