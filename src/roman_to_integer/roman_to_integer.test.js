const romanToInt = require("./roman_to_integer");

test.skip("test example 1 -> III === 3", () => {
	expect(romanToInt("III")).toStrictEqual(3);
});

test.skip("test example 2 -> IV === 4", () => {
	expect(romanToInt("IV")).toStrictEqual(4);
});

test.skip("test example 3 -> IX === 9", () => {
	expect(romanToInt("IX")).toStrictEqual(9);
});

test.skip("test example 4 -> LVIII === 58", () => {
	expect(romanToInt("LVIII")).toStrictEqual(58);
});

test.skip("test example 5 -> MCMXCIV === 1994", () => {
	expect(romanToInt("MCMXCIV")).toStrictEqual(1994);
});
