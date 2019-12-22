import random
import time
import numpy as np
global number

def fill_serial(a,b,mem):
    global number
    for i in range(10):
        for j in range(b):
            mem[i,j]=number
            number=number+1


def fill_random(a,b,mem):
    pass



def observe_random(mem,program,r,c,no_of_sets,assoc):
    staticsize=10
    hit=0
    miss=0
    flag=0
    for i in range(1000):
        module=random.randint(0,4)
        address=random.randint(program[module][0,0],program[module][staticsize-1,c-1])#accessing an address from module  
        print("Adress"+str(address))
        module_row = int((address%(staticsize*c))/c)#gets the row of mudle which has to be brough in cache
        print(module_row)
        cache_set=int(module_row%no_of_sets)
        print(cache_set)
        #cache_set=int(address%(no_of_sets))
        if(assoc!=1):
            init_cache_row=int(cache_set*assoc)
            final_cache_row=int(init_cache_row+assoc-1)
        else:
            init_cache_row=int(cache_set)
            final_cache_row=int(init_cache_row)

 
        print("checking memory")
        print(init_cache_row,end=" ")
        print(final_cache_row)
        break_outer = False
        for i in range (init_cache_row,final_cache_row+1):
            if break_outer:
                break
            for j in range(c):
                print(mem[i,j],end=" ")
                if(mem[i,j]==address):
                    hit=hit+1
                    flag=1
                    break_outer = True
                    break 
        print("mem check complete")
        if(flag==1):
            flag=0
            continue
        if(assoc==1):
            victim=init_cache_row
        else:
            victim=random.randint(init_cache_row,final_cache_row)
        miss=miss+1

        for i in range (c):
            mem[victim,i]=program[module][module_row,i]
    print(hit)
    print(miss)




def observe_lor(mem,mod1,mod2,r,c,no_of_sets,assoc,mem_accesses):
    staticsize=10
    hit=0
    miss=0
    flag=0
    print(mod1)
    print(mod2)
    print(mem)
    program=[mod1,mod2]
    for i in range(mem_accesses):
        module=random.randint(0,1)
        
        address=random.randint(program[module][0,0],program[module][staticsize-1,c-1])#accessing an address from module  
        print("Adress"+str(address))
        module_row = int((address%(staticsize*c))/c)#gets the row of mudle which has to be brough in cache
        print(module_row)
        cache_set=int(module_row%no_of_sets)
        print(cache_set)
        #cache_set=int(address%(no_of_sets))
        if(assoc!=1):
            init_cache_row=int(cache_set*assoc)
            final_cache_row=int(init_cache_row+assoc-1)
        else:
            init_cache_row=int(cache_set)
            final_cache_row=int(init_cache_row)

 
        print("checking memory")
        print(init_cache_row,end=" ")
        print(final_cache_row)
        for i in range (init_cache_row,final_cache_row+1):
            for j in range(c):
                print(mem[i,j],end=" ")
                if(mem[i,j]==address):
                    hit=hit+1
                    flag=1
                    break 
        print("mem check complete")
        if(flag==1):
            flag=0
            continue
        if(assoc==1):
            victim=init_cache_row
        else:
            victim=random.randint(init_cache_row,final_cache_row)
        miss=miss+1

        for i in range (c):
            mem[victim,i]=program[module][module_row,i]
    print(hit)
    print(miss)
    return {'hit_rate':hit/1000, 'miss_rate':miss/1000, 'hit_count':hit, 'miss_count' : miss}

def driver(csize, sets, bsize, mem_accesses):
    

    csize=int(csize)
    sets=int(sets)
    bsize=int(bsize)


    no_of_blocks=int(csize)/bsize
    no_of_blocks=int(no_of_blocks)
    no_of_sets=no_of_blocks/sets
    tem=csize

    max_array = no_of_blocks
    mem = np.arange(max_array*bsize).reshape((max_array,bsize))
    for i in range(max_array):
        for j in range(bsize):
            mem[i,j]=-1
    fill_random(max_array,bsize,mem)

    #program is divided into 3 module so that temporal and spatial locality can be observed

    module_size1=10*bsize
    module_size2=10*bsize
    module_size3=10*bsize
    module_size5=10*bsize
    module_size4=10*bsize

    module1= np.arange(module_size1).reshape((10,bsize))
    module2= np.arange(module_size2).reshape((10,bsize))
    module3= np.arange(module_size3).reshape((10,bsize))
    module4= np.arange(module_size4).reshape((10,bsize))
    module5= np.arange(module_size5).reshape((10,bsize))



    program=[module1,module2,module3,module4,module5]
    global number
    number=0
    for i in range(5):
        fill_serial(max_array,bsize,program[i])
    n1=random.randint(0,4)
    n2=random.randint(0,4)
    while(n2==n1):
        n2=random.randint(0,4)
    output = observe_lor(mem,program[n1],program[n2],max_array,bsize,no_of_sets,sets, mem_accesses)
    #observe_random(mem,program,max_array,bsize,no_of_sets,sets)

    print(program)
    return output

if __name__ == "__main__":
    csize=input("Enter Size Of Cache ")
    sets =input("Enter Set Associativity ")  
    bsize = input("Enter Size Of Block " )
    driver(csize, sets, bsize)
    