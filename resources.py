full_resources = {"Main Page": [], "Link": [], "Resource Title": [], "College": [], "Department": [], "Category": []}

#######################     Academic Resources      #######################

arts_departments = ['Art', 'Music', 'Theature']
i = 0
for d in arts_departments:
    full_resources["Main Page"].append("https://www.usu.edu/academics/colleges/")
    full_resources["Link"].append("https://cca.usu.edu/"+arts_departments[i]+"/")
    full_resources["College"].append("Caine College of the Arts")
    full_resources["Department"].append(arts_departments[i])
    full_resources["Category"].append("Department Information")
    i += 1

full_resources["Main Page"].append("https://www.usu.edu/academics/colleges/")
full_resources["Link"].append("https://cca.usu.edu/")
full_resources["College"].append("Caine College of the Arts")
full_resources["Department"].append("All")
full_resources["Category"].append("College Information")

#this could be mined further
full_resources["Main Page"].append("https://www.usu.edu/academics/colleges/")
full_resources["Link"].append("https://www.usu.edu/degrees/index.cfm?browse&c=8&l=undergraduate")
full_resources["College"].append("Caine College of the Arts")
full_resources["Department"].append("All")
full_resources["Category"].append("Academic Information")


ag_departments = ['advs', 'apec', 'avte', 'laep', 'ndfs', 'psc']
i = 0
for d in ag_departments:
    full_resources["Main Page"].append("https://www.usu.edu/academics/colleges/")
    full_resources["Link"].append("https://caas.usu.edu/"+ag_departments[i]+"/")
    full_resources["College"].append("College of Agriculture and Applied Sciences")
    full_resources["Department"].append(ag_departments[i])
    full_resources["Category"].append("Department Information")
    i += 1
    
full_resources["Main Page"].append("https://www.usu.edu/academics/colleges/")
full_resources["Link"].append("https://aste.usu.edu/")
full_resources["College"].append("Applied Sciences, Technology & Education")
full_resources["Department"].append("All")
full_resources["Category"].append("College Information")

full_resources["Main Page"].append("https://www.usu.edu/academics/colleges/")
full_resources["Link"].append("https://caas.usu.edu/advs/")
full_resources["College"].append("College of Agriculture and Applied Sciences")
full_resources["Department"].append("Animal, Dairy and Veterinary Sciences")
full_resources["Category"].append("College Information")

full_resources["Main Page"].append("https://www.usu.edu/academics/colleges/")
full_resources["Link"].append("https://vetmed.usu.edu/")
full_resources["College"].append("College of Veterinary Medicine")
full_resources["Department"].append("All")
full_resources["Category"].append("College Information")

full_resources["Main Page"].append("https://www.usu.edu/academics/colleges/")
full_resources["Link"].append("https://caas.usu.edu/")
full_resources["College"].append("College of Agriculture and Applied Sciences")
full_resources["Department"].append("All")
full_resources["Category"].append("College Information")

full_resources["Main Page"].append("https://www.usu.edu/academics/colleges/")
full_resources["Link"].append("https://www.usu.edu/degrees/index.cfm?browse&c=1&l=undergraduate")
full_resources["College"].append("College of Agriculture and Applied Sciences")
full_resources["Department"].append("All")
full_resources["Category"].append("Academic Information")

eng_departments = ['be/', 'cee', 'ece', 'eed', 'mae']
i = 0
for d in eng_departments:
    full_resources["Main Page"].append("https://www.usu.edu/academics/colleges/")
    full_resources["Link"].append("https://engineering.usu.edu/"+eng_departments[i]+"/")
    full_resources["College"].append("College of Agriculture and Applied Sciences")
    full_resources["Department"].append(eng_departments[i])
    full_resources["Category"].append("Department Information")
    i += 1

full_resources["Main Page"].append("https://www.usu.edu/academics/colleges/")
full_resources["Link"].append("https://engineering.usu.edu/")
full_resources["College"].append("College of Engineering")
full_resources["Department"].append("All")
full_resources["Category"].append("College Information")

full_resources["Main Page"].append("https://www.usu.edu/academics/colleges/")
full_resources["Link"].append("https://www.usu.edu/degrees/index.cfm?browse&c=4&l=undergraduate")
full_resources["College"].append("College of Engineering")
full_resources["Department"].append("All")
full_resources["Category"].append("Academic Information")

hum_departments = ['aerospace', 'cai', 'csph-department', 'history', 'english', 'journalism', 'military-science', 'political-science', 'social-work', 'soca-department', 'languages']
hum_departments_full = ['Air Force ROTC', 'CAI', 'Communications Studies & Philosophy', 'History', 'English', 'Journalism', 'Military Science', 'Political Science', 'Social Work','Sociology and Anthropology', 'World Languages and Cultures' ]
i = 0
for d in hum_departments:
    full_resources["Main Page"].append("https://www.usu.edu/academics/colleges/")
    full_resources["Link"].append("https://usu.edu/"+hum_departments[i]+"/")
    full_resources["College"].append("College of Agriculture and Applied Sciences")
    full_resources["Department"].append(hum_departments_full[i])
    full_resources["Category"].append("Department Information")
    i += 1
    
full_resources["Main Page"].append("https://www.usu.edu/academics/colleges/")
full_resources["Link"].append("https://chass.usu.edu/")
full_resources["College"].append("College of Humanities and Social Science")
full_resources["Department"].append("All")
full_resources["Category"].append("College Information")

full_resources["Main Page"].append("https://www.usu.edu/academics/colleges/")
full_resources["Link"].append("https://www.usu.edu/degrees/index.cfm?browse&c=5&l=undergraduate")
full_resources["College"].append("College of Humanities and Social Science")
full_resources["Department"].append("All")
full_resources["Category"].append("Academic Information")

#working on teh College of Science
sc_departments = ['biology', 'chem', 'cs', 'geo', 'math', 'physics']
i = 0
for d in sc_departments:
    full_resources["Main Page"].append("https://www.usu.edu/academics/colleges/")
    full_resources["Link"].append("https://usu.edu/"+sc_departments[i]+"/")
    full_resources["College"].append("College of Agriculture and Applied Sciences")
    full_resources["Department"].append(sc_departments[i])
    full_resources["Category"].append("Department Information")
    i += 1

full_resources["Main Page"].append("https://www.usu.edu/academics/colleges/")
full_resources["Link"].append("https://www.usu.edu/science/")
full_resources["College"].append("College of Science")
full_resources["Department"].append("All")
full_resources["Category"].append("College Information")

full_resources["Main Page"].append("https://www.usu.edu/academics/colleges/")
full_resources["Link"].append("https://www.usu.edu/degrees/index.cfm?browse&c=6&l=undergraduate")
full_resources["College"].append("College of Science")
full_resources["Department"].append("All")
full_resources["Category"].append("Academic Information")

full_resources["Main Page"].append("https://www.usu.edu/academics/colleges/")
full_resources["Link"].append("https://vetmed.usu.edu/")
full_resources["College"].append("College of Veterinary Medicine")
full_resources["Department"].append("All")
full_resources["Category"].append("College Information")

full_resources["Main Page"].append("https://www.usu.edu/academics/colleges/")
full_resources["Link"].append("https://www.usu.edu/degrees/index.cfm?browse&c=27&l=undergraduate")
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
    full_resources["College"].append("College of Agriculture and Applied Sciences")
    full_resources["Department"].append(ed_departments_full[i])
    full_resources["Category"].append("Department Information")
    i += 1
    
full_resources["Main Page"].append("https://www.usu.edu/academics/colleges/")
full_resources["Link"].append("https://comdde.usu.edu/")
full_resources["College"].append("College of Agriculture and Applied Sciences")
full_resources["Department"].append("Communicative Disorders and Deaf Education")
full_resources["Category"].append("Department Information")    

full_resources["Main Page"].append("https://www.usu.edu/academics/colleges/")
full_resources["Link"].append("https://nursing.usu.edu/")
full_resources["College"].append("College of Agriculture and Applied Sciences")
full_resources["Department"].append("Nursing")
full_resources["Category"].append("Department Information") 

full_resources["Main Page"].append("https://www.usu.edu/academics/colleges/")
full_resources["Link"].append("https://cehs.usu.edu/")
full_resources["College"].append("College of Education and Human Services")
full_resources["Department"].append("All")
full_resources["Category"].append("College Information")

full_resources["Main Page"].append("https://www.usu.edu/academics/colleges/")
full_resources["Link"].append("https://www.usu.edu/degrees/index.cfm?browse&c=3&l=undergraduate")
full_resources["College"].append("College of Education and Human Services")
full_resources["Department"].append("All")
full_resources["Category"].append("Academic Information")

bus_departments = ['dais', 'economicsandfinance', 'management', 'marketingandstrategy', 'acct']
bus_departments_full = ['Data Analytics & Information Systems', 'Economics and Finance', 'Management', 'Marketing and Strategy', 'Accounting']
i = 0
for d in bus_departments:
    full_resources["Main Page"].append("https://www.usu.edu/academics/colleges/")
    full_resources["Link"].append("https://huntsman.usu.edu/"+bus_departments[i]+"/")
    full_resources["College"].append("College of Agriculture and Applied Sciences")
    full_resources["Department"].append(bus_departments_full[i])
    full_resources["Category"].append("Department Information")
    i += 1
    
full_resources["Main Page"].append("https://www.usu.edu/academics/colleges/")
full_resources["Link"].append("https://huntsman.usu.edu/")
full_resources["College"].append("Huntsman School of Business")
full_resources["Department"].append("All")
full_resources["Category"].append("College Information")

full_resources["Main Page"].append("https://www.usu.edu/academics/colleges/")
full_resources["Link"].append("https://www.usu.edu/degrees/index.cfm?browse&c=2&l=undergraduate")
full_resources["College"].append("Huntsman School of Business")
full_resources["Department"].append("All")
full_resources["Category"].append("Academic Information")    

nat_departments = ['envs', 'wats', 'wild']
nat_departments_full = ['Environment and Society', 'Watershed Sciences', 'Wildland Resources']
i = 0
for d in nat_departments:
    full_resources["Main Page"].append("https://www.usu.edu/academics/colleges/")
    full_resources["Link"].append("https://huntsman.usu.edu/"+nat_departments[i]+"/")
    full_resources["College"].append("College of Agriculture and Applied Sciences")
    full_resources["Department"].append(nat_departments_full[i])
    full_resources["Category"].append("Department Information")
    i += 1
    
full_resources["Main Page"].append("https://www.usu.edu/academics/colleges/")
full_resources["Link"].append("https://qcnr.usu.edu/")
full_resources["College"].append("College of Natural Resources")
full_resources["Department"].append("All")
full_resources["Category"].append("College Information")

full_resources["Main Page"].append("https://www.usu.edu/academics/colleges/")
full_resources["Link"].append("https://www.usu.edu/degrees/index.cfm?browse&c=7&l=undergraduate")
full_resources["College"].append("College of Natural Resources")
full_resources["Department"].append("All")
full_resources["Category"].append("Academic Information") 

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
full_resources["Category"].append("General Health") 

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
full_resources["Category"].append("Relationship Health")

#this would be a good resource if you needed help for a friend
full_resources["Main Page"].append("https://usu.edu/aggiewellness/")
full_resources["Link"].append("https://www.usu.edu/aggiewellness/help-others")
full_resources["Resource Title"].append("Help Others in Distress")
full_resources["College"].append("All")
full_resources["Department"].append("All")
full_resources["Category"].append("Health of Others")

full_resources["Main Page"].append("https://usu.edu/aggiewellness/")
full_resources["Link"].append("https://www.usu.edu/aggiewellness/tools")
full_resources["Resource Title"].append("Access Preventative and Educational Tools")
full_resources["College"].append("All")
full_resources["Department"].append("All")
full_resources["Category"].append("All Health")

full_resources["Main Page"].append("https://usu.edu/aggiewellness/")
full_resources["Link"].append("https://www.usu.edu/aggiewellness/tools")
full_resources["Resource Title"].append("Improve Your Mental Well-Being")
full_resources["College"].append("All")
full_resources["Department"].append("All")
full_resources["Category"].append("All Health")

####################      Safety Resources      ##########################

print(full_resources)