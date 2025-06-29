from spm._runtime import Runtime


def _lbex(*args, **kwargs):
    """
      This function will add the field "subspace" to the sourcemodel definition.  
         
        The subspace projection is based on the LBEX (local basis expansion)  
        method.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/lbex.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("lbex", *args, **kwargs)
