import re
total_count = 0
miss_graduation = 0

def generate_combinations(n, slots):
    global total_count
    global miss_graduation
    stack = [(0, [])]

    while stack:
        index, current_combination = stack.pop()

        if index == n:
            cur_comb = ''.join(current_combination)
            pattern = re.compile(r'A{4,}')
            if not bool(pattern.search(cur_comb)):
                total_count += 1
                if not bool(pattern.search(cur_comb)) and cur_comb[-1] == 'A':
                    miss_graduation += 1
        else:
            for slot in slots:
                new_combination = current_combination + [slot]
                stack.append((index + 1, new_combination))

    print(f"{miss_graduation}/{total_count}")

days = int(input("Enter number of days:"))
slots = ['P', 'A']
generate_combinations(days, slots)
