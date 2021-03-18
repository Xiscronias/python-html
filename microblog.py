from flask import Flask

app = Flask("microblog")

#comenta aqui corno
@app.route("/")
def index ():
     return "natalia amor mamada aqui pfv (￣▽￣)" 

app.run()