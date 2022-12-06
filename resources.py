full_resources = {"Main Page": [], "Link": [], "Resource Title": [], "College": [], "Department": [], "Category": []}

#######################     Academic Resources      #######################

#there are more academic resources on this page    https://www.usu.edu/current-students/

arts_departments = ['Art', 'Music', 'Theature']
i = 0
for d in arts_departments:
    full_resources["Main Page"].append("https://www.usu.edu/academics/colleges/")
    full_resources["Link"].append("https://cca.usu.edu/"+arts_departments[i]+"/")
    full_resources["Resource Title"].append("College Specific Information")
    full_resources["College"].append("Caine College of the Arts")
    full_resources["Department"].append(arts_departments[i])
    full_resources["Category"].append("General - Department Information")
    i += 1

full_resources["Main Page"].append("https://www.usu.edu/academics/colleges/")
full_resources["Link"].append("https://cca.usu.edu/")
full_resources["Resource Title"].append("College Specific Information")
full_resources["College"].append("Caine College of the Arts")
full_resources["Department"].append("All")
full_resources["Category"].append("General - College Information")

#this could be mined further
full_resources["Main Page"].append("https://www.usu.edu/academics/colleges/")
full_resources["Link"].append("https://www.usu.edu/degrees/index.cfm?browse&c=8&l=undergraduate")
full_resources["Resource Title"].append("College Specific Information")
full_resources["College"].append("Caine College of the Arts")
full_resources["Department"].append("All")
full_resources["Category"].append("Academic Information")


ag_departments = ['advs', 'apec', 'avte', 'laep', 'ndfs', 'psc']
ag_departments_full = ['Animal, Dairy and Veterinary Sciences', 'Applied Economics', 'Applied Sciences, Technology and Education', 'Aviation and Technical Education', 'Landscape Architecture and Environmental Planning', 'Nutrition, Dietetics, and Food Sciences', 'Plants, Soils, and Climate', 'School of Veterinary Medicine']
i = 0
for d in ag_departments:
    full_resources["Main Page"].append("https://www.usu.edu/academics/colleges/")
    full_resources["Link"].append("https://caas.usu.edu/"+ag_departments[i]+"/")
    full_resources["Resource Title"].append("College Specific Information")
    full_resources["College"].append("College of Agriculture and Applied Sciences")
    full_resources["Department"].append(ag_departments_full[i])
    full_resources["Category"].append("General - Department Information")
    i += 1
    
full_resources["Main Page"].append("https://www.usu.edu/academics/colleges/")
full_resources["Link"].append("https://aste.usu.edu/")
full_resources["Resource Title"].append("College Specific Information")
full_resources["College"].append("All")
full_resources["Department"].append("All")
full_resources["Category"].append("General - College Information")

full_resources["Main Page"].append("https://www.usu.edu/academics/colleges/")
full_resources["Link"].append("https://caas.usu.edu/advs/")
full_resources["Resource Title"].append("College Specific Information")
full_resources["College"].append("College of Agriculture and Applied Sciences")
full_resources["Department"].append("Animal, Dairy and Veterinary Sciences")
full_resources["Category"].append("General - College Information")

full_resources["Main Page"].append("https://www.usu.edu/academics/colleges/")
full_resources["Link"].append("https://vetmed.usu.edu/")
full_resources["Resource Title"].append("College Specific Information")
full_resources["College"].append("College of Veterinary Medicine")
full_resources["Department"].append("All")
full_resources["Category"].append("General - College Information")

full_resources["Main Page"].append("https://www.usu.edu/academics/colleges/")
full_resources["Link"].append("https://caas.usu.edu/")
full_resources["Resource Title"].append("College Specific Information")
full_resources["College"].append("College of Agriculture and Applied Sciences")
full_resources["Department"].append("All")
full_resources["Category"].append("General - College Information")

full_resources["Main Page"].append("https://www.usu.edu/academics/colleges/")
full_resources["Link"].append("https://www.usu.edu/degrees/index.cfm?browse&c=1&l=undergraduate")
full_resources["Resource Title"].append("College Specific Information")
full_resources["College"].append("College of Agriculture and Applied Sciences")
full_resources["Department"].append("All")
full_resources["Category"].append("Academic Information")

eng_departments = ['be/', 'cee', 'ece', 'eed', 'mae']
eng_departments_full = ['Biological Engineering', 'Civil and Environmental Engineering', 'Electrical and Computer Engineering', 'Engineering Education', 'Mechanical and Aerospace Engineering']
i = 0
for d in eng_departments:
    full_resources["Main Page"].append("https://www.usu.edu/academics/colleges/")
    full_resources["Link"].append("https://engineering.usu.edu/"+eng_departments[i]+"/")
    full_resources["Resource Title"].append("College Specific Information")
    full_resources["College"].append("College of Agriculture and Applied Sciences")
    full_resources["Department"].append(eng_departments_full[i])
    full_resources["Category"].append("General - Department Information")
    i += 1

full_resources["Main Page"].append("https://www.usu.edu/academics/colleges/")
full_resources["Link"].append("https://engineering.usu.edu/")
full_resources["Resource Title"].append("College Specific Information")
full_resources["College"].append("College of Engineering")
full_resources["Department"].append("All")
full_resources["Category"].append("General - College Information")

full_resources["Main Page"].append("https://www.usu.edu/academics/colleges/")
full_resources["Link"].append("https://www.usu.edu/degrees/index.cfm?browse&c=4&l=undergraduate")
full_resources["Resource Title"].append("College Specific Information")
full_resources["College"].append("College of Engineering")
full_resources["Department"].append("All")
full_resources["Category"].append("Academic Information")

hum_departments = ['aerospace', 'cai', 'csph-department', 'history', 'english', 'journalism', 'military-science', 'political-science', 'social-work', 'soca-department', 'languages']
hum_departments_full = ['Air Force ROTC', 'Center for Anticipatory Intelligence', 'Communications Studies & Philosophy', 'History', 'English', 'Journalism', 'Military Science', 'Political Science', 'Social Work','Sociology and Anthropology', 'World Languages and Cultures' ]
i = 0
for d in hum_departments:
    full_resources["Main Page"].append("https://www.usu.edu/academics/colleges/")
    full_resources["Link"].append("https://usu.edu/"+hum_departments[i]+"/")
    full_resources["Resource Title"].append("College Specific Information")
    full_resources["College"].append("College of Agriculture and Applied Sciences")
    full_resources["Department"].append(hum_departments_full[i])
    full_resources["Category"].append("General - Department Information")
    i += 1
    
full_resources["Main Page"].append("https://www.usu.edu/academics/colleges/")
full_resources["Link"].append("https://chass.usu.edu/")
full_resources["Resource Title"].append("College Specific Information")
full_resources["College"].append("College of Humanities and Social Sciences")
full_resources["Department"].append("All")
full_resources["Category"].append("General - College Information")

full_resources["Main Page"].append("https://www.usu.edu/academics/colleges/")
full_resources["Link"].append("https://www.usu.edu/degrees/index.cfm?browse&c=5&l=undergraduate")
full_resources["Resource Title"].append("College Specific Information")
full_resources["College"].append("College of Humanities and Social Sciences")
full_resources["Department"].append("All")
full_resources["Category"].append("Academic Information")

#working on teh College of Science
sc_departments = ['biology', 'chem', 'cs', 'geo', 'math', 'physics']
sc_departments_full = ['Biology', 'Chemistry and Biochemistry', 'Computer Science', 'Geosciences','mathematics and Statistics', 'Physics']
i = 0
for d in sc_departments:
    full_resources["Main Page"].append("https://www.usu.edu/academics/colleges/")
    full_resources["Link"].append("https://usu.edu/"+sc_departments[i]+"/")
    full_resources["Resource Title"].append("College Specific Information")
    full_resources["College"].append("College of Agriculture and Applied Sciences")
    full_resources["Department"].append(sc_departments_full[i])
    full_resources["Category"].append("General - Department Information")
    i += 1

full_resources["Main Page"].append("https://www.usu.edu/academics/colleges/")
full_resources["Link"].append("https://www.usu.edu/science/")
full_resources["Resource Title"].append("College Specific Information")
full_resources["College"].append("College of Science")
full_resources["Department"].append("All")
full_resources["Category"].append("General - College Information")

full_resources["Main Page"].append("https://www.usu.edu/academics/colleges/")
full_resources["Link"].append("https://www.usu.edu/degrees/index.cfm?browse&c=6&l=undergraduate")
full_resources["Resource Title"].append("College Specific Information")
full_resources["College"].append("College of Science")
full_resources["Department"].append("All")
full_resources["Category"].append("Academic Information")

full_resources["Main Page"].append("https://www.usu.edu/academics/colleges/")
full_resources["Link"].append("https://vetmed.usu.edu/")
full_resources["Resource Title"].append("College Specific Information")
full_resources["College"].append("College of Veterinary Medicine")
full_resources["Department"].append("All")
full_resources["Category"].append("General - College Information")

full_resources["Main Page"].append("https://www.usu.edu/academics/colleges/")
full_resources["Link"].append("https://www.usu.edu/degrees/index.cfm?browse&c=27&l=undergraduate")
full_resources["Resource Title"].append("College Specific Information")
full_resources["College"].append("College of Veterinary Medicine")
full_resources["Department"].append("All")
full_resources["Category"].append("Academic Information")

#College of Education and human services
ed_departments = ['hdfs', 'itls', 'khs', 'psychology', 'teal', 'sperc']
ed_departments_full = ['Human Development and Family Studies', 'Instructional Technology & Learning Sciences', 'Kinesiology and Health Science', 'Psychology', 'Teacher Education and Leadership', 'Special Education and Rehabilitation Counseling']
i = 0
for d in ed_departments:
    full_resources["Main Page"].append("https://www.usu.edu/academics/colleges/")
    full_resources["Link"].append("https://cehs.usu.edu/"+ed_departments[i]+"/")
    full_resources["Resource Title"].append("College Specific Information")
    full_resources["College"].append("College of Agriculture and Applied Sciences")
    full_resources["Department"].append(ed_departments_full[i])
    full_resources["Category"].append("General - Department Information")
    i += 1
    
full_resources["Main Page"].append("https://www.usu.edu/academics/colleges/")
full_resources["Link"].append("https://comdde.usu.edu/")
full_resources["College"].append("College of Agriculture and Applied Sciences")
full_resources["Resource Title"].append("College Specific Information")
full_resources["Department"].append("Communicative Disorders and Deaf Education")
full_resources["Category"].append("General - Department Information")    

full_resources["Main Page"].append("https://www.usu.edu/academics/colleges/")
full_resources["Link"].append("https://nursing.usu.edu/")
full_resources["Resource Title"].append("College Specific Information")
full_resources["College"].append("College of Agriculture and Applied Sciences")
full_resources["Department"].append("Nursing")
full_resources["Category"].append("General - Department Information") 

full_resources["Main Page"].append("https://www.usu.edu/academics/colleges/")
full_resources["Link"].append("https://cehs.usu.edu/")
full_resources["Resource Title"].append("College Specific Information")
full_resources["College"].append("College of Education and Human Services")
full_resources["Department"].append("All")
full_resources["Category"].append("General - College Information")

full_resources["Main Page"].append("https://www.usu.edu/academics/colleges/")
full_resources["Link"].append("https://www.usu.edu/degrees/index.cfm?browse&c=3&l=undergraduate")
full_resources["Resource Title"].append("College Specific Information")
full_resources["College"].append("College of Education and Human Services")
full_resources["Department"].append("All")
full_resources["Category"].append("Academic Information")

bus_departments = ['dais', 'economicsandfinance', 'management', 'marketingandstrategy', 'acct']
bus_departments_full = ['Data Analytics & Information Systems', 'Economics and Finance', 'Management', 'Marketing and Strategy', 'Accounting']
i = 0
for d in bus_departments:
    full_resources["Main Page"].append("https://www.usu.edu/academics/colleges/")
    full_resources["Link"].append("https://huntsman.usu.edu/"+bus_departments[i]+"/")
    full_resources["Resource Title"].append("College Specific Information")
    full_resources["College"].append("College of Agriculture and Applied Sciences")
    full_resources["Department"].append(bus_departments_full[i])
    full_resources["Category"].append("General - Department Information")
    i += 1
    
full_resources["Main Page"].append("https://www.usu.edu/academics/colleges/")
full_resources["Link"].append("https://huntsman.usu.edu/")
full_resources["Resource Title"].append("College Specific Information")
full_resources["College"].append("Huntsman School of Business")
full_resources["Department"].append("All")
full_resources["Category"].append("General - College Information")

full_resources["Main Page"].append("https://www.usu.edu/academics/colleges/")
full_resources["Link"].append("https://www.usu.edu/degrees/index.cfm?browse&c=2&l=undergraduate")
full_resources["Resource Title"].append("College Specific Information")
full_resources["College"].append("Huntsman School of Business")
full_resources["Department"].append("All")
full_resources["Category"].append("Academic Information")    

nat_departments = ['envs', 'wats', 'wild']
nat_departments_full = ['Environment and Society', 'Watershed Sciences', 'Wildland Resources']
i = 0
for d in nat_departments:
    full_resources["Main Page"].append("https://www.usu.edu/academics/colleges/")
    full_resources["Link"].append("https://huntsman.usu.edu/"+nat_departments[i]+"/")
    full_resources["Resource Title"].append("College Specific Information")
    full_resources["College"].append("College of Agriculture and Applied Sciences")
    full_resources["Department"].append(nat_departments_full[i])
    full_resources["Category"].append("General - Department Information")
    i += 1
    
full_resources["Main Page"].append("https://www.usu.edu/academics/colleges/")
full_resources["Link"].append("https://qcnr.usu.edu/")
full_resources["Resource Title"].append("College Specific Information")
full_resources["College"].append("College of Natural Resources")
full_resources["Department"].append("All")
full_resources["Category"].append("General - College Information")

full_resources["Main Page"].append("https://www.usu.edu/academics/colleges/")
full_resources["Link"].append("https://www.usu.edu/degrees/index.cfm?browse&c=7&l=undergraduate")
full_resources["Resource Title"].append("College Specific Information")
full_resources["College"].append("College of Natural Resources")
full_resources["Department"].append("All")
full_resources["Category"].append("Academic Information") 

#Everything before this needs a line added for resource title
#################     Health Resources       #################################

#most of thiese links have others within them. They could be mined further if needed
full_resources["Main Page"].append("https://www.usu.edu/current-students/")
full_resources["Link"].append("https://www.usu.edu/aggiewellness/shwc/")
full_resources["Resource Title"].append("Support and Nourish Your Body")
full_resources["College"].append("All")
full_resources["Department"].append("All")
full_resources["Category"].append("Physical Health") 

full_resources["Main Page"].append("https://www.usu.edu/current-students/")
full_resources["Link"].append("https://www.usu.edu/aggiewellness/shwc/")
full_resources["Resource Title"].append("Find Resources")
full_resources["College"].append("All")
full_resources["Department"].append("All")
full_resources["Category"].append("Other Health - All") 

full_resources["Main Page"].append("https://usu.edu/aggiewellness/")
full_resources["Link"].append("https://www.usu.edu/aggiewellness/mental-health")
full_resources["Resource Title"].append("Improve Your Mental Well-Being")
full_resources["College"].append("All")
full_resources["Department"].append("All")
full_resources["Category"].append("Mental Health")

full_resources["Main Page"].append("https://usu.edu/aggiewellness/")
full_resources["Link"].append("https://www.usu.edu/aggiewellness/recreation")
full_resources["Resource Title"].append("Maintain Physical Wellness")
full_resources["College"].append("All")
full_resources["Department"].append("All")
full_resources["Category"].append("Physical Health")

full_resources["Main Page"].append("https://usu.edu/aggiewellness/")
full_resources["Link"].append("https://www.usu.edu/aggiewellness/relationship-wellness")
full_resources["Resource Title"].append("Create Healthy Relationships")
full_resources["College"].append("All")
full_resources["Department"].append("All")
full_resources["Category"].append("Other Health - Relationship")

#this would be a good resource if you needed help for a friend
full_resources["Main Page"].append("https://usu.edu/aggiewellness/")
full_resources["Link"].append("https://www.usu.edu/aggiewellness/help-others")
full_resources["Resource Title"].append("Help Others in Distress")
full_resources["College"].append("All")
full_resources["Department"].append("All")
full_resources["Category"].append("Other Health - All")

full_resources["Main Page"].append("https://usu.edu/aggiewellness/")
full_resources["Link"].append("https://www.usu.edu/aggiewellness/tools")
full_resources["Resource Title"].append("Access Preventative and Educational Tools")
full_resources["College"].append("All")
full_resources["Department"].append("All")
full_resources["Category"].append("Other Health - All")

full_resources["Main Page"].append("https://usu.edu/aggiewellness/")
full_resources["Link"].append("https://www.usu.edu/aggiewellness/tools")
full_resources["Resource Title"].append("Improve Your Mental Well-Being")
full_resources["College"].append("All")
full_resources["Department"].append("All")
full_resources["Category"].append("Other Health - All")

full_resources["Main Page"].append("https://www.usu.edu/snac/")
full_resources["Link"].append("https://www.usu.edu/snac/")
full_resources["Resource Title"].append("Student Nutrition Access Center (SNAC)")
full_resources["College"].append("All")
full_resources["Department"].append("All")
full_resources["Category"].append("Physical Health & Financial Support")

####################      Safety Resources      ##########################

full_resources["Main Page"].append("https://usu.edu/aggiewellness/")
full_resources["Link"].append("https://www.usu.edu/dps/")
full_resources["Resource Title"].append("Department of Public Safety")
full_resources["College"].append("All")
full_resources["Department"].append("All")
full_resources["Category"].append("Safety - All")

full_resources["Main Page"].append("https://usu.edu/aggiewellness/")
full_resources["Link"].append("https://www.usu.edu/dps/emergency/alerts")
full_resources["Resource Title"].append("Aggie Alerts")
full_resources["College"].append("All")
full_resources["Department"].append("All")
full_resources["Category"].append("Safety - All")

#campus can jump start cars and unlock your car if you leave the keys in it
#this is cool, would have to code a lot more things though
full_resources["Main Page"].append("https://usu.edu/aggiewellness/")
full_resources["Link"].append("https://www.usu.edu/dps/police")
full_resources["Resource Title"].append("USU Police Department")
full_resources["College"].append("All")
full_resources["Department"].append("All")
full_resources["Category"].append("Safety and Services")

full_resources["Main Page"].append("https://usu.edu/aggiewellness/")
full_resources["Link"].append("https://www.usu.edu/student-conduct/")
full_resources["Resource Title"].append("Office of Student Conduct and Community Standards")
full_resources["College"].append("All")
full_resources["Department"].append("All")
full_resources["Category"].append("Safety - All")

############### Financial Resources ##################

full_resources["Main Page"].append("https://www.usu.edu/current-students/")
full_resources["Link"].append("https://www.usu.edu/student-conduct/")
full_resources["Resource Title"].append("Tuition and Payment")
full_resources["College"].append("All")
full_resources["Department"].append("All")
full_resources["Category"].append("Financial - Tuition Information")

full_resources["Main Page"].append("https://www.usu.edu/current-students/")
full_resources["Link"].append("https://login.usu.edu/cas/login?service=https%3A%2F%2Fsecure.touchnet.com%3A443%2FC20241_tsa%2Fweb%2Fcaslogin.jsp")
full_resources["Resource Title"].append("Online Tuition Payment")
full_resources["College"].append("All")
full_resources["Department"].append("All")
full_resources["Category"].append("Financial - Tuition Information")

full_resources["Main Page"].append("https://www.usu.edu/current-students/")
full_resources["Link"].append("https://www.usu.edu/financial-support/federalaid")
full_resources["Resource Title"].append("Federal Aid at USU")
full_resources["College"].append("All")
full_resources["Department"].append("All")
full_resources["Category"].append("Financial Support")

full_resources["Main Page"].append("https://www.usu.edu/current-students/")
full_resources["Link"].append("https://www.usu.edu/financial-support/scholarships")
full_resources["Resource Title"].append("Scholarships")
full_resources["College"].append("All")
full_resources["Department"].append("All")
full_resources["Category"].append("Financial Support")

full_resources["Main Page"].append("https://www.usu.edu/current-students/")
full_resources["Link"].append("https://www.usu.edu/financial-support/smmc")
full_resources["Resource Title"].append("Student Money Mangement Center")
full_resources["College"].append("All")
full_resources["Department"].append("All")
full_resources["Category"].append("Financial Support")

full_resources["Main Page"].append("https://www.usu.edu/financial-support/")
full_resources["Link"].append("https://www.usu.edu/financial-support/")
full_resources["Resource Title"].append("Student Financial Support")
full_resources["College"].append("All")
full_resources["Department"].append("All")
full_resources["Category"].append("Financial Support")

################     Registration Resources      ####################

full_resources["Main Page"].append("https://www.usu.edu/current-students/")
full_resources["Link"].append("https://catalog.usu.edu/content.php?catoid=12&navoid=3320")
full_resources["Resource Title"].append("Academic & Registration Calendars")
full_resources["College"].append("All")
full_resources["Department"].append("All")
full_resources["Category"].append("Academic - Registration Information")

full_resources["Main Page"].append("https://www.usu.edu/current-students/")
full_resources["Link"].append("https://www.usu.edu/registrar/records/")
full_resources["Resource Title"].append("Records - Who You Are on Paper")
full_resources["College"].append("All")
full_resources["Department"].append("All")
full_resources["Category"].append("General - Personal Information")

full_resources["Main Page"].append("https://www.usu.edu/current-students/")
full_resources["Link"].append("https://www.usu.edu/registrar/records/access/")
full_resources["Resource Title"].append("Access Your Records")
full_resources["College"].append("All")
full_resources["Department"].append("All")
full_resources["Category"].append("General - Personal Information")

full_resources["Main Page"].append("https://www.usu.edu/current-students/")
full_resources["Link"].append("https://www.usu.edu/registrar/registration/resolving-holds")
full_resources["Resource Title"].append("Resolving Holds")
full_resources["College"].append("All")
full_resources["Department"].append("All")
full_resources["Category"].append("Academic - Registration Problems")

full_resources["Main Page"].append("https://www.usu.edu/current-students/")
full_resources["Link"].append("https://www.usu.edu/registrar/graduation/")
full_resources["Resource Title"].append("Graduation")
full_resources["College"].append("All")
full_resources["Department"].append("All")
full_resources["Category"].append("Academic - Graduation Information")

full_resources["Main Page"].append("https://www.usu.edu/current-students/")
full_resources["Link"].append("https://www.usu.edu/registrar/registration/")
full_resources["Resource Title"].append("Registration - How to Register")
full_resources["College"].append("All")
full_resources["Department"].append("All")
full_resources["Category"].append("Academic - Registration Information")

full_resources["Main Page"].append("https://www.usu.edu/current-students/")
full_resources["Link"].append("https://www.usu.edu/advisors/")
full_resources["Resource Title"].append("Find Your Advisor")
full_resources["College"].append("All")
full_resources["Department"].append("All")
full_resources["Category"].append("Academic Information & Academic - Registration Problems")

######################     USU Academic Resources     #######################

full_resources["Main Page"].append("https://www.usu.edu/current-students/")
full_resources["Link"].append("https://www.usu.edu/academics/colleges/")
full_resources["Resource Title"].append("Colleges and Schools")
full_resources["College"].append("All")
full_resources["Department"].append("All")
full_resources["Category"].append("Academic Information")

full_resources["Main Page"].append("https://www.usu.edu/current-students/")
full_resources["Link"].append("https://www.usu.edu/degrees/")
full_resources["Resource Title"].append("Find a Degree")
full_resources["College"].append("All")
full_resources["Department"].append("All")
full_resources["Category"].append("Academic Information")

full_resources["Main Page"].append("https://www.usu.edu/current-students/")
full_resources["Link"].append("https://www.usu.edu/advising/")
full_resources["Resource Title"].append("Advising")
full_resources["College"].append("All")
full_resources["Department"].append("All")
full_resources["Category"].append("Academic Information")

full_resources["Main Page"].append("https://www.usu.edu/current-students/")
full_resources["Link"].append("https://catalog.usu.edu/")
full_resources["Resource Title"].append("General Catalog")
full_resources["College"].append("All")
full_resources["Department"].append("All")
full_resources["Category"].append("Academic Information")

full_resources["Main Page"].append("https://www.usu.edu/current-students/")
full_resources["Link"].append("https://www.usu.edu/commencement/")
full_resources["Resource Title"].append("Commencement")
full_resources["College"].append("All")
full_resources["Department"].append("All")
full_resources["Category"].append("Academic - Graduation Information")

full_resources["Main Page"].append("https://www.usu.edu/current-students/")
full_resources["Link"].append("https://research.usu.edu/")
full_resources["Resource Title"].append("USU Office of Research")
full_resources["College"].append("All")
full_resources["Department"].append("All")
full_resources["Category"].append("Academic Information - Research")

#this is a big one with a lot of links
full_resources["Main Page"].append("https://www.usu.edu/current-students/")
full_resources["Link"].append("https://www.usu.edu/academic-support/")
full_resources["Resource Title"].append("Academic Support")
full_resources["College"].append("All")
full_resources["Department"].append("All")
full_resources["Category"].append("Academic Support")

full_resources["Main Page"].append("https://www.usu.edu/current-students/")
full_resources["Link"].append("https://www.usu.edu/asp//")
full_resources["Resource Title"].append("Academic Success Programs")
full_resources["College"].append("All")
full_resources["Department"].append("All")
full_resources["Category"].append("Academic Support")

#######################       Diversity and Inclusion     #################

full_resources["Main Page"].append("https://www.usu.edu/current-students/")
full_resources["Link"].append("https://www.usu.edu/equity/")
full_resources["Resource Title"].append("Office of Equity")
full_resources["College"].append("All")
full_resources["Department"].append("All")
full_resources["Category"].append("Diversity and Inclusion")

full_resources["Main Page"].append("https://www.usu.edu/current-students/")
full_resources["Link"].append("https://www.usu.edu/inclusion/")
full_resources["Resource Title"].append("Inclusion Center")
full_resources["College"].append("All")
full_resources["Department"].append("All")
full_resources["Category"].append("Diversity and Inclusion")

full_resources["Main Page"].append("https://www.usu.edu/current-students/")
full_resources["Link"].append("https://chass.usu.edu/interfaith/")
full_resources["Resource Title"].append("Interfaith Initiative")
full_resources["College"].append("All")
full_resources["Department"].append("All")
full_resources["Category"].append("Diversity and Inclusion")

full_resources["Main Page"].append("https://www.usu.edu/current-students/")
full_resources["Link"].append("https://www.usu.edu/intersections/")
full_resources["Resource Title"].append("Challenging Inequality")
full_resources["College"].append("All")
full_resources["Department"].append("All")
full_resources["Category"].append("Diversity and Inclusion & Academic Information - Research")

full_resources["Main Page"].append("https://www.usu.edu/current-students/")
full_resources["Link"].append("https://www.usu.edu/latinx/")
full_resources["Resource Title"].append("Latinx Cultural Center")
full_resources["College"].append("All")
full_resources["Department"].append("All")
full_resources["Category"].append("Diversity and Inclusion")

full_resources["Main Page"].append("https://www.usu.edu/current-students/")
full_resources["Link"].append("https://www.usu.edu/global-engagement/")
full_resources["Resource Title"].append("Office of Global Engagement")
full_resources["College"].append("All")
full_resources["Department"].append("All")
full_resources["Category"].append("Diversity and Inclusion")

full_resources["Main Page"].append("https://www.usu.edu/current-students/")
full_resources["Link"].append("https://www.usu.edu/think-care-act/")
full_resources["Resource Title"].append("Aggies Think, Care, Act")
full_resources["College"].append("All")
full_resources["Department"].append("All")
full_resources["Category"].append("Diversity and Inclusion")

full_resources["Main Page"].append("https://www.usu.edu/current-students/")
full_resources["Link"].append("https://www.usu.edu/freespeech/")
full_resources["Resource Title"].append("Free Speech and Expression")
full_resources["College"].append("All")
full_resources["Department"].append("All")
full_resources["Category"].append("Diversity and Inclusion")

######################     Involvement     #########################

full_resources["Main Page"].append("https://www.usu.edu/current-students/")
full_resources["Link"].append("https://www.usu.edu/student-affairs/")
full_resources["Resource Title"].append("Division of Student Affairs")
full_resources["College"].append("All")
full_resources["Department"].append("All")
full_resources["Category"].append("Involvement & Wellness")

full_resources["Main Page"].append("https://www.usu.edu/current-students/")
full_resources["Link"].append("https://www.usu.edu/involvement/")
full_resources["Resource Title"].append("Student Involvement")
full_resources["College"].append("All")
full_resources["Department"].append("All")
full_resources["Category"].append("Involvement")

full_resources["Main Page"].append("https://www.usu.edu/current-students/")
full_resources["Link"].append("https://www.usu.edu/involvement/clubs/index")
full_resources["Resource Title"].append("USUSA Clubs")
full_resources["College"].append("All")
full_resources["Department"].append("All")
full_resources["Category"].append("Involvement")

full_resources["Main Page"].append("https://www.usu.edu/current-students/")
full_resources["Link"].append("https://www.usu.edu/involvement/fsl/index")
full_resources["Resource Title"].append("Fraternity and Sorority Life")
full_resources["College"].append("All")
full_resources["Department"].append("All")
full_resources["Category"].append("Involvement & Other Health - Social")

full_resources["Main Page"].append("https://www.usu.edu/current-students/")
full_resources["Link"].append("https://www.usu.edu/involvement/hurd/")
full_resources["Resource Title"].append("Utah State Hurd")
full_resources["College"].append("All")
full_resources["Department"].append("All")
full_resources["Category"].append("Involvement & Physical Health - Athletics")

full_resources["Main Page"].append("https://www.usu.edu/current-students/")
full_resources["Link"].append("https://www.usu.edu/involvement/spirit-squad/")
full_resources["Resource Title"].append("The USU Spirit Squad")
full_resources["College"].append("All")
full_resources["Department"].append("All")
full_resources["Category"].append("Involvement & Physical Health - Athletics")


#################      Campus Life    ################

full_resources["Main Page"].append("https://www.usu.edu/current-students/")
full_resources["Link"].append("https://www.usu.edu/housing/")
full_resources["Resource Title"].append("Housing Services")
full_resources["College"].append("All")
full_resources["Department"].append("All")
full_resources["Category"].append("USU Living")

full_resources["Main Page"].append("https://www.usu.edu/current-students/")
full_resources["Link"].append("https://utahstateaggies.com/")
full_resources["Resource Title"].append("Aggies.com")
full_resources["College"].append("All")
full_resources["Department"].append("All")
full_resources["Category"].append("Physical Health - Athletics")

#this link shows live how many people are in the gym and where
#would be really fun to scrape it over a couple months and figure out when people go to the gym
full_resources["Main Page"].append("https://www.usu.edu/current-students/")
full_resources["Link"].append("https://www.usu.edu/campusrec/")
full_resources["Resource Title"].append("Campus Recreation")
full_resources["College"].append("All")
full_resources["Department"].append("All")
full_resources["Category"].append("USU Living & Physical Health - Athletics")

full_resources["Main Page"].append("https://www.usu.edu/current-students/")
full_resources["Link"].append("https://www.usu.edu/campusrec/facilities/arc")
full_resources["Resource Title"].append("Aggie Recreation Center (ARC)")
full_resources["College"].append("All")
full_resources["Department"].append("All")
full_resources["Category"].append("USU Living & Physical Health")

full_resources["Main Page"].append("https://www.usu.edu/current-students/")
full_resources["Link"].append("https://www.usu.edu/campusrec/outdoor/")
full_resources["Resource Title"].append("Outdoor Programs")
full_resources["College"].append("All")
full_resources["Department"].append("All")
full_resources["Category"].append("USU Living & Physical Health")

full_resources["Main Page"].append("https://www.usu.edu/current-students/")
full_resources["Link"].append("https://usustatesman.com/")
full_resources["Resource Title"].append("The Utah Statesman")
full_resources["College"].append("All")
full_resources["Department"].append("All")
full_resources["Category"].append("USU Living")

full_resources["Main Page"].append("https://www.usu.edu/current-students/")
full_resources["Link"].append("https://radio.usu.edu/")
full_resources["Resource Title"].append("Aggie Radio")
full_resources["College"].append("All")
full_resources["Department"].append("All")
full_resources["Category"].append("USU Living")

#################   On-Campus Resources   ####################

full_resources["Main Page"].append("https://www.usu.edu/current-students/")
full_resources["Link"].append("https://library.usu.edu/")
full_resources["Resource Title"].append("USU Libraries")
full_resources["College"].append("All")
full_resources["Department"].append("All")
full_resources["Category"].append("On-Campus Resources & Academic Information")

full_resources["Main Page"].append("https://www.usu.edu/current-students/")
full_resources["Link"].append("https://www.usu.edu/drc/")
full_resources["Resource Title"].append("Disability Resource Center")
full_resources["College"].append("All")
full_resources["Department"].append("All")
full_resources["Category"].append("On-Campus Resources")

full_resources["Main Page"].append("https://www.usu.edu/current-students/")
full_resources["Link"].append("https://www.usu.edu/veterans/")
full_resources["Resource Title"].append("Veteran's Resource Office")
full_resources["College"].append("All")
full_resources["Department"].append("All")
full_resources["Category"].append("On-Campus Resources")

full_resources["Main Page"].append("https://www.usu.edu/current-students/")
full_resources["Link"].append("https://it.usu.edu/labs/computer-labs/")
full_resources["Resource Title"].append("Computer Labs")
full_resources["College"].append("All")
full_resources["Department"].append("All")
full_resources["Category"].append("On-Campus Resources")

full_resources["Main Page"].append("https://www.usu.edu/current-students/")
full_resources["Link"].append("https://www.usu.edu/writing/")
full_resources["Resource Title"].append("Utah State Writing Center")
full_resources["College"].append("All")
full_resources["Department"].append("All")
full_resources["Category"].append("On-Campus Resources & Academic Information")

full_resources["Main Page"].append("https://www.usu.edu/current-students/")
full_resources["Link"].append("https://www.usucampusstore.com/")
full_resources["Resource Title"].append("Campus Store")
full_resources["College"].append("All")
full_resources["Department"].append("All")
full_resources["Category"].append("On-Campus Resources")

#############     Career Prep Resources      ###############

full_resources["Main Page"].append("https://www.usu.edu/career-design-center/")
full_resources["Link"].append("https://www.usu.edu/career-design-center/")
full_resources["Resource Title"].append("Career Design Center")
full_resources["College"].append("All")
full_resources["Department"].append("All")
full_resources["Category"].append("Career Prep Resources")

full_resources["Main Page"].append("https://www.usu.edu/career-design-center/")
full_resources["Link"].append("https://www.usu.edu/career-design-center/students/drop-ins")
full_resources["Resource Title"].append("Career Design Center - Drop-ins")
full_resources["College"].append("All")
full_resources["Department"].append("All")
full_resources["Category"].append("Career Prep Resources")

full_resources["Main Page"].append("https://www.usu.edu/career-design-center/students/resources-by-college/index")
full_resources["Link"].append("https://www.usu.edu/career-design-center/students/resources-by-college/index")
full_resources["Resource Title"].append("Career Resources by College")
full_resources["College"].append("All")
full_resources["Department"].append("All")
full_resources["Category"].append("Career Prep Resources")

full_resources["Main Page"].append("https://www.usu.edu/career-design-center/students/resources-by-college/index")
full_resources["Link"].append("https://www.usu.edu/career-design-center/students/resources-by-college/cca/index")
full_resources["Resource Title"].append("Arts Career Education")
full_resources["College"].append("Caine College of the Arts")
full_resources["Department"].append("All")
full_resources["Category"].append("Career Prep Resources")

full_resources["Main Page"].append("https://www.usu.edu/career-design-center/students/resources-by-college/index")
full_resources["Link"].append("https://www.usu.edu/career-design-center/students/resources-by-college/caas/index")
full_resources["Resource Title"].append("Agriculture & Applied Sciences Career Education")
full_resources["College"].append("College of Agriculture and Applied Sciences")
full_resources["Department"].append("All")
full_resources["Category"].append("Career Prep Resources")

full_resources["Main Page"].append("https://www.usu.edu/career-design-center/students/resources-by-college/index")
full_resources["Link"].append("https://huntsman.usu.edu/start/")
full_resources["Resource Title"].append("Huntsman Career Education")
full_resources["College"].append("Huntsman School of Business")
full_resources["Department"].append("All")
full_resources["Category"].append("Career Prep Resources")

full_resources["Main Page"].append("https://www.usu.edu/career-design-center/students/resources-by-college/index")
full_resources["Link"].append("https://www.usu.edu/career-design-center/students/resources-by-college/cehs/index")
full_resources["Resource Title"].append("Education and Human Services Career Education")
full_resources["College"].append("College of Education and Human Services")
full_resources["Department"].append("All")
full_resources["Category"].append("Career Prep Resources")

full_resources["Main Page"].append("https://www.usu.edu/career-design-center/students/resources-by-college/index")
full_resources["Link"].append("https://www.usu.edu/career-design-center/students/resources-by-college/engineering/index")
full_resources["Resource Title"].append("Engineering Career Education")
full_resources["College"].append("College of Engineering")
full_resources["Department"].append("All")
full_resources["Category"].append("Career Prep Resources")

full_resources["Main Page"].append("https://www.usu.edu/career-design-center/students/resources-by-college/index")
full_resources["Link"].append("https://www.usu.edu/career-design-center/students/resources-by-college/exploratory/index")
full_resources["Resource Title"].append("Exploratory Career Education")
full_resources["College"].append("Undeclared")
full_resources["Department"].append("All")
full_resources["Category"].append("Career Prep Resources")

full_resources["Main Page"].append("https://www.usu.edu/career-design-center/students/resources-by-college/index")
full_resources["Link"].append("https://www.usu.edu/career-design-center/students/resources-by-college/chass/index")
full_resources["Resource Title"].append("Humanities & Social Sciences Career Education")
full_resources["College"].append("College of Humanities and Social Sciences")
full_resources["Department"].append("All")
full_resources["Category"].append("Career Prep Resources")

full_resources["Main Page"].append("https://www.usu.edu/career-design-center/students/resources-by-college/index")
full_resources["Link"].append("https://www.usu.edu/career-design-center/students/resources-by-college/natural-resources/index")
full_resources["Resource Title"].append("Natural Resources Career Education")
full_resources["College"].append("College of Natural Resources")
full_resources["Department"].append("All")
full_resources["Category"].append("Career Prep Resources")

full_resources["Main Page"].append("https://www.usu.edu/career-design-center/students/resources-by-college/index")
full_resources["Link"].append("https://www.usu.edu/career-design-center/students/resources-by-college/science/index")
full_resources["Resource Title"].append("Science Career Education")
full_resources["College"].append("College of Science")
full_resources["Department"].append("All")
full_resources["Category"].append("Career Prep Resources")

#################    Housing Resources    ####################

full_resources["Main Page"].append("https://www.usu.edu/housing/index")
full_resources["Link"].append("https://www.usu.edu/housing/single/")
full_resources["Resource Title"].append("Single Housing")
full_resources["College"].append("All")
full_resources["Department"].append("All")
full_resources["Category"].append("USU Living - Housing Resources")

full_resources["Main Page"].append("https://www.usu.edu/housing/index")
full_resources["Link"].append("https://www.usu.edu/housing/other/")
full_resources["Resource Title"].append("Other Housing Resources")
full_resources["College"].append("All")
full_resources["Department"].append("All")
full_resources["Category"].append("USU Living - Housing Resources")

full_resources["Main Page"].append("https://www.usu.edu/housing/index")
full_resources["Link"].append("https://www.usu.edu/campus-life/living/")
full_resources["Resource Title"].append("Living on Campus")
full_resources["College"].append("All")
full_resources["Department"].append("All")
full_resources["Category"].append("USU Living - Housing Resources")

full_resources["Main Page"].append("https://www.usu.edu/housing/index")
full_resources["Link"].append("https://www.usu.edu/housing/family/")
full_resources["Resource Title"].append("Family Housing")
full_resources["College"].append("All")
full_resources["Department"].append("All")
full_resources["Category"].append("USU Living - Housing Resources")

##################    Food Resources      #############


#Career Prep Resources ----- Done for now, could probably find some more resources though
#finding housing Resources
#
#make sure that the USU clinic is here and clear
def unique(list1):
    # insert the list to the set
    list_set = set(list1)
    # convert the set to the list
    unique_list = (list(list_set))
    u_list = []
    for x in unique_list:
        u_list.append(x)
    return u_list

college_vals = unique(full_resources['College'])
sorted_college_vals = sorted(college_vals)
department_vals = unique(full_resources['Department'])
sorted_department_vals = sorted(department_vals)
resource_vals = unique(full_resources['Category'])
sorted_resource_vals = sorted(resource_vals)
title_vals = unique(full_resources['Resource Title'])
        
# print("Colleges: ", "\n", sorted_college_vals)
# print("Departments: ", "\n", sorted_department_vals)
# print("Resource Categories: ", "\n", sorted_resource_vals)

college_list = full_resources['College']
department_list = full_resources['Department']
resource_list = full_resources['Category']
link_list = full_resources['Link']
title_list = full_resources['Resource Title']

# i = 0
# for c in college_list:
#     if c == 'Huntsman School of Business':
#         if 'Academic' in resource_list[i]:
#             print("College:", college_list[i], '\n', "Department:", department_list[i], '\n', "Resource Type:", resource_list[i], "Resource Link:", link_list[i], '\n')
#     elif c == 'All' and 'Academic' in resource_list[i]:
#         print("resource:", resource_list[i], "Link:", link_list[i])
#     i += 1

def search (college, department, resources):
    print_list = []
    i = 0
    for r in title_list:
        if resources in resource_list[i]:
            if department_list[i] == department: 
                st = "College: " + college_list[i] + ', ' + "Department: " + department_list[i] + ', ' + "Resource Title: " + title_list[i] + ', ' + "Resource Type: " + resource_list[i] + ', ' + "Resource Link: " + link_list[i]
                print_list.append(st)
            if college_list[i] == college:
                st = "College: " + college_list[i] + ', ' + "Department: " + department_list[i] + ', ' + "Resource Title: " + title_list[i] + ', ' + "Resource Type: " + resource_list[i] + ', ' + "Resource Link: " + link_list[i]
                print_list.append(st)
            if college_list[i] == 'All':
                st = "College: " + college_list[i] + ', ' + "Department: " + department_list[i] + ', ' + "Resource Title: " + title_list[i] + ', ' + "Resource Type: " + resource_list[i] + ', ' + "Resource Link: " + link_list[i]
                print_list.append(st)
        i += 1
    with open(r'/home/ubuntu/environment/huntsman_scholar_final_proj/results.txt', 'w') as fp:
        for p in print_list:
            # write each item on a new line
            fp.write("%s\n" % p)
        print('Done')

    return print_list

print(search('Caine College of the Arts', 'Art', 'Physical'))

    
# college = 'Q5'
# department = 'Q4'
# resources = 'Q6'