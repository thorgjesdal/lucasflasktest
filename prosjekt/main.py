from flask import Flask, request, render_template  #importerer flask


app = Flask(__name__)  #app: navn for serveren

@app.route('/')  #lager siden til hjemsiden
def index():
    return render_template('hjem.html') #definerer innholdet til siden

@app.route('/get-text', methods=['GET', 'POST'])  #siden som skal hente resultatet, POST for å kunne hente svaret
def ferdig():
    #Funksjonen som skal gjennomføres når knappen trykkes må være i denne løkken
    svar = request.form['tekst_input'] #svar = inputen

    FILNAVN = 'prosjekt/resultat/ny_fil.txt'  #navnet på filen som skal lages
    with open (FILNAVN, 'w') as fil:
        fil.write('Hello world ' + svar)

    return render_template('ferdig.html', svar=svar) #nye nettsiden

if __name__ == '__main__':
    app.run(debug=True)  #gjør at serveren kjører når du kjører programmet