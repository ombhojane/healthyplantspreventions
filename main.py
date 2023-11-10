import streamlit as st
import openai

# Set your OpenAI API key
openai.api_key = st.secrets["openai_api_key"]

def generate_prevention_info(disease_name):
    prompt_template = """Suggest evidence-based preventive measures for the following scenario involving plants and diseases:

- Plant: '{plant_name}'
- Disease: '{disease_name}'

Provide the preventive measures in a structured format with clear explanations. Consider the following guidelines:

- Prevention 1: Details on the first prevention method.
- Prevention 2: Details on the second prevention method.
- Prevention 3: Details on additional prevention methods.

Include actionable steps a gardener or farmer could take. Be concise in your explanations, avoiding unnecessary details. Focus on providing valuable insights for effective disease management.
"""


    # Use OpenAI GPT-3.5 Turbo to generate prevention information
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt_template,
        max_tokens=300,  # Adjust max_tokens based on desired response length
        temperature=0.7,
        n=1,
    )
    
    return response.choices[0].text.strip()

def main():

    # User input for plant disease
    user_input = st.text_input("Enter the name of the plant disease:")

    if user_input:
        # Convert input to uppercase to enhance recognition
        disease_name = user_input.strip().capitalize()

        # Generate prevention information using GPT-3.5 Turbo
        prevention_info = generate_prevention_info(disease_name)

        # Display prevention information
        st.header(f"Prevention Information for {disease_name}")
        st.write(prevention_info)

if __name__ == "__main__":
    main()
