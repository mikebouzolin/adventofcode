reports = []
safe_reports = 0
with open("day2_input.txt", "r") as f:
    for line in f:
        reports.append([int(x) for x in line.split()])

for report in reports:
    iterations = 0
    for i in range(len(report) - 1):
        iterations += 1
        if report[i] - report[i+1] < -3 or report[i] - report[i+1] == 0 or report[i] - report[i+1] > 3:
            print("Bad report", report[i] - report[i+1])
            break
        else:
            #print("Passed first check")
            if report[0] > report[1]:
                should_only_increase = True
            elif report[0] < report[1]:
                should_only_increase = False
            if report[i] < report[i+1] and should_only_increase or report[i] > report[i+1] and not should_only_increase:
                print("Bad report, increase/decrease")
                break
            if i == len(report) - 2:
                safe_reports+=1
            
print(safe_reports)
