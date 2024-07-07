/**
 * @param {number} n
 * @return {function} counter
 */
var createCounter = function (n) {
    return () => n++;
};