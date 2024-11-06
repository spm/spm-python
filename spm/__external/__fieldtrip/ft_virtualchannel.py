from spm.__wrapper__ import Runtime


def ft_virtualchannel(*args, **kwargs):
    """
      FT_VIRTUALCHANNEL creates virtual channel data, combining numeric data from a data  
        structure defined at the channel level with spatial filter information from a  
        source data structure, and optional parcellation information.  
         
        Use as  
           output = ft_virtualchannel(cfg, data, source)  
        or  
           output = ft_virtualchannel(cfg, data, source, parcellation)  
         
        where the input "data" is a channel-level data structure that can be linearly  
        mapped onto the virtual channel level, e.g. a raw data structure obtained with  
        FT_PREPROCESSING, a timelock structure, obtained with FT_TIMELOCKANALYSIS, or a  
        freq structure with fourierspectra, obtained with FT_FREQANALYSIS.  
         
        The input "source" is a source structure that has been obtained with  
        FT_SOURCEANALYSIS, and which contains spatial filter information for at least one  
        dipole location, in the source.filter, or source.avg.filter field.  
         
        The optional input "parcellation" is described in detail in  
        FT_DATATYPE_PARCELLATION (2-D) or FT_DATATYPE_SEGMENTATION (3-D) and can be  
        obtained from FT_READ_ATLAS or from a custom parcellation/segmentation for your  
        individual subject. Alternatively, the input "source" can already contain a  
        parcellation.  
         
        The configuration "cfg" is a structure that should either contain  
          cfg.pos           = Nx3 matrix containing the dipole positions for the virtual  
                              channel(s). These positions should match the entries in  
                              the source.pos field. (default = [])  
        or  
          cfg.parcellation  = string, name of the field that is used for the  
                              parcel labels. (default = [])  
          cfg.parcel        = string, or cell-array of strings, specifying for which  
                              parcels to return the output. (default = 'all')  
         
        Moreover, the cfg structure can contain  
          cfg.method        = string, determines how the components of the specified virtual  
                              channel(s) are to to be combined. 'svd' (default), 'none', 'pca',  
                              'runica', 'fastica', 'dss'.  
          cfg.numcomponent  = scalar (or 'all'), determines the number of components per virtual  
                              channel in the output. (default = 1)  
         
        See also FT_SOURCEANALYSIS, FT_DATATYPE_PARCELLATION, FT_DATATYPE_SEGMENTATION,  
        FT_SOURCEPARCELLATE, FT_COMPONENTANALYSIS  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/ft_virtualchannel.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_virtualchannel", *args, **kwargs)
