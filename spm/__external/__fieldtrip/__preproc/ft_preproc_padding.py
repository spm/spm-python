from spm.__wrapper__ import Runtime


def ft_preproc_padding(*args, **kwargs):
    """
      FT_PREPROC_PADDING performs padding on the data, i.e. adds or removes samples  
        to or from the data matrix.  
         
        Use as  
          [dat] = ft_preproc_padding(dat, padtype, padlength)  
        or as  
          [dat] = ft_preproc_padding(dat, padtype, prepadlength, postpadlength)  
        where  
          dat           data matrix (Nchan x Ntime)  
          padtype       'zero', 'mean', 'localmean', 'edge', 'mirror', 'nan' or 'remove'  
          padlength     scalar, number of samples that will be padded  
          prepadlength  scalar, number of samples that will be padded before the data  
          postpadlength scalar, number of samples that will be padded after the data  
         
        If padlength is used instead of prepadlength and postpadlength, padding  
        will be symmetrical (i.e. padlength = prepadlength = postpadlength)  
         
        If the data contains NaNs, these are ignored for the computation, but  
        retained in the output. Depending on the type of padding, NaNs may spread  
        to the pads.  
         
        See also FT_PREPROCESSING  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/preproc/ft_preproc_padding.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_preproc_padding", *args, **kwargs)
