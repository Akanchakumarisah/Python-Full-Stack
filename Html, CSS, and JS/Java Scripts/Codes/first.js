// var num1 = 20
// let age = 25
// const PI = 3.14

// // console.log(num1)
// // console.log(age)
// // console.log(PI)
// //

// let globalvar = 28
// let x
// console.log(x)

// // function exmaple() {
// //     const localvar = 89
// //     console.log(globalvar);
// //     console.log(localvar);
// // }

// // exmaple();
// // console.log(localvar);

// let str = "hi"
// let num = 24.4
// let bool = false
// let nul = null
// let sym = Symbol("ASHU")
// let bigNum = 12345678901234567890n

// let nums = [1, 2, 3, 4, 5, 6]
// let numss = [7, 8, 9, 10]
// console.log(nums.concat(numss))

// // spread Operator {...}

// let f1 = ["football", "basketball"];
// let f2 = ["goal", "Basket"];

// console.log([...f1, ...f2])
// // console.log(f3)

// let a = nums.toString()
// console.log(a[1]) //123456
// console.log(typeof (a))

const person = {
    name: "rahul",
    age: 25
}

console.log(person.age)
person.job = "Developer"
console.log(person)

const key = "id"
const user = {
    name: "jhon",
    [key]: 123, 
}
console.log(user.id)