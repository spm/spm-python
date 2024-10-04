from spm.__wrap__ import _Runtime


def spm_dcm_fmri_graph_gen(*args, **kwargs):
  """  Generate adjacency graph for spectral DCM for fMRI  
    FORMAT g = spm_dcm_fmri_graph_gen(x,v,P)  
     
    This routine computes the adjacency matrix (A) for spm_fx_fmri  
     
    see also: spm_fx_fmri  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_dcm_fmri_graph_gen.m)
  """

  return _Runtime.call("spm_dcm_fmri_graph_gen", *args, **kwargs)
