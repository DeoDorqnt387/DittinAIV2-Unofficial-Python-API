### An Unofficial api for DittinAIV2
![](https://github.com/DeoDorqnt387/DittinAIV2-Unofficial-Python-API/blob/main/images/img1.png)
## Example Usage
```python
from ..DittinAIV2.dittin import DittinAI

while True:
    msg = input("You: ")

    dittin = DittinAI()
    response = dittin.chat(msg)
    print(response)
```

## Prerequisites
> Rename the file .env.expl to .env.

> Use pip install -r requirements.txt to install the required dependencies
