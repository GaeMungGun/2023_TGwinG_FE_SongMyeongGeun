class Subject :
    def __init__(self):
        self.score = None
        self.subject_name = None
        self.max_score = None

    def get_subject_name(self):
        return self.subject_name

    def set_score(self, score):
        if (self.subject_name == "국어" or self.subject_name == "수학") :
            if (score > 100) :
                return "100점 이하의 점수를 입력해주세요."
            else :
                self.score = score
        elif (self.subject_name == "역사") :
            if (score > 50) :
                return "50점 이하의 점수를 입력해주세요."
            else :
                self.score = score

    def get_score(self):
        return self.score

    def get_max_score(self):
        return self.max_score

class Korean(Subject) :
    def __init__(self):
        self.subject_name = "국어"
        self.max_score = 100

class Math(Subject) :
    def __init__(self):
        self.subject_name = "수학"
        self.max_score = 100

class History(Subject) :
    def __init__(self):
        self.subject_name = "역사"
        self.max_score = 50

class Student :
    def __init__(self, name):
        self.name = str(name)
        self.kor = Korean()
        self.math = Math()
        self.his = History()
        self.subjects = [self.kor, self.math, self.his]

    def get_name(self):
        return self.name
    
    def make_sum(self):
        return (self.kor.get_score() + self.math.get_score() + self.his.get_score())
    
    def print(self):
        print("===== Student " + self.get_name() + " =====")
        print(self.kor.get_subject_name() + " : " + str(self.kor.get_score()) + " / " + str(self.kor.get_max_score()))
        print(self.math.get_subject_name() + " : " + str(self.math.get_score()) + " / " + str(self.math.get_max_score()))
        print(self.his.get_subject_name() + " : " + str(self.his.get_score()) + " / " + str(self.his.get_max_score()))

def print_rank(students):
    rank_student = []
    tmp = students[0]

    for i in range(len(students)) :
        rank_student.append(students[i])

    for i in reversed(range(len(students))) : 
        for j in range(i) :
            if (rank_student[j].make_sum() < rank_student[j+1].make_sum()) :
                tmp = rank_student[j]
                rank_student[j] = rank_student[j+1]
                rank_student[j+1] = tmp

    for i in range(len(students)) : 
        print("Rank %d : %s ( %d / 250)" % (i + 1, rank_student[i].get_name(), rank_student[i].make_sum()))

# 실행 함수 (수정하지 마세요. 코드 테스트용 함수입니다.)
def Test():
    n = int(input("How many students: "))

    students = []

    for i in range(n):
        name = input("Name of Student: ")

        student = Student(name)

        for subject in student.subjects:
            score = int(input("Score of %s : " %subject.get_subject_name()))
            subject.set_score(score)

        print()
        student.print()
        print()
        students.append(student)

    print("===== Rank =====")
    print_rank(students)

Test()