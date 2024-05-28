const express = require('express')
const app = express()
const port = 3000


// Garante que os dados de POST venham em formato JSON
app.use(express.json())


let data = { 'materials': [] }


// GET geral
app.get('/materials', (req, res) => {
    res.json(data)
})


// GET específico
app.get('/materials/:id', (req, res) => {
    let materialId = parseInt(req.params.id)
    
    let found = data.materials.find(material => material.id === materialId)
    
    if (found) {
        res.json(found)
    } else {
        res.status(404).json({ "message": `Material ${materialId} não encontrado` })
    }
})


// POST para criação de material
app.post('/materials', (req, res) => {
    let newMaterial = req.body
    
    newMaterial.id = data.materials.length
    data.materials.push(newMaterial)
    
    res.status(201).json({ "message": `Material ${newMaterial.id} criado com sucesso` })
})


// DELETE material
app.delete('/materials/:id', (req, res) => {
    let materialId = parseInt(req.params.id)
    let initialLength = data.materials.length

    data.materials = data.materials.filter(material => material.id !== materialId)

    if (data.materials.length < initialLength) {
        res.json({ "message": `Material ${materialId} removido com sucesso` })
    } else {
        res.status(404).json({ "message": `Material ${materialId} não encontrado` })
    }
})


// PUT material
app.put('/materials/:id', (req, res) => {
    let newMaterial = req.body
    newMaterial.id = parseInt(req.params.id)
    let found = false

    data.materials = data.materials.map(material => {
        if (material.id === newMaterial.id) {
            found = true
            return { ...material, ...newMaterial }
        } else {
            return material
        }
    })

    if (found) {
        res.json({ "message": `Material ${newMaterial.id} atualizado com sucesso` })
    } else {
        res.status(404).json({ "message": `Material ${newMaterial.id} não encontrado` })
    }
})


app.listen(port, () => {
    console.log(`Servidor escutando na porta ${port}`)
})
