



##
1. ## **Introduction**

1. ### **Overview**
   ###
Provide description about my network automation with Jenkins project 

1. **SYSTEM OVERVIEW**

Automate the process of configuration network devices using python programing language providing two way to send configuration to network devices by ( SSH or REST API ) and then using Jenkins to  inherent my project the CI/CD philosophy. , asking the user to choose the routing protocol ( OSPF , BGP) or add static route and edit the configuration in yaml file. 

1. ## **System Architecture**

1. ### **Architectural Design**
###
###

- Overview of CI/CD of my project


![](Aspose.Words.4bbfeb75-6aa0-43cf-a59b-8fd8f6307449.001.png)













- ` `The network of the connected devices in my host environment

![](Aspose.Words.4bbfeb75-6aa0-43cf-a59b-8fd8f6307449.002.png)




1. ### **Flow chart Description**
Flow chart of the code to automat the configuration of network device.

![](Aspose.Words.4bbfeb75-6aa0-43cf-a59b-8fd8f6307449.003.png)



















1. ## **CODE  Details**

###
1. ### **Data Description**

![](Aspose.Words.4bbfeb75-6aa0-43cf-a59b-8fd8f6307449.004.png)
1. ### **Code Description and snippets**
Take the choice of ospf protocol to describe the steps of the code

- ospf.yaml file

  ![](Aspose.Words.4bbfeb75-6aa0-43cf-a59b-8fd8f6307449.005.png)






- ospf.j2 file 

  the jinja part to make configuration suitable for ssh commands

  ![](Aspose.Words.4bbfeb75-6aa0-43cf-a59b-8fd8f6307449.006.png)

`	`the jinja part to make configuration suitable for yangmodel

`	`![](Aspose.Words.4bbfeb75-6aa0-43cf-a59b-8fd8f6307449.007.png)

- the output of rendering in case of rest api

 

  ![](Aspose.Words.4bbfeb75-6aa0-43cf-a59b-8fd8f6307449.008.png)

- the output of rendering in case of  SSH

  ![](Aspose.Words.4bbfeb75-6aa0-43cf-a59b-8fd8f6307449.009.png)







1. ## **Jenkins Pipeline**

The steps of the pipeline 

![](Aspose.Words.4bbfeb75-6aa0-43cf-a59b-8fd8f6307449.010.png)




- In the stage of testing running all the combination of possible input

  (bgp,ospf,static)--à(ssh,rest api) that give us 6 possibilities:

  The output of this stage is in log file : [log.txt](https://github.com/Omar-Ahmed97/Network-automation-Project/blob/master/log.txt) 

.![](Aspose.Words.4bbfeb75-6aa0-43cf-a59b-8fd8f6307449.011.png)


