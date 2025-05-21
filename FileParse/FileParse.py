def file_parse(logfile1, logfile2):
        dupe_entries = set()
        parsed_entries = set()
        logfiles = [logfile1, logfile2]

        for logfile in logfiles:
            with open(logfile, 'r') as file:
                for line in file:
                    line = line.strip()
                    this_line = line.split(",")
                    this_entry = (this_line[1], this_line[2])
                    if this_entry in parsed_entries:
                         dupe_entries.add(this_entry)
                    else:
                         parsed_entries.add(this_entry)
            
        return dupe_entries
                         

final_dupes = file_parse("logdata1.csv", "logdata2.csv")
print(final_dupes)

# This is added purely for readability
formatted_dicts_list = []
for dupe in final_dupes:
     formatted_dicts_list.append(
          {
               "UserId": dupe[0],
               "DocId": dupe[1]
          }
     )

print(formatted_dicts_list)