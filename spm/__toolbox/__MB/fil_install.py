from spm.__wrapper__ import Runtime


def fil_install(*args, **kwargs):
    """
      Download files required for Factorisation-based Image Labelling  
        FORMAT [mufile,filfile] = fil_install(datadir)  
         
        https://figshare.com/projects/Factorisation-based_Image_Labelling/128189  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/MB/fil_install.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("fil_install", *args, **kwargs)
