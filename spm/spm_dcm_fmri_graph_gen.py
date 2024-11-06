from spm.__wrapper__ import Runtime


def spm_dcm_fmri_graph_gen(*args, **kwargs):
    """
      Generate adjacency graph for spectral DCM for fMRI  
        FORMAT g = spm_dcm_fmri_graph_gen(x,v,P)  
         
        This routine computes the adjacency matrix (A) for spm_fx_fmri  
         
        see also: spm_fx_fmri  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_dcm_fmri_graph_gen.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dcm_fmri_graph_gen", *args, **kwargs)
