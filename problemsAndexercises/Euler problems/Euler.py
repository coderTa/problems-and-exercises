# Problem 1

def p1():
        total_sum_3 = 0
        total_sum_5 = 0
        total_sum_15 = 0

        for i in range(0, 1000, 3):
                print(i)

        total_sum_3 += i

        for i in range(0, 1000, 5):
                print(i)

        total_sum_5 += i

        for i in range(0, 1000, 15):
                print(i)

        total_sum_15 += i

        print(total_sum_3)
        print(total_sum_5)
        print(total_sum_15)

        total_total_sum = total_sum_3 + total_sum_5 - total_sum_15

        print(total_total_sum)

# Problem 2

def p2():
        num = 1
        num_previous = 1
        num_sum = 0

        while num + num_previous < 4000000:
                temp_num = num    
                num = num + num_previous
                num_previous = temp_num
                print(num)

        if num % 2 == 0:
                num_sum += num

        print(num)
        print(num_sum)


# Problem 3

def p3():
        import math

        big_num = 600851475143
        sqrt_num = math.sqrt(big_num)

        lst_nums = []

        for i in range(1, int(sqrt_num)):
                if big_num % i == 0:
                        lst_nums.append(i)
                        print(lst_nums)

        print(lst_nums)

        for f in lst_nums:
                is_prime = True

                for i in range(2, int(math.sqrt(f))):
                        if f % i == 0:
                                is_prime = False
                
                if is_prime == True:
                        print(f)


# Problem 4

#string_test = "hello"
#print(string_test[0])
#print(string_test[::-1])

def p4():
        num_1 = 100
        num_2 = 100
        counter_1 = 1
        counter_2 = 1

        palindrome = 0

        for i in range(900):
                while num_1 + counter_1 < 1000:
                        num_1 += counter_1
                        mult_1 = str(num_1 * num_2)

                        if mult_1 == mult_1[::-1] and int(mult_1) > palindrome:
                                palindrome = int(mult_1)
                                max_1 = num_1
                                max_2 = num_2

                num_1 = 100
                num_2 += 1

        print(palindrome)
        print(max_1, max_2)

# Problem 5

import time

def p5_a():
        temp_small_num = 2520

        start = time.time()

        while True:
                loop_counter = 0

                for i in range(20):
                        if temp_small_num % (i + 1) == 0:
                                continue
                        else:
                                break 
                        
                        loop_counter += 1
                
                if loop_counter == 20:
                        answer = temp_small_num
                        return answer
                else:
                        temp_small_num += 2520
                        #print(temp_small_num)
                
                if temp_small_num % (2520) == 0:
                        print(time.time() - start, temp_small_num)


#print(p5_a())

import math

def is_prime(num):
        if num == 1:
                return False 
        elif num == 2:
                return True

        for i in range(int(math.sqrt(num))):
                if (num % (i + 2)) == 0:
                        return False

        return True

def prime_factor(num):
        prime_list = []
        prime_dict = {}

        for i in range(num):
                if is_prime(i + 1):
                        print("Found prime %s" % (i + 1))
                        prime_list.append(i + 1)
                        p = 0
        
                        while num % ((i + 1) ** p) == 0:
                                p += 1

                        prime_dict[i + 1] = p - 1
        
        return prime_dict
        
def p5_b():
        prime_list = []
        big_primes = {}

        for i in range(20):
                prime_list.append(prime_factor(i + 1))

        for i in range(len(prime_list)):
                d = prime_list[i]

                for key in d.keys():
                        if key in big_primes and d[key] > big_primes[key]:
                                big_primes[key] = d[key]
                        elif key not in big_primes:
                                big_primes[key] = d[key]

        counter = 1

        for i in big_primes.keys():
                v = i ** big_primes[i]
                counter *= v

        return counter


#print(p5_b())

# Problem 6

def p6():
        total_1 = 0

        for i in range(100):
                total_1 += (i + 1) ** 2
        
        total_2 = 0

        for i in range(100):
                total_2 += i + 1
        
        total_2 = total_2 ** 2

        answer = total_2 - total_1
        print(answer)

#print(p6())

# Problem 7

def p7():
        current_num = 1
        c = 0

        while c != 10001:

                current_num += 1

                if is_prime(current_num) == True:
                        c += 1
                
        return current_num

#print(p7())

# Problem 8

thousand_num = """73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450""".replace("\n", "")

def p8():
        largest_product = 0

        for i in range(1000 - 12):
                current_product = 1
                sub_sect = thousand_num[i : i + 13]
                
                for j in range(13):
                        current_product *= int(sub_sect[j])
                
                if current_product > largest_product:
                        largest_product = current_product

        return largest_product
                
#print(p8())

# Problem 9
# Solved

# Problem 10

def p10():
        total_primes = 0

        for i in range(2000000):
                if is_prime(i + 1):
                        total_primes += i + 1 
                #print(i)
        
        return total_primes

#print(p10())

# Problem 11

grid = """08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48
""".splitlines()

def p11():
        for i in range(len(grid)):
                grid[i] = grid[i].split(" ")

        #print(grid)

        largest_quad = 0

        for r in range(len(grid)):
                for c in range(len(grid) - 3):
                        section = grid[r][c : c + 4]
                        product = 1

                        for t in section:
                                product *= int(t)

                        if product > largest_quad:
                                largest_quad = product

        for c in range(len(grid[0])):
                for r in range(len(grid[0]) - 3):
                        product = 1

                        for i in range (4):
                                element = grid[r + i][c]
                                product *= int(element)

                        if product > largest_quad:
                                largest_quad = product
        
        for r in range(len(grid) - 3):
                for c in range(len(grid) - 3):
                        product = 1

                        for i in range(4):
                                product *= int(grid[r + i][c + i])
                        
                        if product > largest_quad:
                                largest_quad = product

        for r in range(3, len(grid)):
                for c in range(len(grid) - 3):
                        product = 1

                        for i in range(4):
                                product *= int(grid[r - i][c + i])
                        
                        if product > largest_quad:
                                largest_quad = product

        return largest_quad

#print(p11())

# Problem 12

def p12():
        current_tri = 28
        counter = 8
        largest_fact = 6

        while largest_fact < 500:
                current_tri += counter
                counter += 1
                current_facts = 0

                for i in range(int(math.sqrt(current_tri))):
                        if current_tri % (i + 1) == 0:
                                if i + 1 == math.sqrt(current_tri):
                                        current_facts += 1 
                                else:
                                        current_facts += 2

                if current_facts > largest_fact:
                        largest_fact = current_facts
                
        return current_tri

#print(p12())

# Problem 13

def p13():
        with open("p13_bigNum.txt", "r") as big_num:
                data = big_num.readlines()

        total_sum = 0

        for i in range(len(data)):
                data[i] = int(data[i])
        
        for i in range(len(data)):
                total_sum += data[i]
        
        answer = str(total_sum)
        answer = answer[:10]

        return answer

#print(p13())

# Problem 14

def collatz(num):
        total_length = 0
        while num != 1:
                if num % 2 == 0:
                        num /= 2
                else:
                        num *= 3
                        num += 1
                
                total_length += 1
        
        return total_length

def p14():
        longest_collatz = 0
        long_num = 0

        for i in range(1000000 - 1):
                if collatz(i + 1) > longest_collatz:
                        longest_collatz = collatz(i + 1)
                        long_num = i + 1
                print(i)
        
        return long_num

#print(p14())

# Problem 15

def p15():
        fact_40 = math.factorial(40)

        answer = fact_40 / math.factorial(20) ** 2
        return answer

#print(p15())

# Problem 16

def p16():
        str_num = str(2 ** 1000)
        total = 0

        for i in range(len(str_num)):
                total += int(str_num[i])
        
        return total

#print(p16())

#! Problem 17

# Problem 18

def get_child(row, index, array):
        if row == len(array) - 1:
                return 0, 0
        
        child_1 = array[row + 1][index]
        child_2 = array[row + 1][index + 1]

        return child_1, child_2


def p18():
        with open('p18_bigTri.txt', 'r') as big_tri:
                read_big_tri = big_tri.readlines()
                
                for i in range(len(read_big_tri)):
                        split_big_tri = read_big_tri[i].split(' ')
                        
                        for i in range(len(split_big_tri)):
                                split_big_tri[i] = int(split_big_tri[i])

                        read_big_tri[i] = split_big_tri

        duplicate = [[0 for element in row] for row in read_big_tri]

        for i in range(len(read_big_tri) - 1, -1, -1):
                for j in range(len(read_big_tri[i])):
                        max_child = max(get_child(i, j, duplicate))

                        duplicate[i][j] = max_child + read_big_tri[i][j]



        return duplicate[0][0]

#print(p18())

#! Problem 19

def p19(start, end):
        day_count = 0

        for i in range(start, end + 1):
                if i % 100 == 0 and i % 400 != 0:
                        day_count += 365
                elif i % 4 == 0:
                        day_count += 366
                else:
                        day_count += 365

# Problem 20

def p20():
        fact_100 = math.factorial(100)
        str_fact_100 = str(fact_100)
        total_sum = 0

        for i in range(len(str_fact_100)):
                total_sum += int(str_fact_100[i])                        

        return total_sum

#print(p20())

# Problem 21

def d(num):
        factors = []
        for i in range(int(math.sqrt(num))):
                if num % (i + 1) == 0:
                        factors.append(i + 1)
                        if num / (i + 1) != i + 1:
                                factors.append(num / (i + 1))

        return sum(factors) - num

def p21():
        answer = 0
        d_vals = [d(i) for i in range(10000)]
        for i in range(len(d_vals)):
                if d_vals[i] < 10000 and i == d_vals[int(d_vals[i])] and i != d_vals[i]:
                        answer += i
                        answer += d_vals[i]
                        #print(i, d_vals[i])
        
        return answer / 2


#print(p21())

# Problem 22

def p22():
        with open('p22_lstNames.txt', 'r') as name_lst:
                name_contents = name_lst.read()
                split_contents = name_contents.split(',')
                #print(split_contents[-1])
        for i in range(len(split_contents)):
                name = split_contents[i]
                split_contents[i] = name[1:-1]

        sorted_contents = sorted(split_contents)
        
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        alphabet_dict = {alphabet[i] : i + 1 for i in range(len(alphabet))}

        name_score = 0

        for i, name in enumerate(sorted_contents):
                name_total = 0

                for l in name:
                        #try:
                        name_total += alphabet_dict[l]
                        #except:
                                #print(name)
                name_score += name_total * (i + 1)

        return name_score
        #return split_contents[4329], sorted_contents

#print(p22())

# Problem 54

def highest_pattern(hand):
        royal_flush = True
        straight_flush = True
        four_kind = True
        full_house = True
        flush = True
        straight = True
        three_kind = True
        two_pairs = True
        one_pair = True
        hight_card = True

        suit = hand[0][1]
        for i in range(1, len(hand)):
                if hand[i][1] != suit:
                        royal_flush = False
                        straight_flush = False
                        flush = False
                        break

        
        for i in range (len(hand)):
                if hand[i][0] not in 'TJQKA':
                        royal_flush = False

        if royal_flush:
                return 9

def p54():
        with open('p54_pokeHands.txt', 'r') as poker_hands:
                read_poker_hands = poker_hands.readlines()

                for i in range(len(read_poker_hands)):
                        split_poker_hands = read_poker_hands[i].split(' ')
                        hand_1 = split_poker_hands[0 : 5]
                        hand_2 = split_poker_hands[5:]



# Problem 67

def p67():
        with open('p67_bigTri.txt', 'r') as big_tri:
                read_big_tri = big_tri.readlines()
                
                for i in range(len(read_big_tri)):
                        split_big_tri = read_big_tri[i].split(' ')
                        
                        for i in range(len(split_big_tri)):
                                split_big_tri[i] = int(split_big_tri[i])

                        read_big_tri[i] = split_big_tri

        duplicate = [[0 for element in row] for row in read_big_tri]

        for i in range(len(read_big_tri) - 1, -1, -1):
                for j in range(len(read_big_tri[i])):
                        max_child = max(get_child(i, j, duplicate))

                        duplicate[i][j] = max_child + read_big_tri[i][j]



        return duplicate[0][0]

#print(p67())

# Problem 99

def p99():
        log_vals = []
        with open('p99_expNum.txt', 'r') as exp_num:
                read_exp_num = exp_num.readlines()

                for i in range(len(read_exp_num)):
                        base, exponent = read_exp_num[i].split(',')
                        base = int(base)
                        exponent = int(exponent)
                
                        log_vals.append(exponent * math.log(base))

        current_high = log_vals[0]
        current_index = 0

        for i in range(len(log_vals)):
                if current_high < log_vals[i]:
                        current_high = log_vals[i]
                        current_index = i
        
        return current_index + 1

#print(p99())