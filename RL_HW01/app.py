from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    # if request.method == 'POST':
    #     n = int(request.form['n'])
    # return render_template('square.html', n=n)

    if request.method == 'POST':
        n = int(request.form['n'])
        if n < 3 or n > 10:
            return render_template('index.html', error='n must be between 3 and 10')
        return render_template('square.html', n=n)
    else:
        return render_template('index.html')

@app.route('/startGame', methods=['GET', 'POST'])
def startGame():
    # Initialize environment
    if request.method == 'POST':
        n = int(request.form['n'])
        startPos = str(request.form['startPos'])
        startX = startPos.split(",", 1)[0]
        startY = startPos.split(",", 1)[1]
        endPos = str(request.form['endPos'])
        endX = endPos.split(",", 1)[0]
        endY = endPos.split(",", 1)[1]
        blockPos = str(request.form['blockPos'])
        # blockX=[blockPos[0],blockPos[4],blockPos[8]]
        # blockY=[blockPos[0],blockPos[4],blockPos[8]]
        blockX_1 = blockPos[0]
        blockY_1 = blockPos[2]
        blockX_2 = blockPos[4]
        blockY_2 = blockPos[6]
        blockX_3 = blockPos[8]
        blockY_3 = blockPos[10]

    p = subprocess.run(
        [
            'python', 'run_this.py',
            '--n',str(n),
            '--startX',startX,
            '--startY',startY,
            '--endX',endX,
            '--endY',endY,
            '--blockX_1',blockX_1,
            '--blockY_1',blockY_1,
            '--blockX_2',blockX_2,
            '--blockY_2',blockY_2,
            '--blockX_3',blockX_3,
            '--blockY_3',blockY_3,

        ]
    )
    return render_template('square.html', n=n)

if __name__ == '__main__':
    app.run(debug=True)
