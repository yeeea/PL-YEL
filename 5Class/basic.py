class Robot:
    motor=3
    computer=1
    def rotateMotor(a):
        print("Motor operating")
    def motorAngle(a, input):
        answer = input + 60
        return answer

b= Robot()
print(b.motor)
b.rotateMotor()
a=Robot()
print(a.motorAngle(10))
a.computer = 5
print (b.computer)
print (a.computer)
