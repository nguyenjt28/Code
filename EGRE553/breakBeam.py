import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

enable_pin = 18
coil_A_1_pin = 4
coil_A_2_pin = 17
coil_B_1_pin = 23
coil_B_2_pin = 24

forward_pin = 25
backwards_pin = 26
pin = 21

GPIO.setwarnings(False)
GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(forward_pin, GPIO.IN)
GPIO.setup(backwards_pin, GPIO.IN)
GPIO.setup(enable_pin, GPIO.OUT)
GPIO.setup(coil_A_1_pin, GPIO.OUT)
GPIO.setup(coil_A_2_pin, GPIO.OUT)
GPIO.setup(coil_B_1_pin, GPIO.OUT)
GPIO.setup(coil_B_2_pin, GPIO.OUT)
GPIO.output(enable_pin, 1)

def forward(delay, steps):
  for i in range(0, steps):
    setStep(1, 0, 1, 0)
    time.sleep(delay)
    setStep(0, 1, 1, 0)
    time.sleep(delay)
    setStep(0, 1, 0, 1)
    time.sleep(delay)
    setStep(1, 0, 0, 1)
    time.sleep(delay)

def backwards(delay, steps):
  for i in range(0, steps):
    setStep(1, 0, 0, 1)
    time.sleep(delay)
    setStep(0, 1, 0, 1)
    time.sleep(delay)
    setStep(0, 1, 1, 0)
    time.sleep(delay)
    setStep(1, 0, 1, 0)
    time.sleep(delay)

def setStep(w1, w2, w3, w4):
  GPIO.output(coil_A_1_pin, w1)
  GPIO.output(coil_A_2_pin, w2)
  GPIO.output(coil_B_1_pin, w3)
  GPIO.output(coil_B_2_pin, w4)

count = 0
previousState = 1
turned = 0

while True:
  sensorState = GPIO.input(pin)
  delay = 10
  steps = 1
  forward_input = GPIO.input(25)
  backwards_input = GPIO.input(26)

  if not sensorState:
        previousState = sensorState
#       time.sleep(2)

  if previousState != sensorState:
        count += 1
        print("Count: %d" %count)
        previousState = sensorState

  if count == 5:
        if not turned:
                turned = 1
                for i in range(0,20):
                        forward(int(delay) / 1000.0, int(steps))

  if count == 10:
        if turned:
                for i in range(0,20):
                        backwards(int(delay) / 1000.0, int(steps))
        turned = 0
        count = 0

#  if (forward_input == 1):
#        forward(int(delay) / 1000.0, int(steps))
#  if (backwards_input == 1):
#        backwards(int(delay) / 1000.0, int(steps))









