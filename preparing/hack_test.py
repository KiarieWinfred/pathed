import os
import random
from openai import OpenAI

# Function to initialize the OpenAI API client
def initialize_openai():
    try:
        return OpenAI(
            api_key="de1cd11f90b84bef979a279a8fd8a8eb",  # Replace with your actual API key
            base_url="https://api.aimlapi.com"  # Replace with the correct base URL if necessary
        )
    except Exception as e:
        print(f"Error initializing OpenAI client: {e}")
        return None

# Function to interact dynamically with the model and patient
def dynamic_patient_questionnaire():
    client = initialize_openai()
    if client is None:
        return

    # Start with the first question
    current_question = "Which symptoms are you experiencing?"
    patient_responses = []

    for question_num in range(1, 11):  # Limit to 10 questions
        # Ask the current question and collect the patient's response
        print(f"Question {question_num}: {current_question}")
        patient_response = input("> ")
        patient_responses.append(patient_response)

        # Create a dynamic prompt incorporating previous responses
        prompt = f"The patient has reported: '{' '.join(patient_responses)}'. Please generate the most relevant question to help narrow down the possible causes."
        
        print("Prompt:", prompt)
        # Send request to OpenAI to generate the next question
        try:
            response = client.chat.completions.create(
                model="o1-preview",  # Use the appropriate model version
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    },
                ],
                max_tokens=1000,  # Increased tokens for detailed medical questions
            )
            print("Response:", response)
            next_question = response.choices[0].message.content.strip()
            print("next question is:", next_question)
            if next_question:
                current_question = next_question  # Prepare for next iteration
                patient_responses = []
            else:
                print("No valid response, ending the process.")
                break
        except Exception as e:
            print(f"Error during OpenAI API call for next question: {e}")
            break

    # After collecting responses, ask the model for a differential diagnosis
    if patient_responses:
        prompt_for_diagnosis = "Here are the patient's responses:\n"
        for response in patient_responses:
            prompt_for_diagnosis += f"- {response}\n"

        prompt_for_diagnosis += "\nBased on this data, provide 3-5 differential diagnoses and the diagnostic criteria or tests to narrow down the diagnosis."

        try:
            response = client.chat.completions.create(
                model="o1-preview",  # Adjust model version as needed
                messages=[
                    {
                        "role": "user",
                        "content": prompt_for_diagnosis
                    },
                ],
                max_tokens=1000,  # Adjust token limit for diagnosis generation
            )
            diagnosis = response.choices[0].message.content.strip()
            print(f"Assistant: {diagnosis}")
        except Exception as e:
            print(f"Error during OpenAI API call for differential diagnosis: {e}")
    else:
        print("No patient responses recorded. Cannot proceed with diagnosis.")

if __name__ == "__main__":
    dynamic_patient_questionnaire()
