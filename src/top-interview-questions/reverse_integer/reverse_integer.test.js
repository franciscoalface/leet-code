const reverseInteger = require("./reverse_integer");

test("test example 1 -> (123)", () => {
	expect(reverseInteger(123)).toStrictEqual(321);
});

test("test example 2 -> (-123)", () => {
	expect(reverseInteger(-123)).toStrictEqual(-321);
});

test("test example 3 -> (120)", () => {
	expect(reverseInteger(120)).toStrictEqual(21);
});

test("test example 4 -> (0)", () => {
	expect(reverseInteger(0)).toStrictEqual(0);
});

test("test example 5 -> (1534236469)", () => {
	expect(reverseInteger(1534236469)).toStrictEqual(0);
});

test("test example 6 -> (-1534236469)", () => {
	expect(reverseInteger(-1534236469)).toStrictEqual(0);
});
