const longestCommonPrefix = require("./longest_common_prefix");

test.skip("test example 1 -> ['flower','flow','flight'] === 'fl'", () => {
	expect(longestCommonPrefix(["flower", "flow", "flight"])).toStrictEqual("fl");
});

test.skip("test example 2 -> ['dog','racecar','car'] === ''", () => {
	expect(longestCommonPrefix(["dog", "racecar", "car"])).toStrictEqual("");
});
