from website import create_app
import random
from flask import render_template, request
import json
from pprint import pprint as pp


app = create_app()

@app.route("/json_testing")
def json_testing(): 
     with open('/home/gwl7/PokemonGenerator/Python-Webapp/johto.json') as fh:
          d = json.loads(fh.read())
          pp(d[0])
          print(d[0])
     return(d)

#loop through the json, grabbing all names
#loop through and grab all fire types
#list of all 2nd + 3rd evolutions
#list of each type
#app.route("/")
def random_test():
    return "<p>Pokemon Generator Home</p>"

@app.route("/", methods=["POST", "GET"])

def randomtemplate():
     if request.method == "POST":
          selected_type = request.form.get("pokemon_type")
          print(request.form)

      
          with open('/home/gwl7/PokemonGenerator/Python-Webapp/johto.json', "r") as fh:
          
               data = json.load(fh)

          fully_evolved = []    

          for record in data:

           if not record.get("isNfe"):
                 fully_evolved.append(record)

          randomnum=random.randint(0,len(fully_evolved))
          return render_template('randtest.html', randomnum=randomnum, gen_one_pokemon=fully_evolved[randomnum])

          #return request.form
     else:
          gen_one_names = [
               "Bulbasaur", "Ivysaur", "Venusaur",
               "Charmander", "Charmeleon", "Charizard",
               "Squirtle", "Wartortle", "Blastoise",
               "Caterpie", "Metapod", "Butterfree",
               "Weedle", "Kakuna", "Beedrill",
               "Pidgey", "Pidgeotto", "Pidgeot",
               "Rattata", "Raticate",
               "Spearow", "Fearow",
               "Ekans", "Arbok",
               "Pikachu", "Raichu",
               "Sandshrew", "Sandslash",
               "Nidoran♀", "Nidorina", "Nidoqueen",
               "Nidoran♂", "Nidorino", "Nidoking",
               "Clefairy", "Clefable",
               "Vulpix", "Ninetales",
               "Jigglypuff", "Wigglytuff",
               "Zubat", "Golbat",
               "Oddish", "Gloom", "Vileplume",
               "Paras", "Parasect",
               "Venonat", "Venomoth",
               "Diglett", "Dugtrio",
               "Meowth", "Persian",
               "Psyduck", "Golduck",
               "Mankey", "Primeape",
               "Growlithe", "Arcanine",
               "Poliwag", "Poliwhirl", "Poliwrath",
               "Abra", "Kadabra", "Alakazam",
               "Machop", "Machoke", "Machamp",
               "Bellsprout", "Weepinbell", "Victreebel",
               "Tentacool", "Tentacruel",
               "Geodude", "Graveler", "Golem",
               "Ponyta", "Rapidash",
               "Slowpoke", "Slowbro",
               "Magnemite", "Magneton",
               "Farfetch’d",
               "Doduo", "Dodrio",
               "Seel", "Dewgong",
               "Grimer", "Muk",
               "Shellder", "Cloyster",
               "Gastly", "Haunter", "Gengar",
               "Onix",
               "Drowzee", "Hypno",
               "Krabby", "Kingler",
               "Voltorb", "Electrode",
               "Exeggcute", "Exeggutor",
               "Cubone", "Marowak",
               "Hitmonlee", "Hitmonchan",
               "Lickitung",
               "Koffing", "Weezing",
               "Rhyhorn", "Rhydon",
               "Chansey",
               "Tangela",
               "Kangaskhan",
               "Horsea", "Seadra",
               "Goldeen", "Seaking",
               "Staryu", "Starmie",
               "Mr. Mime",
               "Scyther",
               "Jynx",
               "Electabuzz",
               "Magmar",
               "Pinsir",
               "Tauros",
               "Magikarp", "Gyarados",
               "Lapras",
               "Ditto",
               "Eevee", "Vaporeon", "Jolteon", "Flareon",
               "Porygon",
               "Omanyte", "Omastar",
               "Kabuto", "Kabutops",
               "Aerodactyl",
               "Snorlax",
               "Articuno", "Zapdos", "Moltres",
               "Dratini", "Dragonair", "Dragonite",
               "Mewtwo", "Mew"]
          
          randomnum=random.randint(0,len(gen_one_names))
          return render_template('randtest.html', randomnum=randomnum, gen_one_pokemon=gen_one_names[randomnum])






if __name__ == '__main__':
    app.run(debug=True)

