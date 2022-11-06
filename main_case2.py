from cases.case2.case_two import CaseTwo

kls = CaseTwo()

# Manter ou nao os espacos em brancos do texto?

lines = kls.last_lines(file_name='files/my_file_2.txt')
while True:
    try:
        next(lines)
    except StopIteration:
        break

print('\n\nFIM\n')
