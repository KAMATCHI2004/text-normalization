import re
from num2words import num2words
abbreviations = {
    "Dr.": "Doctor",
    "Mr.": "Mister",
    "Mrs.": "Mistress",
    "Ms.": "Miss",
    "St.": "Street",
    "Ave.": "Avenue",
    "Rd.": "Road",
    "Inc.": "Incorporated",
    "Ltd.": "Limited",
    "Co.": "Company",
    "Corp.": "Corporation",
    "etc.": "et cetera",
    "i.e.": "that is",
    "e.g.": "for example",
    "Jr.": "Junior",
    "Sr.": "Senior",
    "No.": "Number",
    "Dept.": "Department",
    "vs.": "versus",
    "Univ.": "University",
    "Gov.": "Governor",
    "Pres.": "President",
    "Prof.": "Professor"
}
def convert_numbers(text):
    return re.sub(r'\b\d+\b', lambda x: num2words(int(x.group(0))), text)
def replace_abbreviations(text):
    for abbrev, full_form in abbreviations.items():
        text = re.sub(r'\b' + re.escape(abbrev) + r'\b', full_form, text)
        text = re.sub(r'\b' + re.escape(abbrev[:-1]) + r'\b', full_form, text)
    return text
def normalize_text(text):
    text = replace_abbreviations(text)
    text = convert_numbers(text)
    text = re.sub(r'[^\w\s]', '', text)
    return text
while True:
    input_text = input("Enter text to normalize: ")
    normalized_text = normalize_text(input_text)
    print("\nNormalized Text:")
    print(normalized_text)
    print("\nKindly enter the next phrase.\n")
