function sumZero(arr) {
    let left = 0;
    let right = arr.length - 1;

    while (right > left) {
        let sum = arr[left] + arr[right];
        if (sum > 0) {
            --right;
        } else if (sum < 0) {
            ++left;
        } else {
            return [arr[left], arr[right]];
        }
    }

}


console.log(

    sumZero([-4, -3, -2, -1, 0, 1, 2, 5])
);