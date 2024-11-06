from spm.__wrapper__ import Runtime


def ft_appendsource(*args, **kwargs):
    """
      FT_APPENDSOURCE concatenates multiple volumetric source reconstruction data  
        structures that have been processed separately.  
         
        Use as  
          combined = ft_appendsource(cfg, source1, source2, ...)  
         
        If the source reconstructions were computed for different ROIs or different slabs  
        of a regular 3D grid (as indicated by the source positions), the data will be  
        concatenated along the spatial dimension.  
         
        If the source reconstructions were computed on the same source positions, but for  
        different frequencies and/or latencies, e.g. for time-frequency spectrally  
        decomposed data, the data will be concatenated along the frequency and/or time  
        dimension, but only of the frequency or time axes are well-behaved, i.e. all data  
        points along the dimension of interest should be sortable across data objects;  
        interleaving across data objects is not possible.  
         
        See also FT_SOURCEANALYSIS, FT_DATATYPE_SOURCE, FT_APPENDDATA, FT_APPENDTIMELOCK,  
        FT_APPENDFREQ  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/ft_appendsource.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_appendsource", *args, **kwargs)
