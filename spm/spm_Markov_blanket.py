from spm.__wrapper__ import Runtime


def spm_Markov_blanket(*args, **kwargs):
    """
      Markovian partition  
        FORMAT [x,y] = spm_Markov_blanket(J,z,m,R)  
        J  - Jacobian  
        z  - {1 x N}  partition of states (indices)  
        m  - number of internal states [default: 3]  
         
        x  - {3 x n} particular partition of state indices  
            x{1,j} - active states of j-th partition  
            x{2,j} - sensory states of j-th partition  
            x{3,j} - internal states of j-th partition  
         
        y  - {3 x n} particular partition of partition indices  
            y{1,j} - active states of j-th partition  
            y{2,j} - sensory states of j-th partition  
            y{3,j} - internal states of j-th partition  
         
        Partition or Grouping (coarse-scaling) operator  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_Markov_blanket.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_Markov_blanket", *args, **kwargs)
