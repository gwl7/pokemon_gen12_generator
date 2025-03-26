import json
from  pprint import pprint as pp

def json_testing(): 
     with open('/home/gwl7/PokemonGenerator/Python-Webapp/johto.json', "r") as fh:
     
          data = json.load(fh)

     fully_evolved = []    

     for record in data:

          print(record["id"], record["name"])

          if not record.get("isNfe"):
               fully_evolved.append(record)

     print("Fully Evolved:")
     pp(fully_evolved)          

     fully_evo_comprehension = [x for x in data if not x.get("isNfe")]
     print(fully_evolved == fully_evo_comprehension)

if __name__ == "__main__":
    json_testing()

