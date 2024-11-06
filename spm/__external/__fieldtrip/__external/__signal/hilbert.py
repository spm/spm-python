from spm.__wrapper__ import Runtime


def hilbert(*args, **kwargs):
    """
      Computes analytic signal  
        FORMAT [x] = hilbert(xr)  
         
        Returns analytic signal x = xr + i*xi such that   
        xi is the Hilbert transform of real vector xr.  
       __________________________________________________________________________  
        Copyright (C) 2009 Wellcome Trust Centre for Neuroimaging  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/external/signal/hilbert.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("hilbert", *args, **kwargs)
