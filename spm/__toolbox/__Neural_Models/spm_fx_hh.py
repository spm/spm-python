from spm.__wrapper__ import Runtime


def spm_fx_hh(*args, **kwargs):
    """
      state equation for a single Hodgkin-Huxley like unit  
        FORMAT [y] = spm_fx_hh(x,u,P)  
         
        states  
       --------------------------------------------------------------------------  
        x(1) = proportion of open channels        % AMPA  
        x(2) = proportion of open channels        % GABA  
        x(3) = proportion of open channels        % K - slow  
        x(4) = proportion of open channels        % NMDA  
        x(5) = V                  % transmembrane potential mV  
        x(6) = t                  % time since last spike  
         
        u    = input - opening rate of AMPA channels  
         
        P(1) = opening rate of AMPA channels  
        P(1) = opening rate of GABA channels  
        P(1) = opening rate of NMDA channels  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/Neural_Models/spm_fx_hh.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_fx_hh", *args, **kwargs)
