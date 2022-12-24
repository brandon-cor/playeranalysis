# For Positions - LCMF, LCMF3, LDMF, DMF, RCMF, RCMF3, RDMF

import csv
list = []
with open('Player_A_Diop.csv', encoding="utf-8") as f:q
    csv_reader = csv.reader(f)
    for line in csv_reader:
        # print(line)
        if 'LCMF' in line[3]:
            line[31] = ((float(line[6])/float(line[5])) + float(line[8]) + (float(line[10])/float(line[9])) + (
                float(line[19])/float(line[18])) + (float(line[13])/float(line[12])) + (float(line[28])/float(line[27]))/6)

        if 'LCMF3' in line[3]:
            line[31] = ((float(line[6])/float(line[5])) + float(line[8]) + (float(line[10])/float(line[9])) + (
                float(line[19])/float(line[18])) + (float(line[13])/float(line[12])) + (float(line[28])/float(line[27]))/6)

        if 'LDMF' in line[3]:
            line[31] = ((float(line[6])/float(line[5])) + float(line[8]) + (float(line[10])/float(line[9])) + (
                float(line[19])/float(line[18])) + (float(line[13])/float(line[12])) + (float(line[28])/float(line[27]))/6)

        if 'DMF' in line[3]:
            line[31] = ((float(line[6])/float(line[5])) + float(line[8]) + (float(line[10])/float(line[9])) + (
                float(line[19])/float(line[18])) + (float(line[13])/float(line[12])) + (float(line[28])/float(line[27]))/6)

        if 'RCMF' in line[3]:
            line[31] = ((float(line[6])/float(line[5])) + float(line[8]) + (float(line[10])/float(line[9])) + (
                float(line[19])/float(line[18])) + (float(line[13])/float(line[12])) + (float(line[28])/float(line[27]))/6)

        if 'RCMF3' in line[3]:
            line[31] = ((float(line[6])/float(line[5])) + float(line[8]) + (float(line[10])/float(line[9])) + (
                float(line[19])/float(line[18])) + (float(line[13])/float(line[12])) + (float(line[28])/float(line[27]))/6)

        if 'RDMF' in line[3]:
            line[31] = ((float(line[6])/float(line[5])) + float(line[8]) + (float(line[10])/float(line[9])) + (
                float(line[19])/float(line[18])) + (float(line[13])/float(line[12])) + (float(line[28])/float(line[27]))/6)

        list.append(line)

with open('Player_A_Diop2.csv', 'w', encoding="utf8", newline='') as f:
    writer = csv.writer(f)
    for line in list:
        writer.writerow(line)
