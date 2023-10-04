// получаем значение из локального хранилища браузера (если оно есть)
let nick = localStorage.getItem("login") 
// если не нашли значение, то запрашиваем и сохраняем
if(!nick)
{
    nick = prompt("Введите ваш логин")
    localStorage.setItem("login", nick)
}


let login = document.querySelector(".login")

login.textContent = "Логин: " + nick

let count = localStorage.getItem("count") 
if(!count)
{
    count = 0
}
let points = document.querySelector(".points")

let but = document.querySelector(".but")
//  меняем css нашей кнопки
// расположение в формате относительно экрана
but.style.position = 'absolute'

function Click()
{
    count += 1
    localStorage.setItem("count", count)
    points.textContent = "Очки: " + count

    let maxX = window.innerWidth - 100
    let maxY = window.innerHeight - 50
    // Math.random() - случайное число от 0 до 1
    let newX = Math.random() * maxX
    let newY = Math.random() * maxY
    // меняем расположение на новое
    but.style.left = newX + 'px'
    but.style.top = newY + 'px'
}
function Restart()
{
    localStorage.clear()
}