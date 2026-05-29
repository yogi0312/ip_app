const express = require('express');
const os = require('os');
const dns = require('dns');

const app = express();
const port = 5000;

app.get('/', (req, res) => {
  const hostname = os.hostname();
  dns.lookup(hostname, (err, address) => {
    if (err) {
      return res.status(500).json({ error: 'Unable to resolve IP address' });
    }
    res.json({ message: `The IP address is: ${address}` });
  });
});

app.get('/greet', (req, res) => {
  res.json({ message: 'Hi how are you' });
});

app.listen(port, '0.0.0.0', () => {
  console.log(`Server is running on http://0.0.0.0:${port}`);
});
