import json
import requests

from openai import OpenAIApi

class BackendApplication:
    def init(self, database):
        self.database = database

        # Create an OpenAI API object
        self.openai = OpenAIApi(openai_api_key="YOUR_OPENAI_API_KEY")

    def generate_chatbot_link(self, prompt, business_data):
        # Extract the prompt and business data from the database
        prompt = self.database.get_prompt()
        business_data = self.database.get_business_data()

        # Generate a ChatGPT prompt based on the extracted data
        chatgpt_prompt = f"Generate a chatbot based on the following prompt: {prompt} and business data: {business_data}"

        # Send the ChatGPT prompt to the ChatGPT API and receive the response
        chatgpt_response = self.openai.generate(chatgpt_prompt)

        # Save the ChatGPT response to the database
        self.database.save_chatbot_response(chatgpt_response)

        # Generate a relative link or unique identifier for the chatbot
        chatbot_link = f"/chatbot/{chatgpt_response.id}"

        # Return the chatbot link
        return chatbot_link
