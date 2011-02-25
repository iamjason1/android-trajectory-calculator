
import sys,subprocess
from math import *
#The file passed by argument
input_file=open(sys.argv[1],'r')

report_file="./reports/"+sys.argv[1].split(".")[0]+"_LPF-NACC.csv"
#Output strings
last_acc=[0.0,0.0,0.0]
last_grav=[0.0,0.0,0.0]
clean="current time,LPFx,LPFy,LPFz,NACCx,NACCy,NACCz\n"

NANOINSEC=1000000000


#Turns the lineal acc into lineal vel, and standarize the format of the rotational vel
for line in input_file:
	first_split=line.split(",",1)
	second_split=first_split[1].split(",")
	current_time=float(second_split[0])/NANOINSEC
	if (first_split[0]=="LPF"):		
		last_grav=[float(second_split[1]),float(second_split[2]),float(second_split[3])]
		clean+=str(current_time)+","+str(last_grav[0])+","+str(last_grav[1])+","+str(last_grav[2])+","+str(last_acc[0])+","+str(last_acc[1])+","+str(last_acc[2])+"\n"
		
	if(first_split[0]=="NACC"):
		last_acc=[float(second_split[1]),float(second_split[2]),float(second_split[3])]
		clean+=str(current_time)+","+str(last_grav[0])+","+str(last_grav[1])+","+str(last_grav[2])+","+str(last_acc[0])+","+str(last_acc[1])+","+str(last_acc[2])+"\n"
		
input_file.close()


output_file=open(report_file,'w')
output_file.write(clean)
output_file.close()