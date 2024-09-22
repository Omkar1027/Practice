// console.log(null==0)
// console.log(null<0)
// console.log(null>0)

// const aId=123
// const bId=123
// console.log(aId===bId);

/*
console.log(typeof 1)
console.log(typeof "1")
console.log(typeof 59591n)
console.log(typeof true)
console.log(typeof null)
console.log(typeof undefined)
console.log(typeof Symbol)

let heros=[]
let none={}
let f=function(){}
console.log(typeof heros)
console.log(typeof none)
console.log(typeof f)
*/

/*
let a='omkar'
let b=a
b='Omkar'

console.table(a+b);

function f(){
    email:"omkadam"
}

let f2=f

f2.email="om"
console.log(f);
console.log(f2);
*/

/*
console.log(`Hello ny name is ${"Omkar Kadam"} and I am coding thorugh ${"Javascript"} now`);

let s= new String ("OmkarKadamSoCalled")
// console.log(typeof s, s);
const a=s.slice(-10,12)
console.log(a);

const str="Today is a beautiful day to start js"

const chars=str.split(' ')
console.log(chars[3])
*/

/*
let min=-555, max=1
console.log(Math.floor((Math.random()*(max-min+1)) + min));

let myD=new Date(2005,0,9, 0,41)
console.log(myD.toString());

let n=Date.toString()
console.log(n.getFullYear());
*/

/*
const abc=[1,2,[1,3],2,[2,[3]]]
console.log(abc.flat(2));

const mySym=Symbol("ok")
const obj={
    [mySym]:"ok",
    name:"oo"
}
console.log(typeof obj.mySym);
console.log(obj.name);

obj.greet=function(){
    console.log("Hello",obj.name);
}

console.log(obj.greet());

function greeting(name){
    if(!name){
        console.log("nahi hai name ");
        return
    }
    console.log("Hello",name);
}
greeting()
*/

const a=10
{
    const a=9
    console.log(a);
    function b(){
        console.log("99");     
    }    
}
console.log(b());

function aaa(){ let user = "om "
    console.log(this.user)}

(function a(){
    console.log("1")
})();
((name)=>(
    console.log(name)
))("om")