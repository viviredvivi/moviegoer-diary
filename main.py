from tkinter import *
from tkinter import messagebox
import json


def save_record():
    title_data = movie_entry.get()
    date_data = date_entry.get()
    place_data = place_entry.get()
    director_data = movie_director_entry.get()
    country_data = country_entry.get()
    production_year_data = year_entry.get()
    notes_data = notes_entry.get()

    new_data = {
        title_data: {
            "date": date_data,
            "place": place_data,
            "director": director_data,
            "country": country_data,
            "production year": production_year_data,
            "notes": notes_data,
        }
    }

    if len(title_data) == 0 or len(date_data) == 0 or len(place_data) == 0 \
            or len(director_data) == 0 or len(country_data) == 0 \
            or len(production_year_data) == 0 or len(notes_data) == 0:
        messagebox.showinfo(title="Oops",
                            message="Please don't leave any field empty!")
    else:
        try:
            with open("data.json", "r") as saving_file:
                data = json.load(saving_file)
        except FileNotFoundError:
            with open("data.json", "w") as saving_file:
                json.dump(new_data, saving_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as saving_file:
                json.dump(data, saving_file, indent=4)
        finally:
            movie_entry.delete(0, END)
            date_entry.delete(0, END)
            place_entry.delete(0, END)
            movie_director_entry.delete(0, END)
            country_entry.delete(0, END)
            year_entry.delete(0, END)
            notes_entry.delete(0, END)


def read_record():
    title_data = movie_entry.get()
    try:
        with open("data.json") as search_file:
            search_data = json.load(search_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found.")
    else:
        if title_data in search_data:
            searched_date = search_data[title_data]["date"]
            searched_place = search_data[title_data]["place"]
            searched_director = search_data[title_data]["director"]
            searched_country = search_data[title_data]["country"]
            searched_year = search_data[title_data]["production year"]
            searched_notes = search_data[title_data]["notes"]
            messagebox.showinfo(title=title_data,
                                message=f"Saw it on: {searched_date}\n\n"
                                        f"Place that I saw it at: "
                                        f"{searched_place}\n\n"
                                        f"Directed by: {searched_director}\n\n"
                                        f"Production country: "
                                        f"{searched_country}\n\n"
                                        f"Year of production: "
                                        f"{searched_year}\n\n"
                                        f"A few thoughts/hot take about it: "
                                        f"{searched_notes}")
        else:
            messagebox.showinfo(title="Error",
                                message=f"No details for {title_data} exist.")
    finally:
        movie_entry.delete(0, END)


user_interface = Tk()
user_interface.title("Moviegoer Diary")
user_interface.config(padx=35, pady=35, bg="white")

moviegoer_diary_header = Label(text="MY MOVIEGOER DIARY",
                               font=("Courier", 30, "bold"),
                               bg="white", fg="black")
moviegoer_diary_header.grid(column=0, row=0, padx=35, pady=35, columnspan=3)

canvas = Canvas(width=250, height=180, bg="white", highlightthickness=0)
film_vector_img = PhotoImage(file="film_vector.png")
canvas.create_image(120, 80, image=film_vector_img)
canvas.grid(column=2, row=2, rowspan=5)

movie_title = Label(text="Movie title:", bg="white", fg="black")
movie_title.grid(column=0, row=1, sticky="E")

movie_entry = Entry(width=20, highlightthickness=0, bg="white", fg="black")
movie_entry.grid(column=1, row=1)
movie_entry.focus()

search = Button(text="Search for existing entry",
                width=18, pady=5, highlightthickness=0,
                bg="white", fg="black", command=read_record)
search.grid(column=2, row=1)

date = Label(text="Saw it on (DD.MM.YYYY):", bg="white", fg="black")
date.grid(column=0, row=2, sticky="E")

date_entry = Entry(width=20, highlightthickness=0, bg="white", fg="black")
date_entry.grid(column=1, row=2)
date_entry.focus()

place = Label(text="Cinema or other place that I saw it at:",
              bg="white", fg="black")
place.grid(column=0, row=3, sticky="E")

place_entry = Entry(width=20, highlightthickness=0, bg="white", fg="black")
place_entry.grid(column=1, row=3)

movie_director = Label(text="Directed by:", bg="white", fg="black")
movie_director.grid(column=0, row=4, sticky="E")

movie_director_entry = Entry(width=20, highlightthickness=0,
                             bg="white", fg="black")
movie_director_entry.grid(column=1, row=4)

country = Label(text="Production country:", bg="white", fg="black")
country.grid(column=0, row=5, sticky="E")

country_entry = Entry(width=20, highlightthickness=0, bg="white", fg="black")
country_entry.grid(column=1, row=5)

production_year = Label(text="Production year (YYYY):",
                        bg="white", fg="black", compound="right")
production_year.grid(column=0, row=6, sticky="E")

year_entry = Entry(width=20, highlightthickness=0, bg="white", fg="black")
year_entry.grid(column=1, row=6)

notes = Label(text="A few thoughts/hot take about it:", bg="white", fg="black")
notes.grid(column=0, row=7, sticky="E")

notes_entry = Entry(width=48, highlightthickness=0, bg="white", fg="black")
notes_entry.grid(column=1, columnspan=2, row=7)

add = Button(text="Add new entry", width=20, pady=10, highlightthickness=0,
             bg="white", fg="black", command=save_record)
add.grid(column=1, row=8, columnspan=2)


user_interface.mainloop()
