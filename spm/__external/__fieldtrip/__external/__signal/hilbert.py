from spm._runtime import Runtime


def hilbert(*args, **kwargs):
    r"""
      Computes analytic signal  
        FORMAT [x] = hilbert(xr)  
         
        Returns analytic signal x = xr + i*xi such that   
        xi is the Hilbert transform of real vector xr.  
       __________________________________________________________________________  
        Copyright (C) 2009 Wellcome Trust Centre for Neuroimaging  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/external/signal/hilbert.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("hilbert", *args, **kwargs)
