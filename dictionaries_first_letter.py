# Write your count_first_letter function here:
def count_first_letter(names):
  dictionary = {}
  for key in names.keys():
    if key[0] in dictionary:
      dictionary.update({key[0]:dictionary[key[0]]+len(names[key])})
    else:
      dictionary.update({key[0]:+len(names[key])})
  return dictionary
# Uncomment these function calls to test your  function:
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 4, "L": 3}
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Sannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 7}