from spm.__wrapper__ import Runtime


def spm_kron(*args, **kwargs):
    """
      Kronecker tensor product with sparse outputs   
        FORMAT K = spm_kron(A,B)  
               K = spm_kron(A)  
         
          KRON(X,Y) is the Kronecker tensor product of X and Y.  
          The result is a large matrix formed by taking all possible  
          products between the elements of X and those of Y.   For  
          example, if X is 2 by 3, then KRON(X,Y) is  
         
             [ X(1,1)*Y  X(1,2)*Y  X(1,3)*Y  
               X(2,1)*Y  X(2,2)*Y  X(2,3)*Y ]  
          
        When called with a single cell array input, the tensor product is formed  
        recursively.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_kron.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_kron", *args, **kwargs)
