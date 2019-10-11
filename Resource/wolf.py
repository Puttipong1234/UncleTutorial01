import wolframalpha
import wikipedia
import requests
from translation import google


appId = 'APER4E-58XJGHAVAK'
client = wolframalpha.Client(appId)


# method that search wikipedia... 
def search_wiki(keyword=''):
      
  keyword=google(keyword, dst = 'en')
  # running the query
  searchResults = wikipedia.search(keyword)
  # If there is no result, print no result
  if not searchResults:
    # print("No result from Wikipedia")
    return 'ไม่พบคำว่า {} ที่ท่านต้องการค้นหา กรุณาค้นหาใหม่อีกครั้งค่ะ'.format(keyword)
  # Search for page... try block 
  try:
    page = wikipedia.page(searchResults[0])
  except wikipedia.DisambiguationError as err:
    page = wikipedia.page(err.options[0])
  
  wikiTitle = page.title.encode('utf-8')
  wikiSummary = page.summary.encode('utf-8')
  res=google(wikiSummary, dst = 'th')
  return (res[0:180] + '......')
    

def search(text=''):
    res = client.query(text)
    # Wolfram cannot resolve the question
    if res['@success'] == 'false':
        pass
    # Wolfram was able to resolve question
    else:
        result = ''
        # pod[0] is the question
        pod0 = res['pod'][0]
        # pod[1] may contains the answer
        pod1 = res['pod'][1]
        # checking if pod1 has primary=true or title=result|definition
        if (('definition' in pod1['@title'].lower()) or ('result' in  pod1['@title'].lower()) or (pod1.get('@primary','false') == 'true')):
            # extracting result from pod1
            result = resolveListOrDict(pod1['subpod']).decode("utf-8") 
            question = resolveListOrDict(pod0['subpod'])
            question = removeBrackets(question)
            # primaryImage(question)
        else:
            # extracting wolfram question interpretation from pod0
            question = resolveListOrDict(pod0['subpod'])
            # removing unnecessary parenthesis
            question = removeBrackets(question)
            # searching for response from wikipedia
            result = search_wiki(question)
            # primaryImage(question)
        return (result.decode("utf-8")[0:140] + '......')

def removeBrackets(variable):
  return variable.split('(')[0]

def resolveListOrDict(variable):
  if isinstance(variable, list):
    return variable[0]['plaintext']
  else:
    return variable['plaintext']

def primaryImage(title=''):
    url = 'http://en.wikipedia.org/w/api.php'
    data = {'action':'query', 'prop':'pageimages','format':'json','piprop':'original','titles':title}
    try:
        res = requests.get(url, params=data)
        key = res.json()['query']['pages'].keys()[0]
        imageUrl = res.json()['query']['pages'][key]['original']['source']
        return imageUrl
    except Exception as err:
        print('Exception while finding image:= '+str(err))
 


