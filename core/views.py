from django.shortcuts import render

# Create your views here.
def sonika(request):

    datas={'hin':75,'eng':73,'san':67,'eco':78,'soc':88}
    tl= sum(datas.values())
    print(tl)
    # 
    totals={'total':tl}
    def result(tl):
        if tl > 300 : 
            return 'first '   
            
 
        elif tl >250:
            return 'second'
            
        elif tl > 230:
            return 'third'
            
        else:
            return  'Fail'
    a=result(tl)
    
 
    # res = {a:tl}   
     
    
    # sona=datas|totals |res 
    # print(sona)
    # sonas={'sona':'data'},'res':{a:tl}}
    
    sona={'datas':{'hin':75,'eng':73,'san':67,'eco':78,'soc':88},'totals':{'total':tl},'res':{'tl':a}}    
    # totals={'total':tl}
    return render(request,'core/sonika.html',sona)
     
def rashmi(request):
    datar={"hin":75,'eng':68,'phy':48,'che':44,'mat':45}
    tl=sum(datar.values())
    
    totalr={'total':tl}
    def result(tl):
        if tl > 300 : 
            return 'first '   
            
 
        elif tl >250:
            return 'second'
            
        elif tl > 230:
            return 'third'
            
        else:
            return  'Fail'
    a=result(tl)
    # rashmir=datar|totalr
    rashmi={'datar':{"hin":75,'eng':68,'phy':48,'che':44,'mat':45},'totalr':{'total':tl},'res':{'tl':a}} 
    return render(request,'core/rashmi.html',rashmi)
def himanshu(request):
    datah={"hin":67,'eng':68,'phy':68,'che':89,'mat':88}
    tl=sum(datah.values())
    # hm={'datah':{"hin":67,'eng':68,'phy':69,'che':89,'mat':88},'totalh':{'total':tl}}
    totalh={'total':tl}
    # hm=datah|totalh
    def result(tl):
        if tl > 300 : 
            return 'first '   
            
 
        elif tl >250:
            return 'second'
            
        elif tl > 230:
            return 'third'
            
        else:
            return  'Fail'
    a=result(tl)

    hm={'datah':{"hin":67,'eng':68,'phy':69,'che':89,'mat':88},'totalh':{'total':tl},'res':{'tl':a}}


    return render(request,'core/himanshu.html',hm)
def ravi(request):
    datard={"hin":75,'eng':67,'phy':68,'che':78,'mat':89}
    tl=sum(datard.values())
    totalrd={'total':tl}
    rd=datard|totalrd 
    # rd={'datard':{"hin":75,'eng':67,'phy':68,'che':78,'mat':89},'totalrd':{'total':tl}} 
    def result(tl):
        if tl > 300 : 
            return 'first '   
            
 
        elif tl >250:
            return 'second'
            
        elif tl > 230:
            return 'third'
            
        else:
            return  'Fail'
    a=result(tl)
    rd={'datard':{"hin":75,'eng':67,'phy':68,'che':78,'mat':89},'totalrd':{'total':tl},'res':{'tl':a}} 
    return render(request,'core/ravi.html',rd) 

def dishu(request):
    datadd={"hin":75,'eng':67,'phy':68,'che':78,'mat':89}
    tl=sum(datadd.values())
    totaldd={'total':tl}
    dd=datadd|totaldd 
    # dd={'datadd':{"hin":75,'eng':67,'phy':68,'che':78,'mat':89},'totalrd':{'total':tl}} 
    def result(tl):
        if tl > 300 : 
            return 'first '   
            
 
        elif tl >250:
            return 'second'
            
        elif tl > 230:
            return 'third'
            
        else:
            return  'Fail'
    a=result(tl)
    dd={'datadd':{"hin":75,'eng':67,'phy':68,'che':78,'mat':89},'totaldd':{'total':tl},'res':{'tl':a}} 
    return render(request,'core/dishu.html',dd) 
def result(request):
    pass 
# ,
 # tl=sum(data.values())
    # print(tl)
    # # total={'total':tl}
    # # data1={'total':tl,'data':data}
    
#     dict ={"a":1,'B':2}
# print(sum(dict.values()))  
# who to merge to dictioneries 
# d1={'a':23,'b':21}
# d2={'c':43,'d':42}         
# d3 = d1 | d2
    # print(3)

