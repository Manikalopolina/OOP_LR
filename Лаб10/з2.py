# Определение класса "MedService"
class MedService:
    def __init__(self, clinic_name, clinic_address, patient_lastname, insurance_number, exam_date, doctor_lastname, doctor_position, diagnosis):
        self.clinic_name = clinic_name
        self.clinic_address = clinic_address
        self.patient_lastname = patient_lastname
        self.insurance_number = insurance_number
        self.exam_date = exam_date
        self.doctor_lastname = doctor_lastname
        self.doctor_position = doctor_position
        self.diagnosis = diagnosis

    def __str__(self):
        return f"MedService:\nClinic: {self.clinic_name}\nAddress: {self.clinic_address}\nPatient: {self.patient_lastname}\nInsurance: {self.insurance_number}\nExam Date: {self.exam_date}\nDoctor: {self.doctor_lastname}, {self.doctor_position}\nDiagnosis: {self.diagnosis}"

# Класс "PreventiveExam", наследуется от класса "MedService"
class PreventiveExam(MedService):
    def __init__(self, clinic_name, clinic_address, patient_lastname, insurance_number, exam_date, doctor_lastname, doctor_position, diagnosis, exam_type, year, validity_period, result):
        super().__init__(clinic_name, clinic_address, patient_lastname, insurance_number, exam_date, doctor_lastname, doctor_position, diagnosis)
        self.exam_type = exam_type
        self.year = year
        self.validity_period = validity_period
        self.result = result

    def __str__(self):
        return f"{super().__str__()}\nExam Type: {self.exam_type}\nYear: {self.year}\nValidity Period: {self.validity_period}\nResult: {self.result}"

# Класс "Vaccination", наследуется от класса "MedService"
class Vaccination(MedService):
    def __init__(self, clinic_name, clinic_address, patient_lastname, insurance_number, exam_date, doctor_lastname, doctor_position, diagnosis, vaccine_name, vaccine_date, validity_period):
        super().__init__(clinic_name, clinic_address, patient_lastname, insurance_number, exam_date, doctor_lastname, doctor_position, diagnosis)
        self.vaccine_name = vaccine_name
        self.vaccine_date = vaccine_date
        self.validity_period = validity_period

    def __str__(self):
        return f"{super().__str__()}\nVaccine Name: {self.vaccine_name}\nVaccine Date: {self.vaccine_date}\nValidity Period: {self.validity_period}"

# Класс "PediatricCare", наследуется от класса "MedService"
class PediatricCare(MedService):
    def __init__(self, clinic_name, clinic_address, patient_lastname, insurance_number, exam_date, doctor_lastname, doctor_position, diagnosis, birth_certificate, gender, age):
        super().__init__(clinic_name, clinic_address, patient_lastname, insurance_number, exam_date, doctor_lastname, doctor_position, diagnosis)
        self.birth_certificate = birth_certificate
        self.gender = gender
        self.age = age

    def __str__(self):
        return f"{super().__str__()}\nBirth Certificate: {self.birth_certificate}\nGender: {self.gender}\nAge: {self.age}"



preventive_exam = PreventiveExam('Your Clinic', 'Советская 22', 'Маникало', '12345', '08.11.23', 'Белуш', 'терапевт', 'Сколиоз', 'стационарный', 2023, '1 year', 'Norm')
print(preventive_exam)

vaccination = Vaccination ('Your Clinic', 'Булочная 35', 'Белуш', '12345', '08.11.23', 'Маникало', 'хирург', 'что-то', 'lala Vaccine', '08/11/23', 1 )
print(vaccination)

pediatric_care = PediatricCare('Your Clinic', 'Пирожковая 1', 'Макей', '12345', '08/11/23', 'Казойть', 'терапевт', 'что-то', "0123456789", "ж", 16)
print(pediatric_care)
