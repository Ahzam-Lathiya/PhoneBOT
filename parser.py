from rasa_nlu.model import Interpreter

def predict_intent(text):
    interpreter = Interpreter.load('./models/nlu/default/bot')
    print(interpreter.parse(text))

xstr=input("Enter: ")
predict_intent(xstr)
