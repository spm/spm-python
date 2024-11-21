from spm.__wrapper__ import Runtime


def FieldMap_create(*args, **kwargs):
    """
      Function to create VDM file from fieldmap images and can be called  
        using FieldMap_preprocess.m  
         
        This function uses routines from the FieldMap toolbox to:  
        1) Create a single field map from input fieldmap data.  
        2) Convert fieldmap to a voxel displacement map (vdm_* file).  
        3) Match vdm_* to input EPI(s) which should be the first image  
        that each session will be realigned/unwarped to. Writes out matched vdm  
        file with name extension 'session' or a user-specified name.  
        4) Each selected EPI is unwarped and written out with the prefix 'u'.  
         
        For details about the FieldMap toolbox, see FieldMap.md. For a  
        description of the components of the structure IP, see FieldMap.m.  
        For an introduction to the theoretcial and practical principles behind  
        the toolbox, see FieldMap_principles.md.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/FieldMap/FieldMap_create.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("FieldMap_create", *args, **kwargs)
