from spm.__wrapper__ import Runtime


def FEP_Manifold(*args, **kwargs):
    """
      This demonstration routine simulates the emergence of life - as defined  
        in terms of active inference - using a synthetic primordial soup. The key  
        aspect of this dynamics is that there is a separation between dynamical  
        states and structural states; where the dynamical states of the  
        microsystem are equipped with a Lorentz attractor and the structural  
        states correspond to position and velocity. The flow of structural  
        states conforms to classical Newtonian mechanics. Crucially, the physical  
        motion of each microsystem is coupled to its internal dynamics and vice  
        versa; where the coupling among dynamics rests upon short range  
        (electrochemical) forces. This means that the dependencies among the  
        dynamics of each microsystem dependent on their positions. This induces a  
        dependency of the systems structural integrity on its internal dynamics -  
        which leads to biological self-organisation. This biological self-  
        organisation is illustrated in terms of the following:  
         
        i) the existence of a Markov blanket that separates internal and external  
        states, where the internal states are associated with a system that  
        engages in active or embodied inference.  
         
        ii) emergent inference is demonstrated by showing that the internal  
        states can predict the extent states, despite their separation by the  
        Markov blanket.  
         
        iii) this inference (encoded by the internal dynamics) is necessary to  
        maintain structural integrity, as illustrated by simulated lesion  
        experiments, in which the influence of various states are quenched.  
         
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/FEP_Manifold.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("FEP_Manifold", *args, **kwargs, nargout=0)
