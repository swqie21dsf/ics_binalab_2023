import os

for i in range(16):
    for j in range(16):
        for k in range(16):
            res = os.popen("echo " + str(i) + " " + str(j) + " " + str(k) + " | " + "./phase7").read()
            if "Congratulations" in res:
                print(str(i) +" " + str(j) + " " + str(k))

