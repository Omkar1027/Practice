// // console.log(null==0)
// // console.log(null<0)
// // console.log(null>0)

// // const aId=123
// // const bId=123
// // console.log(aId===bId);

// /*
// console.log(typeof 1)
// console.log(typeof "1")
// console.log(typeof 59591n)
// console.log(typeof true)
// console.log(typeof null)
// console.log(typeof undefined)
// console.log(typeof Symbol)

// let heros=[]
// let none={}
// let f=function(){}
// console.log(typeof heros)
// console.log(typeof none)
// console.log(typeof f)
// */

// /*
// let a='omkar'
// let b=a
// b='Omkar'

// console.table(a+b);

// function f(){
//     email:"omkadam"
// }

// let f2=f

// f2.email="om"
// console.log(f);
// console.log(f2);
// */

// /*
// console.log(`Hello ny name is ${"Omkar Kadam"} and I am coding thorugh ${"Javascript"} now`);

// let s= new String ("OmkarKadamSoCalled")
// // console.log(typeof s, s);
// const a=s.slice(-10,12)
// console.log(a);

// const str="Today is a beautiful day to start js"

// const chars=str.split(' ')
// console.log(chars[3])
// */

// /*
// let min=-555, max=1
// console.log(Math.floor((Math.random()*(max-min+1)) + min));

// let myD=new Date(2005,0,9, 0,41)
// console.log(myD.toString());

// let n=Date.toString()
// console.log(n.getFullYear());
// */

// /*
// const abc=[1,2,[1,3],2,[2,[3]]]
// console.log(abc.flat(2));

// const mySym=Symbol("ok")
// const obj={
//     [mySym]:"ok",
//     name:"oo"
// }
// console.log(typeof obj.mySym);
// console.log(obj.name);

// obj.greet=function(){
//     console.log("Hello",obj.name);
// }

// console.log(obj.greet());

// function greeting(name){
//     if(!name){
//         console.log("nahi hai name ");
//         return
//     }
//     console.log("Hello",name);
// }
// greeting()
// */

// /*
// const a=10
// {
//     const a=9
//     console.log(a);
//     function b(){
//         console.log("99");     
//     }    
// }
// console.log(b());

// function aaa(){ let user = "om "
//     console.log(this.user)}

// (function a(){
//     console.log("1")
// })();
// ((name)=>(
//     console.log(name)
// ))("om")

// sum =function(){

// }
// */

// const map = new Map()
// map.set('IN', "India")
// console.log(map);

// for (const [key,value] of map){
// console.log(key,"->",value)
// }
// const aa={
//     a:'nine',
//     b:'ten'
// }
// console.log(Object.values(aa));
// const {a:ba}=aa

// const books = [
//     { title: 'Book One', genre: 'Fiction', publish: 1981, edition: 2004 },
//     { title: 'Book Two', genre: 'Non-Fiction', publish: 1992, edition: 2008 },
//     { title: 'Book Three', genre: 'History', publish: 1999, edition: 2007 },
//     { title: 'Book Four', genre: 'Non-Fiction', publish: 1989, edition: 2010 },
//     { title: 'Book Five', genre: 'Science', publish: 2009, edition: 2014 },
//     { title: 'Book Six', genre: 'Fiction', publish: 1987, edition: 2010 },
//     { title: 'Book Seven', genre: 'History', publish: 1986, edition: 1996 },
//     { title: 'Book Eight', genre: 'Science', publish: 2011, edition: 2016 },
//     { title: 'Book Nine', genre: 'Non-Fiction', publish: 1981, edition: 1989 },
//   ];


// const UserBooks=books.filter(pb => {return pb.publish<1999});
// console.log(UserBooks);


setInterval(function(){
    for(i=0;i<99;i++){
        console.log(i)
    }
}, 1000)

