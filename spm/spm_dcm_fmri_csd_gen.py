from spm._runtime import Runtime


def spm_dcm_fmri_csd_gen(*args, **kwargs):
    r"""
      Conversion routine for DEM inversion of DCM for CSD (fMRI)  
        FORMAT y = spm_dcm_fmri_csd_gen(x,v,P)  
         
        This routine computes the spectral response of a network of regions  
        driven by  endogenous fluctuations and exogenous (experimental) inputs.  
        It returns the complex cross spectra of regional responses as a  
        three-dimensional array. The endogenous innovations or fluctuations are  
        parameterised in terms of a (scale free) power law, in frequency space.  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_dcm_fmri_csd_gen.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_dcm_fmri_csd_gen", *args, **kwargs)
