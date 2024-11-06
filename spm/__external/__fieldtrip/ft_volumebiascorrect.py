from spm.__wrapper__ import Runtime


def ft_volumebiascorrect(*args, **kwargs):
    """
      FT_VOLUMEBIASCORRECT corrects the image inhomogeneity bias in an anatomical MRI  
         
        Use as  
          mri_unbias = ft_volumebiascorrect(cfg, mri)  
        where the input mri should be a single anatomical volume organised in a structure  
        as obtained from the FT_READ_MRI function  
         
        The configuration structure can contain  
          cfg.spmversion     = string, 'spm8', 'spm12' (default = 'spm12')  
          cfg.opts           = struct, containing spmversion specific options.  
                               See the code below and the SPM-documentation for  
                               more information.  
         
        See also FT_VOLUMEREALIGN FT_VOLUMESEGMENT FT_VOLUMENORMALISE  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/ft_volumebiascorrect.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_volumebiascorrect", *args, **kwargs)
