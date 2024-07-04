# sample_code_sets/data_generator/data_generator.py

from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            'account_number': fake.unique.random_int(min=1000000000, max=9999999999),
            'account_name': fake.name(),
            'mobile_number': fake.phone_number(),
            'total_revenue': fake.random_int(min=1000, max=5000),
            'product_usage': fake.random_int(min=10, max=100),
            'most_used_product': fake.random_int(min=1, max=5),
            'second_most_used_product': fake.random_int(min=1, max=5),
            'third_most_used_product': fake.random_int(min=1, max=5),
        }
        data.append(record)
    return data
