// function calulateArea(width, height) {
//     return (width <=0 || height <=0 ) ? (`Invaild ${width} and ${height}`) : (width*height )
// }

// console(calulateArea(4, 3))
// console.log(calulateArea(4, 0))

const creatmsg = function (msg, pre = "info") { 
    return `[${pre}] ${msg}`;
}

console.log(creatmsg("login success", "CHORES"));