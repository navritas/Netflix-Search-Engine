from tkinter import *
from tkinter import ttk
import json

# Function to switch to the second screen for searching
def switchToSecondScreen():
    # Hide elements from the first screen
    netflixLogoLabel.grid_forget()
    textLabel.grid_forget()
    profile1.grid_forget()
    background.grid_forget()
    
    # Show elements for the second screen
    netflixLogoLabel2.grid(row=0, column=1, pady=10, columnspan=3)
    
    searchLabel.grid(row=1, column=0, pady=10, sticky="e")
    searchBar.grid(row=1, column=1, pady=15, columnspan=3)
    searchButton.grid(row=1, column=4, padx=10, pady=10)
    
    profile2.grid(row=0, column=4, padx=10)
    
    releaseDateLabel.grid(row=2, column=0, padx=10, pady=30, sticky="e")
    releaseDateEntry.grid(row=2, column=1, padx=10, pady=5)
    
    genreLabel.grid(row=2, column=2, padx=10, pady=5, sticky="e")
    genreEntry.grid(row=2, column=3, padx=10, pady=5)
    
    ageRatingLabel.grid(row=3, column=0, padx=10, pady=20, sticky="e")
    ageRatingCombobox.grid(row=3, column=1, padx=10, pady=5)
    
    typeLabel.grid(row=3, column=2, padx=10, pady=5, sticky="e")
    typeCombobox.grid(row=3, column=3, padx=10, pady=5)
    
    resultText.grid(row=4, column=0, columnspan=5, padx=10, pady=10)
    
    scrollbar.grid(row=4, column=5, sticky="nwse")
    
    resultText['yscrollcommand'] = scrollbar.set
    
    resetButton.grid(row=5, column=0, padx=10, pady=10, columnspan=5)
    goBackButton.grid(row=6, column=0, padx=10, pady=10, columnspan=5)

# Function to handle the search button
def searchButtonClick():
    searchQuery = searchBar.get().lower()  
    resultText.config(state=NORMAL)  
    resultText.delete(1.0, END)  
    releaseYearDate = releaseDateEntry.get()
    selectedGenre = genreEntry.get().lower()
    selectedAgeRating = ageRatingCombobox.get()
    selectedType = typeCombobox.get()
    
    titleFound = False

    # Finds matching data and prints results on screen
    for item in data:
        releaseYear = item['release_year']
        if (searchQuery in str(item['title']).lower()) and \
           (releaseYearDate == "" or str(releaseYearDate) == str(releaseYear)) and \
           (selectedGenre == "" or selectedGenre in item['listed_in'].lower()) and \
           (selectedAgeRating == "" or selectedAgeRating == item['rating']) and \
           (selectedType == "" or selectedType == item['type']):
            titleFound = True
            resultText.insert(END, f"Title: {item['title']}\n"
                                  f"Type: {item['type']}\n"
                                  f"Director: {item['director']}\n"
                                  f"Cast: {item['cast']}\n"
                                  f"Country: {item['country']}\n"
                                  f"Date Added: {item['date_added']}\n"
                                  f"Release Year: {item['release_year']}\n"
                                  f"Rating: {item['rating']}\n"
                                  f"Duration: {item['duration']}\n"
                                  f"Genre: {item['listed_in']}\n"
                                  f"Description: {item['description']}\n\n")
    # Input Validation
    if not titleFound:
        resultText.insert(END, "Invalid Input. Try again.")

    resultText.config(state=DISABLED)

# Function to handle the reset button 
def resetButtonClick():
    searchBar.delete(0, END)
    releaseDateEntry.delete(0, END)
    genreEntry.delete(0, END)
    ageRatingCombobox.set("")
    typeCombobox.set("")
    resultText.config(state=NORMAL)
    resultText.delete(1.0, END)
    resultText.config(state=DISABLED)
    
# Function to switch back to the first screen
def switchToFirstScreen():
    # Hide elements from the second screen
    netflixLogoLabel2.grid_forget()
    searchLabel.grid_forget()
    searchBar.grid_forget()
    searchButton.grid_forget()
    releaseDateLabel.grid_forget()
    releaseDateEntry.grid_forget()
    genreLabel.grid_forget()
    genreEntry.grid_forget()
    ageRatingLabel.grid_forget()
    ageRatingCombobox.grid_forget()
    typeLabel.grid_forget()
    typeCombobox.grid_forget()
    resultText.grid_forget()
    scrollbar.grid_forget()
    resetButton.grid_forget()
    goBackButton.grid_forget()
    profile2.grid_forget()

    # Show elements for the first screen
    netflixLogoLabel.grid(row=0, column=2, padx=225, pady=10)
    textLabel.grid(row=4, column=2)
    profile1.grid(row=7, column=2, padx=10, pady=20)
    background.grid(row=10, column=2, padx=55, pady=10)

# Loads data from JSON file
with open("netflix.json", "r") as f:
    data = json.load(f)

# Create the main window
window = Tk()
window.title("NETFLIX")
window.geometry('750x800')
window.configure(bg="black")

# Load images and create labels, buttons, etc for first screen
netflixLogo = PhotoImage(file="netflixLogo.png")
netflixLogoLabel = Label(window, image=netflixLogo, bg="black")
netflixLogoLabel.grid(row=0, column=2, padx=75, pady=10)

backgroundImage = PhotoImage(file="background.png")
background = Label(window, image=backgroundImage, bg="black", borderwidth=0)
background.grid(row=10, column=2, padx=55,pady=10)

textImage = PhotoImage(file="text.png")
textLabel = Label(window, image=textImage, bg="black", fg="white")
textLabel.grid(row=4, column=2)

profile1Image = PhotoImage(file="profile1.png")
profile1 = Button(window, image=profile1Image, command=switchToSecondScreen)
profile1.grid(row=7, column=2, pady=20)

# Load images and create labels, buttons, etc for second screen
netflixLogoLabel2 = Label(window, image=netflixLogo, bg="black")

searchLabel = Label(window, text="Search Titles:", bg="black", fg="white")
searchBar = Entry(window, width=50)
searchImage = PhotoImage(file="searchButton.png")
searchButton = Button(window, image=searchImage, command=searchButtonClick)

profile2Image = PhotoImage(file="profile2.png")
profile2 = Button(window, image=profile2Image, command=switchToFirstScreen)
profile2.grid(row=0, column=4, padx=10)

releaseDateLabel = Label(window, text="Release Year:", bg="black", fg="white")
releaseDateEntry = Entry(window, width=20)

genreLabel = Label(window, text="Genre:", bg="black", fg="white")
genreEntry = Entry(window, width=20)

ageRatingLabel = Label(window, text="Age Rating:", bg="black", fg="white")
ageRatings = ["PG-13", "TV-14", "R", "TV-MA", "TV-PG", "PG"]
ageRatingCombobox = ttk.Combobox(window, values=ageRatings)

typeLabel = Label(window, text="Type:", bg="black", fg="white")
typeValues = ["", "TV Show", "Movie"]
typeCombobox = ttk.Combobox(window, values=typeValues)

resultText = Text(window, bg="black", fg="white", wrap=WORD)

scrollbar = Scrollbar(window, command=resultText.yview)

resetButton = Button(window, text="Reset", command=resetButtonClick)

goBackButton = Button(window, text="Main Menu", command=switchToFirstScreen)

window.mainloop()