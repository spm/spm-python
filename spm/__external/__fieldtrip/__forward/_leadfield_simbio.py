from spm._runtime import Runtime


def _leadfield_simbio(*args, **kwargs):
    r"""
      leadfield_simbio leadfields for a set of dipoles  
         
        [lf] = leadfield_simbio(pos, vol);  
         
        with input arguments  
          pos     a matrix of dipole positions  
                  there can be 'deep electrodes' too!  
          vol     contains a FE volume conductor (output of ft_prepare_vol_sens)  
         
        the output lf is the leadfield matrix of dimensions m (rows) x n*3 (cols)  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/forward/private/leadfield_simbio.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("leadfield_simbio", *args, **kwargs)
