import pixelsparser as pp #burnt owes me 200 GBP
import csv
import sys

try:
    print(sys.argv[1], sys.argv[2])
except IndexError:
    print("Please enter filenames when starting the program!")
else:
    pixels = pp.load(sys.argv[1]) 

    data_file = open(sys.argv[2], 'w+')

    fields = ["Date", "Mood", "Notes", "Tags"]

    writer = csv.writer(data_file)
    writer.writerow(fields)

    entries = 0
    while entries < len(pixels):
        column = [pixels[entries].date.strftime('%d/%m/%y'), pixels[entries].mood, pixels[entries].notes, pixels[entries].tags]
        writer.writerow(column)
        entries += 1
        
    data_file.close()
    print("File Created ^-^!")
