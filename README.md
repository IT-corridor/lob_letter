## Description

A python 3 script for lob (https://github.com/lob/lob-python) that can invoke the Lob Letters API. 
The main idea is that I want to create a spreadsheet file(CSV) with names and addresses (one row per letter), then have Lob mail letters to those names. 

The script would accept 2 parameters on the command line (unless you think of more that we need).

1. Lob API key.  This could be a test or production key.
2. filename of a .csv file containing the following columns:
   filename of an html template file (e.g., my_template.html)
   double_sided  (boolean: true or false)
   color  (boolean: true or false)
   to_name
   to_company
   to_address_line1
   to_address_line2
   to_address_city
   to_address_state
   to_address_zip
   from_name
   from_company
   from_address_line1
   from_address_line2
   from_address_city
   from_address_state
   from_address_zip

Note: the csv file will contain many (e.g. up to 200 different rows, one for each letter).

Some fields in the CSV file (from_*, html filename, double_sided) will probably have the same values for each letter, but it could be nice to have the option to change those per letter in the future.

The html template file (e.g., my_template.html) would be a valid lob html file. I will design the html file separately. But for now you can use the example here: https://lob.com/docs#letter-example

include a header row in the CSV file. That would be useful so I can just export an entire spreadsheet.

Note that this script will implement a particular document type, and we therefore only use a portion of the available API calls. This will not be a generalized solution or full interface to the API. This will be a specific implementation of one use-case.

## Result

It prints thumbnail link for successful letter creation and write error code and 
message in errors.log file in the same path.

If you want to see the whole letter, remove comment on #58.

## To Run  

python3 lob_letter.py <token> <csv_file>
e.g) python3 lob_letter.py test_a2dbfad509e28fa2219859384227ceba202 e_sheet1.csv

