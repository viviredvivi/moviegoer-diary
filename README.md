# moviegoer-diary
A great little tool for every cinephile, also a GUI app that shows my progress as a Python programmer.

It has straightforward and friendly GUI that allows the user to make entries about watched movies (including details like title, director, date, place etc.) that are saved into a JSON file. User can easily access entries just by typing a movie title (after clicking "Search for existing entry" button, if the entry do exist, a pop-up with previously saved data will be shown).

I've made Moviegoer Diary using tkinter module, using mainly Entry and Label classes. To save and read records I've created two functions and implemented exception handling in each of them (in case that the file doesn't exist yet). 

This app has a lot cleaner and more readable code than my previous one. It also solves a real life problem for a cinephile – big sites like imdb are more of a movie-related data, ratings and reviews databases. If you just want to keep track of the movies that you've watched as well as where and when you've watched it, they're pretty much useless. With Moviegoer Diary you can easily do these things and, thanks to data being saved in .json, make some interesting statistics using other Python modules, like pandas and matplotlib.

I hope you'll find my project useful! If you want to give me some feedback, feel free to do it – I'm still learning and I will be grateful for any advice.
