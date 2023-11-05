from flask import Flask, render_template, Response
import matplotlib.pyplot as plt
import io
import random
import time
import matplotlib

matplotlib.use('agg')

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    # return render_template('index.html')
    return render_template('index.html')

def generate_plot():
    # fig, ax = plt.subplots()
    plt.figure(figsize=(16, 8))
    data = []
    x = []
    for i in range(100):
        data.append(random.randint(0, 100))
        x.append(i + 1)
        # ax.clear()
        plt.xlim([0, 100])
        plt.ylim([0, 100])
        plt.plot(x, data)
        plt.xlabel('Time')
        plt.ylabel('Data')
        plt.title('Real-Time Data Plot')
        plt.draw()

        # Convert the Matplotlib plot to a bytes object
        output = io.BytesIO()
        plt.savefig(output, format='png')
        output.seek(0)
        yield (b'--frame\r\n'
               b'Content-Type: image/png\r\n\r\n' + output.read() + b'\r\n')
        plt.close()

        # Sleep for a second to simulate real-time updates
        time.sleep(1)

@app.route('/plot')
def plot():
    return Response(generate_plot(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    # app.run(debug=True)
    app.run()
