from spm.__wrapper__ import Runtime


def spm_shp_get_model(*args, **kwargs):
    """
      Get the path to a Shape PCA model file, install/download if needed.  
         
        FORMAT path = spm_get_model(name)  
         
        name     - Model variable to return  
                   {'subspace_scaled', 'model_variables', 'Template_{01234}'}  
        dartadir - Data directory [spm('Dir')/tpl/shp]  
        path     - Path to model file  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_shp_get_model.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_shp_get_model", *args, **kwargs)
