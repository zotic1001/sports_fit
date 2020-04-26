def ideal_weight(height, age, gender, body_type):
    if gender == "F":
        if int(age) > 40:
            ideal = ((height - 90) - ((height - 150) / 2))
            return int(ideal) + body_type
        if int(age) < 40:
            ideal = ((int(height) - 100) - ((int(height) - 150)) / 2)
            return int(ideal) + body_type
    if gender == "M":
        if int(age) > 40:
            ideal = ((int(height) - 100) * 1.15)
            return int(ideal) + body_type
        else:
            ideal = (int(height) - 113) * 1.15
            return int(ideal) + body_type


def goal(height, weight, age, gender, body_type):
    return ideal_weight(height, age, gender, body_type) - int(weight)


def set_category(gender, goal):
    if int(goal) < -20:
        category = gender + "VF"  # very fat
    elif int(goal) < -10:
        category = gender + "F"  # fat
    elif int(goal) > 20:
        category = gender + "VT"  # very thin
    elif int(goal) > 10:
        category = gender + "T"  # thin
    elif int(goal) in range(-5, 5):
        category = gender + "N"  # normal
    elif int(goal) in range(-1, 2):
        category = gender + "S"  # sportsmen(атлет)
    else:
        category = gender + "N"
    return category