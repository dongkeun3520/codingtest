def solution(numbers, target):
    answer = 0
    array = [[numbers[0], 0], [-1 * numbers[0], 0]]
    n = len(numbers)
    while array:
        # for i in range(1,len(numbers)):
        temp, index = array.pop()
        index += 1
        if index < n:
            array.append([temp + numbers[index], index])
            array.append([temp - numbers[index], index])
        else:
            if temp == target:
                answer += 1

    return answer
