from spm.__wrapper__ import Runtime


def ft_sourceparcellate(*args, **kwargs):
    """
      FT_SOURCEPARCELLATE combines the source-reconstruction parameters over the parcels, for  
        example by averaging all the values in the anatomically or functionally labeled parcel.  
         
        Use as  
           output = ft_sourceparcellate(cfg, source, parcellation)  
        where the input source is a 2D surface-based or 3-D voxel-based source grid that was for  
        example obtained from FT_SOURCEANALYSIS or FT_COMPUTE_LEADFIELD. The input parcellation is  
        described in detail in FT_DATATYPE_PARCELLATION (2-D) or FT_DATATYPE_SEGMENTATION (3-D) and  
        can be obtained from FT_READ_ATLAS or from a custom parcellation/segmentation for your  
        individual subject. The output is a channel-based representation with the combined (e.g.  
        averaged) representation of the source parameters per parcel.  
         
        The configuration "cfg" is a structure that can contain the following fields  
          cfg.method       = string, method to combine the values, see below (default = 'mean')  
          cfg.parcellation = string, fieldname that contains the desired parcellation  
          cfg.parameter    = cell-array with strings, fields that should be parcellated (default = 'all')  
         
        The values within a parcel or parcel-combination can be combined with different methods:  
          'mean'      compute the mean  
          'median'    compute the median (unsupported for fields that are represented in a cell-array)  
          'eig'       compute the largest eigenvector  
          'min'       take the minimal value  
          'max'       take the maximal value  
          'maxabs'    take the signed maxabs value  
          'std'       take the standard deviation  
         
        See also FT_SOURCEANALYSIS, FT_DATATYPE_PARCELLATION, FT_DATATYPE_SEGMENTATION  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/ft_sourceparcellate.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_sourceparcellate", *args, **kwargs)
