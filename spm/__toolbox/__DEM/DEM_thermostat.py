from spm._runtime import Runtime


def DEM_thermostat(*args, **kwargs):
    r"""
      Demo of multiple constraint satisfaction (smart thermostat)  
       __________________________________________________________________________  
          
        This demonstration routine illustrates the application of active  
        inference to a multiple constraint satisfaction problem. In this example,  
        there are two controllers (i.e., agents) the first can boost the charge  
        of a domestic battery. The second is a heating, ventilation and air  
        conditioning system (HVAC). These two controllers have to operate in  
        tandem to satisfy multiple constraints; namely, keep electricity costs  
        down by boosting during periods of low time of use (ToU) rates, while  
        maintaining room temperature at a comfortable level, when and only when  
        the rule is in use (i.e., occupied). The problem is solved using  
        constraints (i.e., prior preferences) on outcomes. These include  
        consumption (i.e., time of use rates multiplied by the state of the  
        booster), room temperature and battery charge (state of charge; which  
        cannot be at the highest or lowest level of charge).  
         
        This example illustrates the discretisation or course graining of latent  
        states and outcomes at several timescales. First, it illustrates home to  
        use the solutions of underlying state space model (e.g., differential  
        equations) to specify outcomes. Second, it uses a model to illustrate how  
        slow fluctuations (day-to-day) contextualise fast fluctuations (hour two  
        hour) in hidden states generating outcomes. For example, the time of use  
        rate depends upon a daily average, with two hourly peaks. Similarly, the  
        outside (air) temperature fluctuates relatively smoothly, with an initial  
        (early morning) temperature that changes itinerantly from day to day.%  
         
        The results of active inference are shown using a bespoke displays scheme  
        that picks out the outcomes that are equipped with constraints and  
        evaluates constraint satisfaction in terms of the cost; namely, the  
        negative log probability of the realised outcome under prior preferences  
        encoded in (context sensitive) constraints (C). Context sensitivity in  
        this instance is endowed by conditioning prior constraints on one or more  
        hidden factors (here, constraints over room temperature depend upon  
        whether the room is in use or not).  
         
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/DEM_thermostat.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("DEM_thermostat", *args, **kwargs)
