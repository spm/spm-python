from spm.__wrapper__ import Runtime


def ft_headmodel_asa(*args, **kwargs):
    """
      FT_HEADMODEL_ASA reads a volume conduction model from an ASA *.vol  
        file  
         
        ASA is commercial software (http://www.ant-neuro.com) that supports  
        among others the boundary element method (BEM) for EEG. This function  
        allows you to read an EEG BEM volume conduction model from an ASA  
        format file (*.vol) and use that for leadfield computations in  
        MATLAB. Constructing the geometry of the head model from an anatomical  
        MRI and the computation of the BEM system are both handled by ASA.  
          
        Use as  
          headmodel = ft_headmodel_asa(filename)  
         
        See also FT_PREPARE_VOL_SENS, FT_COMPUTE_LEADFIELD  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/forward/ft_headmodel_asa.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_headmodel_asa", *args, **kwargs)
