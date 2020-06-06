# PID controller code by Parikshit Dubey


import matplotlib.pyplot as plt


class PID_controller(object):
    def __init__(self, speed, Kp, Ki, Kd):
        self.KP = Kp
        self.KD = Kd
        self.KI = Ki
        self.speed_set = speed
        self.present_speed = 20
        self.sum_error = 0
        self.now_err = 0
        self.last_err = 0

    def cmd_pid(self):
        self.last_err = self.now_err
        self.now_err = self.speed_set - self.present_speed
        self.sum_error += self.now_err
        self.present_speed = 0.7 * self.present_speed + self.KP * 0.5 * (
                self.speed_set - self.present_speed) + self.KI * 0.5 * self.sum_error + 0.5 * self.KD * (
                                    self.now_err - self.last_err)
        return self.present_speed


pid_values = []
speed_set = []
auto_control_PID = PID_controller(50, 3, 0.5, -0.38)
for i in range(0, 64):
    pid_values.append(auto_control_PID.cmd_pid())
    speed_set.append(auto_control_PID.speed_set)
    print(auto_control_PID.present_speed)
plt.show()
plt.figure('PIDspeed')
plt.ylabel("Vt")
plt.xlabel("t")
plt.plot(pid_values)
plt.plot(speed_set)
plt.show()
