from spm.__wrapper__ import Runtime


def ft_preproc_denoise(*args, **kwargs):
    """
      FT_PREPROC_DENOISE performs a regression of the matrix dat onto refdat, and  
        subtracts the projected data. This is for the purpose of removing signals generated  
        by coils during continuous head motion tracking, for example.  
         
        Use as  
          [dat] = ft_preproc_denoise(dat, refdat, hilbertflag)  
        where  
          dat         data matrix (Nchan1 X Ntime)  
          refdat      data matrix (Nchan2 X Ntime)  
          hilbertflag boolean, regress out the real and imaginary parts of the Hilbert   
                        transformed signal, this is only meaningful for narrow band   
                        reference data (default = false)  
         
        The number of channels of the data and reference data does not have to be the same.  
         
        If the data contains NaNs, the output of the affected channel(s) will be all NaN.  
         
        See also PREPROC  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/preproc/ft_preproc_denoise.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_preproc_denoise", *args, **kwargs)
