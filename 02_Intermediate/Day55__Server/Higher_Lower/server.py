from flask import Flask
import random

app = Flask(__name__)
random_number = random.randint(0, 9)

@app.route('/')
def home():
    return '''
        <h1>Devinez un nombre entre 0 et 9</h1>
        <img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExOWJmaXkwbzM4aWFsMGx1M3hhZTFxY3BhZTh5eXM2N2w0a3d3eDhrYSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/HMpD1QeiWf61PBE3AN/giphy.gif">
        '''

@app.route('/<int:guess>')
def guess_number(guess):
    if guess < random_number:
        return '''
            <h1 style="color:blue;">{} est trop bas !</h1>
            <img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExemNieGpmM2U4MGozM2hzNDlpZ255cDZ3MjlydmxiaXp4MThkZzQxZCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/QnMJm9bVR9nDa/giphy.gif">
        '''.format(guess)
    elif guess > random_number:
        return '''
            <h1 style="color:red;">{} est trop haut !</h1>
            <img src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExamkwaTEwcXM5Z21ibXBxd3RxaWkwazUzdHhldG4ycXphOHg2MWt2YiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/PK1YQhAoBOpP2/giphy.gif">
        '''.format(guess)
    else:
        return '''
            <h1 style="color:green;">{} est parfait !</h1>
            <img src="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExdmhnd25nZ2ZoZGpkazIycjIwdG9sbnl6YnkzN25xZG5yanh6ZHJ5dyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/cWHzCmm1528Ks/giphy.gif">
        '''.format(guess)
    
if __name__ == "__main__":
    app.run(debug=True)