from spm._runtime import Runtime


def spm_RDP_compress(*args, **kwargs):
    r"""
      BMR of superordinate states based upon predicted outcomes  
        FORMAT [MDP] = spm_RDP_compress(MDP,R,[OPT])  
        MDP   - cell array of MDP structures  
        R     - reduction operator  
        OPT   - flag to reduce all levels  
         
        This routine implements a Bayesian model reduction in which the latent  
        (generalised) states that the highest level of the model are merged in a  
        way that entails a minimum loss of mutual information (i.e., cross  
        entropy or expected free energy) between the states of the first stream  
        and predicted outcomes — now and in the future — of subsequent (trailing)  
        streams. These training streams would usually include generalised actions  
        (i.e., policies) and constraints reported by rewarding and costly  
        outcomes at the lowest level.  
       __________________________________________________________________________  
        Copyright (C) 2005 Wellcome Trust Centre for Neuroimaging  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_RDP_compress.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_RDP_compress", *args, **kwargs)
