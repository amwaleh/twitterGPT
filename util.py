
def tokenize_text(result, max_length=280):
  orig_string = result
  list_of_lines = []

  while len(orig_string) > max_length:
      line_length = orig_string[:max_length].rfind(' ')
      list_of_lines.append(orig_string[:line_length])
      orig_string = orig_string[line_length + 1:]
  list_of_lines.append(orig_string)
  
  return list_of_lines