import xml.etree.ElementTree as et

# arrays to hold parts of the xml file
icdCode = []
icdName = []
# array to hold the full code and name
icdCombined = []

# gets xml file and turns it into a linked node list
root = et.parse('custom_models/mental_health/data/codes.xml').getroot()
# counter used for2nd for loop
count = 0

# searches for the tag record then gets the attribute for it
try:
    for skill in root.iter('record'):
        icdCode.append(skill.attrib['id'])

    # searches for the tag field and gets the text associated with it
    for field in root.iter('field'):
        icdName.append(field.text)
        tmp = [icdCode[count], icdName[count]]
        icdCombined.append(tmp)
        count = count + 1
except et.ParseError:
    print("failed")


#print(icdCombined)
