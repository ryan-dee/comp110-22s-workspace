"""Demonstrations of dictionary capabilites."""

# Declaring type of dictionary
schools: dict[str, int]

# Initialize to an empty dictionary
schools = dict()

# Set a key-vaule pairing in the dictionary
schools["UNC"] = 16400
schools["Duke"] = 6717
schools["NCSU"] = 26150

print(schools)

print(f"UNC has {schools['UNC']} students")

# Remove a value from the dictionary
# By its key
schools.pop("Duke")

# test for existence of key
is_duke_present: bool = "Duke" in schools
print(f"duke is present: {is_duke_present}")

for school in schools:
    print(f"Key: {school} -> Value: {schools[school]}")

