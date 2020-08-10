import re

phone_pattern = re.compile(r"(\d{3})-(\d{3})-(\d{4})")

results = re.search(phone_pattern, "408-555-7777")

results.group()

# regex starts with 1
print(results[1])

# using regex to find -s
long_str = "this is a long-string to test the regex-off new things in the longish-hypen string"
pattern = re.compile(r'[\w]+-[\w]+')
print(re.findall(pattern, long_str))
