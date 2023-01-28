
    const https = require('https');
    const agent = new https.Agent({
    rejectUnauthorized: false
    })

    const getBridge = () => {
    fetch('/api/-5aynpcBEYsHNqEcjNPstao7i80FqcBSlo5bqCyj/groups/1', { 
        mode: 'cors',
        headers: { 'Access-Control-Allow-Origin': '*' }
    })
        .then(req => req.json())
        .then(res => {
        console.log(res)
        })
    }

    const toggleDesk = (foo) => {
    fetch('http://192.168.2.100/api/-5aynpcBEYsHNqEcjNPstao7i80FqcBSlo5bqCyj/lights/10/state', { 
        method: 'PUT',
        mode: 'cors',
        headers: {
            'Access-Control-Allow-Origin': '*',
            'Content-Type': 'application/json'
            },
        body: JSON.stringify(foo),
        json: true
        })
    }

    const off = {"transitiontime":0, "bri":255, "on": false}
    const on = {"transitiontime":0, "bri":255, "on": true}

    toggleDesk(off)


