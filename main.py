#縦確認定義
import sys


def checkVertical(bingo):
  for i in range(len(bingo)):
    checklist = []
    for row in bingo:
      checklist.append(row[i])
      if isAllequal(checklist):
        return True
  return false

#リストに入れる→リスト内が全部丸か確認

#横確認定義
def checkHorizontal(bingo):
  for row in bingo:
    if isAllequal(row):
      return True
  return False

#対角線確認定義1
def checkDiagonal(bingo):
  for i in range(len(bingo)):
    checklist = []
    for row in bingo:
      checklist.append(row[i])
      i += 1
    if isAllequal(checklist):
      return True
  return false

#対角線確認定義2
def checkDiagonal(bingo):
  for i in reversed(range(len(bingo))):
    checklist = []
    for row in bingo:
      checklist.append(row[i])
      i -= 1
    if isAllequal(checklist):
      return True
  return false


#リスト内が全部丸か確認
def isAllequal(list):
  for elem in list:
    if elem !== "◯"
      return false
  return True

#ビンゴゲーム枠組み
def main(lines):
  # N * N マスのビンゴを考える
  # N = int(lines[0]) 
  bingo = lines[1:]

  #縦を確認する
  if checkVertical(bingo):
    print("yes")
    return
  #横を確認する
  if checkHorizontal(bingo):
    print("yes")
    return
  #斜めを確認する
  if checkDiagonal(bingo):
    print("yes")
    return

  print("no")


if __name__ == '__main__':
  lines = []
  for l in sys.stdin:
    lines.append(l.rstrip('\r\n'))
  main(lines)