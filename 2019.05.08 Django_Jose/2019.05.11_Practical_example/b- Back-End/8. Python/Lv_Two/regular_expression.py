import re

patterns = ['term1','term2']

text = 'This is a string contains term1, not the other'

# match = re.search(patterns[0],text)
#
# print(type(match))
#
#  print(match.start())
#
## Split()
#
# email ='truonghoangftu2@gmail.com'
# re.split('@',email)
# print(re.split('@',email))


        ##findall()
#
# patterns = ['term1','term2']
#
# text = 'This is a string contains term1, not the other'
#
# print(re.findall(patterns[0],text))

        ## Asterid * and finall(search_term,text)

def multi_re_find(patterns,phrase):
   for pattern in patterns: #Never forget that if str can be iteratable, each cha is an item
       print("I'am searching for "+ pattern)
       print(re.findall(pattern,phrase))
       print('\n')
text= 'asdasd  asd asd  asdd weqwe .as.d ..asddddd ... asd asdddd sdasdddd .dawd'

term=['sd{1,4}']
     #regular expression get the
         # d* as zero or more d
         # d+ as one or more d
         # d? as zero or one d
         # d{number} mean {number} of d
         # d(number, another_number) mean {number} of d or {another_number} of d
         # [] mean any_of_the_inside_characters
         # Ex: [sd] mean s or d. Ex [sd] mean zero or more s,d: sdddsssddss not dsssddss

# multi_re_find(term,text)

        ## exclusion

text1="This is an string!. but this have punctuation. How can we remove ?"

pattern=['[^!?. ]+']
        #^ mean to exclude. This can be consider as a miltipel character
        # spliting
multi_re_find(pattern,text1)

lowercase = ['[a-z]+']
        #[a-z] mean any cha from a to z (lowercase)
        #[A-Z] is for uppercase


            #for special:

special=[r'\d]
        #d mean digits
        #D mean non-digits
        #s mean whitespace
        #S mean none-whitespace
        #w mean all the alphanumeric
        #W mean non-alphanumeric
