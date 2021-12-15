
const str = "https://www.google.com/search?q="

function getInputValue(){

let inputVal = document.getElementById("myInput").value;
console.log(inputVal+' '+"search");
let Fsearch = str+inputVal
console.log(Fsearch);
location.href =Fsearch

}