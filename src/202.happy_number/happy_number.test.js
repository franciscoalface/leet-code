const happyNumber = require("./happy_number");

test("test example 1 -> (19)", () => {
	expect(happyNumber(19)).toStrictEqual(true);
});

test("test example 2 -> (2)", () => {
	expect(happyNumber(2)).toStrictEqual(false);
});
