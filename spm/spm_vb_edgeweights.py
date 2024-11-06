from spm.__wrapper__ import Runtime


def spm_vb_edgeweights(*args, **kwargs):
    """
      Compute edge set and edge weights of a graph  
        FORMAT [edges,weights]= spm_vb_edgeweights(vxyz,img)  
          
        vxyz     list of neighbouring voxels (see spm_vb_neighbors)  
        img      image defined on the node set, e.g. wk_ols. The edge weights   
                 are uniform if this is not given, otherwise they are a function  
                 of the distance in physical space and that between the image  
                 at neighbouring nodes  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_vb_edgeweights.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_vb_edgeweights", *args, **kwargs)
