const http = require('http');

const PORT = 3000;
const HOST = '127.0.0.1';

const server = http.createServer((req, res) => {
    res.writeHead(200, {
        'Content-Type': 'text/plain'
    });

    res.end('Day 9 - Node.js EC2 Server is Running!\n');
});

server.listen(PORT, HOST, () => {
    console.log(`Server running at http://${HOST}:${PORT}`);
});
