from spm.__wrapper__ import Runtime


def DEM_demo_connectivity_fMRI(*args, **kwargs):
    """
      Demonstration of DCM for fMRI-CSD with hierarchical constraints  
       __________________________________________________________________________  
        This demonstration routine illustrates the inversion of resting state  
        fMRI timeseries using a generative model of the adjacency matrix. This  
        model is based upon an embedding space of dimension ED in which the  
        (log) connectivity among nodes is a (radial basis) function of their  
        metric separation. This generative model of connectivity requires a  
        hierarchical constraint on the edges and therefore uses the expectation  
        and maximisation steps of dynamic expectation maximisation. Here, the  
        hidden causes at the first level are the effective connectivity and the  
        hidden causes at the second level are the Lyapunov exponents or   
        eigenvalues of a symmetrical Jacobian or effective connectivity matrix:  
        see DEM_demo_modes_fMRI.m  
         
        Simulated timeseries are generated and inverted under typical priors.  
        This routine that performs a model space search over precisions on the  
        hierarchical constraints and the dimensionality of the embedding space.  
        This illustrates: (i) the increase in model evidence afforded by  
        hierarchical constraints (when they are true) and (ii) the optimal  
        prior precision that reflects the amplitude of random variations in  
        connectivity about the constraints. (iii) Finally,the search over model  
        dimension illustrates how Bayesian model comparison can identify the  
        dimensionality of the metric space generating hierarchical connectivity.  
          
        see also: DEM_demo_modes_fMRI.m  
                  spm_dcm_fmri_csd_DEM.m  
                  spm_dcm_fmri_graph_gen.m  
                  spm_dcm_fmri_mode_gen  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/DEM_demo_connectivity_fMRI.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("DEM_demo_connectivity_fMRI", *args, **kwargs, nargout=0)
