from spm.__wrapper__ import Runtime


def spm_dcm_peb_to_gcm(*args, **kwargs):
    """
      Generate an array of DCMs based on parameters from a PEB model  
        FORMAT [GCM,PEB] = spm_dcm_peb_to_gcm(PEB, GCM_template, options)  
          
        Any parameters not included in the PEB model will be fixed at their   
        prior means (alternative fixed values can be selected).  
         
        -------------------------------------------------------------------------  
        Inputs:  
         
        PEB - PEB model containing at least the following fields:  
         
                       PEB.Ep   - group level parameter means  
          
                       PEB.Pind - indices within the DCM of parameters included  
                                  in the PEB.  
         
                       PEB.beta - between-subjects variance for each parameter is  
                                  set to a fraction of the within-subject DCM  
                                  priors: GCM_template{x}.M.pC / beta  
         
                       PEB.Ce   - alternatively, a between-subjects covariance  
                                  matrix can be provided, in which case beta is   
                                  ignored  
         
        GCM_template - cell array of dimension [1 x models], where each element  
                       is a DCM. These DCMs provide the structure of the models  
                       that will be simulated (so don't need to be estimated).  
         
                       If any parameters are not included in the PEB, they will  
                       be fixed at values in GCM_template{m}.Ep. If this is not  
                       present, they will be fixed at the priors in  
                       GCM_template.M.pE{1}.  
         
                       Alternatively, a matrix of size [subjects x models] can be  
                       given, allowing subject-specific values for parameters not  
                       in included in the PEB.  
         
        options - settings structure for the simulation with fields:  
         
                  options.nsubjects - number of subjects to generate  
         
                  options.ratio - the ratio of posterior:prior covariance for  
                                  the PEB model. [default 2]  
         
        Returns:  
         
        GCM  - DCM array populated with simulated data  
        PEB  - PEB structure updated with PEB.Ce if not already present  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_dcm_peb_to_gcm.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dcm_peb_to_gcm", *args, **kwargs)
