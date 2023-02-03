# **tellolib**

### **_To install:_**
```terminal
pip install tellolib
```
or

```terminal
pip3 install tellolib
```

### **[PyPI Link](https://pypi.org/project/tellolib/)**


---
### **Sample Code:**

```python
from tellolib import tello

tello = tello.Tello(1111) # 1111 specifies the UDP port that the server that communicates with the tello binds to

tello.connect() # connects to tello
tello.takeoff()
tello.forward(20)
tello.land()
```
---
