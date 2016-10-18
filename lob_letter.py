import csv
import lob
import os
import sys


# parameter validation
if len(sys.argv) < 3:
    print("Please provide a token and an input CSV file as an argument.")
    print("usage: python lob_letter.py <LOB_TOKEN> <CSV_FILE>")
    sys.exit(1)

# test_a2dbfad509e28fa2219859384227ceba202
lob.api_key = sys.argv[1]
input_filename = sys.argv[2]   
input_ = open(input_filename, 'r')

input_csv = csv.DictReader(input_)
# print(input_csv.fieldnames) 

errors_filename = 'errors.log'
errors = open(errors_filename, 'w')

err_count = 0

# Loop through input CSV rows
for idx, row in enumerate(input_csv):
    # Create letter from row
    try:
        html_file = open(row['html_filename'], 'r')
        letter_html = html_file.read()
        html_file.close()

        letter = lob.Letter.create(
            to_address={
                'name': row['to_name'],
                'company': row['to_company'],
                'address_line1': row['to_address_line1'],
                'address_line2': row['to_address_line2'],
                'address_city':  row['to_address_city'],
                'address_zip':   row['to_address_zip'],
                'address_state': row['to_address_state'],
            },
            from_address={
                'name': row['from_name'],
                'company': row['from_company'],
                'address_line1': row['from_address_line1'],
                'address_line2': row['from_address_line2'],
                'address_city':  row['from_address_city'],
                'address_zip':   row['from_address_zip'],
                'address_state': row['from_address_state'],
            },
            file=letter_html,
            double_sided=row['double_sided'].lower()=='true',
            color=row['color'].lower()=='true'
        )
        print(letter['thumbnails'][0]['medium'])
        # print(letter)
    except Exception as e:
        error_row = dict(row)
        error_row['error'] = str(e)
        errors.write(str(error_row))
        err_count += 1

print('')
print('Done with ' + (str(err_count) if err_count else 'no') + ' errors.')
