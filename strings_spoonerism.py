# Write your make_spoonerism function here:
def make_spoonerism(word1, word2):
  if len(word1) !=0 and len(word2) != 0:
    letter1 = word1[0]
    letter2 = word2[0]
    word1_changed = letter2 + word1[1:]
    word2_changed = letter1 + word2[1:]
    return word1_changed + ' ' + word2_changed
  else:
    return "Missing words"
# Uncomment these function calls to test your function:
print(make_spoonerism("Codecademy", "Learn"))
# should print Lodecademy Cearn
print(make_spoonerism("Hello", "world!"))
# should print wello Horld!
print(make_spoonerism("a", "b"))
# should print b a
print(make_spoonerism("", ""))