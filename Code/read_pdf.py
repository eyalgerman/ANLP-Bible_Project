from PyPDF2 import PdfReader
import re
import openpyxl
import pandas as pd

def read_pdf(file_path):
    reader = PdfReader(file_path)

    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "Data with Numbers"
    
    # Write the headers to the first row
    sheet.append(["מספר שאלה", "שאלה"])

    pattern = re.compile(r'^(\d+)\s+(.*)')
    pattern2 = re.compile(r'\d')

    count = 0
    with open("read_pdf.txt", 'w') as output_file:
        for page in reader.pages:
            if count < 9:
                page_text = page.extract_text()
                #pattern = re.compile(r'\d')
                for line in page_text.split('\n'):
                    line = line.replace('[', '').replace(']', '').replace(".", '').replace('"', '').replace(';', '').replace('?', "").replace("'", '');

                    match = pattern.match(line)
                    if match:
                        num_row = match.group(1)
                        data = match.group(2)
                        sheet.append([num_row, data])

                    if pattern2.search(line):
                        output_file.write(line.replace('[', '').replace(']', '') + '\n')
                            #print(line.replace('[', '').replace(']', ''))

            count = count + 1
    workbook.save("read_pdf.xlsx")

pdf_text = read_pdf('questions_database.pdf')
print(pdf_text)

# Step 1: Read Excel files into DataFrames
read_pdf_df = pd.read_excel('read_pdf.xlsx', engine='openpyxl')
questions_df = pd.read_excel('questions.xlsx', engine='openpyxl')
print(questions_df)

# Step 2: Merge DataFrames on the common column "מספר שאלה" and "שאלה"
merged_df = pd.merge(questions_df, read_pdf_df, left_on='שאלה', right_on='מספר שאלה', how='left')

# Step 3: Replace the "שאלה" column in questions_df with the corresponding questions
questions_df['שאלה'] = merged_df['שאלה_y']

# Step 4: Save the updated DataFrame to a new Excel file
questions_df.to_excel('updated_questions.xlsx', index=False, engine='openpyxl')

print("Updated questions.xlsx with questions from read_pdf.xlsx successfully.")