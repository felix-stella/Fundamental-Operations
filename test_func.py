from function import *
import time
start_time=time.time()
exp=Expression(5,100000)
questions,answers=exp.run()
end_time=time.time()
print('time:',end_time-start_time)
print('generated_times:',exp.generation_times)
#with open('./question', "w") as file:
#    for question in questions:
#        file.write(question + "\n")
#with open('./answer', "w") as file:
#    for answer in answers:
#        file.write(answer + "\n")
