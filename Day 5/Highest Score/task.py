student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

print(sum(student_scores))
print(max(student_scores))

max_score = 0
for s in student_scores:
    if s > max_score:
        max_score = s
print(max_score)