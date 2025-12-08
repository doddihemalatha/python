text=input("enter a sentence: ")
words=text.split()
freq={}
for w in words:
  if w in freq:
    freq[w]+=1
  else:
    freq[w]=1
print(freq)
