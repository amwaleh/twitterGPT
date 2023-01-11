
from util import tokenize_text
from chat_gpt import invoke_chatgpt
from twitter import update_status

chat = invoke_chatgpt()
list_of_lines = tokenize_text(chat)
update_status(list_of_lines)


# response = openai.Image.create(
#   prompt="",
#   n=1,
#   size="1024x1024"
# )
# image_url = response['data'][0]['url']
# print(image_url)