function sortedFrequency(arr, x) {
    let numsFirst = findNums(arr, x)
    if (numsFirst == -1) return numsFirst;
    let numsLast = findNumsEnd(arr, x)
    return numsLast - numsFirst +1;
}

function findNums(arr, x, low = 0, high = arr.length -1){
    if(high >=low){
        let mid = low +Math.floor((high+low)/2)
        if ((mid === 0 || x > arr[mid -1]) && arr[mid] ===0){
        return mid;
        }else if(x >arr[mid]){
        return findNums(arr,mid +1,high)
        }
        return findNums(arr,low,mid-1)
    }
    return -1;
}

function findNumsEnd(arr, x, low = 0, high = arr.length -1){
    if(high >=low){
        let mid = low +Math.floor((high+low)/2)
        if ((mid === arr.length -1 || x < arr[mid +1]) && arr[mid] ===x){
        return mid;
        }else if(x<arr[mid]){
        return findNums(arr,mid +1,high)
        }
        return findNums(arr,low,mid-1)
    }
    return -1;
}

module.exports = sortedFrequency