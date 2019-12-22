


Working:
  
  1) Program starts by taking cache size,set associativity, cache block size and the user program size as input from user.
  2) Number of sets are calculated from above data and program is divided into 5 modules, with block size matching to cache block size
  3) Modules are then filled up with addresses in ascending order. Each address representing an instruction loaded in main memory
  Now we have to option: Either observe random module access which doesn't exploit locality of refrence so all 5 modules participate in memory referencing
  or to observe locality only 2 modules are asking for memory accesses
  
  4) For Locality observation we have function observe_lor() is used:
            i)    This funtion gets cache memory, two randomly selected modules out of five modules, cache's no of blocks as 'r', cache's blocksize 
                  as 'c' which is same for each module's blocksize, number of sets,set associativity and no of blocks in each module as parameter.
            ii)   Function access memory 1000 time with initial loop, and for every loop one module is randomly selected from which any address
                  is picked randomly
            iii)  Block number for that address is evaluated and in case of associativity greater than 1, set on which address has to be checked is calculated
            iv)   In case of associative cache inital and final block contained in sets are determined and these blocks are checked whether required address 
                  resides in or not. In case of direct mapped cache one block is checked for address.
            v)    If address resides in set or block it's a hit and program continues for next access.
            vi)   In case of miss, that is generated address doesn't reside in set or block, the block which has to be fetched is determined and replaced is with the
                  checked block. If cache is associative one block is randomly selected for replacement, and the block brought from memory replaces victim block.
 5) For random access, that is program is not spending it's most of time with a pirticular code area we have observe_random() funtion.
            i)    This function takes all 5 modules of program for memory accesses, cache's no of blocks as 'r', cache's blocksize 
                  as 'c' which is same for each module's blocksize, number of sets,set associativity and number of blocks in each module as parameter.
            ii)   Function access memory 1000 time with initial loop, and for every loop one module is randomly selected from which any address
                  is picked randomly
            iii)  Program continues similiar to above after this step.
            
  6) A very clear diversity is observed in:
    i)    Change of cache size, with reference to a same program size if cache size is kept smaller or equal to program size, increasing cache size greater
          than program size doesn't reflect a major effeciency.
    ii)   Direct mapped cache isn't found to be very efficient because for more than 1 modules because of frequent replacement.
    iii)  Increasing set associativity and and block size brings a major efficiency
