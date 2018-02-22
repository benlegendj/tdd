/**
 * Created by bendeh on 2/21/2018.
 */
const assert=require("chai").assert;
const myownlevels=require("../src/main.js");

describe("binary_converter", function () {
    it("should return binary equivalent of 5",function () {
        assert.equal(myownlevels.binary_converter(5), 101)
    })

    it("should return binary equivalent of 2",function () {
        assert.equal(myownlevels.binary_converter(5),10)
    })


})