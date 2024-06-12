const http = require("http");
const fs = require('fs').promises;
 
const host = 'localhost';
const port = 8000;

const requestListener = function (req, res) {
    fs.readFile(__dirname + "/index.html")
    .then(contents => {
        res.setHeader("Content-Type", "text/html");
        res.writeHead(200);
        res.end(contents);
    })
    .catch(err => {
        res.writeHead(500);
        res.end(err);
        return;
    });
};

const server = http.createServer(requestListener);
server.listen(port, '192.168.1.143', () => {
    console.log(`Server is running on http://${host}:${port} 192.168.1.143:8000`);
});