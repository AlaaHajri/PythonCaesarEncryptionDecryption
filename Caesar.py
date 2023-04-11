#########################################################################################
import openpyxl

# Load the workbook and select the sheet
wb = openpyxl.load_workbook("Caesar_mapping.xlsx")
sheet = wb.active

# Create an empty dictionary to hold the mapping
mapping = {}

# Iterate over the rows of the sheet and add the mapping to the dictionary
for row in sheet.iter_rows(min_row=2, values_only=True):
    letter, mapped_letter = row
    mapping[letter] = mapped_letter

print(mapping)
#########################################################################################

string = "xultpaajcxitltlxaarpjhtiwtgxktghidhipxciwtvgtpilpit ghlxiwiwtxgqadds"
result = ""

# Iterate through the string and replace each letter using the mapping
for letter in string:
    if letter in mapping:
        result += mapping[letter]
    else:
        result += letter


print(string,"with length:", len(string)) # Print the original msg if you wanna compare results 
print(result,"with length:", len(result)) # Print the result  
#########################################################################################
# Saving the results in an excel file:
import pandas as pd
import openpyxl

df = pd.DataFrame([[string, len(string)], [result, len(result)], ],
                  index=['Source', 'Destination', ], columns=[' ', 'Character Length'])

print(df)
#                                                                 Character Length
# Source       xultpaajcxitltlxaarpjhtiwtgxktghidhipxciwtvgtp...                68
# Destination  IFWEAaaUNITEWEWIaaCAUSETHERIVERSTOSTAINTHEGREA...                68

df.to_excel('Caesar_result.xlsx', sheet_name='new_sheet_name')