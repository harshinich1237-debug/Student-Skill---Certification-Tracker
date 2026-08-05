class Certification:
    def __init__(self):
        self.certificates=[]
    def add_certificate(self):
        certificate = input("Enter Certification Name: ")
        self.certificates.append(certificate)
        print("Certification Added Successfully!")
    def show_certificate(self):
        print("\nCertifications")
        if len(self.certificates)==0:
            print("No Certifications Found")
        else:
            for certificate in self.certificates:
                print("-", certificate)