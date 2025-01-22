count = 0        # 과목 개수 
sum_score = 0    # 학점 총합 
all_sum = 0      # 과목별 학점 * 등급의 총합 


while count <= 20:
    count += 1
    name, score, grade = map(str, input().split())

    if grade != "P":
        if grade == 'A+':
            grade = 4.5
        elif grade == "A0":
            grade = 4.0
        elif grade == "B+":
            grade = 3.5
        elif grade == "B0":
            grade = 3.0
        elif grade == "C+":
            grade = 2.5
        elif grade == "C0":
            grade = 2.0
        elif grade == "D+":
            grade = 1.5
        elif grade == "D0":
            grade = 1.0
        else:
            grade = 0.0

        sum_score += float(score)
        sum_score_grade = float(score) * float(grade)      # 과목 학점 * 등급 
        all_sum += sum_score_grade


    if count == 20:
        print(all_sum / sum_score)
        break