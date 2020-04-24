import re
import pyperclip

# Create a regex for phone numbers
phoneRegex = re.compile(r'''
(
((\d\d\d) | (\(\d\d\d))?	# area code
(\s|-)						# first separator
\d\d\d						# first 3 digits
-							# separator
\d\d\d\d					# last 4 digits
((ext(\.)?\s|x) 			# extension optional - word part
(\d{2,5}))?					# extension optional - number part
)
''', re.VERBOSE)

# Create a regex for the email
emailRegex = re.compile(r'''

[a-zA-Z0-9_.+]+				# name part
@							#@ symbol				
[a-zA-Z0-9_.+]+				# domain part
''', re.VERBOSE)

# Get the text off the clipboard
text = pyperclip.paste()

# Extrat email and phone
extractPhone = phoneRegex.findall(text)
extractEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phone in extractPhone:
	allPhoneNumbers.append(phone[0])

#print(allPhoneNumbers)
#print(extractEmail)

results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractEmail)

print(results)