from DittinAIV2.dittin import DittinAI

while True:
    msg = input("You: ")

    dittin = DittinAI()
    response = dittin.chat(msg)
    print(response)