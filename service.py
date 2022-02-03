import random 

rand_count = 6
ban_count = 3
candidates1 = []
candidates2 = []
bans1 = []
bans2 = []
pick1 = []
pick2 = []

civ_list = [
 "Britons"          , 
 "Byzantines"       , 
 "Celts"            , 
 "Chinese"          , 
 "Franks"           , 
 "Goths"            , 
 "Japanese"         , 
 "Mongols"          , 
 "Persians"         , 
 "Saracens"         , 
 "Teutons"          , 
 "Turks"            , 
 "Vikings"          , 
 "Aztecs"           , 
 "Huns"             , 
 "Koreans"          , 
 "Mayans"           , 
 "Spanish"          , 
 "Incas"            , 
 "Indians"          , 
 "Italians"         , 
 "Magyars"          , 
 "Slavs"            , 
 "Berbers"          , 
 "Ethiopians"       , 
 "Malians"          , 
 "Portuguese"       , 
 "Burmese"          , 
 "Khmer"            , 
 "Malay"            , 
 "Vietnamese"       , 
 "Bulgarians"       , 
 "Cumans"           , 
 "Lithuanians"      , 
 "Tatars"           , 
#  "Burgundians"      , 
#  "Sicilians"        , 
#  "Bohemians"        , 
#  "Poles"            
 ]

# def get_opt():
#     global rand_count 
#     global ban_count
#     val = input("Default Ban-Pick? y or n: ")
#     print(val)
#     if(val != "y"):
#         val = input("Enter rand_count: ")
#         if(int(val)>10):
#             val=10
#         else:
#             val=int(val)
#         rand_count = int(val)
#         val = input("Enter ban_count: ")
#         if(ban_count!=(rand_count-2)):
#             ban_count = rand_count-2
#         ban_count = int(val)

def gen_rand_civ(rand_count):
    random.shuffle(civ_list)
    candidates1 = civ_list[0:rand_count]
    random.shuffle(civ_list)
    candidates2 = civ_list[0:rand_count]
    return candidates1, candidates2


def ban_pick():
    global bans1
    global bans2
    global pick1
    global pick2
    temp1 = candidates1.copy()
    temp2 = candidates2.copy()
    for i in range(ban_count):
        print("candidates1: {}".format(temp1))
        val = input("Enter the banned civ from candidates1: ")
        temp1.remove(val)
        bans1.append(val)
        print("candidates2: {}".format(temp2))
        val = input("Enter the banned civ from candidates2: ")
        temp2.remove(val)
        bans2.append(val)
    print("candidates1: {}".format(temp1))
    # val = input("Enter the picked civ from candidates1: ")
    # pick1=val
    # print("candidates2: {}".format(temp2))
    # val = input("Enter the picked civ from candidates2: ")
    # pick2=val
    random.shuffle(temp1)
    random.shuffle(temp2)
    for i in range(3):
        print("Round#{}: {} vs {}".format(i, temp1[i], temp2[i])) 

def gen_matches(bans1, bans2, candidates1, candidates2):
    civis1 = []
    civis2 = []
    print(bans1, bans2)
    print(candidates1, candidates2)
    for i, can in enumerate(candidates1):
        if i + 1 not in bans1:
            civis1.append(can)

    for i, can in enumerate(candidates2):
        if i + 1 not in bans2:
            civis2.append(can)

    random.shuffle(civis1)
    random.shuffle(civis2)

    return civis1, civis2



def report():
    report = open("test.rpt", 'w') 
    print("candidates1: {}\ncandidates2: {}\nbans1: {}\nbans2: {}\npick1: {}\npick2: {}\n".format(candidates1, candidates2, bans1, bans2, pick1, pick2))
    report.write("candidates1: {}\ncandidates2: {}\nbans1: {}\nbans2: {}\npick1: {}\npick2: {}\n".format(candidates1, candidates2, bans1, bans2, pick1, pick2))

if __name__ == '__main__': 
    # get_opt()
    gen_rand_civ()
    ban_pick()
    # report()

