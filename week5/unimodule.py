class UniModule:
    def __init__(self,code,name,year,credit,grade=None,PFP=None,discovery=None):
        self.code = code
        self.name = name
        self.year = year
        self.credit = credit
        if grade is None:
            self.grade = 0
        else:
            self.grade = grade
        if PFP is None:
            self.PFP = False
        else:
            self.PFP = PFP
        if discovery is None:
            self.discovery = False
        else:
            self.discovery = discovery

    def display_details(self):
        temp1 = ""
        temp2 = ""
        if not self.PFP:
            temp1 = "N"
        if not self.discovery:
            temp2 = "N"
        print(self.code + ":" + self.name + ":Y" + str(self.year) + ":" + str(self.credit) + "CR:" + str(self.grade) + "GRD:" + temp1 + "PFP:" + temp2 + "Disc")


class Transcript:
    def __init__(self):
        self.modules = []

    def add_module(self,item):
        if not isinstance(item,UniModule):
            raise ValueError("expected item be an instance of UniModule.")
        elif item not in self.modules:
            self.modules.append(item)         
        else:
            raise ValueError("module already exists!")
            

    def print_transcript(self):
        for item in self.modules:
            item.display_details()

if __name__ == "__main__":

    COMP1012 = UniModule("COMP1011", "Intro to Prog.", 1, 10, grade=75, discovery=True)
    COMP1121 = UniModule("COMP1121", "Databases", 1, 10, PFP=True)
    COMP1211 = UniModule("COMP1211", "Comp. Arch.", 1, 10, grade=80, PFP=True)
    t_student1 = Transcript()
    t_student1.add_module(COMP1012)
    t_student1.add_module(COMP1121)
    t_student1.add_module(COMP1211)
    t_student1.print_transcript()
