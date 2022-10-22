from flask import Flask, request,render_template
import CodeTest_python 


app = Flask(__name__)

@app.route("/codetest", methods=['GET', 'POST'])
def route_codetest_main():
    try:
        request.form["VDB"]
        VDB = True
    except Exception as e:
        VDB = False
    
    result,answer,RC,codecoler,variable_timechange = CodeTest_python.M_264910_test(request.form["inputcode"],request.form["testcase"],VDB)
    return render_template('CodeTest/CT_main.html',\
    message_result = result , \
    message_answer = answer , \
    message_code = RC , \
    message_codecolor = codecoler , \
    message_variable_timechange = variable_timechange, \
    save = {"inputcode" : request.form["inputcode"] , \
            "testcase" : request.form["testcase"] , \
            "cols" : request.form["colsSlider"] , \
            "row" : request.form["rowSlider"]})

@app.route('/', methods=['GET', 'POST'])
def form():
    return render_template('CodeTest/CT_main.html',message = "",\
        message_code = None , \
        message_codecolor = None , \
        message_variable_timeChange = None , \
        save = {"inputcode" : "", \
            "testcase" : "" , \
            "cols" : 100 , \
            "row" : 10})

# アプリケーションを動かすためのおまじない
if __name__ == "__main__":
    app.run(port = 8000, debug=True)