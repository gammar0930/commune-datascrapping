import tkinter as tk
from YouTubeMusicAPI import search


def search_music():
    query = entry_query.get()
    start_date = entry_start_date.get()
    end_date = entry_end_date.get()
    music_type = entry_music_type.get()

    query_with_type = f"{query} {music_type}"
    result = search(f"{query_with_type} {start_date} {end_date}")

    if result:
        result_text.delete(1.0, tk.END)  # Clear previous result
        result_text.insert(tk.END, result)
    else:
        result_text.delete(1.0, tk.END)  # Clear previous result
        result_text.insert(tk.END, "No Result Found")


# Create the main application window
app = tk.Tk()
app.title("Youtube Music Scraper")

# Create input fields and labels
label_query = tk.Label(app, text="Search Query:")
entry_query = tk.Entry(app)
label_start_date = tk.Label(app, text="Start Date (YYYY-MM-DD):")
entry_start_date = tk.Entry(app)
label_end_date = tk.Label(app, text="End Date (YYYY-MM-DD):")
entry_end_date = tk.Entry(app)
label_music_type = tk.Label(app, text="Music Type:")
entry_music_type = tk.Entry(app)

# Create search button
search_button = tk.Button(app, text="Search", command=search_music)

# Create result display area
result_text = tk.Text(app, height=10, width=50)

# Place input fields, labels, button, and result display in the window
label_query.pack()
entry_query.pack()
label_start_date.pack()
entry_start_date.pack()
label_end_date.pack()
entry_end_date.pack()
label_music_type.pack()
entry_music_type.pack()
search_button.pack()
result_text.pack()

# Start the application
app.mainloop()
