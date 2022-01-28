from flask import Flask , render_template ,url_for
app=Flask(__name__)

posts=[
    {
        "author":"Corey S",
        "title":"post 1",
        "content":"FIrst Post Content",
        "date":"April 20,2018"
        
    },
    {
        "author":"Corey S",
        "title":"post 2",
        "content":"Second Post Content",
        "date":"April 21,2018"
        
    }
]

#Route Decorators are a way to add addiitonal functionality to a function
@app.route("/") #Home Page of oour website
@app.route("/home")#multiple routes can point to same page
def hello():
    return render_template("home.html",posts=posts)

@app.route("/about")
def about():
    return render_template("about.html",title="about")


#This is only true if this script is run directly and not as a module

if __name__ == "__main__":
    app.run(debug=True)
    
