from spm.__wrapper__ import Runtime


def _fdr(*args, **kwargs):
    """
      FDR false discovery rate  
         
        Use as  
          h = fdr(p, q)  
         
        The input argument p is a vector or matrix with (uncorrected) p-values, the input argument  
        q is a scalar that reflects the critical alpha-threshold for the inferential decision. The  
        output argument h is a boolean matrix (same size as p) denoting for each sample whether   
        the null hypothesis can be rejected.   
         
        This implements  
          Genovese CR, Lazar NA, Nichols T.  
          Thresholding of statistical maps in functional neuroimaging using the false discovery rate.  
          Neuroimage. 2002 Apr;15(4):870-8.  
         
        There are two types of FDR correction (Benjamini-Hochberg & Benjamini-Yekutieli), of  
        which the second is currently implemented.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/fdr.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("fdr", *args, **kwargs)
