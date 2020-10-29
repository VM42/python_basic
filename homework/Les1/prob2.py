# Problem 2 (input in sec result in hrs/mts/sec)

TotalInSec = int(input(" Введи время в секундах\n>>>"))
# in this one I probably should used % as arifmetic op. but not sure how so
hrs = int(TotalInSec // 3600)
mts = int((TotalInSec - hrs * 3600) // 60)
sec = int(TotalInSec - (hrs * 3600 + mts * 60))
print(f"Время {hrs}h : {mts}min : {sec}sec")
