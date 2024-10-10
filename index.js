
const uncompress = (s) => {

    let result = [];
    let i = 0, j = 0;


    while (j < s.length) {
        if (isInteger(s[j])) {
            j += 1;
        } else {
            const num = Number(s.slice(i, j));
            for (let count = 0; count < num; count++) {
                result.push(s[j]);
            }
            j += 1;
            i = j;
        }
    }

    return result.join("");
};

function isInteger(s) {
    let code = s.charCodeAt();
    if (code <= 57 && code >= 48) {
        return true;
    }
    return false;
}

console.log(uncompress("2c3a1t")); // -> 'ccaaat'
console.log(uncompress("4s2b")); // -> 'ssssbb'
console.log(uncompress("2p1o5p")); // -> 'ppoppppp'
console.log(uncompress("3n12e2z")); // -> 'nnneeeeeeeeeeeezz'
