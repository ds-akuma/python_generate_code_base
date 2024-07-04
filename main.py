# sample_code_sets/main.py

from data_generator.data_generator import generate_fake_data
from algorithms.proprietary_algo import calculate_total_revenue

def main():
    # Specify the number of records to generate
    num_records = 10
    
    # Generate sample data
    data = generate_fake_data(num_records)
    
    # Calculate total revenue for each record
    for record in data:
        record['calculated_total_revenue'] = calculate_total_revenue(record)
    
    # Print the generated data
    for record in data:
        print(record)

if __name__ == "__main__":
    main()
