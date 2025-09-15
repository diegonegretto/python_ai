from google import genai

class PythonAI:
    
    def __init__(self, api_key, model="gemini-2.5-flash"):
        self.client = genai.Client(api_key=api_key)
        self.model = model


    def ask(self, prompt):
        prompt += " Responda em até 250 caracteres."
        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt
        )

        return response.text
