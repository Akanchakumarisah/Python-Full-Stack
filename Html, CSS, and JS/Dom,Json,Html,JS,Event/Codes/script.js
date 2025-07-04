const html = document.getElementsByTagName("p")
// for (let p of html) {
//     p.textContent = "Updated content"
// }

// console.log(paragraphs)
// paragraphs.textContent = "Updated content"

const bg_p1 = document.querySelector("#para1")
console.log(bg_p1)

const bg_p = document.querySelectorAll("p")
for (let b_p of bg_p) {
    b_p.style.backgroundColor = "yellow";
}

const parent = document.querySelector("#para1")
const first = parent.firstChild
const first_nodeName = parent.firstChild.nodeName
console.log(first)
console.log(first_nodeName)

const element = document.querySelector("p")
const idval = element.getAttribute("id")
console.log(idval)

const element1 = document.querySelector("span")
element1.setAttribute("class", "span_Class")