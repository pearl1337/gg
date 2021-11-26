import express from 'express'
import config from './config.js'
import router from './routes/main.js'
import bodyParser from 'body-parser'

const app = express()

app.use(bodyParser.urlencoded({ extended: false }))
app.use(router)

app.listen(config.PORT, (err)=> {
    console.log("Server has been started on port" + config.PORT)
})