if __name__ == '__main__':
    student_record = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student_record.append([score,name])
    student_record.sort()
    frist_lowest = student_record[0][0]
    for frist_peer,_ in student_record[0:]:
        if frist_lowest == frist_peer:
            continue
        second_lowest = frist_peer
        break
        
    for grade,name in student_record[1:]:
        if grade == second_lowest:
            print(name)