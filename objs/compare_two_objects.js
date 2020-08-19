function compareTwoObjects(obj1, obj2) {
  // write your code here
  const l1 = Object.keys(obj1)
  const l2 = Object.keys(obj2)

  if (l1.length != l2.length) return false

  for (let key in obj1) {
    if (!obj2[key]) return false
    if (obj1[key] != obj2[key]) return false
  }
  return true
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
