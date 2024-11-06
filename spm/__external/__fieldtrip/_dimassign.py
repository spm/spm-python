from spm.__wrapper__ import Runtime


def _dimassign(*args, **kwargs):
    """
      function M=dimassign(A,dim,idx,B);  
          
        The purpose of the function is shown by the following example:  
        If A and B are multidimensional matrixes,  
        A=dimassign(A,4,23,B); is the same as A(:,:,:,23,:,:,...)=B;  
        The difference is that the dimention is selected by a scalar, not by  
        the place between the brackets.  
        A(2,4,3)=B; will then be written as: A=dimassign(A,[1,2,3],[2,4,3],B);  
        In this last case B, of cource, must be a scalar.  
        A([1,2],:,3)=B; can be written as: A=dimassign(A,[1,3],{[1,2],3},B);  
        Of cource, again, the dimensions of B must fit!   
        (size(B)==size(A([1,2],:,3) in this particular case)  
         
        See also the function DIMINDEX  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/dimassign.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("dimassign", *args, **kwargs)
