spam_amount = 0
print(spam_amount)

# Order Spam, egg, Spam, Spam, bacon and Spam (4 more servings of Spam)
spam_amount = spam_amount + 4

if spam_amount > 0:
    print("But I don't want ANY spam!")

viking_song = "Spam " * spam_amount
print (viking_song)

print("Hello World")

# Before I got this file to upload, I had to re-clone using SSH key
# So next I had to learn how to create an SSH key on my Mac
# After that, I installed the SSH key onto my GitHub
# Then, I got stuck for 15-20 minutes getting an "Git: host key verification failed" error
# I figured out I was getting this error because git@github.com was not added to SSH
# So I had to use ssh -T git@github.com in the terminal 
# Is this ok?

# Codeacademy
# I can't just put an equation 25 * 68 + 13 / 28, I need to print it.

print(25 * 68 + 13 / 28)

quilt_width = 8
quilt_length = 12

squares = quilt_width * quilt_length
print("Will need: " + str(squares) + " squares.")

quilt_length = 8
squares = quilt_width * quilt_length
print("Will need: " + str(squares) + " squares.")
beg_text = "Will need:"
end_text = "squares."
print(beg_text, squares, end_text)

team = []
for i in range(4):
    team.append([])
for person in range(1, 29):
    for i in range(4):
        if person % 4 == i:
            team[i].append(person)

for i in range(4):
    print("Team {} are persons {}".format(i, team[i]))   
