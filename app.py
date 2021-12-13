from flask import Flask, render_template,request,redirect
from flask import g
import random,string
import sqlite3

app = Flask(__name__)



def getdb():
    db = getattr( g,'_database',None)
    if db is None:
        db = g._databse = sqlite3.connect("short_urls.db")
    return db

@app.route("/status")
def index():
    return 'Up and running'

def GetDisplayData():
    db = getdb()

    c = db.cursor()
    c.execute("SELECT * FROM link")
    data = c.fetchall()
    return data

def DeleteLink(short_code):
    db = getdb()
    c = db.cursor()
    c.execute("DELETE FROM link WHERE link.short_url=?",(short_code,))
    db.commit()
    print("Suppresion du lien pour "+short_code)
    return

@app.route("/")
def main():
    return redirect("/display")

@app.route("/display")
def display():
    data = GetDisplayData()
    return render_template("display.html",liste = data)

@app.route("/display/delete/<string:short_code>")
def display_delete(short_code):
    DeleteLink(short_code)
    return redirect("/display")

@app.route("/add",methods=["GET","POST"])
def add():

    if request.method == "POST":
        url = request.form.get("target_url")
        code = request.form.get("short_code")

        db = getdb()
        c = db.cursor()

        c.execute("SELECT * FROM link WHERE link.long_url=? OR link.short_url=?",(url,code))

        x = c.fetchall()
        if x == [] and url!="" and code!="" and not("/" in code): # il n'y a pas eu de pb d'unicité

            c.execute("INSERT INTO link VALUES (?,?,?)",(url,code,0))
            db.commit()

            data = GetDisplayData()
            return render_template("add.html",liste = data, base_case=False,error=False)
        else :
            data = GetDisplayData()
            return render_template("add.html",liste = data, base_case=False,error=True)

    else :
        data = GetDisplayData()
        return render_template("add.html",liste = data, base_case=True,error=False)

@app.route("/add/delete/<string:short_code>")
def add_delete(short_code):
    DeleteLink(short_code)
    return redirect("/add")

def GenerateLink():

    db = getdb()
    c = db.cursor()

    SHORTCODE_LENGTH = 4;
    alphabet = string.ascii_letters + string.digits

    valide = False
    while not valide:
        short_code = ''.join(random.choice(alphabet) for i in range(SHORTCODE_LENGTH))
        print(short_code)
        c.execute("SELECT * FROM link WHERE link.short_url=?",(short_code,))
        x = c.fetchall()
        if x == []:
            valide = True
            print("Genere lien =" + short_code)
            break
        print("ECHEC GENERATION LIEN, NOUVELLE ESSAI")
        SHORTCODE_LENGTH+=1
    return short_code

@app.route("/shorten",methods=["GET","POST"])
def shorten():

    if request.method == "POST":

        target_url = request.form.get("target_url")
        
        db = getdb()
        c = db.cursor()

        c.execute("SELECT * FROM link WHERE link.long_url=?",(target_url,))
        x = c.fetchall()

        if x == [] and target_url!="":

            generated_link = GenerateLink()
            c.execute("INSERT INTO link VALUES (?,?,?)",(target_url,generated_link,0))
            db.commit()

            data = GetDisplayData()
            return render_template("shorten.html",liste=data,base_case=False,error=False)
        else:
            data = GetDisplayData()
            return render_template("shorten.html",liste=data,base_case=False,error=True)
    else :
        data = GetDisplayData()
        return render_template("shorten.html", liste = data,base_case=True,error=False)

@app.route("/shorten/delete/<string:short_code>")
def shorten_delete(short_code):
    DeleteLink(short_code)
    return redirect("/shorten")

@app.route("/r/<string:short_code>")
def redirection(short_code):
    print("Redirection grace au short_code = "+ short_code)

    db = getdb()
    c = db.cursor()

    c.execute("SELECT * FROM link WHERE link.short_url=?",(short_code,))
    x = c.fetchall()

    if x!=[]:

        c.execute("UPDATE link SET visite = ? WHERE long_url=?",(x[0][2]+1,x[0][0]))
        print("Nouveau nb visite = " + str(x[0][2]+1))
        db.commit()

        return redirect(x[0][0])
    else:
        return render_template("error.html",faux_lien=short_code)



    
