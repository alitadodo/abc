def remove_dollar_sign(s):
    remove = s.replace("$","")
    return remove
text ="You can 1 $"
print(remove_dollar_sign(text))


string_with_no_dollars = remove_dollar_sign("$80% percent of $life is to show $up")
if string_with_no_dollars == "80% percent of life is to show up":
    print("Your function is correct")
else:
    print("Oops, there's a bug")