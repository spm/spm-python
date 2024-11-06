from spm.__wrapper__ import Runtime


def spm_vb_ppm_anova(*args, **kwargs):
    """
      Bayesian ANOVA using model comparison  
        FORMAT spm_vb_ppm_anova(SPM)  
         
        SPM    -  Data structure corresponding to a full model (ie. one  
                  containing all experimental conditions).  
                    
        This function creates images of differences in log evidence  
        which characterise the average effect, main effects and interactions  
        in a factorial design.   
         
        The factorial design is specified in SPM.factor. For a one-way ANOVA   
        the images   
         
          avg_effect.<ext>  
          main_effect.<ext>  
         
        are produced. For a two-way ANOVA the following images are produced  
         
          avg_effect.<ext>  
          main_effect_'factor1'.<ext>  
          main_effect_'factor2'.<ext>  
          interaction.<ext>  
         
        These images can then be thresholded. For example a threshold of 4.6   
        corresponds to a posterior effect probability of [exp(4.6)] = 0.999.   
        See paper VB4 for more details.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_vb_ppm_anova.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_vb_ppm_anova", *args, **kwargs, nargout=0)
