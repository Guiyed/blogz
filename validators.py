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


def validateUsername(username):
  if username == "":
    return 'User is empty'
  elif not re.match("^[A-Za-z]{3,20}$", username):
    return 'User must contains between 3 and 20 alphanumeric characters'  
  return ''


def validatePassword(password):
  if password == "":
    return "Password is empty"
  elif not re.match("^[A-Za-z0-9]{3,20}$", password):
    return 'Password must be between 3 and 20 characters'
  return ''

def validateRetype(element,retype):
  if len(element) > 0:
    if element != retype:
      return "Passwords do not match"      
  return ''


def validateEmail(email):
  if email:
    if not re.match("^[A-Za-z0-9]{3,20}@[A-Za-z]+\.[a-zA-Z]+$", email):
      return "Email must be between 3 and 20 characters, must contains one '@', one '.' and no empty '  ' spaces "  
  return ''

      #^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$"
      #elif not re.match("[^@]+@[^@]+\.[^@]+", email):




def main():
  title = 'gui que mas'
  body = '1234 kdsjfs f-fe felkj '
  user = 'gui'
  passw = '1234'
  mail = 'hd3@q.c'
  
  print(validateTitle(title))  
  print(validateBody(body))
  print(validateUsername(user))  
  print(validatePassword(passw))   
  print(validateRetype(passw,'1234')) 
  print(validateEmail(mail))


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