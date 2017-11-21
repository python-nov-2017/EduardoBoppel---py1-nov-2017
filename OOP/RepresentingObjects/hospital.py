class Patient(object):
    
    Patient_id = 1
    def __init__(self, name, allergies):
        self.id = Patient.Patient_id
        self.name = name
        self.allergies = allergies
        self.bed = None

        Patient.Patient_id += 1

    def __repr__(self):
        return "<Parient object {}, name: {}, allergies: {}, bed: {}>".format(self.id, self.name, self.allergies, self.bed)

class Hospital(object):
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.patients = {}
        for x in range(1, self.capacity+1):
            self.patients[x] = "Empty"


    def admit(self, patient):               
        for bed, pat in self.patients.iteritems():
            if pat == "Empty":
                self.patients[bed] = patient
                patient.bed = bed
                return self
            
        print "no empty beds, hospital full"
        return self

        
    def discharge(self, patient):
        for bed, pat in self.patients.iteritems():
            if pat.name == patient:
                self.patients[bed] = "Empty"
                pat.bed = None
                return
        
        print "No patients with that name"
        return self
    

    def status(self):
        beds = []
        for bed, pat in self.patients.iteritems():
            if pat == "Empty":
                beds += bed, "Empty"
            else:
                beds += bed, pat.name
        print beds

    def __repr__(self):
        return "<Hospital object, name: {}, capacity: {}, patients: {}>".format(self.name, self.capacity, self.patients)



if __name__ == "__main__":
    myHospital = Hospital("General Hospital", 3)
    myHospital.status()


    myHospital.admit(Patient("George", "Nuts" ))
    myHospital.admit(Patient("Carlos", "Nuts" ))
    myHospital.admit(Patient("Jenny", "Nuts" ))
    myHospital.admit(Patient("John", "Nuts" ))
    myHospital.status()


    myHospital.discharge("Carlos")

    myHospital.admit(Patient("John", "Nuts" ))
    myHospital.status()