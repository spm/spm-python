from spm._runtime import Runtime


def fiff_define_constants(*args, **kwargs):
    """
      Authors: Alexandre Gramfort <alexandre.gramfort@inria.fr>  
                 Matti Hämäläinen <msh@nmr.mgh.harvard.edu>  
         
        License: BSD-3-Clause  
        Copyright the MNE-Python contributors.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/mne/fiff_define_constants.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("fiff_define_constants", *args, **kwargs)
