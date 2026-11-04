from spm._runtime import Runtime


def spm_dcm_fmri_graph_gen(*args, **kwargs):
    r"""
      Generate adjacency graph for spectral DCM for fMRI  
        FORMAT g = spm_dcm_fmri_graph_gen(x,v,P)  
         
        This routine computes the adjacency matrix (A) for spm_fx_fmri  
         
        see also: spm_fx_fmri  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_dcm_fmri_graph_gen.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_dcm_fmri_graph_gen", *args, **kwargs)
