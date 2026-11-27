from spm._runtime import Runtime


def spm_mg_switch(*args, **kwargs):
    r"""
      Switching output  
        FORMAT s = spm_mg_switch(V)  
         
        Switching output s: determined by voltage (V) dependent magnesium  
        blockade parameters as per Durstewitz, Seamans & Sejnowski 2000.  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/dcm_meeg/spm_mg_switch.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_mg_switch", *args, **kwargs)
