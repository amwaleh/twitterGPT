
import openai
import os


def invoke_chatgpt(text=None):
  prompt = text if text is not None else "provide only one, either a tech tip or engineering management tip" 
  openai.api_key = os.environ['OPENAI_KEY'] 
  response = openai.Completion.create(model="text-davinci-003", 
                                      prompt=prompt, 
                                      temperature=0.5,
                                      max_tokens=2048)

  result = response.get("choices")[0].get("text")
  return result