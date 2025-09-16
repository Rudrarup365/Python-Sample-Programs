from faker import Faker
import pandas as pd
from datetime import datetime as dt

fake = Faker('en_US') # You can specify a locale, e.g., 'en_US'
def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'email': fake.email(),
            'address': fake.address(),
            'job_title': fake.job(),
            'company': fake.company(),
            'phone_number': fake.phone_number(),
            'date_of_birth': fake.date_of_birth(minimum_age=18, maximum_age=65),
            'random_id': fake.uuid4()
            }
        data.append(record)
    return data

num_records = 100
fake_data_list = generate_fake_data(num_records)
df = pd.DataFrame(fake_data_list)
df['Full Name']=df['first_name'] + " " + df['last_name']
df['Monthnum']=pd.to_datetime(df['date_of_birth']).dt.month
df['Month']=pd.to_datetime(df['date_of_birth']).dt.month_name()
df['Day']=pd.to_datetime(df['date_of_birth']).dt.day
df_sorted = df.sort_values(by=['Monthnum','Day'])
df_sorted=df_sorted.drop(columns=['Monthnum', 'Month','Day']).to_string()
print(df_sorted)