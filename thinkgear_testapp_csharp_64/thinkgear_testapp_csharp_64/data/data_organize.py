import csv

DATA_PATH = "output_raw.csv"
OUTPUT_PATH = "output_organized.csv"
HEADER = ["id", "status", "trial", "packet"]
for i in range(512):
    HEADER.append("raw" + str(i))
ALL_ORGANIZED = []


with open(DATA_PATH, 'r') as file:
    reader = csv.reader(file, delimiter=",")
    next(reader)
    _organized = []
    _id = -1
    _status = -1
    _trial = -1
    _i = 0
    for row in reader:
        if(row[0] != _id or row[1] != _status or row[2] != _trial):
            if(len(_organized) > 0):
                print("id=" + str(_id) + " status=" +
                      str(_status) + " trial=" + str(_trial))
                print(_organized)
                ALL_ORGANIZED.append(_organized)
            print("[INFO] New trial...")
            _id = row[0]
            _status = row[1]
            _trial = row[2]
            _organized = []
            _organized.extend([_id, _status, _trial, _i])
        _organized.append(row[4])
        _i += 1
    print("id=" + _id + " status=" + _status + " trial=" + _trial)
    print(_organized)
    ALL_ORGANIZED.append(_organized)

f = open(OUTPUT_PATH, "w+")
f.close()
with open(OUTPUT_PATH, "w") as file:
    writer = csv.writer(file, delimiter=",")
    writer.writerow(HEADER)
    for line in ALL_ORGANIZED:
        writer.writerow(line)
