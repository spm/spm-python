from spm.__wrapper__ import Runtime


def ft_headmodeltype(*args, **kwargs):
    """
      FT_HEADMODELTYPE determines the type of volume conduction model of the head  
         
        Use as  
          [type] = ft_headmodeltype(headmodel)  
        to get a string describing the type, or  
          [flag] = ft_headmodeltype(headmodel, desired)  
        to get a boolean value.  
         
        For EEG the following volume conduction models are recognized  
          singlesphere       analytical single sphere model  
          concentricspheres  analytical concentric sphere model with up to 4 spheres  
          halfspace          infinite homogenous medium on one side, vacuum on the other  
          openmeeg           boundary element method, based on the OpenMEEG software  
          bemcp              boundary element method, based on the implementation from Christophe Phillips  
          dipoli             boundary element method, based on the implementation from Thom Oostendorp  
          asa                boundary element method, based on the (commercial) ASA software  
          simbio             finite element method, based on the SimBio software  
          fns                finite difference method, based on the FNS software  
          interpolate        interpolate the potential based on pre-computed leadfields  
         
        and for MEG the following volume conduction models are recognized  
          singlesphere       analytical single sphere model  
          localspheres       local spheres model for MEG, one sphere per channel  
          singleshell        realisically shaped single shell approximation, based on the implementation from Guido Nolte  
          infinite           magnetic dipole in an infinite vacuum  
          interpolate        interpolate the potential based on pre-computed leadfields  
         
        See also FT_COMPUTE_LEADFIELD, FT_READ_HEADMODEL, FT_HEADMODEL_BEMCP,  
        FT_HEADMODEL_ASA, FT_HEADMODEL_DIPOLI, FT_HEADMODEL_SIMBIO,  
        FT_HEADMODEL_FNS, FT_HEADMODEL_HALFSPACE, FT_HEADMODEL_INFINITE,  
        FT_HEADMODEL_OPENMEEG, FT_HEADMODEL_SINGLESPHERE,  
        FT_HEADMODEL_CONCENTRICSPHERES, FT_HEADMODEL_LOCALSPHERES,  
        FT_HEADMODEL_SINGLESHELL, FT_HEADMODEL_INTERPOLATE  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/forward/ft_headmodeltype.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_headmodeltype", *args, **kwargs)
