// ==========================
// Part 1: Variables & Conditionals
// ==========================
let username = "Hebron";
let age = 22;

if (age >= 18) {
  console.log(username + " is an adult.");
} else {
  console.log(username + " is a minor.");
}

// ==========================
// Part 2: Custom Functions
// ==========================
function greetUser(name) {
  console.log("Hello, " + name + "! Welcome to my project.");
}

function multiplyNumbers(a, b) {
  return a * b;
}

// Call the functions
greetUser(username);
console.log("Multiplication Result: " + multiplyNumbers(4, 5));

// ==========================
// Part 3: Loops
// ==========================

// For loop
let numbers = [1, 2, 3, 4, 5];
for (let i = 0; i < numbers.length; i++) {
  console.log("Number: " + numbers[i]);
}

// While loop
let count = 0;
while (count < 3) {
  console.log("While Loop Count: " + count);
  count++;
}

// ==========================
// Part 4: DOM Interactions
// ==========================

// 1. Change text when button clicked
document.getElementById("btnChangeText").addEventListener("click", function() {
  document.getElementById("main-title").textContent = "Text Changed with DOM!";
});

// 2. Add new item to list
document.getElementById("btnAddItem").addEventListener("click", function() {
  let newItem = document.createElement("li");
  newItem.textContent = "New Item added!";
  document.getElementById("myList").appendChild(newItem);
});

// 3. Display loop output inside a paragraph
let loopOutput = "";
for (let i = 1; i <= 5; i++) {
  loopOutput += "Count " + i + "<br>";
}
document.getElementById("loop-output").innerHTML = loopOutput;
