const fizzBuzz = require("./fizz_buzz");

test("test example 1 -> (3)", () => {
	expect(fizzBuzz(3)).toStrictEqual(["1", "2", "Fizz"]);
});

test("test example 2 -> (5)", () => {
	expect(fizzBuzz(5)).toStrictEqual(["1", "2", "Fizz", "4", "Buzz"]);
});

test("test example 3 -> (15)", () => {
	expect(fizzBuzz(15)).toStrictEqual([
		"1",
		"2",
		"Fizz",
		"4",
		"Buzz",
		"Fizz",
		"7",
		"8",
		"Fizz",
		"Buzz",
		"11",
		"Fizz",
		"13",
		"14",
		"FizzBuzz",
	]);
});
