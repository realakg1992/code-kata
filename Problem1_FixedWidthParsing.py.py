#!/usr/bin/env python
# coding: utf-8

# In[2]:


import csv

# Function to parse the spec file and return the column names and offsets
def parse_spec_file(spec_file):
    fields = []
    with open(spec_file, 'r', encoding='utf-8') as f:
        for line in f:
            parts = line.strip().split()
            field_name = parts[0]
            field_length = int(parts[1])
            fields.append((field_name, field_length))
    return fields

# Function to parse the fixed-width file using the offsets
def parse_fixed_width_file(input_file, fields):
    rows = []
    
    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.rstrip('\n')  # Strip the newline character at the end
            total_length = sum(length for _, length in fields)
            
            if len(line) < total_length:
                line = line.ljust(total_length)  # Pad the line with spaces
            
            start = 0
            row = []
            for field_name, length in fields:
                field_value = line[start:start + length]
                print(f"Extracting field {field_name}: '{field_value}' with length {length}")  
                row.append(field_value.strip()) 
                start += length
            rows.append(row)
    
    return rows

# Function to write the parsed data into a CSV file
def write_csv(output_file, fields, data):
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        # Write headers (field names)
        headers = [field_name for field_name, _ in fields]
        writer.writerow(headers)
        
        # Write the data 
        writer.writerows(data)

# Main function to execute the pipeline
def main():
    spec_file = 'spec.txt'  # Path to the spec file
    input_file = 'input.fwf'  # Path to the fixed-width input file
    output_file = 'output.csv'  # Path to the CSV output file
    
    fields = parse_spec_file(spec_file)
    data = parse_fixed_width_file(input_file, fields)
    write_csv(output_file, fields, data)

if __name__ == '__main__':
    main()


# In[ ]:




