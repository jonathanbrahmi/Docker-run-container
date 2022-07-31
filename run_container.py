# This programe is write by jonathan brahmi

# Enter the name of images do you want to run  on container
# then enter the  port you want to use for the container
# and open your browse and enter your ip address and port exmple 172.23.208.1:9000


import os

nginx = 0
adejonge_world = 0
jenkins = 0
dockerui = 0


def run_container():
    print(" + Select container\n")
    print(" - Jenkins\n")
    print(" - dockerui \n")
    print(" - nginx  \n")
    print(" - adejonge/helloworld\n")
    contrun = str(input("Which images you want to run>>"))
    portcont = int(input("Select a port to run the container on it>>"))
    os.system(f"docker run -d -p {portcont}:8080 {contrun}")
    os.system("pause")


run_container()
