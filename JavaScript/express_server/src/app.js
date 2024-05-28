const express = require("express")
const app = express()
const port = 3000

let main_page = "<!DOCTYPE html><html><head><title>Acesso permitido</title><style>body {background: linear-gradient(to bottom, #FFFFFF, #94FAFF);display: flex;justify-content: center;align-items: center;height: 100vh;margin: 0;}h1 {text-align: center;}</style></head><body><h1>Acesso permitido</h1></body></html>";

app.get('/', (req, res) => {
    res.send(main_page)
})

app.listen(port, () => {
    console.log("Escutando na porta "+port)
})
