# Mission Background
An expedition of an alien race called Binarians from planet Xenu, which is located in Vela constellation, has recently wound up in our Solar system. Their civilization is dedicated to establishing peace and justice throughout the universe. However, Binarians are not the most patient race in the universe: if they deem a species too violent, they simply annihilate it.  
Binarian spaceship dropped out of warp near Saturn earlier this year, and is expected to approach the Earth in a couple of days. In the meantime, they have studied the Earth and human race, and come to a conclusion that we are greedy savages who kill each other, wage absurd wars, and let many people starve and live in inhuman conditions even though there are enough resources on our planet for everyone.  
Nevertheless, they decided to give us one last chance to avoid annihilation of our race if we can prove that we are actually intelligent and worthy of life in this universe. Our satellites intercepted the transmissions of their encrypted messages, and a team of world’s top cryptologists, linguists, and computer scientists was assembled in secluded, top-secret facilities to work on deciphering those messages.  
However, someone managed to sabotage the mission and we lost all contact with the team just as they were on the verge of a breakthrough. Luckily, there was a backup plan that the saboteur didn’t know about: one team member was secretly uploading their findings with each progress to a secure cloud. We may not be able to establish contact with the team in time to save the Earth, so it is now up to you, the students of Hacettepe University Computer Engineering Department, to complete the mission and save our planet and the whole human race from extinction.  
# Mission: Decrypt Alien Message
The original Binarian message consists of characters and symbols unknown to humans, but the linguists assigned ASCII characters to each symbol to simplify the process of language decryption. They managed to extrapolate the meaning of the words included in the message, and compile a Binarian-English Dictionary. The compiled dictionary is stored in dictionary.txt which we are supposed to import into our program (use the Python dictionary data structure). 
<br>
Each line consists of a word in Binarian followed by its English meaning, and the type of the word in parentheses (n stands for noun, v for verb, adj for adjective, pro for pronoun, conj for conjunction, num for numbers, adv for adverbials, excl for exclamation, ques for question). 

The file that contains the original and whole Binarian transmission is jumbled. Some lines contain the actual text of their message, whereas other lines that start with certain characters contain data about Binarian race and their home-world: 
> Lines that start with ‘+’ contain astrophysical data about the Binarian planet, 
> Lines that start with ‘#’ contain metadata, 
> All other lines form the whole Binarian message when pieced together

Our first mission is to extract the whole message text from the file binarian_transmission.txt (only the message, not any other included data!) and translate it word-for-word and line-by-line into English using the Binarian-English Dictionary. If a word is not in the dictionary, it should stay as it is (do not omit the word in your translation!). You should both output your translation to the console and store it in a file named binarian_message.txt

# Mission: Data Extraction and Calculations
Binarians don’t use decimal number system like us; they use binary numbers. We need to uncover all numerical data about their home-planet hidden in their transmission (hint: remember that lines holding the astrophysical data about Binarian planet start with a ‘+’ sign).  
Our second mission involves extracting numerical data from their transmission and presenting it in a human-readable form. Since the numbers will be binary, we need to convert them into numbers in base ten. For this part of the mission, complete the function binary_to_decimal() in the template file, which we will use for the number base conversion. 
We are supposed to find the distance of their planet from the earth in light-years, temperature of their planet, and its orbital-speed. One extra task for you to do is to convert the obtained distance in light-years to kilometers. We do not need to convert orbital-speed and temperature values as they are already given in km/s and degrees Celsius respectively. For this part of the mission, complete the function ly_to_km() in the template file, which we will use for converting light-years to kilometers. 
> Note: We both output our results to the console and store them in a file named computations.txt. 
# Mission: Translate a Message for Peace to Binarian Language
Our last mission is to translate a message of peace into Binarian language, which will then be transmitted in hope that it will be enough to prove that we are indeed an intelligent and peaceful race, and that we do not deserve to be obliterated from this planet.  
The message to be translated is given in the text file named peace_message.txt. 
<br>
For this part of the mission, complete the functions english_to_binarian() and decimal_to_binary() in the template file. decimal_to_binary() function will convert a number in base ten to a binary number. 
Our program output the translated message, line by line (not as a single string!), both to the console and into the text file named message.txt.  
 
