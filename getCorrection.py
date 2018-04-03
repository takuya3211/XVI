import os
import glob
import csv
# rename MedicalRecordNumber to serial number using Taioh.txt
# git_test

keyword = "./PatB/*.INI.XVI"
#print(keyword)
files=glob.glob(keyword)
#files = './MorningPenta/1.3.46.423632.33592720171226235853625.1.27.12.201785854015.INI.XVI'
writefile = open('./test.csv', 'w')
writefile.write("Date, Time, approver, x, y, z, x-rot, y-rot, z-rot \n")
#print(len(files[0]))
#print(len(files[1]))
#print(files[0])
#print(files[1])
filenamelength = 65 #very poor
for file in files:
	print(file)
	print (len(file))
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
				for i in range(3):
					if float(splitCorrection[i + 3]) > 350.0:
						splitCorrection[i+3] = float(splitCorrection[i + 3]) - 360
				correction = splitCorrection[0] + "," + splitCorrection[1] + "," + splitCorrection[2] + "," + str(splitCorrection[3]) + "," + str(splitCorrection[4]) + "," +  str(splitCorrection[5])
			######poor code ! fix it !  to here ########
					
		text_tuple = (date+ ',', time+ ',', approvalby+ ',', correction)
		text = "".join(map(str,text_tuple))
		textlist.append(text)
		#print(textlist[0])
		
		for x in textlist: 
			if len(file) > filenamelength:
				writefile.write(str(textlist[0]) + '\n')
	print("Finished!!")