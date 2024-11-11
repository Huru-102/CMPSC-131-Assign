#----------------------------------------------------------
# Name: Hunter Ruch
# E-mail Address: hdr5114@psu.edu
# Class: CMPSC 131 Section
# Lab #:7
#----------------------------------------------------------

def main():
    
    numList = list(randomizer()) ##generates initial list
    print(f'Here is the list: {numList}')
    print()

    ##accumulator variables defined
    totalLesser = 0 
    totalGreater = 0

    num = int(input('what number should I add to the list? '))
    
    if num in numList:   ##check for number input being in list
        print(f'{num} is already in the list')
    else:
        numList.append(num)
        print(f'adding {num}...')
        print(f'Here is the revised list: {numList}')
        print()

    num_terms = len(numList)

    averageL = average(numList, num_terms) ##calculates  average
    print(f'Average is: {averageL:.2f}')
    
    for index in range(0, num_terms): ##tally counter for whether a number is greater or lesser than the average
        if (numList[index] > averageL):
            totalGreater += 1
        elif (numList[index] < averageL):
            totalLesser += 1
    
    print(f'There are {totalGreater} numbers above the average.')
    print(f'There are {totalLesser} numbers below the average.')


def randomizer():
    import random
    num_terms = 10
    list1 = [0] * num_terms
    
    for index in range(0, 10):
        list1[index] = int(random.randint(1, 100))

    return list1
    
def average(list1, totalNum):
    total = 0
    
    for index in range(0, totalNum):
        total += float(list1[index])

    average = total / totalNum
    
    return average

main()
