import os

def save_data(data, file_name="daily_update.txt"):
    try:
        with open(file_name, "w") as file:
            file.write(data)
        return f"Data saved to {file_name}"
    except Exception as e:
        return f"Error saving data: {e}"
