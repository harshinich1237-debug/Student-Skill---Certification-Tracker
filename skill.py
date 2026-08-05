class Skill:
    def __init__(self):
        self.skills = []
    def add_skill(self):
        skill=input("Enter Skill Name: ")
        self.skills.append(skill)
        print("Skill Added Successfully!")
    def show_skill(self):
        print("\nSkills")
        if len(self.skills)==0:
            print("No Skills Found")
        else:
            for i in self.skills:
                print("-", i)