from spm.__wrapper__ import Runtime


def spm_MDP_factor_graph(*args, **kwargs):
    """
      Draws a factor graph corresponding to MDP  
        FORMAT spm_MDP_factor_graph(MDP)  
         
        MDP.A{G}(O,N1,...,NF) - likelihood of O outcomes given hidden states  
        MDP.B{F}(NF,NF,MF)    - transitions among states under MF control states  
         
        This routine draws a simplified (normal style) factor graph  based upon  
        the size of likelihood and prior probability matrices (and labels). The  
        resulting graph can either be interpreted in terms of a factor graph with  
        factors corresponding to white boxes. Alternatively, it can be  
        interpreted as a graphical model with coloured boxes corresponding to  
        random variables. The magenta boxes denote outcomes (at intermediate  
        levels of deep models, if specified). The cyan boxes denote hidden states  
        and the puce boxes represent policies. If a hidden state is controllable  
        (i.e., has more than one control dependent probability transition matrix)  
        it is labelled in blue (and the hidden states are shown as a stack of  
        boxes to indicate they are conditioned on several policies). Key message  
        passing is illustrated with three arrows, corresponding to ascending  
        likelihoods, forward and backward messages (1, 2 and 3,respectively).  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/spm_MDP_factor_graph.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_MDP_factor_graph", *args, **kwargs, nargout=0)
