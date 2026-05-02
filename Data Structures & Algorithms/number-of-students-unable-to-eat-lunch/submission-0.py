class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        sand_len = len(sandwiches)
        result = 0
        while True:
            if not sandwiches:
                break
            if sandwiches[0] not in students:
                result = len(students)
                break
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
            else:
                student = students.pop(0)
                students.append(student)
                
        return result
                
            