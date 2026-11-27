from spm._runtime import Runtime


def spm_MDP_conv(*args, **kwargs):
    r"""
      Multidimensional dot (inner) product  
        FORMAT [gg] = spm_MDP_conv(n,d)  
         
        n(1,2) - Size of image matrix  
        d      - Number of pixel displacements  
         
        gg{g}  - Cell array of output indices for each modality g  
         
        This illustrative routine returns a cell array of output indices that map  
        from modalities (i.e., the likelihood tensors) to outputs. This  
        effectively allows one to implement a simple form of weight sharing by  
        changing the mapping from modalities to outputs in a systematic way.  
        Here, we consider translations as exemplar affine mappings from  
        modalities to outputs.  
          
        The resulting cell array is then used during inversion to estimate the  
        latent states encoding a fine transformations. The dimensions of the cell  
        array (gg) correspond to orthogonal transformations and, implicitly, the  
        shape of domain states (ff) on which they depend. By using an explicit  
        geometry the transformations are strictly divergence; in the sense that  
        one modality can generate multiple outputs; however, each transformation  
        or mapping generates the same number of outputs (and is thereby informed  
        by the same number).  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_MDP_conv.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_MDP_conv", *args, **kwargs)
