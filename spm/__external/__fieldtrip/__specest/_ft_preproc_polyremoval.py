from spm.__wrapper__ import Runtime


def _ft_preproc_polyremoval(*args, **kwargs):
    """
      FT_PREPROC_POLYREMOVAL removed an Nth order polynomal from the data  
         
        Use as  
          dat = ft_preproc_polyremoval(dat, order, begsample, endsample, flag)  
        where  
          dat        data matrix (Nchans X Ntime)  
          order      the order of the polynomial  
          begsample  index of the begin sample for the estimate of the polynomial  
          endsample  index of the end sample for the estimate of the polynomial  
          flag       optional boolean to specify whether the first order basis  
                     vector will zscored prior to computing higher order basis  
                     vectors from the first-order basis vector (and the beta  
                     weights). This is to avoid numerical problems with the  
                     inversion of the covariance when the polynomial is of high  
                     order/number of samples is large.  
         
        If begsample and endsample are not specified, it will use the whole  
        window to estimate the polynomial.  
         
        For example  
          ft_preproc_polyremoval(dat, 0)  
        removes the mean value from each channel and  
          ft_preproc_polyremoval(dat, 1)  
        removes the mean and the linear trend.  
         
        If the data contains NaNs, these are ignored for the computation, but  
        retained in the output.  
         
        See also FT_PREPROC_BASELINECORRECT, FT_PREPROC_DETREND  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/specest/private/ft_preproc_polyremoval.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_preproc_polyremoval", *args, **kwargs)
