# coding: UTF-8
import os
import glob
import csv
# git_test2

#  keyword = "./*.INI.XVI"
keyword = "./PatB/*.INI.XVI"
files=glob.glob(keyword)

writefile = open('./test.csv', 'w')
writefile.write("Date, Time, approver, x, y, z, x-rot, y-rot, z-rot \n")

#ここ後で改良
filenamelength = 65 #very poor
for file in files:
	if len(file) > filenamelength:
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
				
			#359.0degを-1.0degに変更
				splitCorrection = correction.split(",")
				for i in range(3):
					if float(splitCorrection[i + 3]) > 350.0:
						splitCorrection[i+3] = float(splitCorrection[i + 3]) - 360
				correction = splitCorrection[0] + "," + splitCorrection[1] + "," + splitCorrection[2] + "," + str(splitCorrection[3]) + "," + str(splitCorrection[4]) + "," +  str(splitCorrection[5])
					
		text_tuple = (date+ ',', time+ ',', approvalby+ ',', correction)
		text = "".join(map(str,text_tuple))
		textlist.append(text)
		#print(textlist[0])
		
		for x in textlist: 
			if len(file) > filenamelength:
				writefile.write(str(textlist[0]) + '\n')
print("Finished!!")