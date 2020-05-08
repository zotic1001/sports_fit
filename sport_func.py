def ideal_weight(height, age, gender, body_type):  # расчёт идеального веса человека
    # с учетом роста, возраста, пола, телосложения(по формулам из интернета)
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


def goal(height, weight, age, gender, body_type):  # расчет того на сколько кг нужно изменить свой вес
    return ideal_weight(height, age, gender, body_type) - int(weight)


def set_category(gender, goal):  #определение категории человека по массе
    if int(goal) < -13:
        category = gender + "VF"  # very fat
    elif (int(goal) < -5) and (int(goal) > -13):
        category = gender + "F"  # fat
    elif int(goal) > 15:
        category = gender + "VT"  # very thin
    elif int(goal) > 5:
        category = gender + "T"  # thin
    elif (int(goal) < 5) and (int(goal) > -5):
        category = gender + "N"  # normal
    else:
        category = gender + "N"
    return category