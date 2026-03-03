from kumed import Hospital, Patient

myHospital = Hospital()
gibbons = Patient("Gibbons", "John", 50, "Being too cool.", 7)

me = Patient("Frias", "Lucas", 19, "mega virgin", 9)
myHospital.addPatient(gibbons)
myHospital.addPatient(me)
myHospital.search(1)
