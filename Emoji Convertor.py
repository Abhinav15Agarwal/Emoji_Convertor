#Simple use of a dictionary

msg = input("> ").split(' ')
emoji = {
    ":)" : "😊",
    ":(" : "😌"
}
# Can add more emojis as you please
for words in msg:
    print(emoji.get(words, words), end= " ") # check for every word in msg, if emoji is found then convert using dictionary otherwise
                                             # return the same word

