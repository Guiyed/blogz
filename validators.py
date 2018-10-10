import re  
  
def validateTitle(blogTitle):
  if blogTitle == "":
    return 'Please fill in the Title'
  elif not re.match("^[A-Za-z0-9\s\-_,\.!:;()''""]{1,100}$", blogTitle):
    return 'Title must contain between 1 and 100 alphanumeric characters'  
  
  return ''


def validateBody(bodyText):
  if bodyText == "":
    return "Please fill in the Body of the Blog"

  elif not re.match("^[A-Za-z0-9\s\-_,\!.:;()''""]{1,500}$",bodyText):
    return 'Password must be between 1 and 500 characters'    
  return ''


def main():
  title = 'gui que mas'
  body = '1234 kdsjfs f-fe felkj '
  print(validateTitle(title))  
  print(validateBody(body))

  title = ''
  body = ''
  print(validateTitle(title))  
  print(validateBody(body)) 

  title = 'Incididunt in do eiusmod esse et labore quis labore aute eu reprehenderit et aute consectetur. Duis eiusmod ut laborum proident.'
  body = '''Elit anim cupidatat id proident do quis do laborum reprehenderit ad magna irure do. Eiusmod laboris nostrud excepteur est fugiat nostrud deserunt. Dolor proident aliquip anim eiusmod excepteur. Amet do qui ad veniam aliquip reprehenderit nisi cupidatat mollit consectetur sit reprehenderit ad. Cupidatat dolor elit commodo officia ipsum elit ipsum ad pariatur. Irure eu excepteur ut cupidatat Lorem ex.

Ad commodo nostrud occaecat consequat ea sint amet consectetur. Deserunt dolore ad ex incididunt elit mollit. Non exercitation non ex voluptate.'''
  print(validateTitle(title))  
  print(validateBody(body))  

if __name__ == "__main__":
  main()   