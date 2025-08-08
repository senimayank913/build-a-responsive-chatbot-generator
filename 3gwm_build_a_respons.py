# Import necessary libraries
import tkinter as tk
from tkinter import messagebox
import random
import json

# Define a class for the chatbot generator
class ChatbotGenerator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Responsive Chatbot Generator")
        self.root.geometry("500x600")

        # Create a frame for the input fields
        self.input_frame = tk.Frame(self.root, bg="gray")
        self.input_frame.pack(fill="x", padx=10, pady=10)

        # Create a label and entry for the chatbot name
        self.name_label = tk.Label(self.input_frame, text="Chatbot Name:", bg="gray")
        self.name_label.pack(side="left", padx=5, pady=5)
        self.name_entry = tk.Entry(self.input_frame, width=30)
        self.name_entry.pack(side="left", padx=5, pady=5)

        # Create a label and text area for the chatbot responses
        self.responses_label = tk.Label(self.input_frame, text="Responses:", bg="gray")
        self.responses_label.pack(side="left", padx=5, pady=5)
        self.responses_text = tk.Text(self.input_frame, width=40, height=10)
        self.responses_text.pack(side="left", padx=5, pady=5)

        # Create a button to generate the chatbot
        self.generate_button = tk.Button(self.root, text="Generate Chatbot", command=self.generate_chatbot)
        self.generate_button.pack(fill="x", padx=10, pady=10)

        # Create a frame for the output
        self.output_frame = tk.Frame(self.root, bg="gray")
        self.output_frame.pack(fill="x", padx=10, pady=10)

        # Create a text area for the output
        self.output_text = tk.Text(self.output_frame, width=60, height=10)
        self.output_text.pack(fill="both", expand=True, padx=5, pady=5)

    def generate_chatbot(self):
        # Get the chatbot name and responses from the input fields
        chatbot_name = self.name_entry.get()
        responses = self.responses_text.get("1.0", "end-1c")

        # Split the responses into individual responses
        responses = responses.splitlines()

        # Create a dictionary to store the chatbot data
        chatbot_data = {
            "name": chatbot_name,
            "responses": responses
        }

        # Convert the chatbot data to JSON
        chatbot_json = json.dumps(chatbot_data, indent=4)

        # Display the chatbot JSON in the output text area
        self.output_text.delete("1.0", "end")
        self.output_text.insert("1.0", chatbot_json)

    def run(self):
        self.root.mainloop()

# Create an instance of the ChatbotGenerator class and run it
generator = ChatbotGenerator()
generator.run()