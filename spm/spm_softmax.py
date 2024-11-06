from spm.__wrapper__ import Runtime


def spm_softmax(*args, **kwargs):
    """
      Softmax (e.g., neural transfer) function over columns  
        FORMAT [y] = spm_softmax(x,k)  
         
        x - numeric array array  
        k - precision, sensitivity or inverse temperature (default k = 1)  
         
        y  = exp(k*x)/sum(exp(k*x))  
         
        NB: If supplied with a matrix this routine will return the softmax  
        function over columns - so that spm_softmax([x1,x2,..]) = [1,1,...]  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_softmax.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_softmax", *args, **kwargs)
