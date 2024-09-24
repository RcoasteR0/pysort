the_list = [
        6,      82,      21,      58,      22,      54,      71,     215,      99,     227, 
       73,      24,      17,      44,     144,      78,      25,      66,      47,       3, 
       87,      33,     312,     242,      42,      61,     348,     346,      98,      92, 
       83,     100,      94,      40,       5,     458,     364,      26,      64,     735, 
       90,     489,      72,     504,      88,      97,     226,     218,     186,     168, 
]

count = len(the_list)

def sort_bubble(arr):
  print('-- Bubble', '-' * 60)
  print(f'before: {arr}')

  end = count - 1
  while end > 0:
    for i in range(end):
      if arr[i] > arr[i + 1]:
        arr[i], arr[i + 1] = arr[i + 1], arr[i]
    end = end - 1

  print(f'after : {len(arr)=}, {arr}')

def sort_select(arr):
  print('** Select', '*' * 60)
  print(f'before: {arr}')

  start = 0
  while start < count:
    small = start
    for i in range(start + 1, count):
      if arr[small] > arr[i]:
        small = i
    arr[start], arr[small] = arr[small], arr[start]
    start = start + 1

  print(f'after : {len(arr)=}, {arr}')

def sort_insert(arr):
  print('== Insert', '=' * 60)
  print(f'before: {arr}')

  for i in range(1, count):
    select = i
    while select > 0:
      if arr[select] < arr[select - 1]:
        arr[select], arr[select - 1] = arr[select - 1], arr[select]
        select = select - 1
      else:
        break
    
  print(f'after : {len(arr)=}, {arr}')

def sort_shell(arr):
  print('++ Shell', '+' * 60)
  print(f'before: {arr}')

  for i in range(5):
    interval = 5 - i
    for j in range(interval):
      for k in range(j + interval, count, interval):
        select = k
        while select > 0:
          if arr[select] < arr[select - interval]:
            arr[select], arr[select - interval] = arr[select - interval], arr[select]
            select = select - interval
          else:
            break

  print(f'after : {len(arr)=}, {arr}')

def main():
  sort_bubble(the_list[:])
  sort_insert(the_list[:])
  sort_select(the_list[:])
  sort_shell(the_list[:])

if __name__ == '__main__':
  main()

