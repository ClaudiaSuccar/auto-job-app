from datetime import date

# Holds skills most relevant to me
keywords = ['.net', 'cad', 'analysis', 'processing', 'cobol', 'spreadsheet', 'excel', 'ms office', 'microsoft office', 'python', 'html', 'css', 'sql', 'mysql', 'javascript', 'frontend', 'front end', 'web application', 'web development', 'leader', 'leadership', 'communication', 'collaborative', 'collaboration', 'problem-solving', 'dom', 'learner', 'learn', 'github', 'git', 'linux', 'windows', 'mac']

# Read lines within document
descfile = open('description.txt', 'r')
description = descfile.readlines()

# Parses list into string
description = str(description).lower()

# Initialize empty list to store found keywords in description file
keywords_found = []

# Stores found keywords into the list
for word in keywords:
    if word in description:
        keywords_found.append(word)

print('Keywords found', keywords_found)

# stores keywords related to job category
data = ['.net', 'cobol', 'python', 'analysis', 'spreadsheet', 'excel', 'processing', 'sql', 'mysql']
frontend = ['frontend', 'front end', 'javascript', 'html', 'css', 'web application', 'web development', 'dom']

# Initialize empty list to store how many data or frontend keywords were found
data_found = []
frontend_found = []

# Creates two separate lists that hold both data or frontend keywords, if number of keywords found is greater than 3
if len(keywords_found) >= 3:
    for word in keywords_found:
        if word in data:
            data_found.append(word) # add found keyword to corresponding job type
        elif word in frontend:
            frontend_found.append(word)
else:
    print('Not enough keywords found.')

# Initialize empty string to hold job type
jobtype = ''

# Determines if the job post is either a data job or frontend job, however if the above condition did not append anything, it will be an unsuitable job
# Sets job type to either data or frontend
if len(data_found) > len(frontend_found):
    print('Use data resume.')
    jobtype = 'data'
elif len(data_found) < len(frontend_found):
    jobtype = 'frontend'
    print('Use frontend resume.')
else:
    print('Either data or frontend.')

# The following take in information to prepare for cover letter,
company = input("Exit or enter company name to proceed: ")
print('Company name is', company)

# Gets and formats current date for header
date = date.today().strftime("%m/%d/%y")

#Asks for inputs which will be inserted into the cover letter
jobtitle = input("Enter job title: ")
source = input("Enter job post source: ")
mission = input("Enthusiasm for <mission>: ")
problem = input("Desire to solve <problem>: ")
technology = input("Known for building <technology>: ")
emphasis = input("With emphasis on <emphasis>: ")
skill1 = input("Skill 1: ")
skill2 = input("Skill 2: ")
skill3 = input("Skill 3: ")

# Setup for cover letters
frontend_cover = "Setup cover letter here.\nInput string format -> {0} {1} {2} {3} {4} {5} {6} {7} {8} {9} {10}".format(date, jobtitle, source, company, mission, problem, technology, emphasis, skill1, skill2, skill3)

data_cover = "Setup cover letter here.\nInput string format -> {0} {1} {2} {3} {4} {5} {6} {7} {8} {9} {10}".format(date, jobtitle, source, company, mission, problem, technology, emphasis, skill1, skill2, skill3)

# References the cover.txt file
cover = open('cover.txt', 'w')

# Writes cover letter based on jobtype
if jobtype == 'frontend':
    cover.write(frontend_cover)
    print('Writing frontend cover...\nComplete! See cover.txt file.')
else:
    cover.write(data_cover)
    print('Writing data cover...\nComplete! See cover.txt file.')
ECHO is on.
