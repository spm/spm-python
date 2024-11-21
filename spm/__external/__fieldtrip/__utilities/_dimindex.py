from spm.__wrapper__ import Runtime


def _dimindex(*args, **kwargs):
    """
      DIMINDEX makes a selection from a multi-dimensional array where the dimension is  
        selected by a scalar, not by the place between the brackets.  
         
        Use as  
          M = dimindex(A,dim,idx)  
         
        The purpose of the function is shown by the following example:  
         
        A(:,:,:,23,:,:,...) is the same as dimindex(A,4,23)  
        A(2,4,3)            is the same as dimindex(A,[1,2,3],[2,4,3])  
        A(4,:,[5:10])       is the same as dimindex(A,[1,3],{4,[5:10]})  
         
        See also the function DIMASSIGN  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/private/dimindex.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("dimindex", *args, **kwargs)
