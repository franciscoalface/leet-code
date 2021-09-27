const reverseString = require("./reverse_string");

test("test example 1 -> (['h','e','l','l','o'])", () => {
	expect(reverseString(["h", "e", "l", "l", "o"])).toStrictEqual([
		"o",
		"l",
		"l",
		"e",
		"h",
	]);
});

test("test example 2 -> (['H','a','n','n','a','h'])", () => {
	expect(reverseString(["H", "a", "n", "n", "a", "h"])).toStrictEqual([
		"h",
		"a",
		"n",
		"n",
		"a",
		"H",
	]);
});
