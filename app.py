from tkinter import *
import pandas as pd
import matplotlib.pyplot as plt

root = Tk()
root.title('Goodreads Analyzer')
root.geometry('800x500')

# input box
data = Entry(root)
data.place(relx=0.025, rely=0.05, relwidth=0.7)

# output text box
output = Text(root, width=40)
output.place(relx=0.025, rely=0.2, relwidth=0.7, relheight=0.775)

# to give the initial statistics


def Analyze():
    datafile = str(data.get())
    csv = pd.read_csv(datafile)
    df = csv[csv['My Rating'] != 0]
    total_books = df['Book Id'].count()
    total_pages = int(df['Number of Pages'].sum(axis=0, skipna=True))
    unique_authors = df['Author'].nunique()
    avg_rating = round(df['Average Rating'].mean(), 2)
    labelBooks = Label(root, text="Total Books: " + str(total_books))
    labelBooks.place(relx=0.1, rely=0.1)
    labelPages = Label(root, text="Total Pages: " + f"{total_pages:,d}")
    labelPages.place(relx=0.6, rely=0.1)
    labelAuthors = Label(
        root, text="Unique Authors Read: " + str(unique_authors))
    labelAuthors.place(relx=0.1, rely=0.15)
    labelAvgRating = Label(
        root, text="Average Goodreads Rating: " + str(avg_rating))
    labelAvgRating.place(relx=0.6, rely=0.15)

#pie chart
def piechart(labs, values):
    plt.pie(values, labels=labs, autopct='%1.1f%%')
    plt.show()

# to give the list of most read authors


def Authors():
    datafile = str(data.get())
    csv = pd.read_csv(datafile)
    df = csv[csv['My Rating'] != 0]
    most_read_authors = df['Author'].value_counts().head(20)
    output.delete(1.0, END)
    output.insert(END, most_read_authors)

# to give the list of most read publishers


def Publishers():
    datafile = str(data.get())
    csv = pd.read_csv(datafile)
    df = csv[csv['My Rating'] != 0]
    most_common_publishers = df['Publisher'].value_counts().head(10)
    output.delete(1.0, END)
    output.insert(END, most_common_publishers)

# to give a list of no of books read by time periods


def Eras():
    datafile = str(data.get())
    csv = pd.read_csv(datafile)
    df = csv[csv['My Rating'] != 0]
    century_21 = len(df[(df['Original Publication Year'] > 2000)])
    century_20 = len(df[(df['Original Publication Year'] <= 2000) &
                        (df['Original Publication Year'] > 1900)])
    century_19 = len(df[(df['Original Publication Year'] <= 1900) &
                        (df['Original Publication Year'] > 1800)])
    century_16_18 = len(df[(df['Original Publication Year'] <= 1800) &
                           (df['Original Publication Year'] > 1500)])
    century_10_15 = len(df[(df['Original Publication Year'] <= 1500) &
                           (df['Original Publication Year'] > 1000)])
    century_0_10 = len(df[(df['Original Publication Year'] <= 1000) &
                          (df['Original Publication Year'] > 0)])
    century_bc = len(df[(df['Original Publication Year'] <= 0)])
    centuries = "After 2000:                " + str(century_21) + "\n" + \
                "From 1901 AD to 2000 AD:   " + str(century_20) + "\n" + \
                "From 1801 AD to 1900 AD:   " + str(century_19) + "\n" + \
                "From 1501 AD to 1800 AD    " + str(century_16_18) + "\n" + \
                "From 1001 AD to 1500 AD:   " + str(century_10_15) + "\n" + \
                "From 0 AD to 1000 AD:      " + str(century_0_10) + "\n" + \
                "Before 0 AD:               " + str(century_bc)
    output.delete(1.0, END)
    output.insert(END, centuries)
    c = [century_21, century_20, century_19, century_16_18, century_10_15, century_0_10, century_bc]
    c_l = ["21st century","20th century","19th century","16-18th century","10-15th century","1-10th century","Before Christ"]
    piechart(c_l,c)
# to give a list of no of books read by thickness/pages


def Thickness():
    datafile = str(data.get())
    csv = pd.read_csv(datafile)
    df = csv[csv['My Rating'] != 0]
    books_1000 = len(df[df['Number of Pages'] >= 1000])
    books_500 = len(df[(df['Number of Pages'] >= 500)
                       & (df['Number of Pages'] < 1000)])
    books_250 = len(df[(df['Number of Pages'] >= 250)
                       & (df['Number of Pages'] < 500)])
    books_100 = len(df[(df['Number of Pages'] >= 100)
                       & (df['Number of Pages'] < 250)])
    books_0 = len(df[df['Number of Pages'] < 100])
    books = "1000+ pages:     " + str(books_1000) + "\n" + \
            "500-999 pages:   " + str(books_500) + "\n" + \
            "250-499 pages:   " + str(books_250) + "\n" + \
            "100-249 pages:   " + str(books_100) + "\n" + \
            "0-99 pages:      " + str(books_0)
    output.delete(1.0, END)
    output.insert(END, books)
    b = [books_1000,books_500,books_250,books_100,books_0]
    b_l = ["1000+","500-999","250-499","100-249","0-99"]
    piechart(b_l, b)


# to give a list of no of books by my ratings


def Ratings():
    datafile = str(data.get())
    csv = pd.read_csv(datafile)
    df = csv[csv['My Rating'] != 0]
    r1 = len(df[df['My Rating'] == 1])
    r2 = len(df[df['My Rating'] == 2])
    r3 = len(df[df['My Rating'] == 3])
    r4 = len(df[df['My Rating'] == 4])
    r5 = len(df[df['My Rating'] == 5])
    ratings = "5 STARS:   " + str(r5) + "\n" + \
              "4 STARS:   " + str(r4) + "\n" + \
              "3 STARS:   " + str(r3) + "\n" + \
              "2 STARS:   " + str(r2) + "\n" + \
              "1 STARS:   " + str(r1)
    output.delete(1.0, END)
    output.insert(END, ratings)
    r = [r1, r2, r3, r4, r5]
    r_l = ['5-STAR', '4-STAR', '3-STAR', '2-STAR', '1-STAR']
    piechart(r_l, r)
    





# analyze  button
analyzeButton = Button(root, text="Analyze", command=Analyze)
analyzeButton.place(relx=0.75, rely=0.05, relwidth=0.2)

# most read authors button
authorsButton = Button(
    root, text="Most Read Authors?", command=Authors)
authorsButton.place(relx=0.75, rely=0.2, relwidth=0.2)

# most read publishers button
publishersButton = Button(
    root, text="Most Read Publishers?", command=Publishers)
publishersButton.place(relx=0.75, rely=0.35, relwidth=0.2)

# breakdown by eras button
eraButton = Button(root, width=20, text="Breakdown by Eras", command=Eras)
eraButton.place(relx=0.75, rely=0.5, relwidth=0.2)

# breakdown by pages button
thicknessButton = Button(root, text="Breakdown by Pages", command=Thickness)
thicknessButton.place(relx=0.75, rely=0.65, relwidth=0.2)

# breakdown by personal rating button
ratingsButton = Button(root, text="Breakdown by Your Ratings", command=Ratings)
ratingsButton.place(relx=0.75, rely=0.8, relwidth=0.2)

# pie chart button for ratings


root.mainloop()
