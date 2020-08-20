function compareTwoObjects(obj1, obj2) {
  // write your code here
  for (let key in obj1) {

  }
}

// Test cases to verify
// true
// const a = { a: 1, b: 2 };
// const b = { a: 1, b: 2 };
// console.log(compareTwoObjects(a, b))
// true
// const a = { b: 2, a: 1 };
// const b = { a: 1, b: 2 };
// console.log(compareTwoObjects(a, b))

// false
// const a = { a: 100, b: 2 };
// const b = { a: 1, b: 2 };
// console.log(compareTwoObjects(a, b))

// // // // false
// const a = { a: 1, b: 2, c: 3 };
// const b = { a: 1, b: 2 };
// console.log(compareTwoObjects(a, b))

// false
const a = { a: 1, b: 2, c: { d: 4, e: 5 } };
const b = { a: 1, b: 2, c: { d: 4, e: 5 } };
console.log(compareTwoObjects(a, b))
