from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    text=request.GET['fulltext']
    words=text.split()
    word_dictionary = {}    #<단어 : 몇번, ...>

    for word in words:
        if word in word_dictionary:
            #increase
            word_dictionary[word]+=1
        else:
            #add to dictionary
            word_dictionary[word]=1
    # 딕셔너리의 key,value값 각각따로 리스트 만들어서 담아두기      
    key_list = list(word_dictionary.keys())
    value_list = list(word_dictionary.values())
 
     # 중복숫자 내림차순으로 정렬
    for big in range(0,len(key_list)-1):
        for small in range(big+1,len(key_list)):
            if value_list[big] < value_list[small]:
                x = key_list[small]
                key_list[small] = key_list[big]
                key_list[big] = x
                x = value_list[small]
                value_list[small] = value_list[big]
                value_list[big] = x

    # 중복숫자가 같은 단어간 오름차순으로 정렬
    for big in range(0,len(key_list)-1):
        for small in range(big+1,len(key_list)):
            if value_list[big] < value_list[small]:
                break
            elif value_list[big] == value_list[small]:
                if key_list[big] > key_list[small]:
                    x = key_list[small]
                    key_list[small] = key_list[big]
                    key_list[big] = x
                    x = value_list[small]
                    value_list[small] = value_list[big]
                    value_list[big] = x

    # key,value값으로 나눴던 리스트를 다시 딕셔너리로 합치기
    dic = {}
    for a in range(0,len(key_list)):
        dic[key_list[a]] = value_list[a]

    return render(request, 'result.html', {'full' : text, 'total' : len(words), 'dictionary' : dic.items()})
