from website import create_app #create_app is function created in website folder, init file
import random
from flask import render_template, request #imports jinja2 framework (passes code from py to html format)
import json
from pprint import pprint as pp
import psycopg2

app = create_app() #creates app


@app.route("/", methods=["POST", "GET"])

def testtesmplate():
     
     page_count=index()

     if request.method == "POST": #if form is submitted

          with open('johto.json', "r") as fh: 
                    data = json.load(fh)   #load in johto.json
     
          chosen_type = request.form.get('pokemon_type')
          gen_one_selected = request.form.get('Generation_one') == "value1"
          gen_two_selected = request.form.get('Generation_two') == "value2"
          fully_evolved_selected = request.form.get("fully evolved") == "fully_evolved"

          resulting_pokemon = []

          for pokemon in data:
               if chosen_type not in pokemon['types']:
                    continue

               if gen_one_selected and pokemon['id'] >= 152:
                     continue
               if gen_two_selected and pokemon["id"] < 152:
                     continue
               if not gen_one_selected and not gen_two_selected:
                     pass #allow all generations
               
               if fully_evolved_selected and not "isNfe" in pokemon:
                     continue
               resulting_pokemon.append(pokemon['name'])

               if resulting_pokemon:
                     generate_random = random.choice(resulting_pokemon)

               else:
                     generate_random = "No matching"


               
               print("Fully evolved checkbox value:", request.form.get("fully_evolved"))
               print(f"{pokemon['name']} - isNfe: {pokemon.get('isNfe')}")


          return render_template('randtest.html', pokemon_picture=generate_random, page_count=page_count)
                    
                    

     else:
          return render_template('randtest.html', page_count=page_count)

     
def get_db_connection():
      return psycopg2.connect(
            host="ep-raspy-cake-a4er20z3-pooler.us-east-1.aws.neon.tech",
            database="neondb",
            user='neondb_owner',
            password="npg_Aj9IicxVR6Og" 
      )

def index():
      conn = get_db_connection()
      cur = conn.cursor()
      cur.execute('UPDATE page_counter SET count = count + 1 WHERE id = 1 RETURNING count;')
      new_count = cur.fetchone()[0]
      conn.commit()
      cur.close()
      conn.close()
      return(new_count)

      


if __name__ == '__main__':
     app.run(debug=True)

