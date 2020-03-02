![PyPI](https://img.shields.io/pypi/v/pybase24)
![GitHub](https://img.shields.io/github/license/mildmelon/pybase24?style=flat)

# Base24 encode/decoder for Python

Encoder and decoder for the [Base24 encoding](https://www.kuon.ch/post/2020-02-27-base24/),
python implementation of https://github.com/kuon/java-base24

## Usage

Install with pip:
```
$ pip install pybase24
```

Example:
```python
from pybase24 import encode24, decode24


data = b'my test data'  # Length of bytes must be a multiple of 4

enc_data = encode24(data)
print(enc_data)  # 'G67S97T4WR2XEP4STZYE8'

dec_data = decode24(enc_data)
print(dec_data)  # bytearray(b'my test data')

assert data == dec_data  # True
```

## License

Licenses under the MIT License (LICENSE-MIT or http://opensource.org/licenses/MIT)
