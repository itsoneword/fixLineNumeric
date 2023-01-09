# fixLineNumeric
Python solution helping to delete numeric of each line


The code will modify this:
```python
 42# Enable logging
 43logging.basicConfig(
 44    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
 45)
 46logger = logging.getLogger(__name__)
 47
 48GENDER, PHOTO, LOCATION, BIO = range(4)
 ```
 
 into this:
 ```python
 # Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

GENDER, PHOTO, LOCATION, BIO = range(4)

 ```
 
 
