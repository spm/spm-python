from spm._runtime import Runtime


def fil_install(*args, **kwargs):
    r"""
      Download files required for Factorisation-based Image Labelling  
        FORMAT [mufile,filfile] = fil_install(datadir)  
         
        https://figshare.com/projects/Factorisation-based_Image_Labelling/128189  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/MB/fil_install.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("fil_install", *args, **kwargs)
