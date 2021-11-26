import userService from '../services/user.js'


class User{
    login(req, res){
        console.log(req.body)
    }
}


export default new User()