# Day 31 of 100 Days of Code
## Flash Cards

Today's lesson was purely project based, and tested our *tkinter* skills (in combination with everything else we've learnt). The project was to create a flash card programme for learning a language (or any other subject). I have been trying to learn Russian when I can, so I decided to create Russian vocabulary.

We used data from [hermitdave](https://github.com/hermitdave/FrequencyWords/), who has a program which searches for the most frequent words in subtitles from various movies in a multitude of languages. I didn't use all 50 000 of his words as this would be far too many, so I just chose about 100 from the middle (to avoid too many being "the" and "a" etc.)

The program reads the csv file using *pandas* and will randomly display one of the words in Russian on the card. After 3 seconds the card flips to show the English translation. If the user got it right, they click the "tick" button, and if not they click the "cross". A new word appears and the program tracks which words you do and don't know so that next time it only asks the unknown words.

All in all this was a fun project that tested our *tkinter* and *pandas* skills so far.