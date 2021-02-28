import sys
import decimal


def checkBMI(weight, heigh):
    bmi = round(weight/((heigh/100)**2),1)
    if bmi < 18.5:
        return f'You are BMI is :{bmi} \n You are Underweight'
    elif bmi >= 18.5 and bmi <= 24.9:
        return f'You are BMI is :{bmi} \n You are Normal'
    elif bmi >= 25.0 and bmi <= 29.9:
        return f'You are BMI is :{bmi} \n You are Overweight'
    elif bmi >= 30.0 and bmi <= 34.9:
        return f'You are BMI is :{bmi} \n You are Obese'
    elif bmi > 35:
        return f'You are BMI is :{bmi} \n You are Extremely Obese'
    return weight/((heigh/100)**2)


if __name__ == '__main__':
    print(checkBMI(float(sys.argv[1]), float(sys.argv[2])))
