import csv

positions = ['LCMF', 'LCMF3', 'LDMF', 'DMF', 'RCMF', 'RCMF3', 'RDMF']

with open('Player_A_Diop.csv', encoding="utf-8") as f_in, open('Player_A_Diop2.csv', 'w', encoding="utf8", newline='') as f_out:
    csv_reader = csv.reader(f_in)
    writer = csv.writer(f_out)

    for line in csv_reader:
        if line[3] in positions:
            # checks for midfielder's stats: goals, assists, completed passes
            line[31] = ((float(line[6])/float(line[5])) + float(line[8]) + (float(line[10])/float(line[9])) + (
                float(line[19])/float(line[18])) + (float(line[13])/float(line[12])) + (float(line[28])/float(line[27]))/6)
        writer.writerow(line)


'''
Things to keep in mind:

The importance of different stats: Different stats may have different weights or values in determining a player's rating. For example, goals scored might be given more weight than completed passes.

The context of the stats: The value of a player's stats may vary depending on the context in which they were achieved. For example, a player who scored many goals in a weak league might not be rated as highly as a player who scored fewer goals in a stronger league.

The position of the player: Different positions may require different skills and stats, so a rating system may need to take into account the specific demands of each position.
'''
