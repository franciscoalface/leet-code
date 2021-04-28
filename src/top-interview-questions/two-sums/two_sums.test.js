const twoSum = require("./two_sum");

test("test example 1 -> ([2, 7, 11, 15], 9)", () => {
	expect(twoSum([2, 7, 11, 15], 9)).toStrictEqual([0, 1]);
});

test("test example 2 -> ([3, 2, 4], 6)", () => {
	expect(twoSum([3, 2, 4], 6)).toStrictEqual([1, 2]);
});

test("test example 3 ([3, 3], 6)", () => {
	expect(twoSum([3, 3], 6)).toStrictEqual([0, 1]);
});
