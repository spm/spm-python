from spm._runtime import Runtime


def spm_dcm_tfm_image(*args, **kwargs):
    r"""
      Display time-frequency complex cross spectra  
        FORMAT spm_dcm_tfm_image(csd,top,pst,hz)  
          
        csd - (t x w x n x n): a data array over t time bins, w frequency bins  
                              and n times n channels  
        pst - peristimulus time (for plotting)  
        Hz  - frequency range (for plotting)  
        top - [0/1] switch to display at the top or bottom of the current figure  
       __________________________________________________________________________  
         
        This routine displays complex cross spectra over peristimulus time as  
        images of the absolute values (coherence) and cross covariance functions  
        over pairs of channels.  
         
        See also: spm_dcm_tfm_responses (and spm_dcm_tfm_transfer)   
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/dcm_meeg/spm_dcm_tfm_image.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_dcm_tfm_image", *args, **kwargs, nargout=0)
