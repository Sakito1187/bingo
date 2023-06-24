import sys

#縦確認定義
def check_vertical(bingo_size, bingo):
  for i in range(bingo_size):
    #確認するラインの要素をリストに入れる
    checklist = []
    for row in bingo:
      checklist.append(row[i])

    #ビンゴか確認
    if is_bingo(checklist):
      return True
  return False


#横確認定義
def check_horizontal(bingo_size, bingo):
  for row in bingo:
    if is_bingo(row):
      return True
  return False

#対角線確認定義
def check_diagonal(bingo_size, bingo):
  diag1 = [bingo[i][i] for i in range(bingo_size)]
  if is_bingo(diag1):
    return True

  diag2 = [bingo[i][bingo_size - i - 1] for i in range(bingo_size)]
  if is_bingo(diag2):
    return True
  
  return False

#リスト内が全部丸か確認
def is_bingo(list):
  for elem in list:
    if elem != 'o':
      return False
  return True

def main(lines):
  bingo_size = int(lines[0])
  bingo = lines[1:]

  #縦を確認する
  if check_vertical(bingo_size, bingo):
    print("yes")
    return

  #横を確認する
  if check_horizontal(bingo_size, bingo):
      print("yes")
      return

  #斜めを確認する
  if check_diagonal(bingo_size, bingo):
      print("yes")
      return

  print("no")


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
      lines.append(l.rstrip('\r\n'))
    main(lines)

