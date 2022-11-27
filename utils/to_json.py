import json

arr = []


def words_to_json(filename: str):
  with open(filename+'.txt', encoding='utf-8') as f1:
    for i in f1:
      n = i.lower().split('\n')[0]
      if n != '':
        arr.append(n)
        

  with open(filename+'.json', 'w', encoding='utf-8') as f2:
    json.dump(arr, f2)