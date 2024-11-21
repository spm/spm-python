from spm.__wrapper__ import Runtime


def memtoc(*args, **kwargs):
    """
      MEMTOC return the memory that was used  
         
          MEMTIC and MEMTOC functions work together to measure memory usage.  
          MEMTIC, by itself, saves the current memory footprint that MEMTOC  
          uses later to measure the memory that was used between the two.  
         
        Use as  
          MEMTIC  
          MEMTOC  
        to print the estimated memory use on screen, or  
          MEMTIC  
          M = MEMTOC  
        to return the estimated memory (in bytes) in variable M, or  
          C = MEMTIC  
          M = MEMTOC(C)  
        to specifically estimate the memory use between a well-defined tic/toc pair.  
         
        Note that MATLAB uses internal memory allocation, garbage collection, shallow  
        copies of variables, and virtual memory. Due to the advanced handling of  
        memory for its variables, it is not easy and in certain cases not possible to  
        make a reliable and reproducible estimate based on the memory information  
        provided by the operating system.  
         
        Example: measure the memory increase due to allocating a lot of memory.  
        Doing a "clear x" following the allocation and prior to MEMTOC does not  
        affect the memory that is reported.  
         
          memtic  
          n = 125; x = cell(1,n);  
          for i=1:n  
            x{i} = randn(1000,1000); % 8kB per item  
            disp(i);  
          end  
          whos x  
          memtoc  
         
        See also TIC, TOC  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/memtoc.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("memtoc", *args, **kwargs)
