
filename_input='C:/Users/chiu yu-en/Desktop/程式碼/Novel.107021027/07_倚天屠龍記.txt'
word_cnt={}
word_cnt_pun={}
file_path_punctuation='C:/Users/chiu yu-en/Desktop/程式碼/ChineseArticlesProcessing/punctuation.txt'
word_punctuation={}

with open(file_path_punctuation,'r',encoding='utf8') as fp:
    file_read=fp.read()
    for c in file_read:
        word_punctuation[c]=0

with open(filename_input,'r',encoding='big5') as fr:
    file_read=fr.read()
  
    for c in file_read:
        if c in word_punctuation:
            if c in word_cnt_pun:
                word_cnt_pun[c]=word_cnt_pun[c]+1
            else:
                word_cnt_pun[c]=1
        else:
            if c in word_cnt:
                word_cnt[c]=word_cnt[c]+1
            else:
                word_cnt[c]=1

for key in sorted(word_cnt_pun, key=word_cnt_pun.get, reverse=True):
    print(key, word_cnt_pun[key])

'''
for key in sorted(word_cnt, key=word_cnt.get, reverse=True):
    print(key,word_cnt[key])
'''