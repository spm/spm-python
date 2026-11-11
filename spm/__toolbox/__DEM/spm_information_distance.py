from spm._runtime import Runtime


def spm_information_distance(*args, **kwargs):
    r"""
      information geometry of a likelihood mapping  
        FORMAT [D,C] = spm_information_distance(a)  
        a{g}    - Dirichlet tensor for modality g  
         
        D       - information distance (nats);  
        C       - correlation (similarity) matrix (normalised)  
         
        This routine uses the information geometry inherent in a likelihood  
        mapping. It computes a similarity matrix (C) based upon the information  
        distance (D) between columns of a likelihood tensor (i.e., implicit  
        categorical distributions), or vice versa.  
       __________________________________________________________________________  
        Karl Friston  
        Copyright (C) 2012-2022 Wellcome Centre for Human Neuroimaging  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_information_distance.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_information_distance", *args, **kwargs)
