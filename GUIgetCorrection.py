import os
import glob
import csv
import Tkinter, tkFileDialog
# rename MedicalRecordNumber to serial number using Taioh.txt
#root = Tkinter.Tk()
#root.withdraw()
#fTyp = [("","*.XVI")]

#dirname = tkFileDialog.askdirectory(initialdir="./")
#dirname = dirname + "/"
dirname = "./PatA/"
filename = dirname + "*.INI.XVI"
#print(dirname)
#print(keyword)
files=glob.glob(filename)
#files = './MorningPenta/1.3.46.423632.33592720171226235853625.1.27.12.201785854015.INI.XVI'
writefile = open('./test.csv', 'w')
writefile.write("Date, Time, approver, x, y, z, x-rot, y-rot, z-rot \n")
#print(len(files[0]))
#print(len(files[1]))
##print(files[0])
print(files[1])
filenamelength = 55 #very poor
for file in files:
	if len(file) > filenamelength:
		#print(len(file))
		textlist = []
		for line in open(file,'r'):
			line = line.replace('\n','')
			line = line.replace('\r','')
			if 'AlignmentApprovalDate' in line:
				date = line.replace('AlignmentApprovalDate=','')
				excelDate=date[0:4] + "/" + date[4:6] + "/" + date[6:8]
				date = excelDate 
				
				#date.append(line)
				#print line
			if 'AlignmentApprovalTime' in line:
				time = line.replace('AlignmentApprovalTime=','')
				#time.append(line)
				#print line
			if 'AlignmentApprovalBy' in line:
				approvalby = line.replace('AlignmentApprovalBy=','')
				#approvalby.appen(line)
				#print line
			if 'Align.correction' in line:
				correction = line.replace('Align.correction=','')
			######poor code ! fix it ! from here ########
				#correction.append(line)
				#print line
				splitCorrection = correction.split(",")
				#print splitCorrection[3]
				
				rotx = float(splitCorrection[3])
				roty = float(splitCorrection[4])
				rotz = float(splitCorrection[5])
				if rotx > 350.0:
					rotx = rotx - 360.0
				if roty > 350.0:
					roty = roty - 360.0
				if rotz > 350.0:
					rotz = rotz - 360.0
				
				correction2 = splitCorrection[0] + "," + splitCorrection[1] + "," + splitCorrection[2] + "," + str(rotx) + "," + str(roty) + "," +  str(rotz)
			######poor code ! fix it !  to here ########
				#correction.append(line)
				#print line
		text_tuple = (date+ ',', time+ ',', approvalby+ ',', correction2)
		text = "".join(map(str,text_tuple))
		textlist.append(text)
		#print(textlist[0])
		
	for x in textlist: 
		if len(file) > filenamelength:
			writefile.write(str(textlist[0]) + '\n')
print("Finished!!")