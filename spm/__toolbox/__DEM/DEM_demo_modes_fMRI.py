from spm.__wrapper__ import Runtime


def DEM_demo_modes_fMRI(*args, **kwargs):
    """
      Demonstration of spectral DCM for fMRI with eigenvector constraints  
       __________________________________________________________________________  
        This demonstration routine illustrates the inversion of resting state  
        fMRI timeseries using a generative model of the adjacency matrix. This  
        model is based upon the eigenmodes of the functional connectivity matrix,  
        which are the eigenvectors of the effective connectivity matrix or  
        Jacobian - assuming the effective connectivity is symmetrical. This means  
        it is only necessary to estimate the eigenvalues; in other words, one  
        unknown parameter per node.  
         
        Simulated timeseries are generated and inverted under typical priors.  
        This routine then performs a model space search over the decay rates of  
        stable (dissipative) modes and the number of unstable modes.  
        This illustrates: (i) the increase in model evidence afforded by  
        hierarchical constraints (when they are true) and (ii) the identification  
        of the principle modes underlying connectivity.  
         
        NB: To see the model optimisation delete the 'return' at about line 200  
          
        see also: DEM_demo_connectivity_fMRI  
                  spm_dcm_fmri_mode_gen  
                  spm_dcm_fmri_mode  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/DEM_demo_modes_fMRI.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("DEM_demo_modes_fMRI", *args, **kwargs, nargout=0)
