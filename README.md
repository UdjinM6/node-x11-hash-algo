node-x11-hash-algo
===============

x11 hashing algorithm for node.js

Usage
-----

Install

```bash
npm install node-x11-hash-algo
```

```javascript
var x11 = require('node-x11-hash-algo');

var darkcoinGenesisBlock = new Buffer("010000000000000000000000000000000000000000000000000000000000000000000000c762a6567f3cc092f0684bb62b7e00a84890b990f07cc71a6bb58d64b98e02e0dee1e352f0ff0f1ec3c927e6", 'hex');

var hashedData = x11.hash(darkcoinGenesisBlock);

console.log(hashedData); //<SlowBuffer 2c bc f8 3b 62 91 3d 56 f6 05 c0 e5 81 a4 88 72 83 94 28 c9 2e 5e b7 6c d7 ad 94 bc af 0b 00 00>
console.log(hashedData.toString('hex')); //2cbcf83b62913d56f605c0e581a48872839428c92e5eb76cd7ad94bcaf0b0000


```

Credits
-------
* [Keccak](http://en.wikipedia.org/wiki/Keccak) - Guido Bertoni, Joan Daemen, Michaël Peeters, and Gilles Van Assche
* [Skein](http://en.wikipedia.org/wiki/Skein_(hash_function)) - Bruce Schneier, Stefan Lucks, Niels Ferguson, Doug Whiting, Mihir Bellare, Tadayoshi Kohno, Jon Callas and Jesse Walker.
* [BLAKE](http://en.wikipedia.org/wiki/BLAKE_(hash_function)) - Jean-Philippe Aumasson, Luca Henzen, Willi Meier, and Raphael C.-W. Phan
* [Grøstl](http://en.wikipedia.org/wiki/Gr%C3%B8stl) - Praveen Gauravaram, Lars Knudsen, Krystian Matusiewicz, Florian Mendel, Christian Rechberger, Martin Schläffer, and Søren S. Thomsen
* [X11](http://www.darkcoin.io/) - Evan Duffield
