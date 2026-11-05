from spm._runtime import Runtime


def ft_appendsens(*args, **kwargs):
    r"""
      FT_APPENDSENS concatenates multiple sensor definitions that have been processed  
        separately.  
         
        Use as  
          combined = ft_appendsens(cfg, sens1, sens2, ...)  
         
        A call to FT_APPENDSENS results in the label, pos and ori fields to be  
        concatenated, and the tra matrix to be merged. Any duplicate electrodes  
        will be removed. The labelold and chanposold fields are kept under the  
        condition that they are identical across the inputs.  
         
        See also FT_ELECTRODEPLACEMENT, FT_ELECTRODEREALIGN, FT_DATAYPE_SENS,  
        FT_APPENDDATA, FT_APPENDTIMELOCK, FT_APPENDFREQ, FT_APPENDSOURCE  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/ft_appendsens.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("ft_appendsens", *args, **kwargs)
