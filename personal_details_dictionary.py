def create_personal_details_dictionary():
  """
  Creates a dictionary of personal details for multiple people.

  Returns:
    A dictionary containing the personal details of each person.
  """

  people_details = {}
  num_people = int(input("Enter the number of people: "))

  for i in range(num_people):
    person_details = {}
    name = input("Enter name for person {}: ".format(i + 1))
    age = int(input("Enter age for person {}: ".format(i + 1)))
    occupation = input("Enter occupation for person {}: ".format(i + 1))

    person_details["Name"] = name
    person_details["Age"] = age
    person_details["Occupation"] = occupation

    people_details["Person {}".format(i + 1)] = person_details

  return people_details

# Create the dictionary of personal details
people_dict = create_personal_details_dictionary()

# Print the dictionary
print(people_dict)