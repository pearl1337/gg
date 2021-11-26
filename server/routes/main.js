import { Router } from 'express'
import userController from '../controllers/user.js'

const router = new Router()


router.post('/login', userController.login)


export default router