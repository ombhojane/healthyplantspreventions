import streamlit as st
import openai

# Set your OpenAI API key
openai.api_key = "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"

def generate_prevention_info(disease_name):
    prompt = f"Provide preventive measures for the plant disease: {disease_name}."
    
    # Use OpenAI GPT-3.5 Turbo to generate prevention information
    response = openai.Completion.create(
        engine="text-davinci-003",  # You can use "text-davinci-003" or another available engine
        prompt=prompt,
        max_tokens=150,  # Adjust max_tokens based on desired response length
        temperature=0.7,  # Adjust temperature for creativity vs. determinism
        n=1,  # Number of completions to generate
    )
    
    return response.choices[0].text.strip()

def main():
    st.title("Plant Disease Prevention Information")

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
