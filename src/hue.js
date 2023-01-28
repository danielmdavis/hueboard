
    import { useState } from 'react';

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

    const toggleDesk = (body) => {
    fetch('http://192.168.2.100/api/-5aynpcBEYsHNqEcjNPstao7i80FqcBSlo5bqCyj/lights/10/state', { 
        method: 'PUT',
        mode: 'cors',
        headers: {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': '*',
            'Content-Type': 'application/json'
            },
        body: JSON.stringify(body),
        json: true
        })
    }

    const off = {"transitiontime":0, "bri":255, "on": false}
    const on = {"transitiontime":0, "bri":255, "on": true}

    


    export default function App() {

        const [keyPressed, setKeyPressed] = useState(false)
        toggleDesk(off)
        function handleKeyPress(e) {
            let key = e.key
            console.log('foo')
            if (keyPressed === false || key == '0') { 
                toggleDesk(on)
                setKeyPressed(true) 
            }
            else if (keyPressed === true || key == '0') { 
                toggleDesk(off)
                setKeyPressed(false) 
            }
        }



        return (
            <div >
                <input type="text" onKeyPress={(e) => handleKeyPress(e)} />
            </div>
        )
    }