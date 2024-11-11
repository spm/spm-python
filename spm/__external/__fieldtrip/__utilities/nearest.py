from spm.__wrapper__ import Runtime


def nearest(*args, **kwargs):
    """
      NEAREST return the index of an array nearest to a scalar  
         
        Use as  
          [indx] = nearest(array, val, insideflag, toleranceflag)  
         
        The second input val can be a scalar, or a [minval maxval] vector for  
        limits selection.  
         
        If not specified or if left empty, the insideflag and the toleranceflag  
        will default to false.  
         
        The boolean insideflag can be used to specify whether the value should be  
        within the array or not. For example nearest(1:10, -inf) will return 1,  
        but nearest(1:10, -inf, true) will return an error because -inf is not  
        within the array.  
         
        The boolean toleranceflag is used when insideflag is true. It can be used  
        to specify whether some tolerance should be allowed for values that are  
        just outside the array. For example nearest(1:10, 0.99, true, false) will  
        return an error, but nearest(1:10, 0.99, true, true) will return 1. The  
        tolerance that is allowed is half the distance between the subsequent  
        values in the array.  
         
        See also FIND  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/nearest.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("nearest", *args, **kwargs)
