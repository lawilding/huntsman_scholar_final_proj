import pandas as pd
import numpy

data = pd.read_csv('/home/ubuntu/environment/huntsman_scholar_final_proj/Results/Resource Needs Survey.csv')
data = data.drop(columns = ['RecipientLastName', 'RecipientFirstName', 'RecipientEmail','ResponseID', 'ResponseSet', 'IPAddress', 'StartDate', 'EndDate','LocationLatitude',
       'LocationLongitude', 'LocationAccuracy','ExternalDataReference', 'Finished', 'Status'])
data.drop([0,1], axis=0, inplace=True)
print(data.columns)
print(data)

data.to_csv('/home/ubuntu/environment/huntsman_scholar_final_proj/Results/Resource_Needs_Edit.csv')