from pyswip import Prolog
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-v","--verbose", help="increase output verbosity",action="store_true")
parser.add_argument("-q","--query", help="show query",action="store_true")
args = parser.parse_args()
prolog = Prolog()
prolog.consult("assign1.pl")
file = open('test.txt', 'r')
lines = file.readlines()
correct_answers = 0;
for line in lines:
    expected_answer = line.split('%')[1].strip()
    query = line.split('%')[0]
    return_set=list(prolog.query(query))
    if len(return_set)==0:
        returned_answer='false'
    else:
        returned_answer='correct'
    is_Correct = "You answered wrong"
    if(expected_answer==returned_answer):
        is_Correct = "You answered right"
        correct_answers+=1
    if args.query:
        print(query, is_Correct)
    if args.verbose:
        if returned_answer=='correct':
            print(return_set[0],'\n')
        else:
            print(False,'\n')

print("{} out of {} queries returned correct solutions".format(correct_answers,len(lines)))
# for soln in prolog.query("s(P,[the,old,woman,and,the,old,man,gave,the,poor,young,man,whom,they,liked,a,white,envelope,in,the,shed,behind,the,building],[])."):
#     print(soln)
